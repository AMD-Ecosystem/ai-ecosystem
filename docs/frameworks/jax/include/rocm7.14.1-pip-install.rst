.. selected:: rocm-ver=7.14.1

   3. If you don't have an existing ROCm installation, install ROCm using the
      following command; otherwise, proceed to installing JAX libraries.

      .. selected:: fam=all

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-all]==7.14.1"

      .. selected:: gfx=gfx950

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx950]==7.14.1"

      .. selected:: gfx=gfx942

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx942]==7.14.1"

      .. selected:: gfx=gfx90a

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx90a]==7.14.1"

      .. selected:: gfx=gfx1200

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx1200]==7.14.1"

      .. selected:: gfx=gfx1201

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx1201]==7.14.1"

      .. selected:: gfx=gfx1100

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx1100]==7.14.1"

      .. selected:: gfx=gfx1101

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx1101]==7.14.1"

      .. selected:: gfx=gfx1102

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "rocm[libraries,device-gfx1102]==7.14.1"

   4. Install the ROCm-enabled JAX libraries.

      .. note::

         The ``jax`` and ``jaxlib`` packages are not published to the AMD package
         repository. After installing GFX architecture-based ``jax_rocm7_plugin``
         and ``jax_rocm7_pjrt`` packages from the AMD repository, install
         ``jax`` and ``jaxlib`` from `PyPI <https://pypi.org/project/jax>`__.

      .. selected:: jax-ver=0.10.0

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "jax_rocm7_plugin==0.10.0+rocm7.14.1" \
                "jax_rocm7_pjrt==0.10.0+rocm7.14.1"

            # Install jax from PyPI
            python -m pip install \
                "jax==0.10.0" \
                "jaxlib==0.10.0"

      .. selected:: jax-ver=0.9.1

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "jax_rocm7_plugin==0.9.1+rocm7.14.1" \
                "jax_rocm7_pjrt==0.9.1+rocm7.14.1"

            # Install jax from PyPI
            python -m pip install \
                "jax==0.9.1" \
                "jaxlib==0.9.1"

