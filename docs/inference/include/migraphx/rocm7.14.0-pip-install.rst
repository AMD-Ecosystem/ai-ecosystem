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

      4. ONNX Runtime accelerates machine learning inference using the MIGraphX
         execution provider on ROCm-supported GPUs. See the :doc:`installation
         <onnxruntime>` guidance.
