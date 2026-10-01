:selector-toc2: Installation environment
:selector-toc2-icon: fa-solid fa-computer

****************
Install MIGraphX
****************

MIGraphX is AMD's graph inference engine for optimizing and executing ONNX
models on AMD GPUs using ROCm. This page describes how to install the version
of MIGraphX that ships with your selected ROCm release.

.. selector:: ROCm version
   :key: rocm-ver

   .. selector-option:: 10.1.0
      :value: 10.1.0
      :width: 3

   .. selector-option:: 10.0.0
      :value: 10.0.0
      :width: 3

   .. selector-option:: 7.14.1
      :value: 7.14.1
      :width: 3

   .. selector-option:: 7.14.0
      :value: 7.14.0
      :width: 3

.. selected:: rocm-ver=10.0.0

   .. selector:: Installation method
      :key: i

      .. selector-option:: pip
         :value: pip
         :width: 12

.. selected:: rocm-ver=10.1.0 rocm-ver=7.14.1 rocm-ver=7.14.0

   .. selector:: Installation method
      :key: i

      .. selector-option:: Package manager
         :value: pkgman
         :width: 6

      .. selector-option:: pip
         :value: pip
         :width: 6

Prerequisites
=============

.. selected:: rocm-ver=10.1.0

   MIGraphX 2.18 is currently supported on:

   * ``gfx950`` AMD Instinct MI355X, MI350X, and MI350P

   * ``gfx942`` AMD Instinct MI325X, MI300X, and MI300A

   * ``gfx90a`` AMD Instinct MI250X, MI250, and MI210

   * ``gfx1200``, ``gfx1201``, ``gfx1100``, ``gfx1101``, and ``gfx1102`` Radeon GPUs.

   * ``gfx1153``, ``gfx1152``, ``gfx1151``, and ``gfx1150`` Ryzen AI processors.

   See the `ROCm compatibility matrix
   <https://rocm.docs.amd.com/en/docs-10.1.0/compatibility/compatibility-matrix.html>`__
   for more information.

.. selected:: rocm-ver=10.0.0

   MIGraphX is currently supported on:

   * ``gfx950`` AMD Instinct MI355X and MI350X

   * ``gfx942`` AMD Instinct MI325X and MI300X

   * ``gfx1200``, ``gfx1201``, ``gfx1100``, ``gfx1101``, and ``gfx1102`` Radeon GPUs.

   See the `ROCm compatibility matrix
   <https://rocm.docs.amd.com/en/docs-10.0.0/compatibility/compatibility-matrix.html>`__
   for more information.

.. selected:: rocm-ver=7.14.1

   MIGraphX is currently supported on ``gfx950`` AMD Instinct MI355X and MI350X
   data center GPUs and ``gfx942`` MI325X and MI300X GPUs. See the `ROCm
   compatibility matrix
   <https://rocm.docs.amd.com/en/docs-7.14.1/compatibility/compatibility-matrix.html>`__
   for more information.

.. selected:: rocm-ver=7.14.0

   MIGraphX is currently supported on ``gfx950`` AMD Instinct MI355X and MI350X
   data center GPUs and ``gfx942`` MI325X and MI300X GPUs. See the `ROCm
   compatibility matrix
   <https://rocm.docs.amd.com/en/docs-7.14.0/compatibility/compatibility-matrix.html>`__
   for more information.

.. selected:: i=pip

   .. selected:: rocm-ver=10.1.0

      - Ensure your system has Python 3.12 installed and accessible.

   .. selected:: rocm-ver=10.0.0 rocm-ver=7.14.1 rocm-ver=7.14.0

      - Ensure your system has Python 3.14 or 3.12 installed and accessible.

.. _migraphx-package-install:

Install MIGraphX on Linux
=========================

MIGraphX requires ROCm to be installed on your system first.

Install ROCm
------------

.. selected:: rocm-ver=10.1.0

   For instructions, see `Install AMD ROCm 10.1.0
   <https://rocm.docs.amd.com/en/docs-10.1.0/install/rocm.html?fam=all>`__. Use the
   selector panel on that page to view instructions appropriate for your system
   environment.

.. selected:: rocm-ver=10.0.0

   For instructions, see `Install AMD ROCm 10.0.0
   <https://rocm.docs.amd.com/en/docs-10.0.0/install/rocm.html?fam=all>`__. Use the
   selector panel on that page to view instructions appropriate for your system
   environment.

.. selected:: rocm-ver=7.14.1

   For instructions, see `Install AMD ROCm 7.14.1
   <https://rocm.docs.amd.com/en/docs-7.14.1/install/rocm.html?fam=all>`__. Use the
   selector panel on that page to view instructions appropriate for your system
   environment.

.. selected:: rocm-ver=7.14.0

   For instructions, see `Install AMD ROCm 7.14.0
   <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=all>`__. Use the
   selector panel on that page to view instructions appropriate for your system
   environment.

.. include:: ./include/migraphx/rocm10.1.0-pkg-install.rst

.. include:: ./include/migraphx/rocm10.0.0-pkg-install.rst

.. include:: ./include/migraphx/rocm7.14.1-pkg-install.rst

.. include:: ./include/migraphx/rocm7.14.0-pkg-install.rst

.. include:: ./include/migraphx/rocm10.1.0-pip-install.rst

.. include:: ./include/migraphx/rocm10.0.0-pip-install.rst

.. include:: ./include/migraphx/rocm7.14.1-pip-install.rst

.. include:: ./include/migraphx/rocm7.14.0-pip-install.rst

.. Verify your installation
.. ------------------------
..
.. .. selected:: i=pkgman
..
..    1. Download the test packages.
..
..       .. tab-set::
..
..          .. tab-item:: Debian-based distros
..             :sync: deb
..
..             .. code-block:: bash
..
..                wget https://rocm.frameworks-prereleases.amd.com/deb-staging/device-all/migraphx-tests_2.16.0+rocm7.14.0rc3.4bcfe75.py312_amd64.deb
..
..          .. tab-item:: RPM-based distros
..             :sync: rpm
..
..             .. code-block:: bash
..
..                wget https://rocm.frameworks-prereleases.amd.com/rpm-staging/device-all/migraphx/migraphx-tests-2.16.0.rocm7.14.0rc3.4bcfe75-1.el8.x86_64.rpm
..
..    2. Install the test packages.
..
..       .. tab-set::
..
..          .. tab-item:: Debian-based distros
..             :sync: deb
..
..             .. code-block:: bash
..
..                sudo dpkg -i migraphx-tests_2.16.0+rocm7.14.0rc3.4bcfe75.py312_amd64.deb
..
..          .. tab-item:: RPM-based distros
..             :sync: rpm
..
..             .. code-block:: bash
..
..                sudo rpm -i migraphx-tests-2.16.0.rocm7.14.0rc3.4bcfe75-1.el8.x86_64.rpm
..
..    3. Run the test suite. Set ``ROCM_PATH`` to your ROCm installation directory
..       which differs depending on how you installed it.
..
..       .. code-block:: bash
..
..          cd /opt/rocm/libexec/installed-tests/migraphx/
..          mkdir /tmp/migraphx
..          cp -r * /tmp/migraphx
..          cd /tmp/migraphx/
..
..          export ROCM_PATH=/opt/rocm
..          export LD_LIBRARY_PATH=$ROCM_PATH/lib:$LD_LIBRARY_PATH
..          ctest -V
..
.. .. selected:: i=pip
..
..    1. Download the test wheel (for PyTest) and tarball (for CTest).
..
..       .. code-block:: bash
..
..          wget https://rocm.frameworks-prereleases.amd.com/whl-staging/device-all/migraphx-tests/migraphx_tests-2.16.0+rocm7.14.0rc3.4bcfe75-cp312-none-manylinux_2_28_x86_64.whl
..          wget https://rocm.frameworks.amd.com/whl-multi-arch/migraphx/migraphx-2.16.0%2Brocm7.14.0.tar.gz
..
..    2. Install the test wheel.
..
..       .. code-block:: bash
..
..          python -m pip install migraphx_tests-2.16.0+rocm7.14.0rc3.4bcfe75-cp312-none-manylinux_2_28_x86_64.whl
..
..    3. Run the PyTest suites.
..
..       .. code-block:: bash
..
..          ln -sf .venv/lib/python3.12/site-packages/migraphx/onnx_migraphx .venv/lib/python3.12/site-packages/onnx_migraphx
..          export LD_LIBRARY_PATH=$PWD/lib:/opt/rocm/lib:$LD_LIBRARY_PATH
..          pytest --pyargs migraphx_tests -v
..
..    4. Extract and run the CTest suite.
..
..       .. code-block:: bash
..
..          tar -xzf migraphx-2.16.0+rocm7.14.0.tar.gz
..          cd migraphx-2.16.0+rocm7.14.0
..
..          ln -sf migraphx/onnx_migraphx ../.venv/lib/python3.12/site-packages/onnx_migraphx
..          export LD_LIBRARY_PATH=$PWD/lib:/opt/rocm/lib:$LD_LIBRARY_PATH
..          ctest --test-dir . -j4 --output-on-failure
