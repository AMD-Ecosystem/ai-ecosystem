.. selected:: rocm-ver=7.14.0

   .. selected:: i=pip
      :heading: Install MIGraphX 2.16.0 using pip
      :heading-level: 3

      .. _migraphx-wheel-install:

      After installing ROCm, install MIGraphX. This method installs MIGraphX into
      a Python virtual environment.

      1. Create and activate a virtual environment or activate an existing ROCm 7.14.0 environment.
         To create a new Python 3.12 virtual environment:

         .. code-block:: bash

            python3.12 -m venv .venv
            source .venv/bin/activate

      2. Download the wheel.

         .. code-block:: bash

            wget https://rocm.frameworks.amd.com/whl-multi-arch/migraphx/migraphx-2.16.0%2Brocm7.14.0-cp312-none-manylinux_2_28_x86_64.whl

      3. Install the wheels and required packages.

         .. code-block:: bash

            python -m pip install migraphx-2.16.0+rocm7.14.0-cp312-none-manylinux_2_28_x86_64.whl

      4. Importing MIGraphX may fail with a missing shared library error, such
         as ``libmigraphx_gpu.so.2016000: cannot open shared object file`` or
         ``libhiprtc.so.7: cannot open shared object file``. ROCm's pip wheels
         place their shared libraries inside your virtual environment's
         ``site-packages`` instead of ``/opt/rocm``. As a workaround, update
         ``LD_LIBRARY_PATH`` to link to the required ROCm libraries. Set the
         environment variable for the current shell session with the virtual
         environment active so the paths resolve correctly. Run this command
         again in each new shell session after activating the virtual
         environment.

         .. code-block:: bash

            # MIGraphX Environment Setup
            ROCM_SDK_CORE=$(python -c "import _rocm_sdk_core, os; print(os.path.dirname(_rocm_sdk_core.__file__))")
            ROCM_SDK_LIBRARIES=$(python -c "import _rocm_sdk_libraries, os; print(os.path.dirname(_rocm_sdk_libraries.__file__))")
            export LD_LIBRARY_PATH=$ROCM_SDK_CORE/lib:$ROCM_SDK_CORE/lib/rocm_sysdeps/lib:$ROCM_SDK_LIBRARIES/lib:$LD_LIBRARY_PATH

      5. Verify your installation.

         Confirm that ``migraphx-driver`` and the ``migraphx`` Python module are
         available in your virtual environment and report the expected version.

         .. code-block:: bash

            migraphx-driver --version
            python -c "import migraphx; print(migraphx.__version__)"

         You should see MIGraphX 2.16.0 in the output:

         .. code-block:: text

            MIGraphX Version: 2.16.0
            2.16.0+rocm7.14.0

      6. ONNX Runtime accelerates machine learning inference using the MIGraphX
         execution provider on ROCm-supported GPUs. See the :doc:`installation
         <onnxruntime>` guidance.

   .. selected:: i=pip
      :heading: Uninstall MIGraphX
      :heading-level: 3

      1. Remove the virtual environment containing MIGraphX.

         .. code-block:: bash

            deactivate
            rm -rf .venv
