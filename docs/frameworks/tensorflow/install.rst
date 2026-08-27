:selector-toc2: Installation environment
:selector-toc2-icon: fa-solid fa-computer

.. _tensorflow-install:

**********************************
Install TensorFlow for ROCm 10.0.0
**********************************

This page guides you through installing TensorFlow with ROCm support on AMD
Instinct GPUs running Linux. It applies to `supported AMD GPUs and platforms
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

   .. selector-option:: pip
      :value: pip rocm-ver=10.0.0
      :width: 12

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
        <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.0/index.html>`__.

.. selected:: i=docker

   * Ensure the host system has `Docker Engine
     <https://docs.docker.com/engine/install/>`__ installed.

.. selected:: i=pip

   * Ensure your system has a `supported Python version
     <https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support>`__
     installed and accessible: **3.12**

   * Complete the ROCm Core SDK installation prerequisites for installing via pip. See `Prerequisites
     (Install ROCm 10.0.0)
     <https://rocm.docs.amd.com/en/docs-10.0.0/install/rocm.html#prerequisites>`__ for
     instructions.

.. include:: ./include/rocm10.0.0-docker.rst

.. include:: ./include/rocm10.0.0-pip-install.rst

.. _tensorflow-known-issues:

Known issues
============

After installing ``rocm_tensorflow`` using pip, attempting to run TensorFlow
can result in multiple ``ImportError``.

.. code-block::

   ImportError: libhipsparse.so.4
   ...
   ImportError: librocm_sysdeps_asm.so.1
   ...

As a workaround, update ``LD_LIBRARY_PATH`` to link to the required ROCm
libraries and system dependencies in your installation path:

.. code-block:: bash

   export LD_LIBRARY_PATH=$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_core/lib:$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_core/lib/rocm_sysdeps/lib:$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_libraries/lib:$LD_LIBRARY_PATH
