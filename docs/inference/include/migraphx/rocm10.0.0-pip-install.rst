.. |PKG_REPO| replace:: https://stable.repo.amd.com/rocm/migraphx/whl-next/
.. |WHL| replace:: "migraphx==2.17.0+rocm10.0.0"

.. selected:: rocm-ver=10.0.0

   .. selected:: i=pip
      :heading: Install MIGraphX 2.17.0 using pip
      :heading-level: 3

      After installing ROCm, install MIGraphX. This method installs MIGraphX into
      a Python virtual environment.

      1. Create and activate a virtual environment or activate an existing ROCm 10.0.0 environment.

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

      2. Install the MIGraphX and ``migraphx-libs`` wheels.

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO| \
                |WHL|

      3. ONNX Runtime accelerates machine learning inference using the MIGraphX
         execution provider on ROCm-supported GPUs. See the :doc:`installation
         <onnxruntime>` guidance.
