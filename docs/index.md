# AMD ROCm AI ecosystem

[ROCm](https://rocm.docs.amd.com/en/latest/) is AMD's open software platform
for GPU computing. This documentation covers the AI ecosystem built on ROCm
  — from framework setup and training to inference serving and performance
  optimization.

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card} Deep learning frameworks
Install popular deep learning on AMD GPUs. Includes hardware-specific
instructions for AMD Instinct and Radeon GPUs and Ryzen APUs across Linux and
Windows using pip.

- [Install PyTorch](frameworks/pytorch/install)
- [Install JAX](frameworks/jax/install)
- [Install TensorFlow](frameworks/tensorflow/install)
:::

:::{grid-item-card} Inference
Serve LLMs and generative AI models using high-performance inference
frameworks.

- [vLLM](inference/vllm)
- [SGLang](inference/sglang)
- [ATOM](https://rocm.docs.amd.com/projects/atom)
- [llama.cpp](inference/llamacpp)
- [MIGraphX](inference/migraphx)
- [ONNX Runtime](inference/onnxruntime)
- [xDiT](inference/xdit)
- [ComfyUI](inference/comfy)
:::

:::{grid-item-card} Distributed inference
Infera orchestrates vLLM, SGLang, or ATOM workers and adds AMD-native tiered KV
cache. The MoRI recipes cover prefill-decode disaggregated serving over RDMA
networking on MI355X clusters.

- [Infera](https://rocm.docs.amd.com/projects/infera)
- [vLLM with MoRI recipe](inference/distributed/vllm-mori-recipe)
- [SGLang with MoRI recipe](inference/distributed/sglang-mori-recipe)
:::

:::{grid-item-card} Training
Train and scale models on AMD GPUs. Primus provides end-to-end training
infrastructure for multiple popular backend frameworks, including Megatron,
TorchTitan, and MaxText.

- [Primus](https://rocm.docs.amd.com/projects/primus)
:::

:::{grid-item-card} GPU kernel development
Write and optimize high-performance GPU kernels for AMD hardware using Python
DSLs, MLIR compiler stacks, and C++ template libraries.

- [FlyDSL](https://rocm.docs.amd.com/projects/FlyDSL)
- [Optimize Triton kernels](optimization/optimize-triton-kernels)
- [Optimize with Composable Kernel](optimization/optimize-with-composable-kernel)
:::

:::{grid-item-card} Optimization
Improve throughput, latency, and memory efficiency for AI workloads on AMD Instinct GPUs.

- [Workload optimization](optimization/workload-optimization)
- [vLLM V1 performance](optimization/vllm-v1-optimization)
- [Model quantization](optimization/model-quantization)
- [Model acceleration libraries](optimization/model-acceleration-libs)
:::

:::{grid-item-card} Tutorials
Hands-on guides and recipes for building AI applications on AMD hardware.

- [AI Playbooks](https://developer.amd.com/playbooks)
- [AI Developer Hub](https://rocm.docs.amd.com/projects/ai-developer-hub)
:::

::::
