:selector-toc2: Installation environment
:selector-toc2-icon: fa-solid fa-computer

.. _pytorch-install:

*******************************
Install PyTorch for ROCm 7.14.0
*******************************

This topic guides you through installing PyTorch with ROCm support on AMD
hardware. It applies to `supported AMD GPUs and platforms
<https://rocm.docs.amd.com/en/docs-7.14.0/about/release-notes.html#ai-ecosystem-support>`__.

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

.. include:: /frameworks/include/gpu-selector-pytorch.rst

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

   .. selector-option:: 2.12.0
      :value: 2.12.0
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

.. selected:: fam=instinct fam=radeon

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
     installed and accessible: 3.11, 3.12, 3.13, or 3.14.

   * Complete the ROCm Core SDK installation prerequisites. See `Prerequisites
     (Install ROCm)
     <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html#prerequisites>`__ for
     instructions.

.. selected:: i=docker
   :heading: Get started

   .. selected:: pytorch-ver=2.12.0

      1. Pull the ROCm PyTorch 2.12.0 Docker image.

         .. tab-set::

            .. tab-item:: Python 3.14
               :sync: py314

               .. code-block:: bash

                  docker pull rocm/pytorch:rocm7.14_ubuntu26.04_py3.14_pytorch_release_2.12.0

            .. tab-item:: Python 3.13
               :sync: py313

               .. code-block:: bash

                  docker pull rocm/pytorch:rocm7.14_ubuntu24.04_py3.13_pytorch_release_2.12.0

            .. tab-item:: Python 3.12
               :sync: py312

               .. code-block:: bash

                  docker pull rocm/pytorch:rocm7.14_ubuntu24.04_py3.12_pytorch_release_2.12.0

            .. tab-item:: Python 3.11
               :sync: py311

               .. code-block:: bash

                  docker pull rocm/pytorch:rocm7.14_ubuntu24.04_py3.11_pytorch_release_2.12.0

   .. selected:: pytorch-ver=2.11.0

      1. Pull the ROCm PyTorch 2.11.0 Docker image.

         .. tab-set::

            .. tab-item:: Python 3.14
               :sync: py314

               .. code-block:: bash

                  docker pull rocm/pytorch:rocm7.14_ubuntu26.04_py3.14_pytorch_release_2.11.0

            .. tab-item:: Python 3.13
               :sync: py313

               .. code-block:: bash

                  docker pull rocm/pytorch:rocm7.14_ubuntu24.04_py3.13_pytorch_release_2.11.0

            .. tab-item:: Python 3.12
               :sync: py312

               .. code-block:: bash

                  docker pull rocm/pytorch:rocm7.14_ubuntu24.04_py3.12_pytorch_release_2.11.0

            .. tab-item:: Python 3.11
               :sync: py311

               .. code-block:: bash

                  docker pull rocm/pytorch:rocm7.14_ubuntu24.04_py3.11_pytorch_release_2.11.0

   .. selected:: pytorch-ver=2.10.0

      1. Pull the ROCm PyTorch 2.10.0 Docker image.

         .. tab-set::

            .. tab-item:: Python 3.14
               :sync: py314

               .. code-block:: bash

                  docker pull rocm/pytorch:rocm7.14_ubuntu26.04_py3.14_pytorch_release_2.10.0

            .. tab-item:: Python 3.13
               :sync: py313

               .. code-block:: bash

                  docker pull rocm/pytorch:rocm7.14_ubuntu24.04_py3.13_pytorch_release_2.10.0

            .. tab-item:: Python 3.12
               :sync: py312

               .. code-block:: bash

                  docker pull rocm/pytorch:rocm7.14_ubuntu24.04_py3.12_pytorch_release_2.10.0

            .. tab-item:: Python 3.11
               :sync: py311

               .. code-block:: bash

                  docker pull rocm/pytorch:rocm7.14_ubuntu24.04_py3.11_pytorch_release_2.10.0

   2. Start the Docker container.

      .. selected:: pytorch-ver=2.12.0

         .. tab-set::

            .. tab-item:: Python 3.14
               :sync: py314

               .. code-block:: bash

                  docker run -it --rm \
                     --device /dev/kfd \
                     --device /dev/dri \
                     --network=host \
                     --ipc=host \
                     --group-add=video \
                     --cap-add=SYS_PTRACE \
                     --security-opt seccomp=unconfined \
                     rocm/pytorch:rocm7.14_ubuntu26.04_py3.14_pytorch_release_2.12.0 \
                     bash

            .. tab-item:: Python 3.13
               :sync: py313

               .. code-block:: bash

                  docker run -it --rm \
                     --device /dev/kfd \
                     --device /dev/dri \
                     --network=host \
                     --ipc=host \
                     --group-add=video \
                     --cap-add=SYS_PTRACE \
                     --security-opt seccomp=unconfined \
                     rocm/pytorch:rocm7.14_ubuntu24.04_py3.13_pytorch_release_2.12.0 \
                     bash

            .. tab-item:: Python 3.12
               :sync: py312

               .. code-block:: bash

                  docker run -it --rm \
                     --device /dev/kfd \
                     --device /dev/dri \
                     --network=host \
                     --ipc=host \
                     --group-add=video \
                     --cap-add=SYS_PTRACE \
                     --security-opt seccomp=unconfined \
                     rocm/pytorch:rocm7.14_ubuntu24.04_py3.12_pytorch_release_2.12.0 \
                     bash

            .. tab-item:: Python 3.11
               :sync: py311

               .. code-block:: bash

                  docker run -it --rm \
                     --device /dev/kfd \
                     --device /dev/dri \
                     --network=host \
                     --ipc=host \
                     --group-add=video \
                     --cap-add=SYS_PTRACE \
                     --security-opt seccomp=unconfined \
                     rocm/pytorch:rocm7.14_ubuntu24.04_py3.11_pytorch_release_2.12.0 \
                     bash

      .. selected:: pytorch-ver=2.11.0

         .. tab-set::

            .. tab-item:: Python 3.14
               :sync: py314

               .. code-block:: bash

                  docker run -it --rm \
                     --device /dev/kfd \
                     --device /dev/dri \
                     --network=host \
                     --ipc=host \
                     --group-add=video \
                     --cap-add=SYS_PTRACE \
                     --security-opt seccomp=unconfined \
                     rocm/pytorch:rocm7.14_ubuntu26.04_py3.14_pytorch_release_2.11.0 \
                     bash

            .. tab-item:: Python 3.13
               :sync: py313

               .. code-block:: bash

                  docker run -it --rm \
                     --device /dev/kfd \
                     --device /dev/dri \
                     --network=host \
                     --ipc=host \
                     --group-add=video \
                     --cap-add=SYS_PTRACE \
                     --security-opt seccomp=unconfined \
                     rocm/pytorch:rocm7.14_ubuntu24.04_py3.13_pytorch_release_2.11.0 \
                     bash

            .. tab-item:: Python 3.12
               :sync: py312

               .. code-block:: bash

                  docker run -it --rm \
                     --device /dev/kfd \
                     --device /dev/dri \
                     --network=host \
                     --ipc=host \
                     --group-add=video \
                     --cap-add=SYS_PTRACE \
                     --security-opt seccomp=unconfined \
                     rocm/pytorch:rocm7.14_ubuntu24.04_py3.12_pytorch_release_2.11.0 \
                     bash

            .. tab-item:: Python 3.11
               :sync: py311

               .. code-block:: bash

                  docker run -it --rm \
                     --device /dev/kfd \
                     --device /dev/dri \
                     --network=host \
                     --ipc=host \
                     --group-add=video \
                     --cap-add=SYS_PTRACE \
                     --security-opt seccomp=unconfined \
                     rocm/pytorch:rocm7.14_ubuntu24.04_py3.11_pytorch_release_2.11.0 \
                     bash

      .. selected:: pytorch-ver=2.10.0

         .. tab-set::

            .. tab-item:: Python 3.14
               :sync: py314

               .. code-block:: bash

                  docker run -it --rm \
                     --device /dev/kfd \
                     --device /dev/dri \
                     --network=host \
                     --ipc=host \
                     --group-add=video \
                     --cap-add=SYS_PTRACE \
                     --security-opt seccomp=unconfined \
                     rocm/pytorch:rocm7.14_ubuntu26.04_py3.14_pytorch_release_2.10.0 \
                     bash

            .. tab-item:: Python 3.13
               :sync: py313

               .. code-block:: bash

                  docker run -it --rm \
                     --device /dev/kfd \
                     --device /dev/dri \
                     --network=host \
                     --ipc=host \
                     --group-add=video \
                     --cap-add=SYS_PTRACE \
                     --security-opt seccomp=unconfined \
                     rocm/pytorch:rocm7.14_ubuntu24.04_py3.13_pytorch_release_2.10.0 \
                     bash

            .. tab-item:: Python 3.12
               :sync: py312

               .. code-block:: bash

                  docker run -it --rm \
                     --device /dev/kfd \
                     --device /dev/dri \
                     --network=host \
                     --ipc=host \
                     --group-add=video \
                     --cap-add=SYS_PTRACE \
                     --security-opt seccomp=unconfined \
                     rocm/pytorch:rocm7.14_ubuntu24.04_py3.12_pytorch_release_2.10.0 \
                     bash

            .. tab-item:: Python 3.11
               :sync: py311

               .. code-block:: bash

                  docker run -it --rm \
                     --device /dev/kfd \
                     --device /dev/dri \
                     --network=host \
                     --ipc=host \
                     --group-add=video \
                     --cap-add=SYS_PTRACE \
                     --security-opt seccomp=unconfined \
                     rocm/pytorch:rocm7.14_ubuntu24.04_py3.11_pytorch_release_2.10.0 \
                     bash

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

   3. Install the appropriate ROCm-enabled PyTorch libraries for your operating
      system and AMD hardware architecture.

      .. selected:: fam=all

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-all]==2.12.0+rocm7.14.0" \
                      "torchvision[device-all]==0.27.0+rocm7.14.0" \
                      "torchaudio==2.12.0+rocm7.14.0"

            .. selected:: os=windows

               .. code-block:: bat

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-all]==2.12.0+rocm7.14.0" "torchvision[device-all]==0.27.0+rocm7.14.0" "torchaudio==2.12.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-all]==2.11.0+rocm7.14.0" \
                      "torchvision[device-all]==0.26.0+rocm7.14.0" \
                      "torchaudio==2.11.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.10.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-all]==2.10.0+rocm7.14.0" \
                      "torchvision[device-all]==0.25.0+rocm7.14.0" \
                      "torchaudio==2.10.0+rocm7.14.0"

      .. selected:: gfx=gfx950

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx950]==2.12.0+rocm7.14.0" \
                      "torchvision[device-gfx950]==0.27.0+rocm7.14.0" \
                      "torchaudio==2.12.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx950]==2.11.0+rocm7.14.0" \
                      "torchvision[device-gfx950]==0.26.0+rocm7.14.0" \
                      "torchaudio==2.11.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.10.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx950]==2.10.0+rocm7.14.0" \
                      "torchvision[device-gfx950]==0.25.0+rocm7.14.0" \
                      "torchaudio==2.10.0+rocm7.14.0"

      .. selected:: gfx=gfx942

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx942]==2.12.0+rocm7.14.0" \
                      "torchvision[device-gfx942]==0.27.0+rocm7.14.0" \
                      "torchaudio==2.12.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx942]==2.11.0+rocm7.14.0" \
                      "torchvision[device-gfx942]==0.26.0+rocm7.14.0" \
                      "torchaudio==2.11.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.10.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx942]==2.10.0+rocm7.14.0" \
                      "torchvision[device-gfx942]==0.25.0+rocm7.14.0" \
                      "torchaudio==2.10.0+rocm7.14.0"

      .. selected:: gfx=gfx90a

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx90a]==2.12.0+rocm7.14.0" \
                      "torchvision[device-gfx90a]==0.27.0+rocm7.14.0" \
                      "torchaudio==2.12.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx90a]==2.11.0+rocm7.14.0" \
                      "torchvision[device-gfx90a]==0.26.0+rocm7.14.0" \
                      "torchaudio==2.11.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.10.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx90a]==2.10.0+rocm7.14.0" \
                      "torchvision[device-gfx90a]==0.25.0+rocm7.14.0" \
                      "torchaudio==2.10.0+rocm7.14.0"

      .. selected:: gfx=gfx908

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx908]==2.12.0+rocm7.14.0" \
                      "torchvision[device-gfx908]==0.27.0+rocm7.14.0" \
                      "torchaudio==2.12.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx908]==2.11.0+rocm7.14.0" \
                      "torchvision[device-gfx908]==0.26.0+rocm7.14.0" \
                      "torchaudio==2.11.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.10.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx908]==2.10.0+rocm7.14.0" \
                      "torchvision[device-gfx908]==0.25.0+rocm7.14.0" \
                      "torchaudio==2.10.0+rocm7.14.0"

      .. selected:: gfx=gfx1200

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1200]==2.12.0+rocm7.14.0" \
                      "torchvision[device-gfx1200]==0.27.0+rocm7.14.0" \
                      "torchaudio==2.12.0+rocm7.14.0"

            .. selected:: os=windows

               .. code-block:: bat

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1200]==2.12.0+rocm7.14.0" "torchvision[device-gfx1200]==0.27.0+rocm7.14.0" "torchaudio==2.12.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1200]==2.11.0+rocm7.14.0" \
                      "torchvision[device-gfx1200]==0.26.0+rocm7.14.0" \
                      "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1201

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1201]==2.12.0+rocm7.14.0" \
                      "torchvision[device-gfx1201]==0.27.0+rocm7.14.0" \
                      "torchaudio==2.12.0+rocm7.14.0"

            .. selected:: os=windows

               .. code-block:: bat

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1201]==2.12.0+rocm7.14.0" "torchvision[device-gfx1201]==0.27.0+rocm7.14.0" "torchaudio==2.12.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1201]==2.11.0+rocm7.14.0" \
                      "torchvision[device-gfx1201]==0.26.0+rocm7.14.0" \
                      "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1100

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1100]==2.12.0+rocm7.14.0" \
                      "torchvision[device-gfx1100]==0.27.0+rocm7.14.0" \
                      "torchaudio==2.12.0+rocm7.14.0"

            .. selected:: os=windows

               .. code-block:: bat

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1100]==2.12.0+rocm7.14.0" "torchvision[device-gfx1100]==0.27.0+rocm7.14.0" "torchaudio==2.12.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1100]==2.11.0+rocm7.14.0" \
                      "torchvision[device-gfx1100]==0.26.0+rocm7.14.0" \
                      "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1101

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1101]==2.12.0+rocm7.14.0" \
                      "torchvision[device-gfx1101]==0.27.0+rocm7.14.0" \
                      "torchaudio==2.12.0+rocm7.14.0"

            .. selected:: os=windows

               .. code-block:: bat

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1101]==2.12.0+rocm7.14.0" "torchvision[device-gfx1101]==0.27.0+rocm7.14.0" "torchaudio==2.12.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1101]==2.11.0+rocm7.14.0" \
                      "torchvision[device-gfx1101]==0.26.0+rocm7.14.0" \
                      "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1102

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1102]==2.12.0+rocm7.14.0" \
                      "torchvision[device-gfx1102]==0.27.0+rocm7.14.0" \
                      "torchaudio==2.12.0+rocm7.14.0"

            .. selected:: os=windows

               .. code-block:: bat

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1102]==2.12.0+rocm7.14.0" "torchvision[device-gfx1102]==0.27.0+rocm7.14.0" "torchaudio==2.12.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1102]==2.11.0+rocm7.14.0" \
                      "torchvision[device-gfx1102]==0.26.0+rocm7.14.0" \
                      "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1103

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1103]==2.12.0+rocm7.14.0" \
                      "torchvision[device-gfx1103]==0.27.0+rocm7.14.0" \
                      "torchaudio==2.12.0+rocm7.14.0"

            .. selected:: os=windows

               .. code-block:: bat

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1103]==2.12.0+rocm7.14.0" "torchvision[device-gfx1103]==0.27.0+rocm7.14.0" "torchaudio==2.12.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1103]==2.11.0+rocm7.14.0" \
                      "torchvision[device-gfx1103]==0.26.0+rocm7.14.0" \
                      "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1030

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1030]==2.12.0+rocm7.14.0" \
                      "torchvision[device-gfx1030]==0.27.0+rocm7.14.0" \
                      "torchaudio==2.12.0+rocm7.14.0"

            .. selected:: os=windows

               .. code-block:: bat

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1030]==2.12.0+rocm7.14.0" "torchvision[device-gfx1030]==0.27.0+rocm7.14.0" "torchaudio==2.12.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1030]==2.11.0+rocm7.14.0" \
                      "torchvision[device-gfx1030]==0.26.0+rocm7.14.0" \
                      "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1151

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1151]==2.12.0+rocm7.14.0" \
                      "torchvision[device-gfx1151]==0.27.0+rocm7.14.0" \
                      "torchaudio==2.12.0+rocm7.14.0"

            .. selected:: os=windows

               .. code-block:: bat

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1151]==2.12.0+rocm7.14.0" "torchvision[device-gfx1151]==0.27.0+rocm7.14.0" "torchaudio==2.12.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1151]==2.11.0+rocm7.14.0" \
                      "torchvision[device-gfx1151]==0.26.0+rocm7.14.0" \
                      "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1150

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1150]==2.12.0+rocm7.14.0" \
                      "torchvision[device-gfx1150]==0.27.0+rocm7.14.0" \
                      "torchaudio==2.12.0+rocm7.14.0"

            .. selected:: os=windows

               .. code-block:: bat

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1150]==2.12.0+rocm7.14.0" "torchvision[device-gfx1150]==0.27.0+rocm7.14.0" "torchaudio==2.12.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1150]==2.11.0+rocm7.14.0" \
                      "torchvision[device-gfx1150]==0.26.0+rocm7.14.0" \
                      "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1152

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1152]==2.12.0+rocm7.14.0" \
                      "torchvision[device-gfx1152]==0.27.0+rocm7.14.0" \
                      "torchaudio==2.12.0+rocm7.14.0"

            .. selected:: os=windows

               .. code-block:: bat

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1152]==2.12.0+rocm7.14.0" "torchvision[device-gfx1152]==0.27.0+rocm7.14.0" "torchaudio==2.12.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1152]==2.11.0+rocm7.14.0" \
                      "torchvision[device-gfx1152]==0.26.0+rocm7.14.0" \
                      "torchaudio==2.11.0+rocm7.14.0"

      .. selected:: gfx=gfx1153

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1153]==2.12.0+rocm7.14.0" \
                      "torchvision[device-gfx1153]==0.27.0+rocm7.14.0" \
                      "torchaudio==2.12.0+rocm7.14.0"

            .. selected:: os=windows

               .. code-block:: bat

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1153]==2.12.0+rocm7.14.0" "torchvision[device-gfx1153]==0.27.0+rocm7.14.0" "torchaudio==2.12.0+rocm7.14.0"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash

                  python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                      "torch[device-gfx1153]==2.11.0+rocm7.14.0" \
                      "torchvision[device-gfx1153]==0.26.0+rocm7.14.0" \
                      "torchaudio==2.11.0+rocm7.14.0"

   4. Verify your PyTorch installation.

      .. code-block:: shell

         python -c "import torch; print(torch.cuda.is_available())"

      This prints ``True`` if PyTorch and ROCm are installed properly and your AMD
      GPUs are detected.

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
