.. |VLLM_VERSION_7141P| replace:: 0.23

.. |VLLM_DOC_7141P| replace:: `vLLM <https://docs.vllm.ai/en/v0.23.0/>`__
.. |VLLM_USAGE_DOC_7141P| replace:: `Using vLLM <https://docs.vllm.ai/en/v0.23.0/usage/>`__
.. |VLLM_DOCKER_INSTALL_DOC_7141P| replace:: `Set up using Docker (vLLM docs) <https://docs.vllm.ai/en/v0.23.0/getting_started/installation/gpu/#amd-rocm_5>`__
.. |VLLM_PIP_INSTALL_DOC_7141P| replace:: `Set up using Python (vLLM docs) <https://docs.vllm.ai/en/v0.23.0/getting_started/installation/gpu/#amd-rocm_3>`__

.. selected:: rocm-ver=7.14.1

   3. Install PyTorch 2.11 in your virtual environment. This should also
      install the ROCm core libraries as a dependency.

      .. selected:: gfx=gfx950

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx950]==2.11.0+rocm7.14.1" \
                "torchvision[device-gfx950]==0.26.0+rocm7.14.1" \
                "torchaudio==2.11.0+rocm7.14.1"

      .. selected:: gfx=gfx942

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx942]==2.11.0+rocm7.14.1" \
                "torchvision[device-gfx942]==0.26.0+rocm7.14.1" \
                "torchaudio==2.11.0+rocm7.14.1"

      .. selected:: gfx=gfx1200

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx1200]==2.11.0+rocm7.14.1" \
                "torchvision[device-gfx1200]==0.26.0+rocm7.14.1" \
                "torchaudio==2.11.0+rocm7.14.1"

      .. selected:: gfx=gfx1201

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx1201]==2.11.0+rocm7.14.1" \
                "torchvision[device-gfx1201]==0.26.0+rocm7.14.1" \
                "torchaudio==2.11.0+rocm7.14.1"

      .. selected:: gfx=gfx1100

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx1100]==2.11.0+rocm7.14.1" \
                "torchvision[device-gfx1100]==0.26.0+rocm7.14.1" \
                "torchaudio==2.11.0+rocm7.14.1"

      .. selected:: gfx=gfx1101

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx1101]==2.11.0+rocm7.14.1" \
                "torchvision[device-gfx1101]==0.26.0+rocm7.14.1" \
                "torchaudio==2.11.0+rocm7.14.1"

      .. selected:: gfx=gfx1102

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx1102]==2.11.0+rocm7.14.1" \
                "torchvision[device-gfx1102]==0.26.0+rocm7.14.1" \
                "torchaudio==2.11.0+rocm7.14.1"

      .. selected:: gfx=gfx1103

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx1103]==2.11.0+rocm7.14.1" \
                "torchvision[device-gfx1103]==0.26.0+rocm7.14.1" \
                "torchaudio==2.11.0+rocm7.14.1"

      .. selected:: gfx=gfx1151

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx1151]==2.11.0+rocm7.14.1" \
                "torchvision[device-gfx1151]==0.26.0+rocm7.14.1" \
                "torchaudio==2.11.0+rocm7.14.1"

      .. selected:: gfx=gfx1150

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx1150]==2.11.0+rocm7.14.1" \
                "torchvision[device-gfx1150]==0.26.0+rocm7.14.1" \
                "torchaudio==2.11.0+rocm7.14.1"

      .. selected:: gfx=gfx1152

         .. code-block:: bash

            python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
                "torch[device-gfx1152]==2.11.0+rocm7.14.1" \
                "torchvision[device-gfx1152]==0.26.0+rocm7.14.1" \
                "torchaudio==2.11.0+rocm7.14.1"

   4. Install Flash Attention.

      .. selected:: fam=instinct

         .. code-block:: bash

            python -m pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-cdna/flash-attn/flash_attn-2.8.3-cp314-cp314-linux_x86_64.whl

      .. selected:: fam=radeon fam=ryzen

         .. code-block:: bash

            python -m pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-rdna/flash-attn/flash_attn-2.8.3-py3-none-any.whl

   .. selected:: fam=instinct

      5. Install `AITER <https://github.com/rocm/aiter>`__.

         .. code-block:: bash

            python -m pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-cdna/amd-aiter/amd_aiter-0.1.13.post2.dev1%2Bgb32deb267.d20260901-cp314-cp314-linux_x86_64.whl

      6. Install the vLLM 0.23.1 wheel using ``uv pip``.

         .. code-block:: bash

            uv pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-cdna/vllm/vllm-0.23.1.dev1%2Brocm7.14.1.g9ddef7117.d20260901-cp314-cp314-linux_x86_64.whl

      7. Upgrade vLLM's ``tensorizer`` dependency as a workaround for
         a :ref:`compatibility issue <vllm-tensorizer-issue>`.

         .. code-block:: bash
            :substitutions:

            python -m pip install --upgrade "tensorizer==2.12.1"

   .. selected:: fam=instinct

      8. Set the following environment variables to prevent errors related to ROCm platform and Flash Attention availability when running vLLM.

         .. code-block:: bash

            export PYTHONPATH=$VIRTUAL_ENV/lib/python3.14/site-packages/_rocm_sdk_core/share/amd_smi
            export FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE

      9. Check your installation.

         .. code-block:: bash

            python -c "import vllm; print('vLLM version:', vllm.__version__)"
            python -c "import torch; print('PyTorch:', torch.__version__); print('HIP available:', torch.cuda.is_available()); print('HIP built:', torch.backends.hip.is_built() if hasattr(torch.backends, 'hip') else 'N/A')"
            python -c "import flash_attn; print('flash-attn:', flash_attn.__version__)"

      10. After setting up your environment, follow the vLLM 0.23.1 usage
          documentation to get started: |VLLM_USAGE_DOC_7141P|.

   .. selected:: fam=radeon fam=ryzen

      5. Install the vLLM 0.23.1 wheel using ``uv pip``.

         .. code-block:: bash

            uv pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-rdna/vllm/vllm-0.23.1.dev1%2Brocm7.14.1.g9ddef7117.d20260831-cp314-cp314-linux_x86_64.whl

      6. Upgrade vLLM's `tensorizer` dependency as a workaround for
         a :ref:`compatibility issue <vllm-tensorizer-issue>`.

         .. code-block:: bash
            :substitutions:

            python -m pip install --upgrade "tensorizer==2.12.1"

      7. Set the following environment variables to prevent errors related to ROCm platform and Flash Attention availability when running vLLM.

         .. code-block:: bash

            export PYTHONPATH=$VIRTUAL_ENV/lib/python3.14/site-packages/_rocm_sdk_core/share/amd_smi
            export FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE

      8. Check your installation.

         .. code-block:: bash

            python -c "import vllm; print('vLLM version:', vllm.__version__)"
            python -c "import torch; print('PyTorch:', torch.__version__); print('HIP available:', torch.cuda.is_available()); print('HIP built:', torch.backends.hip.is_built() if hasattr(torch.backends, 'hip') else 'N/A')"
            python -c "import flash_attn; print('flash-attn:', flash_attn.__version__)"

      9. After setting up your environment, follow the vLLM |VLLM_VERSION_7141P| usage
         documentation to get started: |VLLM_USAGE_DOC_7141P|.

   .. seealso::

      |VLLM_PIP_INSTALL_DOC_7141P|
