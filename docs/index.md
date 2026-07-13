# AMD ROCm AI ecosystem

[ROCm](https://rocm.docs.amd.com/en/latest/) is AMD's open software platform
for GPU computing. This documentation covers the full AI ecosystem built on
ROCm — from framework setup and training to inference serving and performance
optimization.

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card} Deep learning frameworks
Install PyTorch and JAX on AMD GPUs. Includes hardware-specific instructions
for AMD Instinct and Radeon GPUs and Ryzen APUs across Linux and Windows using
pip.

- [Install PyTorch](frameworks/pytorch/install)
- [Install JAX](frameworks/jax/install)
:::

:::{grid-item-card} Training
Scale model training across multiple AMD GPUs using PyTorch distributed primitives
(DDP, RPC, collective communication) for large models that exceed single-GPU memory.

- [Primus](https://rocm.docs.amd.com/projects/primus)
- [Scale model training](training/scale-model-training)
:::

:::{grid-item-card} Inference
Serve LLMs and generative AI models using high-performance inference frameworks.
Covers single-node and distributed multi-GPU deployments.

- [vLLM](inference/vllm)
- [SGLang](inference/sglang)
<!-- - [ATOM](https://rocm.docs.amd.com/projects/atom) -->
- [MIGraphX](inference/migraphx)
- [ONNX Runtime](inference/onnxruntime)
- [xDiT](inference/xdit)
- [ComfyUI](inference/comfy)
:::

:::{grid-item-card} Distributed inference
Multi-node prefill-decode disaggregated serving over RDMA networking
using MoRI (Modular RDMA Interface) on MI355X clusters.

- [vLLM with MoRI recipe](inference/distributed/vllm-mori-recipe)
- [SGLang with MoRI recipe](inference/distributed/sglang-mori-recipe)
:::

:::{grid-item-card} Optimization
Improve throughput, latency, and memory efficiency for AI workloads on AMD Instinct GPUs.

- [Workload optimization](optimization/workload-optimization)
- [vLLM V1 performance](optimization/vllm-v1-optimization)
- [Model quantization](optimization/model-quantization)
- [Model acceleration libraries](optimization/model-acceleration-libs)
- [Triton kernels](optimization/optimize-triton-kernels)
- [Composable Kernel](optimization/optimize-with-composable-kernel)
:::

:::{grid-item-card} Tutorials
Hands-on guides and recipes for building AI applications on AMD hardware.

- [AI Playbooks](https://developer.amd.com/playbooks)
- [AI Developer Hub](https://rocm.docs.amd.com/projects/ai-developer-hub)
:::

::::
