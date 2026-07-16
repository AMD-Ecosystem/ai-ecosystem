:selector-toc2: Installation environment
:selector-toc2-icon: fa-solid fa-computer

.. _jax-install:

***************************
Install JAX for ROCm 7.14.0
***************************

This page guides you through installing JAX with ROCm support on AMD hardware.
It applies to `supported AMD GPUs and platforms
<https://rocm.docs.amd.com/en/docs-7.14.0/about/release-notes.html#ai-ecosystem-support>`__.

.. selector:: Device family
   :key: fam

   .. selector-option:: All
      :value: all w=compute
      :width: 4

   .. selector-option:: AMD Instinct™
      :value: instinct w=compute
      :width: 4
      :toc-label: AMD Instinct

   .. selector-option:: AMD Radeon™
      :value: radeon w=compute
      :width: 4
      :toc-label: AMD Radeon

.. include:: /frameworks/include/gpu-selector-jax.rst

.. selector:: Operating system
   :key: os

   .. selector-option:: Linux
      :value: linux
      :width: 12

.. selector:: JAX version
   :key: jax-ver

   .. selector-option:: 0.10.0
      :value: 0.10.0
      :width: 6

   .. selector-option:: 0.9.1
      :value: 0.9.1
      :width: 6

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

   * Ensure your host system has the AMD GPU Driver (amdgpu) installed. See the
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

   .. important::

      Unlike :doc:`PyTorch </frameworks/pytorch/install>`, the JAX packages
      don't automatically install ROCm library and device packages as
      dependencies. The following section includes recommended instructions to
      install ROCm in a Python virtual environment alongside JAX. See `Install
      ROCm <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html>`__ for other
      installation methods.

.. selected:: i=docker
   :heading: Get started

   .. selected:: jax-ver=0.10.0

      1. Pull the ROCm JAX 0.10.0 Docker image.

         .. tab-set::

            .. tab-item:: Python 3.14
               :sync: py314

               .. code-block:: bash

                  docker pull rocm/jax:rocm7.14-jax0.10.0-py3.14

            .. tab-item:: Python 3.13
               :sync: py313

               .. code-block:: bash

                  docker pull rocm/jax:rocm7.14-jax0.10.0-py3.13

            .. tab-item:: Python 3.12
               :sync: py312

               .. code-block:: bash

                  docker pull rocm/jax:rocm7.14-jax0.10.0-py3.12

            .. tab-item:: Python 3.11
               :sync: py311

               .. code-block:: bash

                  docker pull rocm/jax:rocm7.14-jax0.10.0-py3.11

   .. selected:: jax-ver=0.9.1

      1. Pull the ROCm JAX 0.9.1 Docker image.

         .. tab-set::

            .. tab-item:: Python 3.14
               :sync: py314

               .. code-block:: bash

                  docker pull rocm/jax:rocm7.14-jax0.9.1-py3.14

            .. tab-item:: Python 3.13
               :sync: py313

               .. code-block:: bash

                  docker pull rocm/jax:rocm7.14-jax0.9.1-py3.13

            .. tab-item:: Python 3.12
               :sync: py312

               .. code-block:: bash

                  docker pull rocm/jax:rocm7.14-jax0.9.1-py3.12

            .. tab-item:: Python 3.11
               :sync: py311

               .. code-block:: bash

                  docker pull rocm/jax:rocm7.14-jax0.9.1-py3.11

   2. Start the Docker container.

      .. selected:: jax-ver=0.10.0

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
                     rocm/jax:rocm7.14-jax0.10.0-py3.14 \
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
                     rocm/jax:rocm7.14-jax0.10.0-py3.13 \
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
                     rocm/jax:rocm7.14-jax0.10.0-py3.12 \
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
                     rocm/jax:rocm7.14-jax0.10.0-py3.11 \
                     bash

      .. selected:: jax-ver=0.9.1

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
                     rocm/jax:rocm7.14-jax0.9.1-py3.14 \
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
                     rocm/jax:rocm7.14-jax0.9.1-py3.13 \
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
                     rocm/jax:rocm7.14-jax0.9.1-py3.12 \
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
                     rocm/jax:rocm7.14-jax0.9.1-py3.11 \
                     bash

.. selected:: i=pip
   :heading: Install JAX using pip

   For prerequisite steps and post-installation recommendations, see the `ROCm
   installation instructions <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html>`__.

   1. Set up your Python virtual environment.

      .. tab-set::

         .. tab-item:: Python 3.14

            .. code-block:: bash

               python3.14 -m venv .venv

         .. tab-item:: Python 3.13

            .. code-block:: bash

               python3.13 -m venv .venv

         .. tab-item:: Python 3.12

            .. code-block:: bash

               python3.12 -m venv .venv

         .. tab-item:: Python 3.11

            .. code-block:: bash

               python3.11 -m venv .venv

   2. Activate your Python virtual environment.

      .. code-block:: shell

         source .venv/bin/activate

   3. If you don't have an existing ROCm installation, install ROCm using the
      following command; otherwise, proceed to installing JAX libraries.

      .. selected:: fam=all

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-all]"

      .. selected:: gfx=gfx950

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx950]"

      .. selected:: gfx=gfx942

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx942]"

      .. selected:: gfx=gfx90a

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx90a]"

      .. selected:: gfx=gfx1200

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx1200]"

      .. selected:: gfx=gfx1201

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx1201]"

      .. selected:: gfx=gfx1100

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx1100]"

      .. selected:: gfx=gfx1101

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx1101]"

      .. selected:: gfx=gfx1102

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx1102]"

   4. Install the ROCm-enabled JAX libraries.

      .. note::

         The ``jax`` and ``jaxlib`` packages are not published to the AMD package
         repository. After installing GFX architecture-based ``jax_rocm7_plugin``
         and ``jax_rocm7_pjrt`` packages from the AMD repository, install
         ``jax`` and ``jaxlib`` from `PyPI <https://pypi.org/project/jax>`__.

      .. selected:: jax-ver=0.10.0

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "jax_rocm7_plugin==0.10.0+rocm7.14.0" \
                "jax_rocm7_pjrt==0.10.0+rocm7.14.0"

            # Install jax from PyPI
            python -m pip install \
                "jax==0.10.0" \
                "jaxlib==0.10.0"

      .. selected:: jax-ver=0.9.1

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "jax_rocm7_plugin==0.9.1+rocm7.14.0" \
                "jax_rocm7_pjrt==0.9.1+rocm7.14.0"

            # Install jax from PyPI
            python -m pip install \
                "jax==0.9.1" \
                "jaxlib==0.9.1"

   5. Verify your JAX installation.

      .. code-block:: shell

         python -c "import jax; print(jax.devices())"

      This prints something like ``[RocmDevice(id=0)]`` if JAX and ROCm are
      installed properly and your AMD GPUs are detected.
