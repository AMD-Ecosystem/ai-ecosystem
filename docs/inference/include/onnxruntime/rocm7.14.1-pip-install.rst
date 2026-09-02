.. selected:: rocm-ver=7.14.1

   1. Create and activate a virtual environment or activate an existing ROCm 7.14.0 environment.
      To create a new Python 3.12 virtual environment:

      .. code-block:: bash

         python3.12 -m venv .venv
         source .venv/bin/activate

   2. Download and install the wheels.

      .. code-block:: bash

         python -m pip install https://rocm.frameworks.amd.com/whl-multi-arch/onnxruntime-migraphx/onnxruntime_migraphx-1.23.2%2Brocm7.14.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl

.. selected:: rocm-ver=7.14.1
   :heading: Verify your installation
   :heading-level: 3

   1. Download and extract the test binary zip file.

      .. code-block:: bash

         wget https://rocm.frameworks.amd.com/whl-multi-arch/onnxruntime-migraphx/onnxruntime_migraphx-1.23.2%2Brocm7.14.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.zip
         unzip onnxruntime_migraphx-1.23.2+rocm7.14.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.zip
         cd build/Linux/Release

   2. Run the test suite.

      .. code-block:: bash

         ./onnxruntime_test_all \
             --gtest_filter=-:CudaKernelTest.SoftmaxGrad_LargeTensor_LastAxis_Float16:CudaKernelTest.SoftmaxGrad_LargeTensor_LastAxis_Float16_NoPowerOfTwo:CudaKernelTest.SoftmaxGrad_LargeTensor_AllAxis_Float16:CudaKernelTest.SoftmaxGrad_LargeTensor_AllAxis_Float16_NoPowerOfTwo:CudaKernelTest.LogSoftmaxGrad_LargeTensor_LastAxis_Float16:CudaKernelTest.LogSoftmaxGrad_LargeTensor_LastAxis_Float16_NoPowerOfTwo:CudaKernelTest.LogSoftmaxGrad_LargeTensor_AllAxis_Float16:CudaKernelTest.LogSoftmaxGrad_LargeTensor_AllAxis_Float16_NoPowerOfTwo:ReductionOpTest.ReductionVariationTest:GatherOpTest.Gather_invalid_index_cpu:Scatter.InvalidIndex:GradientCheckerTest.AddGrad:GradientCheckerTest.SubGrad:GradientCheckerTest.MulGrad:GradientCheckerTest.DivGrad:NhwcTransformerTests*:QDQTransformerTests*Sample Output for Unit Test


