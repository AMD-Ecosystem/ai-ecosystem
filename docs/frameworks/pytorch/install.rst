:selector-toc2: Installation environment
:selector-toc2-icon: fa-solid fa-computer

.. _pytorch-install:

************************
Install PyTorch for ROCm
************************

This pages guides you through installing PyTorch with ROCm support on AMD
hardware. It applies to `supported AMD GPUs and platforms
<https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support>`__.

.. selector:: Device family
   :key: fam

   .. selector-option:: All
      :value: all w=compute
      :width: 3

   .. selector-option:: AMD Instinct™
      :value: instinct w=compute
      :width: 3
      :toc-label: AMD Instinct

   .. selector-option:: AMD Radeon™
      :value: radeon w=compute
      :width: 3
      :toc-label: AMD Radeon

   .. selector-option:: AMD Ryzen™
      :value: ryzen w=compute
      :width: 3
      :toc-label: AMD Ryzen

.. datatemplate:yaml:: /data/gpus.yaml
   :template: gpu-selector.rst.jinja

.. selector:: Operating system
   :key: os
   :show-cond: fam=instinct

   .. selector-option:: Linux
      :value: linux
      :width: 12

.. selector:: Operating system
   :key: os
   :show-cond: fam=all fam=radeon fam=ryzen

   .. selector-option:: Linux
      :value: linux
      :width: 6

   .. selector-option:: Windows
      :value: windows
      :width: 6

.. selector:: ROCm version
   :key: rocm-ver

   .. selector-option:: 10.0.0
      :width: 4

   .. selector-option:: 7.14.1
      :width: 4

   .. selector-option:: 7.14.0
      :width: 4

.. selected:: rocm-ver=10.0.0

   .. selector:: PyTorch version
      :key: pytorch-ver
      :show-cond: os=linux

      .. selector-option:: 2.13.0
         :value: 2.13.0
         :width: 4
         :show-cond: fam=instinct fam=all

      .. selector-option:: 2.12.0
         :value: 2.12.0
         :width: 4
         :show-cond: fam=instinct fam=all

      .. selector-option:: 2.11.0
         :value: 2.11.0
         :width: 4
         :show-cond: fam=instinct fam=all

      .. selector-option:: 2.13.0
         :value: 2.13.0
         :width: 6
         :show-cond: fam=radeon fam=ryzen

      .. selector-option:: 2.12.0
         :value: 2.12.0
         :width: 6
         :show-cond: fam=radeon fam=ryzen

.. selected:: rocm-ver=7.14.1 rocm-ver=7.14.0

   .. selector:: PyTorch version
      :key: pytorch-ver
      :show-cond: os=linux

      .. selector-option:: 2.12.0
         :value: 2.12.0
         :width: 4
         :show-cond: fam=instinct fam=all

      .. selector-option:: 2.11.0
         :value: 2.11.0
         :width: 4
         :show-cond: fam=instinct fam=all

      .. selector-option:: 2.10.0
         :value: 2.10.0
         :width: 4
         :show-cond: fam=instinct fam=all

      .. selector-option:: 2.12.0
         :value: 2.12.0
         :width: 6
         :show-cond: fam=radeon fam=ryzen

      .. selector-option:: 2.11.0
         :value: 2.11.0
         :width: 6
         :show-cond: fam=radeon fam=ryzen

.. selector:: PyTorch version
   :key: pytorch-ver
   :show-cond: os=windows

   .. selector-option:: 2.13.0
      :value: 2.12.0
      :width: 12
      :show-cond: rocm-ver=10.0.0

   .. selector-option:: 2.12.0
      :value: 2.12.0
      :width: 12
      :show-cond: rocm-ver=7.14.1 rocm-ver=7.14.0

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

.. selected:: fam=instinct fam=radeon

   .. selected:: rocm-ver=10.0.0

      * Ensure your system has the AMD GPU Driver (amdgpu) installed. See the
        `ROCm compatibility matrix
        <https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html>`__
        for driver support information. For installation instructions, see the
        `AMD GPU Driver documentation
        <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/index.html>`__.

   .. selected:: rocm-ver=7.14.1 rocm-ver=7.14.0

      * Ensure your system has the AMD GPU Driver (amdgpu) installed. See the
        `ROCm compatibility matrix
        <https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html>`__
        for driver support information. For installation instructions, see the
        `AMD GPU Driver documentation
        <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.0/index.html>`__.

.. selected:: i=docker

   * Ensure the host system has `Docker Engine
     <https://docs.docker.com/engine/install/>`__ installed.

.. selected:: i=pip

   * Ensure your system has a `supported Python version
     <https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support>`__
     installed and accessible: **3.11, 3.12, 3.13, or 3.14**.

   .. selected:: rocm-ver=10.0.0

      * Complete the ROCm Core SDK installation prerequisites. See `Prerequisites
        (Install ROCm 10.0.0)
        <https://rocm.docs.amd.com/en/docs-10.0.0/install/rocm.html#prerequisites>`__ for
        instructions.

   .. selected:: rocm-ver=7.14.1

      * Complete the ROCm Core SDK installation prerequisites. See `Prerequisites
        (Install ROCm 7.14.1)
        <https://rocm.docs.amd.com/en/docs-7.14.1/install/rocm.html#prerequisites>`__ for
        instructions.

   .. selected:: rocm-ver=7.14.0

      * Complete the ROCm Core SDK installation prerequisites. See `Prerequisites
        (Install ROCm 7.14.0)
        <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html#prerequisites>`__ for
        instructions.

.. include:: ./include/rocm10.0.0-docker.rst

.. include:: ./include/rocm7.14.1-docker.rst

.. include:: ./include/rocm7.14.0-docker.rst

.. selected:: i=pip
   :heading: Install PyTorch using pip

   1. Set up your Python virtual environment.

      .. tab-set::

         .. tab-item:: Python 3.14

            .. selected:: os=linux

               .. code-block:: bash

                  python3.14 -m venv .venv

            .. selected:: os=windows

               .. code-block:: bat

                  py -3.14 -m venv .venv

         .. tab-item:: Python 3.13

            .. selected:: os=linux

               .. code-block:: bash

                  python3.13 -m venv .venv

            .. selected:: os=windows

               .. code-block:: bat

                  py -3.13 -m venv .venv

         .. tab-item:: Python 3.12

            .. selected:: os=linux

               .. code-block:: bash

                  python3.12 -m venv .venv

            .. selected:: os=windows

               .. code-block:: bat

                  py -3.12 -m venv .venv

         .. tab-item:: Python 3.11

            .. selected:: os=linux

               .. code-block:: bash

                  python3.11 -m venv .venv

            .. selected:: os=windows

               .. code-block:: bat

                  py -3.11 -m venv .venv

   2. Activate your Python virtual environment. For example:

      .. selected:: os=linux

         .. code-block:: bash

            source .venv/bin/activate

      .. selected:: os=windows

         .. code-block:: bat

            .venv\Scripts\activate

   .. include:: ./include/rocm10.0.0-pip-install.rst

   .. include:: ./include/rocm7.14.1-pip-install.rst

   .. include:: ./include/rocm7.14.0-pip-install.rst

   4. Verify your PyTorch installation.

      .. code-block:: shell

         python -c "import torch; print(torch.cuda.is_available())"

      This prints ``True`` if PyTorch and ROCm are installed properly and your AMD
      GPUs are detected.

.. selected:: fam=instinct rocm-ver=10.0.0
   :heading: Known issues

   * Hugging Face model training workloads might see 9–25% lower training
     throughput on AMD Instinct MI350X (gfx950) GPUs, including BART, GPT-2,
     DiT (Diffusion Transformers), BERT, Llama 2 70B Chat, and RoBERTa-large.
     This occurs because AOTriton 0.13b selects a suboptimal flash-attention
     backward kernel instead of the faster 3-kernel split used in AOTriton
     0.11.2b. As a workaround, rebuild PyTorch and pin AOTriton to version
     0.11.2b.

.. selected:: fam=radeon fam=ryzen
   :heading: Known issues

   * PyTorch might display a warning when importing on Linux if the system
     ``libnuma`` package is not installed on some Radeon graphics products, such
     as Radeon AI PRO R9600D. As a workaround, install the system ``libnuma``
     package or configure the library path to use the ROCm-bundled NUMA
     libraries.

   * Lower-than-expected performance might be observed in some large language model
     inference workloads, including vLLM FP16 decode workloads with batch sizes of
     8 or greater, on AMD Radeon RX 7900 Series Graphics, AMD Radeon RX 7800 XT
     Graphics, and AMD Ryzen AI MAX / MAX+ Series Processors when using PyTorch
     versions earlier than 2.14. As a workaround, set the
     TORCH_BLAS_PREFER_HIPBLASLT=1 environment variable to use the hipBLASLt
     backend. This setting becomes the default for these architectures in PyTorch
     2.14.

   * PyTorch training and fine-tuning workloads using Llama-Factory or Unsloth
     might experience GPU resets or application crashes on some AMD Radeon
     graphics products, such as the Radeon RX 9070 Series and Radeon AI PRO
     R9700. As a workaround, set the ``TORCH_BLAS_PREFER_HIPBLASLT=0``
     environment variable to disable hipBLASLt for training and fine-tuning
     workloads. This workaround might result in performance degradation.
