:selector-toc2: Installation environment
:selector-toc2-icon: fa-solid fa-computer

***************************
llama.cpp inference on ROCm
***************************

`llama.cpp <https://llama.app/docs/introduction>`__ is an open-source inference
engine for running LLMs locally. It runs quantized models efficiently on
everyday hardware and has become a pillar of local LLM inference.
This page explains how to set up and run llama.cpp on AMD Radeon™ GPUs and
Ryzen™ APUs.

.. selector:: Device family
   :key: fam

   .. selector-option:: AMD Radeon
      :value: radeon
      :width: 6

   .. selector-option:: AMD Ryzen
      :value: ryzen
      :width: 6

.. datatemplate:yaml:: /data/gpus.yaml
   :template: gpu-selector.rst.jinja

.. selector:: Operating system
   :key: os

   .. selector-option:: Ubuntu 24.04
      :value: ubuntu ubuntu-ver=24.04
      :width: 6

   .. selector-option:: Windows 11
      :value: windows windows-ver=11
      :width: 6

.. selector:: ROCm version
   :key: rocm-ver

   .. selector-option:: 7.14.0
      :value: 7.14.0
      :width: 12

.. selector:: ROCm installation
   :key: i

   .. selector-option:: apt
      :value: pkgman
      :width: 4

   .. selector-option:: pip
      :value: pip
      :width: 4

   .. selector-option:: Tarball
      :value: tar
      :width: 4

----

.. seealso::

   .. selected:: os=ubuntu

      The `<https://github.com/lemonade-sdk/llamacpp-rocm/releases>`__ community
      project publishes nightly llama.cpp builds for Ubuntu that bundle the ROCm
      runtime, in per-architecture packages. With one of those builds you can skip
      installing ROCm and configuring ``LD_LIBRARY_PATH``;
      the AMD GPU driver is still required.

   .. selected:: os=windows

      The `<https://github.com/lemonade-sdk/llamacpp-rocm/releases>`__ community
      project publishes nightly llama.cpp builds for Windows that bundle the ROCm
      runtime, in per-architecture packages. With one of those builds you can skip
      installing ROCm, configuring ``PATH``, and copying the HIP runtime libraries;
      the AMD Software: Adrenalin Edition driver is still required.

.. _llamacpp-sysreqs:

Prerequisites
=============

To run llama.cpp with ROCm on Linux, you need the following prerequisites:

- **GPU platform:** AMD Instinct accelerators, and AMD Radeon discrete GPUs and Ryzen APUs
  supported by ROCm 7.14.0. For the list of supported devices, see the
  `ROCm compatibility matrix <https://rocm.docs.amd.com/en/docs-7.14.0/compatibility/compatibility-matrix.html>`__.

.. selected:: os=ubuntu

   - **Driver:** the AMD GPU Driver (``amdgpu``). This is a separate installation step and is
     not provided by the ROCm packages or the tarball. Instinct and Radeon devices require the
     AMD GPU Driver; supported Ryzen APUs use the inbox kernel driver included with the
     distribution. See `Install ROCm 7.14.0 <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html>`__
     for the driver installation step that applies to your distribution.

   - **Group membership:** your user must be a member of the ``video`` and ``render`` groups.

   - **Additional packages:** ``libgomp1`` provides the OpenMP runtime that llama.cpp links
     against, and ``libcurl4`` is required for model downloading. Install them if they are not
     already present on your system:

     .. code-block:: bash

        sudo apt install libgomp1 libcurl4

.. selected:: os=windows

   - **Driver:** AMD Software: Adrenalin Edition. This is a separate
     installation step and is not provided by the ROCm packages or the tarball.
     See `Install ROCm 7.14.0
     <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html>`__ for the
     driver installation step that applies to your system.

.. _llamacpp-install-rocm:

Install ROCm
------------

llama.cpp requires a ROCm installation on the host system.

.. selected:: rocm-ver=7.14.0

   .. selected:: fam=radeon

      .. selected:: os=ubuntu

         .. selected:: i=pkgman

            .. selected:: gfx=gfx1201

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1201&w=compute&os=ubuntu&i=pkgman>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1200

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1200&w=compute&os=ubuntu&i=pkgman>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1100

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1100&w=compute&os=ubuntu&i=pkgman>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1101

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1101&w=compute&os=ubuntu&i=pkgman>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1102

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1102&w=compute&os=ubuntu&i=pkgman>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1030

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1030&w=compute&os=ubuntu&i=pkgman>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            * Device family: **AMD Radeon**
            * Select your GPU -- importantly, ``gfx`` architecture -- from the dropdown list.
            * Use case: **Compute**
            * Operating system: **Ubuntu**
            * Installation method: **apt** (package manager)

         .. selected:: i=pip

            .. selected:: gfx=gfx1201

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1201&w=compute&os=ubuntu&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1200

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1200&w=compute&os=ubuntu&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1100

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1100&w=compute&os=ubuntu&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1101

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1101&w=compute&os=ubuntu&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1102

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1102&w=compute&os=ubuntu&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1030

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1030&w=compute&os=ubuntu&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            * Device family: **AMD Radeon**
            * Select your GPU -- importantly, ``gfx`` architecture -- from the dropdown list.
            * Use case: **Compute**
            * Operating system: **Ubuntu**
            * Installation method: **pip**

         .. selected:: i=tar

            .. selected:: gfx=gfx1201

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1201&w=compute&os=ubuntu&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1200

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1200&w=compute&os=ubuntu&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1100

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1100&w=compute&os=ubuntu&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1101

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1101&w=compute&os=ubuntu&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1102

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1102&w=compute&os=ubuntu&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1030

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1030&w=compute&os=ubuntu&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            * Device family: **AMD Radeon**
            * Select your GPU -- importantly, ``gfx`` architecture -- from the dropdown list.
            * Use case: **Compute**
            * Operating system: **Ubuntu**
            * Installation method: **Tarball**

      .. selected:: os=windows

         .. selected:: i=pip

            .. selected:: gfx=gfx1201

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1201&w=compute&os=windows&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1200

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1200&w=compute&os=windows&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1100

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1100&w=compute&os=windows&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1101

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1101&w=compute&os=windows&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1102

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1102&w=compute&os=windows&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1030

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1030&w=compute&os=windows&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            * Device family: **AMD Radeon**
            * Select your GPU -- importantly, ``gfx`` architecture -- from the dropdown list.
            * Use case: **Compute**
            * Operating system: **Windows**
            * Installation method: **pip**

         .. selected:: i=tar

            .. selected:: gfx=gfx1201

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1201&w=compute&os=windows&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1200

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1200&w=compute&os=windows&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1100

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1100&w=compute&os=windows&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1101

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1101&w=compute&os=windows&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1102

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1102&w=compute&os=windows&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1030

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=radeon&gfx=gfx1030&w=compute&os=windows&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            * Device family: **AMD Radeon**
            * Select your GPU -- importantly, ``gfx`` architecture -- from the dropdown list.
            * Use case: **Compute**
            * Operating system: **Windows**
            * Installation method: **Tarball**

   .. selected:: fam=ryzen

      .. selected:: os=ubuntu

         .. selected:: i=pkgman

            .. selected:: gfx=gfx1150

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1150&w=compute&os=ubuntu&i=pkgman>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1151

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1151&w=compute&os=ubuntu&i=pkgman>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1152

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1152&w=compute&os=ubuntu&i=pkgman>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1153

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1153&w=compute&os=ubuntu&i=pkgman>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1103

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1103&w=compute&os=ubuntu&i=pkgman>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            * Device family: **AMD Ryzen**
            * Select your GPU -- importantly, ``gfx`` architecture -- from the dropdown list.
            * Use case: **Compute**
            * Operating system: **Ubuntu**
            * Installation method: **apt** (package manager)

         .. selected:: i=pip

            .. selected:: gfx=gfx1150

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1150&w=compute&os=ubuntu&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1151

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1151&w=compute&os=ubuntu&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1152

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1152&w=compute&os=ubuntu&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1153

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1153&w=compute&os=ubuntu&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1103

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1103&w=compute&os=ubuntu&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            * Device family: **AMD Ryzen**
            * Select your GPU -- importantly, ``gfx`` architecture -- from the dropdown list.
            * Use case: **Compute**
            * Operating system: **Ubuntu**
            * Installation method: **pip**

         .. selected:: i=tar

            .. selected:: gfx=gfx1150

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1150&w=compute&os=ubuntu&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1151

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1151&w=compute&os=ubuntu&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1152

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1152&w=compute&os=ubuntu&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1153

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1153&w=compute&os=ubuntu&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1103

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1103&w=compute&os=ubuntu&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            * Device family: **AMD Ryzen**
            * Select your GPU -- importantly, ``gfx`` architecture -- from the dropdown list.
            * Use case: **Compute**
            * Operating system: **Ubuntu**
            * Installation method: **Tarball**

      .. selected:: os=windows

         .. selected:: i=pip

            .. selected:: gfx=gfx1150

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1150&w=compute&os=windows&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1151

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1151&w=compute&os=windows&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1152

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1152&w=compute&os=windows&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1153

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1153&w=compute&os=windows&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1103

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1103&w=compute&os=windows&i=pip>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            * Device family: **AMD Ryzen**
            * Select your GPU -- importantly, ``gfx`` architecture -- from the dropdown list.
            * Use case: **Compute**
            * Operating system: **Windows**
            * Installation method: **pip**

         .. selected:: i=tar

            .. selected:: gfx=gfx1150

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1150&w=compute&os=windows&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1151

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1151&w=compute&os=windows&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1152

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1152&w=compute&os=windows&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1153

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1153&w=compute&os=windows&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            .. selected:: gfx=gfx1103

               See the `Install ROCm 7.14.0
               <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=ryzen&gfx=gfx1103&w=compute&os=windows&i=tar>`__
               guide for instructions; use the selector on the page to update
               the instructions based on your environment. Your ROCm
               installation should target the same environment you plan to
               install llama.cpp in.

            * Device family: **AMD Ryzen**
            * Select your GPU -- importantly, ``gfx`` architecture -- from the dropdown list.
            * Use case: **Compute**
            * Operating system: **Windows**
            * Installation method: **Tarball**

.. selected:: os=ubuntu

   .. important::

      .. selected:: i=pkgman

         When installing via package manager, ROCm is installed system-wide
         under ``/opt/rocm``. This is the installation method the ROCm
         documentation recommends if you are unsure which to choose.

      .. selected:: i=pip

         Install the ``libraries`` extra and the device extra matching your GPU, for example
         ``rocm[libraries,device-gfx1201]``. The ``devel`` extra is not required to run the
         prebuilt llama.cpp binaries; it supplies the ``rocm-sdk`` command-line tool and
         build-time files only.

         Record the path of the virtual environment you create. You need it in
         :ref:`Configure your environment <llamacpp-configure-env>`.

      .. selected:: i=tar

         This guide assumes the tarball is extracted to an ``install`` directory, as the
         installation instructions describe, and refers to that location as ``$ROCM_PATH``.

.. _llamacpp-install:

Install llama.cpp
=================

AMD does not publish its own binaries for llama.cpp. Download a prebuilt
ROCm-enabled release from the `llama.cpp releases page
<https://github.com/ggml-org/llama.cpp/releases>`__. Release assets are named
in the following format:

.. selected:: rocm-ver=7.14.0

   .. selected:: os=ubuntu

      .. code-block::

         llama-<build>-bin-ubuntu-rocm-7.14-x64.tar.gz

      For ROCm 7.14, that is any asset containing ``ubuntu-rocm-7.14``, for
      example ``llama-b10628-bin-ubuntu-rocm-7.14-x64.tar.gz``.

      Verify the checksum of the downloaded file against the digest shown for the asset, then
      extract the archive:

      .. code-block:: bash

         sha256sum llama-b10628-bin-ubuntu-rocm-7.14-x64.tar.gz
         tar -xf llama-b10628-bin-ubuntu-rocm-7.14-x64.tar.gz

      The archive extracts into a directory named after the build, for example ``llama-b10628``.

   .. selected:: os=windows

      .. code-block::

         llama-<build>-bin-win-rocm-win-rocm7.14-x64.zip

      For ROCm 7.14, that is any asset containing ``win-rocm-7.14``, for example
      ``llama-b10539-bin-win-rocm-7.14-x64.zip``.

      Verify the checksum of the downloaded file against the digest shown for the
      asset, then extract the archive. This guide assumes you extract to ``C:\llamacpp``.

      .. code-block:: bat

         certutil -hashfile llama-<build>-bin-win-rocm-7.14-x64.zip SHA256

.. note::

   The archive contains only the llama.cpp executables and their ``ggml``
   backend libraries. It does not include the ROCm runtime, which must be
   installed separately as described in the :ref:`previous section <llamacpp-install-rocm>`.

.. _llamacpp-configure-env:

.. selected:: os=ubuntu
   :heading: Configure your environment (Linux)

   llama.cpp loads the ROCm math libraries at run time and must be able to find them.

   .. selected:: i=pkgman

      ROCm libraries are installed in ``/opt/rocm/lib``. This directory is not added to the
      system library search path by the packages, so add it to ``LD_LIBRARY_PATH``:

      .. code-block:: bash

         export LD_LIBRARY_PATH=/opt/rocm/lib:$LD_LIBRARY_PATH

   .. selected:: i=pip

      A pip installation places the ROCm runtime inside the virtual environment, in two
      directories:

      - ``<venv>/lib/python<version>/site-packages/_rocm_sdk_core/lib``
      - ``<venv>/lib/python<version>/site-packages/_rocm_sdk_libraries/lib``

      Add both to ``LD_LIBRARY_PATH``, replacing ``<venv>`` with the path of your virtual
      environment. The Python version in the path is the one you created the environment with;
      Ubuntu 24.04 provides Python 3.12.

      .. code-block:: bash

         SP=<venv>/lib/python3.12/site-packages
         export LD_LIBRARY_PATH="$SP/_rocm_sdk_core/lib:$SP/_rocm_sdk_libraries/lib:$LD_LIBRARY_PATH"

      .. note::

         Activating the virtual environment is not sufficient. It sets ``PATH``, which ROCm's
         own tools use, but not ``LD_LIBRARY_PATH``, which the llama.cpp executables need.

   .. selected:: i=tar

      The tarball installation instructions already set ``LD_LIBRARY_PATH`` to
      ``$ROCM_PATH/lib``. No further configuration is required.

   To make any of these settings permanent, add it to your shell startup file;
   ``~/.bashrc``, for instance.

.. selected:: i=pip

   .. selected:: os=windows
      :heading: Configure your environment (Windows)

      A pip installation places the ROCm runtime inside the virtual environment in
      two directories:

      - ``<venv>\Lib\site-packages\_rocm_sdk_core\bin``
      - ``<venv>\Lib\site-packages\_rocm_sdk_libraries\bin``

      Add both to your ``PATH`` in the command prompt you use to launch llama.cpp,
      replacing ``<venv>`` with the actual path of your virtual environment, for
      example:

      .. code-block:: bat

         set "PATH=C:\llamacpp\.venv\Lib\site-packages\_rocm_sdk_core\bin;C:\llamacpp\.venv\Lib\site-packages\_rocm_sdk_libraries\bin;%PATH%"

      This setting applies to the current command prompt only. To make it
      permanent, add both directories to your user or system ``PATH`` in your
      Windows settings.

      If the ROCm libraries are not on your ``PATH``, llama.cpp does not report an
      error. It silently falls back to the CPU backend and runs several times
      slower. Use :ref:`Verify the installation <llamacpp-verify-installation>` to confirm
      the GPU is detected.

.. _llamacpp-copy-runtime-libs:

.. selected:: os=windows
   :heading: Copy the HIP runtime libraries

   .. selected:: i=pip

      Copy the following three files from your ROCm installation into the directory
      that contains ``llama-cli.exe``: ``<venv>\Lib\site-packages\_rocm_sdk_core\bin``

      - ``amdhip64_7.dll``
      - ``rocm_kpack.dll``
      - ``amd_comgr.dll``

      Copy all three files. Copying ``amdhip64_7.dll`` on its own prevents
      llama.cpp from using the GPU: the HIP runtime supplied by ROCm depends on
      the matching ``rocm_kpack.dll`` and ``amd_comgr.dll``, and
      ``rocm_kpack.dll`` is not present in ``System32``.

      .. code-block:: bat

         copy "<venv>\Lib\site-packages\_rocm_sdk_core\bin\amdhip64_7.dll" C:\llamacpp\
         copy "<venv>\Lib\site-packages\_rocm_sdk_core\bin\rocm_kpack.dll" C:\llamacpp\
         copy "<venv>\Lib\site-packages\_rocm_sdk_core\bin\amd_comgr.dll"  C:\llamacpp\

   .. selected:: i=tar

      Copy the following three files from your ROCm installation into the directory
      that contains ``llama-cli.exe``: ``C:\TheRock\build\bin``

      - ``amdhip64_7.dll``
      - ``rocm_kpack.dll``
      - ``amd_comgr.dll``

      .. important::

         Copy all three files. Copying ``amdhip64_7.dll`` on its own prevents
         llama.cpp from using the GPU: the HIP runtime supplied by ROCm depends on
         the matching ``rocm_kpack.dll`` and ``amd_comgr.dll``, and
         ``rocm_kpack.dll`` is not present in ``System32``.

      .. code-block:: bat

         copy "C:\TheRock\build\bin\amdhip64_7.dll" C:\llamacpp\
         copy "C:\TheRock\build\bin\rocm_kpack.dll" C:\llamacpp\
         copy "C:\TheRock\build\bin\amd_comgr.dll"  C:\llamacpp\

   .. note::

      The AMD display driver installs its own copy of ``amdhip64_7.dll`` in
      ``C:\Windows\System32``. Windows searches ``System32`` before ``PATH``, so
      the driver's version is loaded in preference to the one supplied by ROCm,
      even when ROCm is on ``PATH``. Because Windows searches the directory
      containing the executable first, copying these libraries next to
      ``llama-cli.exe`` ensures the ROCm version is used.

.. _llamacpp-verify-installation:

Verify the installation
=======================

.. selected:: os=ubuntu

   List the devices visible to llama.cpp:

   .. code-block:: bash

      cd llama-b10628
      ./llama-cli --list-devices

   The output shows the detected GPU and its available memory:

   .. code-block::

      Available devices:
        ROCm0: AMD Radeon RX 9070 XT (16304 MiB, 15770 MiB free)

   If ``Available devices`` is empty, the ROCm libraries were not found. Review
   :ref:`Configure your environment <llamacpp-configure-env>`.

   If instead you see ``error while loading shared libraries: libgomp.so.1``, install
   the additional packages listed in :ref:`System requirements <llamacpp-sysreqs>`.

   Listing the devices confirms that the ROCm libraries were found, but it does not confirm
   that computation runs on the GPU. To verify that, run a short benchmark with a model in
   GGUF format; see :ref:`llamacpp-example`.

.. selected:: os=windows

   List the devices visible to llama.cpp. Make sure to ``cd`` into where the llama.cpp
   binaries are located and that you're in the same shell in which you set your ``PATH``.

   .. selected:: i=pip

      .. code-block:: bat

         cd C:\llamacpp
         llama-cli.exe --list-devices

   .. selected:: i=tar

      .. code-block:: bat

         cd C:\llamacpp
         llama-cli.exe --list-devices

   The output shows the detected GPU and its available memory. For example:

   .. code-block::

      Available devices:
        ROCm0: AMD Radeon RX 7900 XT (20464 MiB, 20315 MiB free)

   .. selected:: i=tar

      If the device is listed but the reported memory is ``0 MiB``, the installation
      is not usable. This occurs when the ``LLVM_PATH`` environment variable is set,
      which the ROCm tarball instructions do system-wide. Copying the HIP runtime
      libraries as described in the :ref:`previous section
      <llamacpp-copy-runtime-libs>` resolves it. Alternatively, clear ``LLVM_PATH``
      before running llama.cpp.

   If no devices are listed at all, the ROCm runtime cannot be found. Review
   :ref:`Configure your environment <llamacpp-configure-env>`.

   Optionally, run the llama.cpp unit tests to validate the installation more
   thoroughly. The test suite takes a considerable amount of time to complete.

   .. code-block:: bat

      test-backend-ops.exe

.. selected:: os=ubuntu
   :heading: Select a GPU

   Systems with both a discrete GPU and an integrated GPU report more than one ROCm device:

   .. code-block::

      Available devices:
        ROCm0: AMD Radeon RX 9070 XT (16304 MiB, 15770 MiB free)
        ROCm1: AMD Radeon Graphics (63199 MiB, 63174 MiB free)

   The integrated GPU reports a large amount of shared system memory and may not be a
   supported ROCm device. To restrict llama.cpp to a specific GPU, set
   ``HIP_VISIBLE_DEVICES`` to its index:

   .. code-block:: bash

      export HIP_VISIBLE_DEVICES=0

.. _llamacpp-example:

Run a llama.cpp example
=======================

Once your llama.cpp environment is set up, experiment with the following steps
to run a model and benchmark your installation. The prebuilt llama.cpp
release includes the executables to exercise the functionality of your
installation.

The two most popular use cases are:

* ``llama-cli``: The main executable to run the model interactively or get a response to a prompt.
* ``llama-bench``: Run a benchmark of your model with different configurations.

.. seealso::

   See `Models (llama.cpp docs) <https://llama.app/models>`__ for a list of
   GGUF-formatted models available to download from Hugging Face.

.. selected:: os=ubuntu

   The following examples assume the llama.cpp executables are in your
   ``llama-<build>`` directory from the :ref:`previous installation step
   <llamacpp-install>` and you've downloaded a model in GGUF format to run.

.. selected:: os=windows

   The following examples assume the llama.cpp executables are in ``C:\llamacpp``
   and you've downloaded a model in GGUF format to run.

llama-cli
---------

1. Use the CLI tool to start the client, replacing ``<model>.gguf`` with the path to a model on your system:

   .. selected:: os=ubuntu

      .. code-block:: bash

         # Replace <build> with your llama.cpp build number
         cd llama-<build>
         ./llama-cli -m <model>.gguf -ngl 999

   .. selected:: os=windows

      .. code-block:: bat

         cd C:\llamacpp
         llama-cli.exe -m <model>.gguf -ngl 999

2. A prompt appears when the client is ready, and you can start interacting with the model:

   .. code-block::

      > Explain what a GPU kernel is in one sentence.
      A GPU kernel is a specialized program within a GPU (Graphics Processing Unit) designed to execute
      instructions for rendering graphical content, such as images or video, on a GPU's hardware architecture.

      [ Prompt: 593.4 t/s | Generation: 286.4 t/s ]

3. To exit, enter ``/exit`` or press ``Ctrl+C``.

To send a single prompt and exit instead of starting an interactive session, add the ``-p`` and ``-st`` flags:

.. selected:: os=ubuntu

   .. code-block:: bash

      ./llama-cli -m <model>.gguf -p "Explain what a GPU kernel is in one sentence." -ngl 999 -st

.. selected:: os=windows

   .. code-block:: bat

      llama-cli.exe -m <model>.gguf -p "Explain what a GPU kernel is in one sentence." -ngl 999 -st

.. note::

   .. selected:: os=ubuntu

      Without ``-st``, ``llama-cli`` answers the prompt supplied by ``-p`` and
      then continues waiting for further input. Use ``./llama-completion`` for
      non-interactive generation.

   .. selected:: os=windows

      Without ``-st``, ``llama-cli`` answers the prompt supplied by ``-p`` and
      then continues waiting for further input. Use ``llama-completion.exe`` for
      non-interactive generation.

llama-bench
-----------

1. Use the CLI tool to start the application, replacing ``<model>.gguf`` with the path to a model on your system:

   .. selected:: os=ubuntu

      .. code-block:: bash

         ./llama-bench -m <model>.gguf -p 16,32,64,128,256,512,1024 -n 64,128 -ngl 999

   .. selected:: os=windows

      .. code-block:: bat

         llama-bench.exe -m <model>.gguf -p 16,32,64,128,256,512,1024 -n 64,128 -ngl 999

2. The result of the command above should be similar to the following when running on an AMD Radeon RX 7900 XT system:

   .. code-block::

      ggml_cuda_init: found 1 ROCm devices (Total VRAM: 20464 MiB):
        Device 0: AMD Radeon RX 7900 XT, gfx1100 (0x1100), VMM: no, Wave Size: 32, VRAM: 20464 MiB
      load_backend: loaded ROCm backend from C:\llamacpp\ggml-hip.dll
      load_backend: loaded RPC backend from C:\llamacpp\ggml-rpc.dll
      load_backend: loaded CPU backend from C:\llamacpp\ggml-cpu-haswell.dll
      | model                          |       size |     params | backend    | ngl |            test |                  t/s |
      | ------------------------------ | ---------: | ---------: | ---------- | --: | --------------: | -------------------: |
      | qwen2 1B Q4_K - Medium         | 462.96 MiB |   630.17 M | ROCm       | 999 |            pp16 |     2406.95 ± 704.75 |
      | qwen2 1B Q4_K - Medium         | 462.96 MiB |   630.17 M | ROCm       | 999 |            pp32 |     3842.56 ± 500.15 |
      | qwen2 1B Q4_K - Medium         | 462.96 MiB |   630.17 M | ROCm       | 999 |            pp64 |    7104.29 ± 1218.73 |
      | qwen2 1B Q4_K - Medium         | 462.96 MiB |   630.17 M | ROCm       | 999 |           pp128 |     8628.19 ± 928.69 |
      | qwen2 1B Q4_K - Medium         | 462.96 MiB |   630.17 M | ROCm       | 999 |           pp256 |   16444.29 ± 1662.23 |
      | qwen2 1B Q4_K - Medium         | 462.96 MiB |   630.17 M | ROCm       | 999 |           pp512 |   24628.13 ± 2498.10 |
      | qwen2 1B Q4_K - Medium         | 462.96 MiB |   630.17 M | ROCm       | 999 |          pp1024 |     26143.12 ± 73.58 |
      | qwen2 1B Q4_K - Medium         | 462.96 MiB |   630.17 M | ROCm       | 999 |            tg64 |        373.29 ± 9.81 |
      | qwen2 1B Q4_K - Medium         | 462.96 MiB |   630.17 M | ROCm       | 999 |           tg128 |        375.70 ± 3.49 |

      build: 78ec4c378 (10539)

3. The ``backend`` column shows ``ROCm`` when the GPU is in use. If it shows
   ``CPU``, the ROCm libraries were not found. Review the :ref:`environment
   configuration steps <llamacpp-install>` to troubleshoot.

Flash Attention is enabled with ``-fa 1`` and is supported on Radeon GPUs through rocWMMA:

.. selected:: os=ubuntu

   .. code-block:: bash

      ./llama-bench -m <model>.gguf -p 512 -n 64 -ngl 999 -fa 1

.. selected:: os=windows

   .. code-block:: bat

      llama-bench.exe -m <model>.gguf -p 512 -n 64 -ngl 999 -fa 1

