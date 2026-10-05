.. |PKG_REPO_1010| replace:: https://stable.repo.amd.com/rocm/migraphx/whl-next/
.. |WHL_1010| replace:: "migraphx==2.18.0+rocm10.1.0"
.. |WHL_LIBS_1010| replace:: "migraphx-libs==2.18.0+rocm10.1.0"

.. selected:: rocm-ver=10.1.0

   .. selected:: i=pip
      :heading: Install MIGraphX 2.18.0 using pip
      :heading-level: 3

      After installing ROCm, install MIGraphX. This method installs MIGraphX into
      a Python virtual environment.

      1. Create and activate a virtual environment or activate an existing ROCm 10.1.0 environment.

         .. tab-set::

            .. tab-item:: Python 3.12
               :sync: py312

               .. code-block:: bash

                  python3.12 -m venv .venv
                  source .venv/bin/activate

      2. Install the MIGraphX and ``migraphx-libs`` wheels.

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1010| \
                |WHL_1010| |WHL_LIBS_1010|

      3. Verify your installation.

         Confirm that ``migraphx-driver`` is available in your virtual
         environment and reports the expected version.

         .. code-block:: bash

            migraphx-driver --version

      4. ONNX Runtime accelerates machine learning inference using the MIGraphX
         execution provider on ROCm-supported GPUs. See the :doc:`installation
         <onnxruntime>` guidance.
