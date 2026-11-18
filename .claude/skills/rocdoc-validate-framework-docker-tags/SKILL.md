---
name: rocdoc-validate-framework-docker-tags
description: >-
  Validate that the Docker image tags recorded in docs/data/docker-tags/*.yaml
  (pytorch.yaml, jax.yaml, tensorflow.yaml, vllm.yaml, sglang.yaml) actually
  exist on Docker Hub. Use when asked to validate, check, verify, or audit the
  Docker tags in the install/inference guides, or before/after a ROCm release
  to confirm published images match the docs. Runs
  tools/validate-docker-tags.py, reports which `repo:tag` values 404, and
  helps distinguish images not yet published (expected during an in-progress
  release) from genuine data errors (typos, wrong naming pattern). Keywords:
  validate docker tags, check docker-tags yaml, docker hub 404, verify
  published images, audit docker-tags data.
allowed-tools: Bash, Read, Grep, Glob
---

# Validate docs/data/docker-tags/*.yaml

`docs/data/docker-tags/*.yaml` (`pytorch.yaml`, `jax.yaml`, `tensorflow.yaml`,
`vllm.yaml`, `sglang.yaml`) record the exact `repo:tag` Docker references shown
in the install/inference guides (rendered via `.. datatemplate:yaml::` and the
per-framework `*-docker.rst.jinja` templates). This skill checks that every
recorded tag actually **resolves** on Docker Hub — it does not fetch or
replace data from an upstream source (there isn't one; these values are
curated here, per release).

## Schema (shared across all five files)

Each file has a `releases` list (newest ROCm version first); each release has
a `rocm_ver` and a list of `variants` (framework versions); each variant has a
`tags` map of dimension-key (e.g. `py312`, `ub24`, `default`, `cdna`/`rdna`) to
a `"repo:tag"` string, for example:

```yaml
py312: "rocm/pytorch:rocm10.2.0_ubuntu24.04_py3.12_pytorch_release_2.15.0"
```

Only the `tags` map values are validated. `name`, `version_selector_key`,
`layout`, and `dimensions` are rendering metadata, not Docker references.

## Run the validator

From the repository root, with the project venv active (needs `requests` and
`pyyaml`, both already in `docs/sphinx/requirements.txt`):

```sh
.venv/bin/python tools/validate-docker-tags.py
```

Or validate a single file:

```sh
.venv/bin/python tools/validate-docker-tags.py docs/data/docker-tags/pytorch.yaml
```

The script extracts every `repo:tag` value and queries Docker Hub's public,
unauthenticated tag-lookup API
(`https://hub.docker.com/v2/repositories/<repo>/tags/<tag>`), which returns
HTTP 200 if the tag exists and 404 if it doesn't. For a tag that resolves, the
same response also includes `full_size` (the compressed image size in
bytes), which the script prints alongside each `OK` line (for example
`OK    rocm/pytorch:rocm10.1.0_..._2.14.0  (10.9 GB)`) — useful for spotting
unexpectedly large/small images. It sleeps briefly between requests to stay
under Docker Hub's rate limit (observed ~180 requests per rolling window,
unauthenticated), and backs off automatically on HTTP 429. It exits non-zero
if any tag fails to resolve, and prints a final summary list of failures
grouped by file.

With ~119 tags across all five files, a full run takes roughly a minute.

## Interpreting failures

A `FAIL` (HTTP 404) means the tag doesn't currently exist on Docker Hub. This
has two very different causes — check which one before touching any docs:

1. **Not yet published.** During an active ROCm release, framework Docker
   images are often built and pushed to Docker Hub *after* the docs are
   drafted. If every failure in a run shares the same (newest) `rocm_ver`
   across multiple files, and every tag for older `rocm_ver`s resolves fine,
   that's a strong signal the images simply haven't landed yet — not a docs
   bug. Don't "fix" the tag strings in this case; re-run the validator
   periodically (or re-run before the release ships) until they resolve.
2. **Genuine data error.** A typo, a stale naming convention (e.g. a Python- or
   Ubuntu-version segment that doesn't match how the image was actually
   tagged), or a tag that was renamed upstream. Suspect this when failures are
   scattered across multiple `rocm_ver`s, or isolated among otherwise-passing
   tags for the same release. Cross-check against the real tag list for that
   repo, for example:

   ```sh
   curl -s "https://hub.docker.com/v2/repositories/rocm/pytorch/tags/?page_size=100&name=<fragment>" \
     | python3 -m json.tool
   ```

   to search for the closest actual tag name, then correct the YAML value to
   match and re-run the validator to confirm.

Do not edit `docs/data/docker-tags/*.yaml` based on a 404 alone — confirm
which case applies first, and only change values you've confirmed are wrong
(case 2). Never invent a replacement tag; only use one you've verified exists.

## After fixing a genuine error

Re-run the validator to confirm the fix, then rebuild the docs (see
`AGENTS.md` for the Sphinx build command) to confirm the page still renders
cleanly, since these tags also appear in generated `docker pull`/`docker run`
code blocks.
