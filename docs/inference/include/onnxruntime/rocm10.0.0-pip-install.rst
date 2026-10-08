.. |PKG_REPO_1000| replace:: https://stable.repo.amd.com/rocm/onnxruntime/whl-next/
.. |WHL_1000| replace:: "onnxruntime-ep-migraphx==1.0.0+rocm10.0.0"

.. selected:: rocm-ver=10.0.0

   1. Create and activate a virtual environment or activate an existing ROCm
      10.0.0 environment.

      .. tab-set::

         .. tab-item:: Python 3.14
            :sync: py314

            .. code-block:: bash

               python3.14 -m venv .venv
               source .venv/bin/activate

         .. tab-item:: Python 3.12
            :sync: py312

            .. code-block:: bash

               python3.12 -m venv .venv
               source .venv/bin/activate

   2. Install MIGraphX using pip. See :doc:`migraphx` for installation instructions.

   3. Install ONNX Runtime and the ``onnxruntime-ep-migraphx`` execution provider plugin.

      .. code-block:: bash
         :substitutions:

         python -m pip install --extra-index-url |PKG_REPO_1000| |WHL_1000|

   4. As a workaround due to packaging issues, create the required soname
      symlink and set library search paths. For example, if you installed
      MIGraphX using pip:

      .. code-block:: bash

         SP=$(python -c "import site; print(site.getsitepackages()[0])")
         ln -sf $SP/onnxruntime/capi/libonnxruntime.so.1.29.0 $SP/onnxruntime/capi/libonnxruntime.so.1
         export LD_LIBRARY_PATH=$SP/onnxruntime/capi:$SP/migraphx_libs:$LD_LIBRARY_PATH

      .. tip::

         The symlink only needs to be created once. For persistence,
         ``LD_LIBRARY_PATH`` should be set for each shell session or added to
         your shell startup script (e.g. ``~/.bashrc``).

   5. Confirm ONNX Runtime is correctly installed and the MIGraphX execution
      provider is available.

      The EP plugin must be explicitly registered using
      ``onnxruntime_ep_migraphx`` before querying available providers.
      ``migraphx`` must be imported first to initialize the ROCm runtime.

      .. code-block:: bash

         python -c "import migraphx, onnxruntime as ort, onnxruntime_ep_migraphx as m; [ort.register_execution_provider_library(n,p) for n,p in zip(m.get_ep_names(), m.get_library_paths())]; print(ort.get_available_providers())"

      You should see ``MIGraphXExecutionProvider`` in the output:

      .. code-block:: text

         ['CPUExecutionProvider', 'MIGraphXExecutionProvider']
