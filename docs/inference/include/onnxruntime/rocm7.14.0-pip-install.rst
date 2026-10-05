.. selected:: rocm-ver=7.14.0

   1. Create and activate a virtual environment or activate an existing ROCm 7.14.0 environment.
      To create a new Python 3.12 virtual environment:

      .. code-block:: bash

         python3.12 -m venv .venv
         source .venv/bin/activate

   2. Download and install the wheels.

      .. code-block:: bash

         python -m pip install https://rocm.frameworks.amd.com/whl-multi-arch/onnxruntime-migraphx/onnxruntime_migraphx-1.23.2%2Brocm7.14.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl
