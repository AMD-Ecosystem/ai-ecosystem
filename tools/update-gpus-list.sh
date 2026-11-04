#!/usr/bin/env bash
# Fetch docs/data/gpus.yaml from the ROCm docs repo and replace the local copy.
# The previous copy is saved alongside it as gpus.yaml.<timestamp>.bak.
# Usage: utils/update-gpus-list.sh [url]
set -euo pipefail

URL="${1:-https://raw.githubusercontent.com/ROCm/rocm-docs/develop/docs/data/gpus.yaml}"
# Convert github.com blob/tree/raw URLs to raw.githubusercontent.com automatically.
URL="$(printf '%s\n' "$URL" | sed -E \
    -e 's#^https://github\.com/([^/]+)/([^/]+)/(blob|tree)/#https://raw.githubusercontent.com/\1/\2/#' \
    -e 's#^https://github\.com/([^/]+)/([^/]+)/raw/refs/(heads|tags)/#https://raw.githubusercontent.com/\1/\2/#' \
    -e 's#^https://github\.com/([^/]+)/([^/]+)/raw/#https://raw.githubusercontent.com/\1/\2/#')"
# If a directory URL was passed (e.g. .../docs/data), append /gpus.yaml.
if [[ ! "$URL" =~ \.ya?ml$ ]]; then
    URL="${URL%/}/gpus.yaml"
fi
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="$ROOT/docs/data/gpus.yaml"
PY="${VIRTUAL_ENV:+$VIRTUAL_ENV/bin/python}"; [ -x "$PY" ] || PY=python3

TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT

CURL_ARGS=(-fsSL --retry 2)
if [[ "$URL" == https://raw.githubusercontent.com/* ]]; then
    TOKEN="${GITHUB_TOKEN:-$(gh auth token 2>/dev/null || true)}"
    if [ -n "$TOKEN" ]; then
        CURL_ARGS+=(-H "Authorization: Bearer $TOKEN")
    fi
fi

curl "${CURL_ARGS[@]}" "$URL" -o "$TMP"

# Sanity check: must parse as YAML and look like the GPU catalog.
"$PY" - "$TMP" <<'PY'
import sys, yaml
d = yaml.safe_load(open(sys.argv[1], encoding="utf-8"))
missing = {"AMD Instinct", "AMD Radeon", "AMD Ryzen"} - set(d or {})
if missing:
    sys.exit(f"downloaded file does not look like gpus.yaml (missing {sorted(missing)})")
PY

# Back up the current copy before replacing it.
BAK=""
if [ -f "$DEST" ]; then
    BAK="$DEST.$(date +%Y%m%d-%H%M%S).bak"
    cp -p "$DEST" "$BAK"
    echo "backed up: $BAK"
fi

chmod 644 "$TMP"
mv "$TMP" "$DEST"

echo "replaced $DEST"
echo "source:  $URL"
echo "sha256:  $(sha256sum "$DEST" | cut -d' ' -f1)"

if [ -n "$BAK" ] && [ -f "$BAK" ]; then
    git --no-pager diff --no-index --color=auto "$BAK" "$DEST" || true
fi
