.. |PKG_REPO_1020| replace:: https://stable.repo.amd.com/rocm/whl-next/
.. |ROCM_VER_1020| replace:: 10.2.0

.. selected:: rocm-ver=10.2.0

   2. **If you don't have an existing ROCm 10.2.0 installation**, you can
      install ROCm using pip as follows. See the `ROCm 10.2.0 installation
      instructions
      <https://rocm.docs.amd.com/en/docs-10.2.0/install/rocm.html>`__ for
      complete guidance and other ROCm installation methods. Otherwise,
      proceed to installing JAX libraries.

      .. selected:: fam=all

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "rocm[libraries,device-all]==|ROCM_VER_1020|"

      .. selected:: gfx=gfx950

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "rocm[libraries,device-gfx950]==|ROCM_VER_1020|"

      .. selected:: gfx=gfx942

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "rocm[libraries,device-gfx942]==|ROCM_VER_1020|"

      .. selected:: gfx=gfx90a

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "rocm[libraries,device-gfx90a]==|ROCM_VER_1020|"

      .. selected:: gfx=gfx1200

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "rocm[libraries,device-gfx1200]==|ROCM_VER_1020|"

      .. selected:: gfx=gfx1201

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "rocm[libraries,device-gfx1201]==|ROCM_VER_1020|"

      .. selected:: gfx=gfx1100

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "rocm[libraries,device-gfx1100]==|ROCM_VER_1020|"

      .. selected:: gfx=gfx1101

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "rocm[libraries,device-gfx1101]==|ROCM_VER_1020|"

      .. selected:: gfx=gfx1102

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "rocm[libraries,device-gfx1102]==|ROCM_VER_1020|"

   3. Install the ROCm-enabled JAX libraries.

      .. note::

         The ``jax`` and ``jaxlib`` packages are not published to the AMD package
         repository. After installing GFX architecture-based ``jax_rocm10_plugin``
         and ``jax_rocm10_pjrt`` packages from the AMD repository, install
         ``jax`` and ``jaxlib`` from `PyPI <https://pypi.org/project/jax>`__.

      .. selected:: jax-ver=0.11.2

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "jax_rocm10_plugin==0.11.2+rocm|ROCM_VER_1020|" \
                "jax_rocm10_pjrt==0.11.2+rocm|ROCM_VER_1020|"

            # Install jax from PyPI
            python -m pip install \
                "jax==0.11.2" \
                "jaxlib==0.11.2"

      .. selected:: jax-ver=0.11.1

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "jax_rocm10_plugin==0.11.1+rocm|ROCM_VER_1020|" \
                "jax_rocm10_pjrt==0.11.1+rocm|ROCM_VER_1020|"

            # Install jax from PyPI
            python -m pip install \
                "jax==0.11.1" \
                "jaxlib==0.11.1"

      .. selected:: jax-ver=0.10.2

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "jax_rocm10_plugin==0.10.2+rocm|ROCM_VER_1020|" \
                "jax_rocm10_pjrt==0.10.2+rocm|ROCM_VER_1020|"

            # Install jax from PyPI
            python -m pip install \
                "jax==0.10.2" \
                "jaxlib==0.10.2"
