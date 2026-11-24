#!/usr/bin/env python3
"""Validate the Docker image tags recorded in docs/data/docker-tags/*.yaml
actually exist on Docker Hub.

Usage:
    tools/validate-docker-tags.py [file ...]

With no arguments, validates every docs/data/docker-tags/*.yaml file. Each
`tags` map value is a "repo:tag" string (for example
"rocm/pytorch:rocm10.2.0_ubuntu24.04_py3.12_pytorch_release_2.15.0"); this
script looks up each one against Docker Hub's public tag API
(https://hub.docker.com/v2/repositories/<repo>/tags/<tag>) and reports any
that return 404 (or another unexpected status).

No authentication is required, but Docker Hub's unauthenticated tag-lookup
endpoint is rate-limited (observed ~180 requests per rolling window). The
script sleeps briefly between requests and backs off on HTTP 429.

Exit status is non-zero if any tag fails to resolve.
"""
import glob
import sys
import time

import requests
import yaml

API = "https://hub.docker.com/v2/repositories/{repo}/tags/{tag}"
REQUEST_DELAY = 0.35  # seconds between requests, to stay under the rate limit


def iter_tags(data):
    """Yield (location, repo, tag) for every tags{} entry in a parsed YAML doc."""
    for release in data.get("releases", []) or []:
        rocm_ver = release.get("rocm_ver", "?")
        for variant in release.get("variants", []) or []:
            version = variant.get("version") or variant.get("vllm_release") or "?"
            for dim, value in (variant.get("tags") or {}).items():
                if ":" not in value:
                    yield (f"rocm_ver={rocm_ver} version={version} dim={dim}", None, value)
                    continue
                repo, tag = value.split(":", 1)
                location = f"rocm_ver={rocm_ver} version={version} dim={dim}"
                yield (location, repo, tag)


def human_size(num_bytes):
    size = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024 or unit == "TB":
            return f"{size:.1f} {unit}" if unit != "B" else f"{int(size)} {unit}"
        size /= 1024


def check_tag(session, repo, tag, retries=3):
    """Return (status_code, full_size_bytes_or_None)."""
    url = API.format(repo=repo, tag=tag)
    for attempt in range(retries):
        resp = session.get(url, timeout=15)
        if resp.status_code == 429:
            wait = 5 * (attempt + 1)
            print(f"  rate limited, waiting {wait}s...", file=sys.stderr)
            time.sleep(wait)
            continue
        if resp.status_code == 200:
            try:
                return resp.status_code, resp.json().get("full_size")
            except ValueError:
                return resp.status_code, None
        return resp.status_code, None
    return resp.status_code, None


def main(argv):
    files = argv[1:] or sorted(glob.glob("docs/data/docker-tags/*.yaml"))
    if not files:
        print("no docker-tags YAML files found", file=sys.stderr)
        return 1

    session = requests.Session()
    session.headers["User-Agent"] = "rocdoc-validate-framework-docker-tags/1.0"

    failures = []
    total = 0

    for path in files:
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        name = data.get("name", path)
        print(f"== {path} ({name}) ==")
        for location, repo, tag in iter_tags(data):
            total += 1
            if repo is None:
                print(f"  MALFORMED  {location}: {tag!r} (no colon)")
                failures.append((path, location, f"{tag} (malformed)"))
                continue
            status, size = check_tag(session, repo, tag)
            ref = f"{repo}:{tag}"
            if status == 200:
                size_str = human_size(size) if size is not None else "unknown size"
                print(f"  OK    {ref}  ({size_str})")
            else:
                print(f"  FAIL  {ref}  (HTTP {status})  [{location}]")
                failures.append((path, location, ref))
            time.sleep(REQUEST_DELAY)

    print()
    print(f"checked {total} tags across {len(files)} file(s); {len(failures)} failed")
    if failures:
        print()
        print("Failures:")
        for path, location, ref in failures:
            print(f"  {path}: {ref}  [{location}]")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
