.. |PKG_REPO_7141| replace:: https://repo.amd.com/rocm/whl-multi-arch/
.. |ROCM_VER_7141| replace:: 7.14.1

.. |FW_REPO_7141| replace:: https://rocm.frameworks.amd.com/whl-multi-arch/

.. selected:: rocm-ver=7.14.1

   .. selected:: i=pip
      :heading: Install TensorFlow using pip

      1. Set up and activate your Python virtual environment.

         .. code-block:: bash

            python3.12 -m venv .venv
            source .venv/bin/activate

      2. **If you don't have an existing ROCm 7.14.1 installation**, you can
         install ROCm using pip as follows. See the `ROCm 7.14.1 installation
         instructions
         <https://rocm.docs.amd.com/en/docs-7.14.1/install/rocm.html>`__ for
         complete guidance and other ROCm installation methods. Otherwise,
         proceed to installing TensorFlow packages.

         .. selected:: gfx=gfx950

            .. code-block:: bash
               :substitutions:

               python -m pip install --index-url |PKG_REPO_7141| \
                   "rocm[libraries,device-gfx950]==|ROCM_VER_7141|"

         .. selected:: gfx=gfx942

            .. code-block:: bash
               :substitutions:

               python -m pip install --index-url |PKG_REPO_7141| \
                   "rocm[libraries,device-gfx942]==|ROCM_VER_7141|"

         .. selected:: gfx=gfx90a

            .. code-block:: bash
               :substitutions:

               python -m pip install --index-url |PKG_REPO_7141| \
                   "rocm[libraries,device-gfx90a]==|ROCM_VER_7141|"

      3. Install the ROCm-enabled TensorFlow libraries.

         .. selected:: tensorflow-ver=2.21

            .. code-block:: bash
               :substitutions:

               python -m pip install --extra-index-url |FW_REPO_7141| \
                   "tensorflow-rocm==2.21.0+rocm|ROCM_VER_7141|"

         .. selected:: tensorflow-ver=2.20

            .. code-block:: bash
               :substitutions:

               python -m pip install --extra-index-url |FW_REPO_7141| \
                   "tensorflow-rocm==2.20.0+rocm|ROCM_VER_7141|"

         .. selected:: tensorflow-ver=2.19

            .. code-block:: bash
               :substitutions:

               python -m pip install --extra-index-url |FW_REPO_7141| \
                   "tensorflow-rocm==2.19.1+rocm|ROCM_VER_7141|"

      4. Update ``LD_LIBRARY_PATH`` as a :ref:`workaround
         <tensorflow-known-issues>` so TensorFlow can discover ROCm libraries and
         system dependencies.

         .. code-block:: bash

            export LD_LIBRARY_PATH=$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_core/lib:$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_core/lib/rocm_sysdeps/lib:$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_libraries/lib:$LD_LIBRARY_PATH

         If ROCm was installed using a different method, update this path to
         point to your actual ROCm installation location.

      5. Verify your TensorFlow installation.

         .. code-block:: shell

            python -c "import tensorflow as tf; print('Built with ROCm:', tf.test.is_built_with_rocm()); print('Visible GPUs:', tf.config.list_physical_devices('GPU'))"
