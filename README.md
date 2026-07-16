<div align="center">
  <img src="docs/images/amd-rocm-logo.png" width="200px" alt="ROCm logo">
  <h3 align="center">
    AI frameworks, inference, and training on AMD GPUs
  </h3>
  <p align="center">
    <a href="https://rocm.docs.amd.com/en/latest/">
      <b>ROCm Core SDK</b>
    </a>
    <span> • </span>
    <a href="https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/">
      <b>AI Ecosystem</b>
    </a>
    <span> • </span>
    <a href="https://instinct.docs.amd.com/latest/">
      <b>GPU Systems and Infrastructure</b>
    </a>
    <span> • </span>
    <a href="https://rocm.blogs.amd.com/">
      <b>Blogs</b>
    </a>
  </p>
</div>

# AMD ROCm™ AI Ecosystem

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/AMD-Ecosystem/ai-ecosystem/badge)](https://scorecard.dev/viewer/?uri=github.com/AMD-Ecosystem/ai-ecosystem)

This repository contains the documentation source for the ROCm AI ecosystem:
guides covering framework installation and setup, large-scale model training,
LLM and diffusion inference serving, and AI workload performance optimization
on AMD GPUs. The ROCm AI ecosystem lives on top of the [ROCm Core
SDK](https://rocm.docs.amd.com/en/latest/), which provides the underlying GPU
runtimes (HIP), compilers, and math libraries for ROCm-accelerated workloads.

>[!IMPORTANT]
>To learn about supported AMD GPUs and operating systems, see the latest [ROCm
>Core SDK release notes](https://rocm.docs.amd.com/en/latest/about/release-notes.html)
>or the [compatibility matrix](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html).

## Build the documentation

This repository builds with Sphinx using the same setup as the other ROCm
documentation projects.

### Linux and WSL

```sh
python3 -mvenv .venv
.venv/bin/python -m pip install -r docs/sphinx/requirements.txt
.venv/bin/python -m sphinx -T -E -b html -d _build/doctrees -D language=en docs _build/html
```

### Windows

```powershell
python -mvenv .venv
.venv\Scripts\python.exe -m pip install -r docs/sphinx/requirements.txt
.venv\Scripts\python.exe -m sphinx -T -E -b html -d _build/doctrees -D language=en docs _build/html
```

Open `_build/html/index.html` in a web browser to view the result.

For further information, see [building documentation](https://rocm.docs.amd.com/en/latest/contribute/building.html).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines and the
[ROCm contribution guide](https://rocm.docs.amd.com/en/latest/contribute/contributing.html)
for the broader process.

## Security

See [SECURITY.md](SECURITY.md) for the security policy and how to report a vulnerability.

## License

See [LICENSE](LICENSE).
