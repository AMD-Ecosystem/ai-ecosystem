# AGENTS.md

Guidance for AI coding agents (and people) working in the ROCm AI Ecosystem
documentation. This is the single source of truth for agent instructions:
OpenCode reads `AGENTS.md` directly and Claude Code reads it when no
`CLAUDE.md` is present.

## What this repo is

Sphinx documentation source for the ROCm AI ecosystem — framework installation,
training, LLM and diffusion inference, and performance optimization on AMD GPUs.
Published HTML at <https://rocm.docs.amd.com/projects/ai-ecosystem/>.

Layout:

- `docs/` — all content and configuration.
  - `docs/frameworks/{pytorch,jax,tensorflow}/` — framework install guides.
  - `docs/inference/`, `docs/optimization/`, `docs/system-setup/` — topical guides.
  - `docs/data/` — shared YAML data (see below).
  - `docs/templates/` — Jinja templates used by `.. datatemplate::`.
  - `docs/extension/rocm_docs_custom/` — local Sphinx extensions.
  - `docs/sphinx/` — `_toc.yml.in`, `requirements.{in,txt}`, static assets.
  - `docs/conf.py` — Sphinx configuration and extension registration.
- `tools/` — maintenance scripts.
- `.claude/skills/` — agent skills.

## Build and verify

```sh
python3 -mvenv .venv
.venv/bin/python -m pip install -r docs/sphinx/requirements.txt
.venv/bin/python -m sphinx -j auto -T -E docs/ _build/
```

- Open `_build/html/index.html` to review.
- Confirm the build has no new errors or warnings before proposing changes.
- Re-run with `-E` (or `touch` the changed `.rst`) when you change templates or
  data files, because incremental builds can miss those.
- Only pre-existing warnings are acceptable; do not add new ones. If a warning
  is unrelated to your change, leave it alone rather than fixing it in the same
  commit.
- CI runs the `rocm-docs-core` linting workflow (`.github/workflows/linting.yml`).

If intersphinx fetching is rate-limited and the build emits related errors or
warnings, disable remote inventory fetching by appending
`-D external_projects_remote_repository=""` to the build command:

```sh
.venv/bin/python -m sphinx -j auto -T -E -D external_projects_remote_repository="" docs _build/html
```

Expect `unknown document` warnings for cross-project references in this mode,
because those references cannot be resolved offline.

## Content conventions

Follow `CONTRIBUTING.md` and the broader
[ROCm documentation conventions](https://rocm.docs.amd.com/en/latest/contribute/contributing.html):

- Follow the [Google developer documentation style guide](https://developers.google.com/style).
  - Second-person voice; sentence-case headings.
  - Language tags on every code block.
  - Prefer evergreen wording over version-specific details.
- Match the style and structure of neighboring pages.
- New pages must be registered in `docs/sphinx/_toc.yml.in` and `docs/index.md`
  for discoverability in the navigation sidebar.
- Pages are written in [MyST-flavored
  Markdown](https://myst-parser.readthedocs.io/en/latest/) or reStructuredText.
  Prefer reStructuredText when dealing with nested directives; otherwise, default
  to MyST Markdown.

## Scope and temp files

- Do not edit generated artifacts (`_build/`, generated `_toc.yml`).
- Load the `rocdoc-update-gpus-list` skill (`.claude/skills/rocdoc-update-gpus-list/SKILL.md`)
  when updating the GPU catalog.
