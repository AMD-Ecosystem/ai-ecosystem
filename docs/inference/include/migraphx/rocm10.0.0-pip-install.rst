.. |PKG_REPO_1000| replace:: https://stable.repo.amd.com/rocm/migraphx/whl-next/
.. |WHL_1000| replace:: "migraphx==2.17.0+rocm10.0.0"

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

            python -m pip install --index-url |PKG_REPO_1000| \
                |WHL_1000|

      3. Importing MIGraphX may fail with a missing shared library error, such
         as ``libhiprtc.so.7: cannot open shared object file``. ROCm's pip
         wheels place their shared libraries inside your virtual environment's
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

      4. Verify your installation.

         Confirm that ``migraphx-driver`` and the ``migraphx`` Python module are
         available in your virtual environment and report the expected version.

         .. code-block:: bash

            migraphx-driver --version
            python -c "import migraphx; print(migraphx.__version__)"

         You should see MIGraphX 2.17.0 in the output:

         .. code-block:: text

            MIGraphX Version: 2.17.0
            2.17.0+rocm10.0.0

      5. ONNX Runtime accelerates machine learning inference using the MIGraphX
         execution provider on ROCm-supported GPUs. See the :doc:`installation
         <onnxruntime>` guidance.

   .. selected:: i=pip
      :heading: Uninstall MIGraphX
      :heading-level: 3

      1. Remove the virtual environment containing MIGraphX.

         .. code-block:: bash

            deactivate
            rm -rf .venv
