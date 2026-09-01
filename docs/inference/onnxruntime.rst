:selector-toc2: Installation environment
:selector-toc2-icon: fa-solid fa-computer

*****************************
Install ONNX Runtime for ROCm
*****************************

`ONNX Runtime <https://onnxruntime.ai/docs/>`__ accelerates machine learning
inference using the :doc:`AMD MIGraphX <migraphx>` execution provider on
ROCm-supported GPUs.

.. selector:: ROCm version
   :key: rocm-ver

   .. selector-option:: 10.0.0
      :value: 10.0.0
      :width: 4

   .. selector-option:: 7.14.1
      :value: 7.14.1
      :width: 4

   .. selector-option:: 7.14.0
      :value: 7.14.0
      :width: 4

.. selector:: Installation method
   :key: i

   .. selector-option:: pip
      :value: pip
      :width: 12

Prerequisites
=============

.. selected:: rocm-ver=10.0.0

   ONNX Runtime is currently supported on:

   * ``gfx950`` AMD Instinct MI355X and MI350X

   * ``gfx942`` AMD Instinct MI325X and MI300X

   * ``gfx1200``, ``gfx1201``, ``gfx1100``, ``gfx1101``, and ``gfx1102`` Radeon GPUs.

   See the `ROCm compatibility matrix
   <https://rocm.docs.amd.com/en/docs-10.0.0/compatibility/compatibility-matrix.html>`__
   for more information.

   * Ensure your system has Python 3.14 or 3.12 installed and accessible.

.. selected:: rocm-ver=7.14.1

   ONNX Runtime is currently supported on ``gfx950`` AMD Instinct MI355X and MI350X
   data center GPUs and ``gfx942`` MI325X and MI300X GPUs. See the `ROCm
   compatibility matrix (ROCm 7.14.1)
   <https://rocm.docs.amd.com/en/docs-7.14.1/compatibility/compatibility-matrix.html>`__
   for more information.

   * Ensure your system has Python 3.12 installed and accessible.

.. selected:: rocm-ver=7.14.0

   ONNX Runtime is currently supported on ``gfx950`` AMD Instinct MI355X and MI350X
   data center GPUs and ``gfx942`` MI325X and MI300X GPUs. See the `ROCm
   compatibility matrix (ROCm 7.14.0)
   <https://rocm.docs.amd.com/en/docs-7.14.0/compatibility/compatibility-matrix.html>`__
   for more information.

   * Ensure your system has Python 3.12 installed and accessible.

Install the ROCm Core SDK
-------------------------

.. selected:: rocm-ver=10.0.0

   For instructions, see `Install AMD ROCm
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

Install ONNX Runtime using pip
------------------------------

.. include:: ./include/onnxruntime/rocm10.0.0-pip-install.rst

.. include:: ./include/onnxruntime/rocm7.14.1-pip-install.rst

.. include:: ./include/onnxruntime/rocm7.14.0-pip-install.rst

.. seealso::

   See `MIGraphX Execution Provider (ONNX Runtime docs)
   <https://onnxruntime.ai/docs/execution-providers/MIGraphX-ExecutionProvider.html#samples>`__
   for more information.
