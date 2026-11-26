.. selected:: rocm-ver=7.14.1

   1. Create and activate a virtual environment or activate an existing ROCm 7.14.1 environment.
      To create a new Python 3.12 virtual environment:

      .. code-block:: bash

         python3.12 -m venv .venv
         source .venv/bin/activate

   2. Install MIGraphX using pip. See :doc:`migraphx` for installation instructions.

   3. Download and install the ONNX Runtime wheel.

      .. code-block:: bash

         python -m pip install https://rocm.frameworks.amd.com/whl-multi-arch/onnxruntime-migraphx/onnxruntime_migraphx-1.23.2%2Brocm7.14.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl

   4. Loading the MIGraphX execution provider may fail with a missing shared
      library error, such as ``libmigraphx_c.so.3`` or ``libamdhip64.so.7:
      cannot open shared object file``. ROCm and MIGraphX pip wheels place
      their shared libraries inside your virtual environment's
      ``site-packages`` instead of ``/opt/rocm``. As a workaround, update
      ``LD_LIBRARY_PATH`` with the virtual environment active so the paths
      resolve correctly. Run this command again in each new shell session
      after activating the virtual environment.

      .. code-block:: bash

         SP=$(python -c "import site; print(site.getsitepackages()[0])")
         ROCM_SDK_CORE=$(python -c "import _rocm_sdk_core, os; print(os.path.dirname(_rocm_sdk_core.__file__))")
         ROCM_SDK_LIBRARIES=$(python -c "import _rocm_sdk_libraries, os; print(os.path.dirname(_rocm_sdk_libraries.__file__))")
         export LD_LIBRARY_PATH=$ROCM_SDK_CORE/lib:$ROCM_SDK_CORE/lib/rocm_sysdeps/lib:$ROCM_SDK_LIBRARIES/lib:$SP/migraphx_libs:$LD_LIBRARY_PATH

   5. Confirm ONNX Runtime is correctly installed and the MIGraphX execution
      provider is available.

      .. code-block:: bash

         python -c "import onnxruntime as ort; print(ort.get_available_providers())"

      You should see ``MIGraphXExecutionProvider`` in the output:

      .. code-block:: text

         ['MIGraphXExecutionProvider', 'CPUExecutionProvider']
