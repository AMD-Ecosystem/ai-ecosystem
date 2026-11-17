:selector-toc2: Installation environment
:selector-toc2-icon: fa-solid fa-computer

.. _pytorch-install:

************************
Install PyTorch for ROCm
************************

This page guides you through installing PyTorch with ROCm support on AMD
hardware. It applies to `supported AMD GPUs and platforms
<https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support>`__.

.. selector:: ROCm version
   :key: rocm-ver

   .. selector-option:: 10.2.0
      :width: 20%

   .. selector-option:: 10.1.0
      :width: 20%

   .. selector-option:: 10.0.0
      :width: 20%

   .. selector-option:: 7.14.1
      :width: 20%

   .. selector-option:: 7.14.0
      :width: 20%

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

.. selected:: rocm-ver=10.2.0

   .. selector:: PyTorch version
      :key: pytorch-ver
      :show-cond: os=linux

      .. selector-option:: 2.15.0
         :value: 2.15.0
         :width: 4
         :show-cond: fam=instinct fam=all

      .. selector-option:: 2.14.0
         :value: 2.14.0
         :width: 4
         :show-cond: fam=instinct fam=all

      .. selector-option:: 2.13.0
         :value: 2.13.0
         :width: 4
         :show-cond: fam=instinct fam=all

      .. selector-option:: 2.15.0
         :value: 2.15.0
         :width: 12
         :show-cond: fam=radeon fam=ryzen

.. selected:: rocm-ver=10.1.0

   .. selector:: PyTorch version
      :key: pytorch-ver
      :show-cond: os=linux

      .. selector-option:: 2.14.0
         :value: 2.14.0
         :width: 4
         :show-cond: fam=instinct fam=all

      .. selector-option:: 2.13.0
         :value: 2.13.0
         :width: 4
         :show-cond: fam=instinct fam=all

      .. selector-option:: 2.12.0
         :value: 2.12.0
         :width: 4
         :show-cond: fam=instinct fam=all

      .. selector-option:: 2.14.0
         :value: 2.14.0
         :width: 12
         :show-cond: fam=radeon fam=ryzen

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

   .. selector-option:: 2.14.0
      :value: 2.14.0
      :width: 12
      :show-cond: rocm-ver=10.2.0 rocm-ver=10.1.0

   .. selector-option:: 2.13.0
      :value: 2.13.0
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

   .. selected:: rocm-ver=10.2.0

      * Ensure your system has the AMD GPU Driver (amdgpu) installed. See the
        `ROCm compatibility matrix
        <https://rocm.docs.amd.com/en/docs-10.2.0/compatibility/compatibility-matrix.html>`__
        for driver support information. For installation instructions, see the
        `AMD GPU Driver documentation
        <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.70.0/index.html>`__.

   .. selected:: rocm-ver=10.1.0

      * Ensure your system has the AMD GPU Driver (amdgpu) installed. See the
        `ROCm compatibility matrix
        <https://rocm.docs.amd.com/en/docs-10.1.0/compatibility/compatibility-matrix.html>`__
        for driver support information. For installation instructions, see the
        `AMD GPU Driver documentation
        <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.60.0/index.html>`__.

   .. selected:: rocm-ver=10.0.0

      * Ensure your system has the AMD GPU Driver (amdgpu) installed. See the
        `ROCm compatibility matrix
        <https://rocm.docs.amd.com/en/docs-10.0.0/compatibility/compatibility-matrix.html>`__
        for driver support information. For installation instructions, see the
        `AMD GPU Driver documentation
        <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/index.html>`__.

   .. selected:: rocm-ver=7.14.1 rocm-ver=7.14.0

      * Ensure your system has the AMD GPU Driver (amdgpu) installed. See the
        `ROCm compatibility matrix
        <https://rocm.docs.amd.com/en/docs-7.14.1/compatibility/compatibility-matrix.html>`__
        for driver support information. For installation instructions, see the
        `AMD GPU Driver documentation
        <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html>`__.

.. selected:: fam=all

   .. selected:: os=linux

      .. selected:: rocm-ver=10.2.0

         * On supported Instinct and Radeon systems, ensure your system has
           the AMD GPU Driver (amdgpu) installed. For installation
           instructions, see the `AMD GPU Driver documentation
           <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.70.0/index.html>`__.
           Supported Ryzen systems require the inbox kernel driver in a
           supported Ubuntu version. See the `ROCm compatibility matrix
           <https://rocm.docs.amd.com/en/docs-10.2.0/compatibility/compatibility-matrix.html>`__
           for driver support information.

      .. selected:: rocm-ver=10.1.0

         * On supported Instinct and Radeon systems, ensure your system has
           the AMD GPU Driver (amdgpu) installed. For installation
           instructions, see the `AMD GPU Driver documentation
           <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.60.0/index.html>`__.
           Supported Ryzen systems require the inbox kernel driver in a
           supported Ubuntu version. See the `ROCm compatibility matrix
           <https://rocm.docs.amd.com/en/docs-10.1.0/compatibility/compatibility-matrix.html>`__
           for driver support information.

      .. selected:: rocm-ver=10.0.0

         * On supported Instinct and Radeon systems, ensure your system has
           the AMD GPU Driver (amdgpu) installed. For installation
           instructions, see the `AMD GPU Driver documentation
           <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/index.html>`__.
           Supported Ryzen systems require the inbox kernel driver in a
           supported Ubuntu version. See the `ROCm compatibility matrix
           <https://rocm.docs.amd.com/en/docs-10.0.0/compatibility/compatibility-matrix.html>`__
           for driver support information.

      .. selected:: rocm-ver=7.14.1 rocm-ver=7.14.0

         * On supported Instinct and Radeon systems, ensure your system has
           the AMD GPU Driver (amdgpu) installed. For installation
           instructions, see the `AMD GPU Driver documentation
           <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html>`__.
           Supported Ryzen systems require the inbox kernel driver in a
           supported Ubuntu version. See the `ROCm compatibility matrix
           <https://rocm.docs.amd.com/en/docs-7.14.1/compatibility/compatibility-matrix.html>`__
           for driver support information.

   .. selected:: os=windows

      .. selected:: rocm-ver=10.2.0

         * Ensure your system has the AMD Software: Adrenalin Edition driver
           installed. See the `ROCm compatibility matrix
           <https://rocm.docs.amd.com/en/docs-10.2.0/compatibility/compatibility-matrix.html>`__
           for driver support information, and the `Adrenalin Edition
           release notes
           <https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-26-11-2.html>`__
           for details.

      .. selected:: rocm-ver=10.1.0

         * Ensure your system has the AMD Software: Adrenalin Edition driver
           installed. See the `ROCm compatibility matrix
           <https://rocm.docs.amd.com/en/docs-10.1.0/compatibility/compatibility-matrix.html>`__
           for driver support information, and the `Adrenalin Edition
           release notes
           <https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-26-11-2.html>`__
           for details.

      .. selected:: rocm-ver=10.0.0

         * Ensure your system has the AMD Software: Adrenalin Edition driver
           installed. See the `ROCm compatibility matrix
           <https://rocm.docs.amd.com/en/docs-10.0.0/compatibility/compatibility-matrix.html>`__
           for driver support information, and the `Adrenalin Edition
           release notes
           <https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-26-11-2.html>`__
           for details.

      .. selected:: rocm-ver=7.14.1 rocm-ver=7.14.0

         * Ensure your system has the AMD Software: Adrenalin Edition driver
           installed. See the `ROCm compatibility matrix
           <https://rocm.docs.amd.com/en/docs-7.14.1/compatibility/compatibility-matrix.html>`__
           for driver support information, and the `Adrenalin Edition
           release notes
           <https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-26-11-2.html>`__
           for details.

.. selected:: i=docker

   * Ensure the host system has `Docker Engine
     <https://docs.docker.com/engine/install/>`__ installed. For more guidance
     on running ROCm workloads in Docker containers, see `Run ROCm Docker
     containers
     <https://rocm.docs.amd.com/en/latest/install/docker-containers.html>`__.

.. selected:: i=pip

   .. selected:: rocm-ver=10.2.0 rocm-ver=10.1.0

      .. selected:: os=linux

         * Ensure your system has a `supported Python version
           <https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support>`__
           installed and accessible: **3.10, 3.11, 3.12, 3.13, or 3.14**.

      .. selected:: os=windows

         * Ensure your system has a `supported Python version
           <https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support>`__
           installed and accessible: **3.11, 3.12, 3.13, or 3.14**.

   .. selected:: rocm-ver=10.0.0 rocm-ver=7.14.1 rocm-ver=7.14.0

      * Ensure your system has a `supported Python version
        <https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support>`__
        installed and accessible: **3.11, 3.12, 3.13, or 3.14**.

   .. selected:: rocm-ver=10.2.0

      * Complete the ROCm Core SDK installation prerequisites. See `Prerequisites
        (Install ROCm 10.2.0)
        <https://rocm.docs.amd.com/en/docs-10.2.0/install/rocm.html#prerequisites>`__ for
        instructions.

   .. selected:: rocm-ver=10.1.0

      * Complete the ROCm Core SDK installation prerequisites. See `Prerequisites
        (Install ROCm 10.1.0)
        <https://rocm.docs.amd.com/en/docs-10.1.0/install/rocm.html#prerequisites>`__ for
        instructions.

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

.. datatemplate:yaml:: /data/docker-tags/pytorch.yaml
   :template: framework-version-docker.rst.jinja

.. selected:: i=pip
   :heading: Install PyTorch using pip

   1. Set up and activate your Python virtual environment.

      .. selected:: os=linux rocm-ver=10.2.0 rocm-ver=10.1.0

         .. tab-set::

            .. tab-item:: Python 3.14

               .. code-block:: bash

                  python3.14 -m venv .venv
                  source .venv/bin/activate

            .. tab-item:: Python 3.13

               .. code-block:: bash

                  python3.13 -m venv .venv
                  source .venv/bin/activate

            .. tab-item:: Python 3.12

               .. code-block:: bash

                  python3.12 -m venv .venv
                  source .venv/bin/activate

            .. tab-item:: Python 3.11

               .. code-block:: bash

                  python3.11 -m venv .venv
                  source .venv/bin/activate

            .. tab-item:: Python 3.10

               .. code-block:: bash

                  python3.10 -m venv .venv
                  source .venv/bin/activate

      .. selected:: os=linux rocm-ver=10.0.0 rocm-ver=7.14.1 rocm-ver=7.14.0

         .. tab-set::

            .. tab-item:: Python 3.14

               .. code-block:: bash

                  python3.14 -m venv .venv
                  source .venv/bin/activate

            .. tab-item:: Python 3.13

               .. code-block:: bash

                  python3.13 -m venv .venv
                  source .venv/bin/activate

            .. tab-item:: Python 3.12

               .. code-block:: bash

                  python3.12 -m venv .venv
                  source .venv/bin/activate

            .. tab-item:: Python 3.11

               .. code-block:: bash

                  python3.11 -m venv .venv
                  source .venv/bin/activate

      .. selected:: os=windows

         .. tab-set::

            .. tab-item:: Python 3.14

               .. code-block:: bat

                  py -3.14 -m venv .venv
                  .venv\Scripts\activate

            .. tab-item:: Python 3.13

               .. code-block:: bat

                  py -3.13 -m venv .venv
                  .venv\Scripts\activate

            .. tab-item:: Python 3.12

               .. code-block:: bat

                  py -3.12 -m venv .venv
                  .venv\Scripts\activate

            .. tab-item:: Python 3.11

               .. code-block:: bat

                  py -3.11 -m venv .venv
                  .venv\Scripts\activate

   .. include:: ./include/rocm10.2.0-pip-install.rst

   .. include:: ./include/rocm10.1.0-pip-install.rst

   .. include:: ./include/rocm10.0.0-pip-install.rst

   .. include:: ./include/rocm7.14.1-pip-install.rst

   .. include:: ./include/rocm7.14.0-pip-install.rst

   3. Verify your PyTorch installation.

      .. code-block:: shell

         python -c "import torch; print('PyTorch:', torch.__version__); print('HIP available:', torch.cuda.is_available()); print('HIP version:', torch.version.hip); print('Devices:', [torch.cuda.get_device_name(i) for i in range(torch.cuda.device_count())])"

      .. selected:: rocm-ver=10.2.0

         You should see output similar to the following with at least one GPU listed:

         .. code-block:: text

            PyTorch: 2.14.0+rocm10.2.0
            HIP available: True
            HIP version: 7.17.26434
            Devices: ['<AMD GPU name>']

.. selected:: fam=instinct rocm-ver=10.2.0 rocm-ver=10.1.0 rocm-ver=10.0.0
   :heading: Known issues

   * Hugging Face model training workloads might see 9–25% lower training
     throughput on AMD Instinct MI350X (gfx950) GPUs, including BART, GPT-2,
     DiT (Diffusion Transformers), BERT, Llama 2 70B Chat, and RoBERTa-large.
     This occurs because AOTriton 0.13b selects a suboptimal flash-attention
     backward kernel instead of the faster 3-kernel split used in AOTriton
     0.11.2b. As a workaround, rebuild PyTorch and pin AOTriton to version
     0.11.2b.

.. selected:: rocm-ver=7.14.1 rocm-ver=7.14.0
   :heading: Known issues

   .. selected:: i=pip

      * On Linux, importing PyTorch might display a rocSHMEM error message about
        a missing ``libnuma`` library.

        .. code-block:: shell-session

           E-001h rocSHMEM Could not open libnuma. Returning       NUMAWrapper@src/gda/numa_wrapper.cpp:48

        While ``libnuma`` is not required for the normal functioning of rocSHMEM,
        you can resolve this message by installing the corresponding development
        package using your Linux distribution's package manager:

        .. tab-set::

           .. tab-item:: apt

              .. code-block:: bash

                 sudo apt update && sudo apt install libnuma-dev

           .. tab-item:: dnf

              .. code-block:: bash

                 sudo dnf install numactl-devel

           .. tab-item:: zypper

              .. code-block:: bash

                 sudo zypper install libnuma-devel

.. selected:: fam=radeon fam=ryzen rocm-ver=7.14.1 rocm-ver=7.14.0
   :heading: Known issues

   * Lower-than-expected performance might be observed in some large language model
     inference workloads, including vLLM FP16 decode workloads with batch sizes of
     8 or greater, on AMD Radeon RX 7900 Series Graphics, AMD Radeon RX 7800 XT
     Graphics, and AMD Ryzen AI MAX / MAX+ Series Processors when using PyTorch
     versions earlier than 2.14. As a workaround, set the
     ``TORCH_BLAS_PREFER_HIPBLASLT=1`` environment variable to use the hipBLASLt
     backend. This setting becomes the default for these architectures in PyTorch
     2.14.

   * PyTorch training and fine-tuning workloads using Llama-Factory or Unsloth
     might experience GPU resets or application crashes on some AMD Radeon
     graphics products, such as the Radeon RX 9070 Series and Radeon AI PRO
     R9700. As a workaround, set the ``TORCH_BLAS_PREFER_HIPBLASLT=0``
     environment variable to disable hipBLASLt for training and fine-tuning
     workloads. This workaround might result in performance degradation.

.. selected:: fam=radeon fam=ryzen rocm-ver=10.0.0
   :heading: Known issues

   * PyTorch training and fine-tuning workloads using Llama-Factory or Unsloth
     might experience GPU resets or application crashes on some AMD Radeon
     graphics products, such as the Radeon RX 9070 Series and Radeon AI PRO
     R9700. As a workaround, set the ``TORCH_BLAS_PREFER_HIPBLASLT=0``
     environment variable to disable hipBLASLt for training and fine-tuning
     workloads. This workaround might result in performance degradation.
