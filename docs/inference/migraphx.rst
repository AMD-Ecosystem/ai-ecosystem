:selector-toc2: Installation environment
:selector-toc2-icon: fa-solid fa-computer

.. |MIGRAPHX_VERSION| replace:: 2.16.0


*************************
Install MIGraphX for ROCm
*************************

MIGraphX is AMD's graph inference engine for optimizing and executing ONNX
models on AMD GPUs using ROCm. This page describes how to install MIGraphX
|MIGRAPHX_VERSION|.

MIGraphX is currently supported on ``gfx950`` AMD Instinct MI355X and MI350X
data center GPUs and ``gfx942`` MI325X and MI300X GPUs. See the `ROCm
compatibility matrix
<https://rocm.docs.amd.com/en/docs-7.14.0/compatibility/compatibility-matrix.html>`__
for more information.

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

.. selected:: i=pip

   - Ensure your system has Python 3.12 installed and accessible.

- ``wget`` available in your shell.

.. _migraphx-package-install:

Install MIGraphX on Linux
=========================

MIGraphX requires the ROCm Core SDK to be installed on your system first.

Install the ROCm Core SDK
-------------------------

For instructions, see `Install AMD ROCm
<https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?fam=all>`__. Use the
selector panel on that page to view instructions appropriate for your system
environment.

.. selected:: i=pkgman
   :heading: Install MIGraphX 2.16.0 via package manager
   :heading-level: 3

   This method installs MIGraphX system-wide via ``.deb`` or ``.rpm`` packages.

   1. Download the packages.

      .. tab-set::

         .. tab-item:: Debian-based distro
            :sync: deb

            .. code-block:: bash

               wget https://rocm.frameworks.amd.com/deb-multi-arch/amdrocm-migraphx/pool/main/amdrocm-migraphx_2.16.0-3.py312_amd64.deb
               wget https://rocm.frameworks.amd.com/deb-multi-arch/amdrocm-migraphx/pool/main/amdrocm-migraphx-dev_2.16.0-3.py312_amd64.deb

         .. tab-item:: RPM-based distro
            :sync: rpm

            .. code-block:: bash

               wget https://rocm.frameworks.amd.com/rpm-multi-arch/amdrocm-migraphx/amdrocm-migraphx-2.16.0-3.x86_64.rpm
               wget https://rocm.frameworks.amd.com/rpm-multi-arch/amdrocm-migraphx/amdrocm-migraphx-devel-2.16.0-3.x86_64.rpm

   2. Install the packages. Supported Debian-based Linux distributions are
      Ubuntu and Debian. Supported RPM-based distributions are RHEL, Oracle Linux,
      Rocky Linux, and SLES.

      .. tab-set::

         .. tab-item:: Debian-based distro
            :sync: deb

            .. code-block:: bash

               sudo dpkg -i \
                 amdrocm-migraphx_2.16.0-3.py312_amd64.deb \
                 amdrocm-migraphx-dev_2.16.0-3.py312_amd64.deb

         .. tab-item:: RPM-based distro
            :sync: rpm

            .. code-block:: bash

               sudo rpm -i \
                 amdrocm-migraphx-2.16.0-3.x86_64.rpm \
                 amdrocm-migraphx-devel-2.16.0-3.x86_64.rpm \

   3. ONNX Runtime accelerates machine learning inference using the MIGraphX
      execution provider on ROCm-supported GPUs. See the :doc:`installation
      <onnxruntime>` guidance.

.. selected:: i=pip
   :heading: Install MIGraphX 2.16.0 using pip
   :heading-level: 3

   .. _migraphx-wheel-install:

   After installing ROCm, install MIGraphX. This method installs MIGraphX into
   a Python virtual environment.

   1. Create and activate a virtual environment or activate an existing ROCm 7.14.0 environment.
      To create a new Python 3.12 virtual environment.

      .. code-block:: bash

         python3.12 -m venv .venv
         source .venv/bin/activate

   2. Download the wheel.

      .. code-block:: bash

         wget https://rocm.frameworks.amd.com/whl-multi-arch/migraphx/migraphx-2.16.0%2Brocm7.14.0-cp312-none-manylinux_2_28_x86_64.whl

   3. Install the wheels and required packages.

      .. code-block:: bash

         python -m pip install migraphx-2.16.0+rocm7.14.0-cp312-none-manylinux_2_28_x86_64.whl

   4. ONNX Runtime accelerates machine learning inference using the MIGraphX
      execution provider on ROCm-supported GPUs. See the :doc:`installation
      <onnxruntime>` guidance.

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
