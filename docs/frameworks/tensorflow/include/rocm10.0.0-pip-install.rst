.. |PKG_REPO_1000| replace:: https://stable.repo.amd.com/rocm/whl-next/
.. |ROCM_VER_1000| replace:: 10.0.0

.. |FW_REPO_1000| replace:: https://rocm.frameworks.amd.com/whl-multi-arch/

.. selected:: rocm-ver=10.0.0

   .. selected:: i=pip
      :heading: Install TensorFlow using pip

      1. Set up and activate your Python virtual environment.

         .. code-block:: bash

            python3.12 -m venv .venv
            source .venv/bin/activate

      2. **If you don't have an existing ROCm 10.0.0 installation**, install it
         following the `ROCm 10.0.0 installation instructions
         <https://rocm.docs.amd.com/en/docs-10.0.0/install/rocm.html>`__; on that page,
         select your installation environment and method.

         .. important::

            If you installed ROCm 10.0.0 using ``pip``, TensorFlow might be
            unable to find ROCm's shared libraries. Update ``LD_LIBRARY_PATH``
            as a :ref:`workaround <tensorflow-known-issues>` so TensorFlow can
            discover ROCm libraries and system dependencies.

            .. code-block:: bash

               export LD_LIBRARY_PATH=$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_core/lib:$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_core/lib/rocm_sysdeps/lib:$VIRTUAL_ENV/lib/python3.12/site-packages/_rocm_sdk_libraries/lib:$LD_LIBRARY_PATH

      3. Install the ROCm-enabled TensorFlow libraries.

         .. selected:: tensorflow-ver=2.21

            .. code-block:: bash
               :substitutions:

               python -m pip install --extra-index-url |FW_REPO_1000| \
                   "tensorflow-rocm==2.21.0+rocm10.0.0"

         .. selected:: tensorflow-ver=2.20

            .. code-block:: bash
               :substitutions:

               python -m pip install --extra-index-url |FW_REPO_1000| \
                   "tensorflow-rocm==2.20.0+rocm10.0.0"

         .. selected:: tensorflow-ver=2.19

            .. code-block:: bash
               :substitutions:

               python -m pip install --extra-index-url |FW_REPO_1000| \
                   "tensorflow-rocm==2.19.1+rocm10.0.0"

      4. Verify your TensorFlow installation.

         .. code-block:: shell

            python -c "import tensorflow as tf; print('Built with ROCm:', tf.test.is_built_with_rocm()); print('Visible GPUs:', tf.config.list_physical_devices('GPU'))"
