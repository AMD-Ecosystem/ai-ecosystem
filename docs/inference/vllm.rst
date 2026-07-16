:selector-toc2: Installation environment
:selector-toc2-icon: fa-solid fa-computer

.. |VLLM_VERSION| replace:: 0.23

.. |VLLM_DOCKER_TAG_CDNA| replace:: docker pull rocm/vllm:rocm7.14.0_cdna_ubuntu24.04_py3.14_pytorch_2.11.0_vllm_0.23.0
.. |VLLM_DOCKER_TAG_RDNA| replace:: rocm/vllm:rocm7.14.0_rdna_ubuntu24.04_py3.14_pytorch_2.11.0_vllm_0.23.0

.. |VLLM_DOC| replace:: `vLLM <https://docs.vllm.ai/en/v0.23.0/>`__
.. |VLLM_USAGE_DOC| replace:: `Using vLLM <https://docs.vllm.ai/en/v0.23.0/usage/>`__
.. |VLLM_DOCKER_INSTALL_DOC| replace:: `Set up using Docker (vLLM docs) <https://docs.vllm.ai/en/v0.23.0/getting_started/installation/gpu/#amd-rocm_5>`__
.. |VLLM_PIP_INSTALL_DOC| replace:: `Set up using Python (vLLM docs) <https://docs.vllm.ai/en/v0.23.0/getting_started/installation/gpu/#amd-rocm_3>`__

**********************************
vLLM inference and serving on ROCm
**********************************

|VLLM_DOC| is an open-source library for fast, memory-efficient LLM inference
and serving. This page describes how to set up and run vLLM on AMD GPUs and
APUs using either a prebuilt Docker image (recommended) or pip. It applies to
`supported AMD GPUs and platforms <https://rocm.docs.amd.com/en/docs-7.14.0/about/release-notes.html#ai-ecosystem-support>`__.

.. selector:: Device family
   :key: fam

   .. selector-option:: AMD Instinct™
      :value: instinct w=compute
      :width: 4
      :toc-label: AMD Instinct

   .. selector-option:: AMD Radeon™
      :value: radeon w=compute
      :width: 4
      :toc-label: AMD Radeon

   .. selector-option:: AMD Ryzen™
      :value: ryzen w=compute
      :width: 4
      :toc-label: AMD Ryzen

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

   .. selector-dropdown:: Ryzen APU
      :key: gpu
      :show-cond: fam=ryzen

      .. selector-option:: AMD Ryzen AI Max+ PRO 395 (gfx1151)
         :value: max-pro-395 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max PRO 390 (gfx1151)
         :value: max-pro-390 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max PRO 385 (gfx1151)
         :value: max-pro-385 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max PRO 380 (gfx1151)
         :value: max-pro-380 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max+ 395 (gfx1151)
         :value: max-395 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max+ 392 (gfx1151)
         :value: max-392 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max+ 388 (gfx1151)
         :value: max-388 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max 390 (gfx1151)
         :value: max-390 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max 385 (gfx1151)
         :value: max-385 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI 9 PRO HX 475 (gfx1150)
         :value: ai-9-pro-hx-475 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 9 PRO HX 470 (gfx1150)
         :value: ai-9-pro-hx-470 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 9 PRO 465 (gfx1150)
         :value: ai-9-pro-465 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 7 PRO 450 (gfx1152)
         :value: ai-7-pro-450 gfx=gfx1152

      .. selector-option:: AMD Ryzen AI 5 PRO 440 (gfx1152)
         :value: ai-5-pro-440 gfx=gfx1152

      .. selector-option:: AMD Ryzen AI 9 HX 475 (gfx1150)
         :value: ai-9-hx-475 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 9 HX 470 (gfx1150)
         :value: ai-9-hx-470 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 9 465 (gfx1150)
         :value: ai-9-465 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 7 450 (gfx1152)
         :value: ai-7-450 gfx=gfx1152

      .. selector-option:: AMD Ryzen AI 9 HX PRO 375 (gfx1150)
         :value: 9-hx-pro-375 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 9 HX PRO 370 (gfx1150)
         :value: 9-hx-pro-370 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 7 PRO 350 (gfx1152)
         :value: ai-7-pro-350 gfx=gfx1152

      .. selector-option:: AMD Ryzen AI 5 PRO 340 (gfx1152)
         :value: ai-5-pro-340 gfx=gfx1152

      .. selector-option:: AMD Ryzen AI 9 HX 375 (gfx1150)
         :value: 9-hx-375 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 9 HX 370 (gfx1150)
         :value: 9-hx-370 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 9 365 (gfx1150)
         :value: 9-365 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 7 350 (gfx1152)
         :value: ai-7-350 gfx=gfx1152

      .. selector-option:: AMD Ryzen AI 7 345 (gfx1152)
         :value: ai-7-345 gfx=gfx1152

      .. selector-option:: AMD Ryzen AI 5 340 (gfx1152)
         :value: ai-5-340 gfx=gfx1152

      .. selector-option:: AMD Ryzen AI 5 330 (gfx1152)
         :value: ai-5-330 gfx=gfx1152

.. selector:: vLLM version
   :key: vllm-ver

   .. selector-option:: 0.23
      :value: 0.23
      :width: 12

.. selector:: Installation method
   :key: i

   .. selector-option:: Docker
      :value: docker
      :width: 6

   .. selector-option:: pip
      :value: pip
      :width: 6

Prerequisites
=============

.. selected:: i=docker

   .. selected:: fam=all fam=instinct fam=radeon

      - For Instinct and Radeon devices, ensure your host system has the AMD
        GPU Driver (amdgpu) installed. See the `ROCm compatibility matrix <https://rocm.docs.amd.com/en/docs-7.14.0/compatibility/compatibility-matrix.html>`__ for driver
        support information. For installation instructions, see the `AMD GPU
        Driver documentation
        <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.0/index.html>`__.

      - Ensure the host system has `Docker Engine
        <https://docs.docker.com/engine/install/>`__ installed.

   .. selected:: fam=ryzen

      Ensure the host system has `Docker Engine
      <https://docs.docker.com/engine/install/>`__ installed.

.. selected:: i=pip

   .. selected:: fam=all fam=instinct fam=radeon

      * For Instinct and Radeon devices, ensure your system has the AMD GPU
        Driver (amdgpu) installed. See the `ROCm compatibility matrix <https://rocm.docs.amd.com/en/docs-7.14.0/compatibility/compatibility-matrix.html>`__ for driver
        support information. For installation instructions, see the `AMD GPU
        Driver documentation
        <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.0/index.html>`__.

   * Ensure your system has `Python 3.14
     <https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support>`__
     installed and accessible.

   * Install `uv <https://docs.astral.sh/uv/getting-started/installation/>`__.

     .. note::

        It's recommended to use `uv <https://docs.astral.sh/uv/pip/>`__ to install
        the vLLM wheel. vLLM has many transitive dependencies, and pip may
        silently pull incompatible versions from PyPI when installing from a
        direct wheel URL. ``uv pip`` resolves dependencies more predictably,
        respecting the exact versions bundled with or required by the wheel.

.. selected:: i=docker
   :heading: Get started

   .. selected:: fam=instinct

      1. Pull the ROCm vLLM |VLLM_VERSION| Docker image.

         .. code-block:: bash
            :substitutions:

            docker pull |VLLM_DOCKER_TAG_CDNA|

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
               |VLLM_DOCKER_TAG_CDNA| \
               bash

   .. selected:: fam=radeon fam=ryzen

      1. Pull the ROCm vLLM |VLLM_VERSION| Docker image.

         .. code-block:: bash
            :substitutions:

            docker pull |VLLM_DOCKER_TAG_RDNA|

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
               |VLLM_DOCKER_TAG_RDNA| \
               bash

   .. seealso::

      |VLLM_DOCKER_INSTALL_DOC|

   3. After setting up your environment, follow the vLLM |VLLM_VERSION| usage
      documentation to get started: |VLLM_USAGE_DOC|.

.. selected:: i=pip
   :heading: Install vLLM using pip

   1. Set up your Python virtual environment.

      .. code-block:: shell

         python3.14 -m venv .venv

   2. Activate your Python virtual environment.

      .. code-block:: shell

         source .venv/bin/activate

   3. Install PyTorch 2.11 in your virtual environment. This should also
      install the ROCm core libraries as a dependency.

      .. selected:: gfx=gfx950

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx950]==2.11.0+rocm7.14.0" \
                "torchvision[device-gfx950]==0.26.0+rocm7.14.0" \
                "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx942

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx942]==2.11.0+rocm7.14.0" \
                "torchvision[device-gfx942]==0.26.0+rocm7.14.0" \
                "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1200

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx1200]==2.11.0+rocm7.14.0" \
                "torchvision[device-gfx1200]==0.26.0+rocm7.14.0" \
                "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1201

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx1201]==2.11.0+rocm7.14.0" \
                "torchvision[device-gfx1201]==0.26.0+rocm7.14.0" \
                "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1100

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx1100]==2.11.0+rocm7.14.0" \
                "torchvision[device-gfx1100]==0.26.0+rocm7.14.0" \
                "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1101

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx1101]==2.11.0+rocm7.14.0" \
                "torchvision[device-gfx1101]==0.26.0+rocm7.14.0" \
                "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1102

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx1102]==2.11.0+rocm7.14.0" \
                "torchvision[device-gfx1102]==0.26.0+rocm7.14.0" \
                "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1103

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx1103]==2.11.0+rocm7.14.0" \
                "torchvision[device-gfx1103]==0.26.0+rocm7.14.0" \
                "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1151

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx1151]==2.11.0+rocm7.14.0" \
                "torchvision[device-gfx1151]==0.26.0+rocm7.14.0" \
                "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1150

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx1150]==2.11.0+rocm7.14.0" \
                "torchvision[device-gfx1150]==0.26.0+rocm7.14.0" \
                "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1152

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx1152]==2.11.0+rocm7.14.0" \
                "torchvision[device-gfx1152]==0.26.0+rocm7.14.0" \
                "torchaudio==2.11.0+rocm7.14.0"

   4. Install Flash Attention.

      .. selected:: fam=instinct

         .. code-block:: bash

            python -m pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-cdna/flash-attn/flash_attn-2.8.3-cp314-cp314-linux_x86_64.whl

      .. selected:: fam=radeon fam=ryzen

         .. code-block:: bash

            python -m pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-rdna/flash-attn/flash_attn-2.8.3-py3-none-any.whl

   .. selected:: fam=instinct

      5. Install `AITER <https://github.com/rocm/aiter>`__.

         .. code-block:: bash

            python -m pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-cdna/amd-aiter/amd_aiter-0.1.13.post2.dev1%2Bgb32deb267-cp314-cp314-linux_x86_64.whl

      6. Install the vLLM 0.23.1 wheel using ``uv pip``.

         .. code-block:: bash

            uv pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-cdna/vllm/vllm-0.23.1.dev1%2Brocm7.14.0.g9ddef7117.d20260715-cp314-cp314-linux_x86_64.whl

   .. selected:: fam=instinct

      7. Set the following environment variables to prevent errors related to ROCm platform and Flash Attention availability when running vLLM.

         .. code-block:: bash

            export PYTHONPATH=$VIRTUAL_ENV/lib/python3.14/site-packages/_rocm_sdk_core/share/amd_smi
            export FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE

      8. Check your installation.

         .. code-block:: bash

            python -c "import vllm; print('vLLM version:', vllm.__version__)"
            python -c "import torch; print('PyTorch:', torch.__version__); print('HIP available:', torch.cuda.is_available()); print('HIP built:', torch.backends.hip.is_built() if hasattr(torch.backends, 'hip') else 'N/A')"
            python -c "import flash_attn; print('flash-attn:', flash_attn.__version__)"

      9. After setting up your environment, follow the vLLM 0.23.1 usage
         documentation to get started: |VLLM_USAGE_DOC|.

   .. selected:: fam=radeon fam=ryzen

      5. Install the vLLM 0.23.1 wheel using ``uv pip``.

         .. code-block:: bash

            uv pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-rdna/vllm/vllm-0.23.1%2Brocm7.14.0-cp314-cp314-linux_x86_64.whl

      6. Set the following environment variables to prevent errors related to ROCm platform and Flash Attention availability when running vLLM.

         .. code-block:: bash

            export PYTHONPATH=$VIRTUAL_ENV/lib/python3.14/site-packages/_rocm_sdk_core/share/amd_smi
            export FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE

      7. Check your installation.

         .. code-block:: bash

            python -c "import vllm; print('vLLM version:', vllm.__version__)"
            python -c "import torch; print('PyTorch:', torch.__version__); print('HIP available:', torch.cuda.is_available()); print('HIP built:', torch.backends.hip.is_built() if hasattr(torch.backends, 'hip') else 'N/A')"
            python -c "import flash_attn; print('flash-attn:', flash_attn.__version__)"

      8. After setting up your environment, follow the vLLM |VLLM_VERSION| usage
         documentation to get started: |VLLM_USAGE_DOC|.

   .. seealso::

      |VLLM_PIP_INSTALL_DOC|

.. selected:: fam=radeon fam=ryzen
   :heading: Known issues

   * Significantly longer warmup times might be observed in some large language
     model inference workloads on AMD Radeon GPUs using vLLM versions v0.21.0
     through v0.25.0. As a workaround, use a vLLM release earlier than v0.21.0
     or upgrade to vLLM v0.26.0 or later, which includes a fix for this issue.
