:selector-toc2: Installation environment
:selector-toc2-icon: fa-solid fa-computer

.. |SGLANG_VERSION| replace:: 0.15.3post1

.. |SGLANG_DOCKER_TAG_ALL| replace:: rocm/sgl-dev:v0.5.13.post1-ubuntu24.04-py3.14-rocm7.14

.. |SGLANG_DOC| replace:: `SGLang <https://docs.sglang.io/>`__
.. |SGLANG_USAGE_DOC| replace:: `Basic usage (SGLang docs) <https://docs.sglang.io/docs/basic_usage/overview>`__
.. |SGLANG_DOCKER_INSTALL_DOC| replace:: `Using Docker (SGLang docs) <https://docs.sglang.io/docs/hardware-platforms/amd_gpu#install-using-docker-recommended>`__
.. |SGLANG_PIP_INSTALL_DOC| replace:: `With pip or uv (SGLang docs) <https://docs.sglang.io/docs/get-started/install#method-1-with-pip-or-uv>`__

************************************
SGLang inference and serving on ROCm
************************************

|SGLANG_DOC| is an open-source library for fast, memory-efficient LLM inference
and serving. This page describes how to set up and run SGLang on AMD GPUs
using either a prebuilt Docker image (recommended) or pip. It applies to
`supported AMD GPUs and platforms <https://rocm.docs.amd.com/en/docs-7.14.0/about/release-notes.html#ai-ecosystem-support>`__.

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

.. selector:: SGLang version
   :key: sgl-ver

   .. selector-option:: 0.15.3post1
      :value: 0.15.3
      :width: 12

.. selector:: Installation method
   :key: i

   .. selector-option:: Docker
      :value: docker
      :width: 12

Prerequisites
=============

- For Instinct and Radeon devices, ensure your host system has the AMD GPU
  Driver (amdgpu) installed. See the `ROCm compatibility matrix <https://rocm.docs.amd.com/en/docs-7.14.0/compatibility/compatibility-matrix.html>`__ for driver support
  information. For installation instructions, see the `AMD GPU Driver
  documentation
  <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.0/index.html>`__.

- Ensure the host system has `Docker Engine
  <https://docs.docker.com/engine/install/>`__ installed.

.. selected:: i=docker
   :heading: Get started

   .. selected:: fam=all

      1. Pull the ROCm SGLang |SGLANG_VERSION| Docker image.

         .. code-block:: bash
            :substitutions:

            docker pull |SGLANG_DOCKER_TAG_ALL|

      2. Start the Docker container.

         .. code-block:: bash
            :substitutions:

            docker run -it --rm \
               --device /dev/kfd \
               --device /dev/dri \
               --network=host \
               --ipc=host \
               --group-add=video \
               --cap-add=SYS_PTRACE \
               --security-opt seccomp=unconfined \
               -v <path/to/your/models>:/app/models \
               -e HF_HOME="/app/models" \
               |SGLANG_DOCKER_TAG_ALL| \
               bash

   .. selected:: fam=instinct

      1. Pull the ROCm SGLang |SGLANG_VERSION| Docker image.

         .. code-block:: bash
            :substitutions:

            docker pull |SGLANG_DOCKER_TAG_ALL|

      2. Start the Docker container.

         .. code-block:: bash
            :substitutions:

            docker run -it --rm \
               --device /dev/kfd \
               --device /dev/dri \
               --network=host \
               --ipc=host \
               --group-add=video \
               --cap-add=SYS_PTRACE \
               --security-opt seccomp=unconfined \
               -v <path/to/your/models>:/app/models \
               -e HF_HOME="/app/models" \
               |SGLANG_DOCKER_TAG_ALL| \
               bash

   .. selected:: fam=radeon fam=ryzen

      1. Pull the ROCm SGLang |SGLANG_VERSION| Docker image.

         .. code-block:: bash
            :substitutions:

            docker pull |SGLANG_DOCKER_TAG_ALL|

      2. Start the Docker container. On Radeon GPUs, disable AITER by unsetting
         ``SGLANG_USE_AITER`` and ``SGLANG_ROCM_FUSED_DECODE_MLA``. See the
         :ref:`known issue <sglang-aiter-ki>` for more information.

         .. code-block:: bash
            :substitutions:

            docker run -it --rm \
               --device /dev/kfd \
               --device /dev/dri \
               --network=host \
               --ipc=host \
               --group-add=video \
               --cap-add=SYS_PTRACE \
               --security-opt seccomp=unconfined \
               -v <path/to/your/models>:/app/models \
               -e HF_HOME="/app/models" \
               -e SGLANG_USE_AITER=false \
               -e SGLANG_ROCM_FUSED_DECODE_MLA=false \
               |SGLANG_DOCKER_TAG_ALL| \
               bash

   .. seealso::

      |SGLANG_DOCKER_INSTALL_DOC|

   3. After setting up your environment, follow the SGLang |SGLANG_VERSION| usage
      documentation to get started: |SGLANG_USAGE_DOC|.

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
