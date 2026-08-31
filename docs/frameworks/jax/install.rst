:selector-toc2: Installation environment
:selector-toc2-icon: fa-solid fa-computer

.. _jax-install:

********************
Install JAX for ROCm
********************

This page guides you through installing JAX with ROCm support on AMD hardware.
It applies to `supported AMD GPUs and platforms
<https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support>`__.

.. selector:: Device family
   :key: fam

   .. selector-option:: All
      :value: all
      :width: 4

   .. selector-option:: AMD Instinct™
      :value: instinct
      :width: 4
      :toc-label: AMD Instinct

   .. selector-option:: AMD Radeon™
      :value: radeon
      :width: 4
      :toc-label: AMD Radeon

.. include:: /frameworks/include/gpu-selector-jax.rst

.. selector:: Operating system
   :key: os

   .. selector-option:: Linux
      :value: linux
      :width: 12

.. selector:: ROCm version
   :key: rocm-ver

   .. selector-option:: 10.0.0
      :value: 10.0.0
      :width: 4

   .. selector-option:: 7.14.1
      :value: 7.14.1
      :width: 4

   .. selector-option:: 7.14.0
      :value: 7.14.0
      :width: 4

.. selected:: rocm-ver=10.0.0

   .. selector:: JAX version
      :key: jax-ver

      .. selector-option:: 0.11.0
         :value: 0.11.0
         :width: 4

      .. selector-option:: 0.10.2
         :value: 0.10.2
         :width: 4

      .. selector-option:: 0.10.0
         :value: 0.10.0
         :width: 4

.. selected:: rocm-ver=7.14.1 rocm-ver=7.14.0

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

   .. selected:: rocm-ver=10.0.0

      * Ensure your system has the AMD GPU Driver (amdgpu) installed. See the
        `ROCm compatibility matrix
        <https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html>`__
        for driver support information. For installation instructions, see the
        `AMD GPU Driver documentation
        <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/index.html>`__.

   .. selected:: rocm-ver=7.14.0

      * Ensure your system has the AMD GPU Driver (amdgpu) installed. See the
        `ROCm compatibility matrix
        <https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html>`__
        for driver support information. For installation instructions, see the
        `AMD GPU Driver documentation
        <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html>`__.

.. selected:: i=docker

   * Ensure the host system has `Docker Engine
     <https://docs.docker.com/engine/install/>`__ installed.

.. selected:: i=pip

   .. selected:: jax-ver=0.10.2 jax-ver=0.10.0 jax-ver=0.9.1

      * Ensure your system has a `supported Python version
        <https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support>`__
        installed and accessible: **3.11, 3.12, 3.13, or 3.14**.

   .. selected:: jax-ver=0.11.0

      * Ensure your system has a `supported Python version
        <https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support>`__
        installed and accessible: **3.12, 3.13, or 3.14**.

   .. selected:: rocm-ver=10.0.0

      * Complete the ROCm Core SDK installation prerequisites for installing via pip. See `Prerequisites
        (Install ROCm 10.0.0)
        <https://rocm.docs.amd.com/en/docs-10.0.0/install/rocm.html#prerequisites>`__ for
        instructions.

   .. selected:: rocm-ver=7.14.1

      * Complete the ROCm Core SDK installation prerequisites for installing via pip. See `Prerequisites
        (Install ROCm 7.14.1)
        <https://rocm.docs.amd.com/en/docs-7.14.1/install/rocm.html#prerequisites>`__ for
        instructions.

   .. selected:: rocm-ver=7.14.0

      * Complete the ROCm Core SDK installation prerequisites for installing via pip. See `Prerequisites
        (Install ROCm 7.14.0)
        <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html#prerequisites>`__ for
        instructions.

   .. important::

      Unlike :doc:`PyTorch </frameworks/pytorch/install>`, the JAX packages
      don't automatically install ROCm library and device packages as
      dependencies. The following section includes recommended instructions to
      install ROCm in a Python virtual environment alongside JAX. See `Install
      ROCm <https://rocm.docs.amd.com/en/latest/install/rocm.html>`__ for other
      installation methods.

.. include:: ./include/rocm10.0.0-docker.rst

.. include:: ./include/rocm7.14.1-docker.rst

.. include:: ./include/rocm7.14.0-docker.rst

.. selected:: i=pip
   :heading: Install JAX using pip

   .. selected:: rocm-ver=10.0.0

      For prerequisite steps and post-installation recommendations, see the `ROCm
      installation instructions <https://rocm.docs.amd.com/en/docs-10.0.0/install/rocm.html>`__.

   .. selected:: rocm-ver=7.14.1

      For prerequisite steps and post-installation recommendations, see the `ROCm
      installation instructions <https://rocm.docs.amd.com/en/docs-7.14.1/install/rocm.html>`__.

   .. selected:: rocm-ver=7.14.0

      For prerequisite steps and post-installation recommendations, see the `ROCm
      installation instructions <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html>`__.

   1. Set up your Python virtual environment.

      .. selected:: jax-ver=0.11.0

         .. tab-set::

            .. tab-item:: Python 3.13

               .. code-block:: bash

                  python3.13 -m venv .venv

            .. tab-item:: Python 3.12

               .. code-block:: bash

                  python3.12 -m venv .venv

            .. tab-item:: Python 3.11

               .. code-block:: bash

                  python3.11 -m venv .venv

      .. selected:: jax-ver=0.10.2 jax-ver=0.10.0

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

   .. include:: ./include/rocm10.0.0-pip-install.rst

   .. include:: ./include/rocm7.14.1-pip-install.rst

   .. include:: ./include/rocm7.14.0-pip-install.rst

   5. Verify your JAX installation.

      .. code-block:: shell

         python -c "import jax; print(jax.devices())"

      This prints something like ``[RocmDevice(id=0)]`` if JAX and ROCm are
      installed properly and your AMD GPUs are detected.

.. selected:: fam=radeon
   :heading: Known issues

   * JAX BERT FP16 training workloads might encounter a segmentation fault on
     some AMD Radeon graphics products, such as the Radeon PRO W7900, causing
     training to terminate unexpectedly. As a workaround, disable XLA GPU
     command buffers by setting the following environment variable before
     launching the workload:

     .. code-block:: bash

        export XLA_FLAGS="--xla_gpu_enable_command_buffer="
