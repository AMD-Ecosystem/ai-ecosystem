:selector-toc2: Installation environment
:selector-toc2-icon: fa-solid fa-computer

****************************
SGLang inference and serving
****************************

`SGLang <https://docs.sglang.io/>`__ is an open-source library for fast,
memory-efficient LLM inference and serving. This page describes how to set up
and run SGLang on AMD GPUs using either a prebuilt Docker image (recommended)
or pip. It applies to `supported AMD GPUs and platforms
<https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support>`__.

.. selector:: Device family
   :key: fam

   .. selector-option:: AMD Instinct™
      :value: instinct w=compute
      :width: 6
      :toc-label: AMD Instinct

   .. selector-option:: AMD Radeon™
      :value: radeon w=compute
      :width: 6
      :toc-label: AMD Radeon

.. ================================================================ GPU / APU ==

.. selected:: fam=instinct fam=radeon fam=ryzen

   .. selector-dropdown:: Instinct GPU
      :key: gpu
      :show-cond: fam=instinct
      :sort: desc

      .. selector-option:: AMD Instinct MI355X (gfx950)
         :value: mi355x gfx=gfx950

      .. selector-option:: AMD Instinct MI350X (gfx950)
         :value: mi350x gfx=gfx950

      .. selector-option:: AMD Instinct MI350P (gfx950)
         :value: mi350p gfx=gfx950

      .. selector-option:: AMD Instinct MI325X (gfx942)
         :value: mi325x gfx=gfx942

      .. selector-option:: AMD Instinct MI300X (gfx942)
         :value: mi300x gfx=gfx942

      .. selector-option:: AMD Instinct MI300A (gfx942)
         :value: mi300a gfx=gfx942

   .. selector-dropdown:: Radeon GPU
      :key: gpu
      :show-cond: fam=radeon
      :sort: desc

      .. selector-option:: AMD Radeon AI PRO R9700 (gfx1201)
         :value: ai-r9700 gfx=gfx1201

      .. selector-option:: AMD Radeon AI PRO R9600D (gfx1201)
         :value: ai-r9600d gfx=gfx1201

      .. selector-option:: AMD Radeon RX 9070 XT (gfx1201)
         :value: rx-9070-xt gfx=gfx1201

      .. selector-option:: AMD Radeon RX 9070 GRE (gfx1201)
         :value: rx-9070-gre gfx=gfx1201

      .. selector-option:: AMD Radeon RX 9070 (gfx1201)
         :value: rx-9070 gfx=gfx1201

      .. selector-option:: AMD Radeon RX 9060 XT LP (gfx1200)
         :value: rx-9060-xt-lp gfx=gfx1200

      .. selector-option:: AMD Radeon RX 9060 XT (gfx1200)
         :value: rx-9060-xt gfx=gfx1200

      .. selector-option:: AMD Radeon RX 9060 (gfx1200)
         :value: rx-9060 gfx=gfx1200

      .. selector-option:: AMD Radeon RX 9050 (4GB) (gfx1200)
         :value: rx-9050-4gb gfx=gfx1200

      .. selector-option:: AMD Radeon RX 9050 (gfx1200)
         :value: rx-9050 gfx=gfx1200

      .. selector-option:: AMD Radeon PRO W7900 Dual Slot (gfx1100)
         :value: w7900-dual-slot gfx=gfx1100

      .. selector-option:: AMD Radeon PRO W7900 (gfx1100)
         :value: w7900 gfx=gfx1100

      .. selector-option:: AMD Radeon PRO W7800 48GB (gfx1100)
         :value: w7800-48gb gfx=gfx1100

      .. selector-option:: AMD Radeon PRO W7800 (gfx1100)
         :value: w7800 gfx=gfx1100

      .. selector-option:: AMD Radeon RX 7900 XTX (gfx1100)
         :value: rx-7900-xtx gfx=gfx1100

      .. selector-option:: AMD Radeon RX 7900 XT (gfx1100)
         :value: rx-7900-xt gfx=gfx1100

      .. selector-option:: AMD Radeon RX 7900 GRE (gfx1100)
         :value: rx-7900-gre gfx=gfx1100

      .. selector-option:: AMD Radeon PRO W7700 (gfx1101)
         :value: w7700 gfx=gfx1101

      .. selector-option:: AMD Radeon RX 7800 XT (gfx1101)
         :value: rx-7800-xt gfx=gfx1101

      .. selector-option:: AMD Radeon RX 7700 XT (gfx1101)
         :value: rx-7700-xt gfx=gfx1101

      .. selector-option:: AMD Radeon RX 7700 (gfx1101)
         :value: rx-7700 gfx=gfx1101

      .. selector-option:: AMD Radeon PRO V710 (gfx1101)
         :value: v710 gfx=gfx1101

      .. selector-option:: AMD Radeon RX 7600 (gfx1102)
         :value: rx-7600 gfx=gfx1102

.. selector:: ROCm version
   :key: rocm-ver

   .. selector-option:: 10.0.0
      :width: 4

   .. selector-option:: 7.14.1
      :width: 4

   .. selector-option:: 7.14.0
      :width: 4

.. selector:: SGLang version
   :key: sgl-ver

   .. selector-option:: 0.5.15
      :value: 0.5.15
      :width: 12
      :show-cond: rocm-ver=10.0.0

   .. selector-option:: 0.5.13
      :value: 0.5.13
      :width: 12
      :show-cond: rocm-ver=7.14.1 rocm-ver=7.14.0

.. selector:: Installation method
   :key: i

   .. selector-option:: Docker
      :value: docker
      :width: 12

Prerequisites
=============

.. selected:: rocm-ver=10.0.0

   - For Instinct and Radeon devices, ensure your host system has the AMD GPU
     Driver (amdgpu) installed. See the `ROCm compatibility matrix (ROCm 10.0.0) <https://rocm.docs.amd.com/en/docs-10.0.0/compatibility/compatibility-matrix.html>`__ for driver support
     information. For installation instructions, see the `AMD GPU Driver
     documentation
     <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html>`__.

.. selected:: rocm-ver=7.14.1

   - For Instinct and Radeon devices, ensure your host system has the AMD GPU
     Driver (amdgpu) installed. See the `ROCm compatibility matrix (ROCm 7.14.1) <https://rocm.docs.amd.com/en/docs-7.14.1/compatibility/compatibility-matrix.html>`__ for driver support
     information. For installation instructions, see the `AMD GPU Driver
     documentation
     <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html>`__.

.. selected:: rocm-ver=7.14.0

   - For Instinct and Radeon devices, ensure your host system has the AMD GPU
     Driver (amdgpu) installed. See the `ROCm compatibility matrix (ROCm 7.14.0) <https://rocm.docs.amd.com/en/docs-7.14.0/compatibility/compatibility-matrix.html>`__ for driver support
     information. For installation instructions, see the `AMD GPU Driver
     documentation
     <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html>`__.

- Ensure the host system has `Docker Engine
  <https://docs.docker.com/engine/install/>`__ installed.

.. include:: ./include/sglang/rocm10.0.0-docker.rst

.. include:: ./include/sglang/rocm7.14.1-docker.rst

.. include:: ./include/sglang/rocm7.14.0-docker.rst

.. selected:: fam=radeon
   :heading: Known issues

   .. _sglang-aiter-ki:

   ROCm 7.14 introduces initial SGLang support for AMD Radeon GPUs. Radeon GPU
   users should disable AITER and unset ``SGLANG_ROCM_FUSED_DECODE_MLA``, as
   both are enabled by default in the SGLang Docker image and may cause some
   workloads to fail. See the `SGLang environment variables reference
   <https://docs.sglang.io/docs/references/environment_variables#environment-variables>`__
   for more details.

   .. code-block:: bash

      export SGLANG_USE_AITER=false
      export SGLANG_ROCM_FUSED_DECODE_MLA=false

   Additionally, some models may not function correctly on Radeon GPUs,
   including certain Mixture-of-Experts (MoE) models (such as GPT-OSS-20B and
   MiniMax-M2.7) and Qwen3-ASR models. Users experiencing these issues are
   recommended to use the latest upstream SGLang versions, which will include
   the necessary fixes once they are merged.

   * SGLang inference workloads using the default AITER attention backend might
     fail on some AMD Radeon graphics products, such as the Radeon PRO W7900,
     Radeon AI PRO R9700, and Radeon RX 9070 XT. As a workaround, configure
     SGLang to use the Triton attention backend (``--attention-backend triton``)
     or disable AITER:

     .. code-block:: bash

        export SGLANG_USE_AITER=0
        export SGLANG_USE_AITER_AR=0
