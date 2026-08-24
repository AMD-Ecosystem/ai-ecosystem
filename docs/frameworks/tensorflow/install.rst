:selector-toc2: Installation environment
:selector-toc2-icon: fa-solid fa-computer

.. _tensorflow-install:

***************************
Install TensorFlow for ROCm
***************************

This page guides you through installing TensorFlow with ROCm support on AMD hardware.
It applies to `supported AMD GPUs and platforms
<https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support>`__.

.. selector:: Device family
   :key: fam

   .. selector-option:: AMD Instinct™
      :value: instinct
      :width: 12
      :toc-label: AMD Instinct

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

   .. selector-option:: AMD Instinct MI250X (gfx90a)
      :value: mi250x gfx=gfx90a

   .. selector-option:: AMD Instinct MI250 (gfx90a)
      :value: mi250 gfx=gfx90a

   .. selector-option:: AMD Instinct MI210 (gfx90a)
      :value: mi210 gfx=gfx90a

.. selector:: Operating system
   :key: os

   .. selector-option:: Linux
      :value: linux
      :width: 12

.. selector:: ROCm version
   :key: rocm-ver

   .. selector-option:: 10.0.0
      :width: 12

.. selector:: TensorFlow version
   :key: tensorflow-ver

   .. selector-option:: 2.21
      :value: 2.21
      :width: 4

   .. selector-option:: 2.20
      :value: 2.20
      :width: 4

   .. selector-option:: 2.19.1
      :value: 2.19
      :width: 4

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
     installed and accessible: 3.12

   * Complete the ROCm Core SDK installation prerequisites. See `Prerequisites
     (Install ROCm)
     <https://rocm.docs.amd.com/en/latest/install/rocm.html#prerequisites>`__ for
     instructions.

.. selected:: i=docker
   :heading: Get started

   .. selected:: tensorflow-ver=2.21

      1. Pull the ROCm TensorFlow 2.21 Docker image.

         .. code-block:: bash

            docker pull rocm/tensorflow:rocm10.0-ubuntu22.04-py3.12-tf2.21

   .. selected:: tensorflow-ver=2.20

      1. Pull the ROCm TensorFlow 2.20 Docker image.

         .. code-block:: bash

            docker pull rocm/tensorflow:rocm10.0-ubuntu22.04-py3.12-tf2.20

   .. selected:: tensorflow-ver=2.19

      1. Pull the ROCm TensorFlow 2.19.1 Docker image.

         .. code-block:: bash

            docker pull rocm/tensorflow:rocm10.0-ubuntu22.04-py3.12-tf2.19.1

   2. Start the Docker container.

      .. selected:: tensorflow-ver=2.21

         .. code-block:: bash

            docker run -it --rm \
               --device /dev/kfd \
               --device /dev/dri \
               --network=host \
               --ipc=host \
               --group-add=video \
               --cap-add=SYS_PTRACE \
               --security-opt seccomp=unconfined \
               rocm/tensorflow:rocm10.0-ubuntu22.04-py3.12-tf2.21 \
               bash

      .. selected:: tensorflow-ver=2.20

         .. code-block:: bash

            docker run -it --rm \
               --device /dev/kfd \
               --device /dev/dri \
               --network=host \
               --ipc=host \
               --group-add=video \
               --cap-add=SYS_PTRACE \
               --security-opt seccomp=unconfined \
               rocm/tensorflow:rocm10.0-ubuntu22.04-py3.12-tf2.20 \
               bash

      .. selected:: tensorflow-ver=2.19.1

         .. code-block:: bash

            docker run -it --rm \
               --device /dev/kfd \
               --device /dev/dri \
               --network=host \
               --ipc=host \
               --group-add=video \
               --cap-add=SYS_PTRACE \
               --security-opt seccomp=unconfined \
               rocm/tensorflow:rocm10.0-ubuntu22.04-py3.12-tf2.19.1 \
               bash

.. selected:: i=pip
   :heading: Install JAX using pip

   For prerequisite steps and post-installation recommendations, see the `ROCm
   installation instructions <https://rocm.docs.amd.com/en/latest/install/rocm.html>`__.

   1. Set up your Python virtual environment.

      .. tab-item:: Python 3.12

         .. code-block:: bash

            python3.12 -m venv .venv

   2. Activate your Python virtual environment.

      .. code-block:: shell

         source .venv/bin/activate

   3. If you don't have an existing ROCm installation, install ROCm using the
      following command; otherwise, proceed to installing JAX libraries.

      .. selected:: gfx=gfx950

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx950]==10.0.0rc4"

      .. selected:: gfx=gfx942

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx942]==10.0.0rc4"

      .. selected:: gfx=gfx90a

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx90a]==10.0.0rc4"

   4. Install the ROCm-enabled TensorFlow libraries.

      .. selected:: tensorflow-ver=2.21

         .. code-block:: bash

            python -m pip install https://rocm.frameworks-prereleases.amd.com/whl-multi-arch-staging/tensorflow-rocm/tensorflow_rocm-2.21.0.dev0%2Bselfbuilt.rocm10.0.0rc4-cp312-cp312-linux_x86_64.whl

      .. selected:: tensorflow-ver=2.20

         .. code-block:: bash

            python -m pip install https://rocm.frameworks-prereleases.amd.com/whl-multi-arch-staging/tensorflow-rocm/tensorflow_rocm-2.20.0.dev0%2Bselfbuilt.rocm10.0.0rc4-cp312-cp312-linux_x86_64.whl

      .. selected:: tensorflow-ver=2.19

         .. code-block:: bash

            python -m pip install https://rocm.frameworks-prereleases.amd.com/whl-multi-arch-staging/tensorflow-rocm/tensorflow_rocm-2.19.1%2Brocm10.0.0rc4-cp312-cp312-linux_x86_64.whl

   5. Update ``LD_LIBRARY_PATH`` as a :ref:`workaround <>` so TensorFlow can discover ROCm libraries and system dependencies.

      .. code-block:: bash

         export LD_LIBRARY_PATH=$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_core/lib:$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_core/lib/rocm_sysdeps/lib:$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_libraries/lib:$LD_LIBRARY_PATH

   5. Verify your TensorFlow installation.

      .. code-block:: shell

         python -c "import tensorflow as tf; print('TensorFlow version: ', tf.__version__)"

.. _tensorflow-known-issues:

Known issues
============

After installing ``rocm_tensorflow`` using pip, attempting to run TensorFlow
results in fatal ``ImportError``s.

.. code-block::

   ImportError: libhipsparse.so.4
   ...
   ImportError: librocm_sysdeps_asm.so.1
   ...

As a workaround, update ``LD_LIBRARY_PATH`` to link to the required ROCm
libraries and system dependencies in your installation path:

.. code-block:: bash

   export LD_LIBRARY_PATH=$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_core/lib:$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_core/lib/rocm_sysdeps/lib:$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_libraries/lib:$LD_LIBRARY_PATH
