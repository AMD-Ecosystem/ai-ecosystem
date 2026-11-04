---
name: rocdoc-update-gpus-list
description: >-
  Refresh docs/data/gpus.yaml, this repo's mirror of the canonical AMD GPU/APU
  catalog maintained in ROCm/rocm-docs. Use when asked to update, sync, refresh,
  or add GPUs to the supported-hardware list, or when preparing a ROCm release's
  GPU data. Handles GitHub URL conversion, private-repo auth, timestamped
  backups, and prints a diff. Keywords: update GPUs, sync gpus.yaml, refresh GPU
  list, add GPU support, supported hardware, ROCm release GPUs.
allowed-tools: Bash, Read, Edit, Grep, Glob
---

# Update docs/data/gpus.yaml

`docs/data/gpus.yaml` is this repo's **mirror** of the AMD GPU/APU catalog (the
`AMD Instinct`, `AMD Radeon`, and `AMD Ryzen` families). The canonical source is
upstream in **`ROCm/rocm-docs`**, per release branch (e.g.
`docs/10.2.0`). Never hand-edit the copy here, and never invent GPU data
locally. Per-framework GPU subsets and ROCm-version conditions belong in that
framework's data/templates, not in this file.

## Release workflow (update upstream first)

When preparing docs for a ROCm release, the GPU list is updated upstream first,
then synced here:

1. Update `docs/data/gpus.yaml` in **`ROCm/rocm-docs`** on the release branch
   (and mirror it to `develop`). That change is the source of truth.
2. Sync this repo from that ref, passing the URL of the updated file:

       tools/update-gpus-list.sh <url>

   For example, once the release branch exists:

       tools/update-gpus-list.sh \
         https://github.com/ROCm/rocm-docs/blob/docs/10.2.0/docs/data/gpus.yaml

   A `github.com` `blob`/`tree`/`raw` URL is rewritten to
   `raw.githubusercontent.com`; a directory URL (e.g. `.../docs/data`) gets
   `/gpus.yaml` appended; `file://` URLs work for a local checkout.
3. Review the printed diff and commit the updated `docs/data/gpus.yaml` on its
   own.

If the release branch isn't public yet, sync from the internal mirror
(`AMD-ROCm-Internal/ROCm-internal@docs/<version>`) and switch to the public URL
once published.

## Run the sync script

From the repository root:

    tools/update-gpus-list.sh [url]

- No argument: fetch the default public source (`ROCm/rocm-docs@develop`).

The script downloads to a temp file and validates it parses as YAML with the
three families, copies the current file to
`docs/data/gpus.yaml.<YYYYMMDD-HHMMSS>.bak`, replaces it, then prints the source
URL, sha256, and a git diff against the backup. `*.bak` is gitignored. It uses
`$VIRTUAL_ENV`'s python (falling back to `python3`) for the YAML check, and
authenticates to `raw.githubusercontent.com` with `$GITHUB_TOKEN` or
`gh auth token` (needed for internal refs).

## Sources

- Canonical (public): `ROCm/rocm-docs`, e.g.
  https://raw.githubusercontent.com/ROCm/rocm-docs/develop/docs/data/gpus.yaml
- Internal / not-yet-public release line:
  https://github.com/AMD-ROCm-Internal/ROCm-internal/tree/docs/10.2.0/docs/data
  (authenticated via `$GITHUB_TOKEN` or `gh auth token`).
- Local sibling checkout (offline):
  file:///home/petepark/amd/rocm/docs/data/gpus.yaml

## Verify and revert

- Compare sha256 with the sibling copy: `sha256sum ../rocm/docs/data/gpus.yaml`.
- Review the printed diff; expected changes are new SKUs / updated links.
- To revert: `mv docs/data/gpus.yaml.<timestamp>.bak docs/data/gpus.yaml`.

## After updating

Commit the new `docs/data/gpus.yaml` on its own so the catalog change is
isolated. Pages read it via `.. datatemplate:yaml::`, so a rebuild picks it up
automatically.
