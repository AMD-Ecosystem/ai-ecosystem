:selector-toc2: Installation environment
:selector-toc2-icon: fa-solid fa-computer

.. _tensorflow-install:

***************************
Install TensorFlow for ROCm
***************************

This page guides you through installing TensorFlow with ROCm support on AMD
Instinct GPUs running Linux. It applies to `supported AMD GPUs and platforms
<https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support>`__.

.. selector:: ROCm version
   :key: rocm-ver

   .. selector-option:: 10.1.0
      :width: 4

   .. selector-option:: 10.0.0
      :width: 4

   .. selector-option:: 7.14.1
      :width: 4

.. selector:: Device family
   :key: fam

   .. selector-option:: AMD Instinct™
      :value: instinct
      :width: 6
      :show-cond: rocm-ver=10.1.0
      :toc-label: AMD Instinct

   .. selector-option:: AMD Radeon™
      :value: radeon
      :width: 6
      :show-cond: rocm-ver=10.1.0
      :toc-label: AMD Radeon

   .. selector-option:: AMD Instinct™
      :value: instinct
      :width: 12
      :show-cond: rocm-ver=10.0.0 rocm-ver=7.14.1
      :toc-label: AMD Instinct

.. selector-dropdown:: Instinct GPU
   :key: gpu
   :show-cond: fam=instinct rocm-ver=10.1.0
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

   .. selector-option:: AMD Radeon AI PRO R9700S (gfx1201)
      :value: amd-radeon-ai-pro-r9700s gfx=gfx1201

   .. selector-option:: AMD Radeon AI PRO R9700 (gfx1201)
      :value: amd-radeon-ai-pro-r9700 gfx=gfx1201

   .. selector-option:: AMD Radeon AI PRO R9600D (gfx1201)
      :value: amd-radeon-ai-pro-r9600d gfx=gfx1201

   .. selector-option:: AMD Radeon AI PRO R9600 (gfx1201)
      :value: amd-radeon-ai-pro-r9600 gfx=gfx1201

   .. selector-option:: AMD Radeon RX 9070 XT (gfx1201)
      :value: amd-radeon-rx-9070-xt gfx=gfx1201

   .. selector-option:: AMD Radeon RX 9070 GRE (gfx1201)
      :value: amd-radeon-rx-9070-gre gfx=gfx1201

   .. selector-option:: AMD Radeon RX 9070 (gfx1201)
      :value: amd-radeon-rx-9070 gfx=gfx1201

   .. selector-option:: AMD Radeon RX 9060 XT LP (gfx1200)
      :value: amd-radeon-rx-9060-xt-lp gfx=gfx1200

   .. selector-option:: AMD Radeon RX 9060 XT (gfx1200)
      :value: amd-radeon-rx-9060-xt gfx=gfx1200

   .. selector-option:: AMD Radeon RX 9060 (gfx1200)
      :value: amd-radeon-rx-9060 gfx=gfx1200

   .. selector-option:: AMD Radeon RX 9050 (gfx1200)
      :value: amd-radeon-rx-9050 gfx=gfx1200

   .. selector-option:: AMD Radeon RX 9050 (4GB) (gfx1200)
      :value: amd-radeon-rx-9050-4gb gfx=gfx1200

   .. selector-option:: AMD Radeon PRO W7900 Dual Slot (gfx1100)
      :value: amd-radeon-pro-w7900-dual-slot gfx=gfx1100

   .. selector-option:: AMD Radeon PRO W7900 (gfx1100)
      :value: amd-radeon-pro-w7900 gfx=gfx1100

   .. selector-option:: AMD Radeon PRO W7800 48GB (gfx1100)
      :value: amd-radeon-pro-w7800-48gb gfx=gfx1100

   .. selector-option:: AMD Radeon PRO W7800 (gfx1100)
      :value: amd-radeon-pro-w7800 gfx=gfx1100

   .. selector-option:: AMD Radeon PRO W7700 (gfx1101)
      :value: amd-radeon-pro-w7700 gfx=gfx1101

   .. selector-option:: AMD Radeon RX 7900 XTX (gfx1100)
      :value: amd-radeon-rx-7900-xtx gfx=gfx1100

   .. selector-option:: AMD Radeon RX 7900 XT (gfx1100)
      :value: amd-radeon-rx-7900-xt gfx=gfx1100

   .. selector-option:: AMD Radeon RX 7900 GRE (gfx1100)
      :value: amd-radeon-rx-7900-gre gfx=gfx1100

   .. selector-option:: AMD Radeon RX 7800 XT (gfx1101)
      :value: amd-radeon-rx-7800-xt gfx=gfx1101

   .. selector-option:: AMD Radeon RX 7700 XT (gfx1101)
      :value: amd-radeon-rx-7700-xt gfx=gfx1101

   .. selector-option:: AMD Radeon RX 7700 (gfx1101)
      :value: amd-radeon-rx-7700 gfx=gfx1101

   .. selector-option:: AMD Radeon RX 7600 (gfx1102)
      :value: amd-radeon-rx-7600 gfx=gfx1102

   .. selector-option:: AMD Radeon PRO V710 (gfx1101)
      :value: amd-radeon-pro-v710 gfx=gfx1101

.. selector-dropdown:: Instinct GPU
   :key: gpu
   :show-cond: fam=instinct rocm-ver=10.0.0 rocm-ver=7.14.1
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

.. selector:: TensorFlow version
   :key: tensorflow-ver
   :show-cond: rocm-ver=10.1.0

   .. selector-option:: 2.21
      :value: 2.21
      :width: 6

   .. selector-option:: 2.20
      :value: 2.20
      :width: 6
      :show-cond: fam=instinct

.. selector:: TensorFlow version
   :key: tensorflow-ver
   :show-cond: rocm-ver=10.0.0 rocm-ver=7.14.1

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

   .. selected:: rocm-ver=10.1.0 rocm-ver=10.0.0

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
        <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html>`__.

.. selected:: i=docker

   * Ensure the host system has `Docker Engine
     <https://docs.docker.com/engine/install/>`__ installed. For more guidance
     on running ROCm workloads in Docker containers, see `Run ROCm Docker
     containers
     <https://rocm.docs.amd.com/en/latest/install/docker-containers.html>`__.

.. selected:: i=pip

   * Ensure your system has a `supported Python version
     <https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support>`__
     installed and accessible: **3.12**

   .. selected:: rocm-ver=10.1.0

      * Complete the ROCm Core SDK installation prerequisites for installing via pip. See `Prerequisites
        (Install ROCm 10.1.0)
        <https://rocm.docs.amd.com/en/docs-10.1.0/install/rocm.html#prerequisites>`__ for
        instructions.

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

.. include:: ./include/rocm10.1.0-docker.rst

.. include:: ./include/rocm10.0.0-docker.rst

.. include:: ./include/rocm7.14.1-docker.rst

.. include:: ./include/rocm10.1.0-pip-install.rst

.. include:: ./include/rocm10.0.0-pip-install.rst

.. include:: ./include/rocm7.14.1-pip-install.rst

.. _tensorflow-known-issues:

.. selected:: i=pip
   :heading: Known issues

   After installing ``rocm_tensorflow`` using pip, attempting to run TensorFlow
   can result in multiple ``ImportError``\ s.

   As a workaround, update ``LD_LIBRARY_PATH`` to link to the required ROCm
   libraries and system dependencies in your installation path:

   .. code-block:: bash

      export LD_LIBRARY_PATH=$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_core/lib:$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_core/lib/rocm_sysdeps/lib:$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_libraries/lib:$LD_LIBRARY_PATH
