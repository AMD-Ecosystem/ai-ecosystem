.. |PKG_REPO| replace:: https://stable.repo.amd.com/rocm/whl-next/
.. |ROCM_VER| replace:: 10.0.0

.. |FW_REPO| replace:: https://rocm.frameworks.amd.com/whl-multi-arch/

.. selected:: rocm-ver=10.0.0

   .. selected:: i=pip
      :heading: Install TensorFlow using pip

      For prerequisite steps and post-installation recommendations, see the `ROCm
      installation instructions <https://rocm.docs.amd.com/en/latest/install/rocm.html>`__.

      1. Set up your Python virtual environment.

         .. code-block:: bash

            python3.12 -m venv .venv

      2. Activate your Python virtual environment.

         .. code-block:: shell

            source .venv/bin/activate

      3. If you don't have an existing ROCm installation, install ROCm using the
         following command; otherwise, proceed to installing TensorFlow packages.

         .. selected:: gfx=gfx950

            .. code-block:: bash
               :substitutions:

               python -m pip install --index-url |PKG_REPO| \
                   "rocm[libraries,device-gfx950]==|ROCM_VER|"

         .. selected:: gfx=gfx942

            .. code-block:: bash
               :substitutions:

               python -m pip install --index-url |PKG_REPO| \
                   "rocm[libraries,device-gfx942]==|ROCM_VER|"

         .. selected:: gfx=gfx90a

            .. code-block:: bash
               :substitutions:

               python -m pip install --index-url |PKG_REPO| \
                   "rocm[libraries,device-gfx90a]==|ROCM_VER|"

      4. Install the ROCm-enabled TensorFlow libraries.

         .. selected:: tensorflow-ver=2.21

            .. code-block:: bash
               :substitutions:

               python -m pip install --extra-index-url |FW_REPO| \
                   "tensorflow-rocm==2.21.0+rocm10.0.0"

         .. selected:: tensorflow-ver=2.20

            .. code-block:: bash
               :substitutions:

               python -m pip install --extra-index-url |FW_REPO| \
                   "tensorflow-rocm==2.20.0+rocm10.0.0"

         .. selected:: tensorflow-ver=2.19

            .. code-block:: bash
               :substitutions:

               python -m pip install --index-url |FW_REPO| \
                   "tensorflow-rocm==2.19.1+rocm10.0.0"

      5. Update ``LD_LIBRARY_PATH`` as a :ref:`workaround
         <tensorflow-known-issues>` so TensorFlow can discover ROCm libraries and
         system dependencies.

         .. code-block:: bash

            export LD_LIBRARY_PATH=$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_core/lib:$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_core/lib/rocm_sysdeps/lib:$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_libraries/lib:$LD_LIBRARY_PATH

      5. Verify your TensorFlow installation.

         .. code-block:: shell

            python -c "import tensorflow as tf; print('TensorFlow version: ', tf.__version__); print('GPUs:', tf.config.list_physical_devices('GPU'))"
