.. |PKG_REPO| replace:: https://stable.repo.amd.com/rocm/whl-next/
.. |ROCM_VER| replace:: rocm10.0.0
.. |FW_REPO| replace:: https://rocm.frameworks.amd.com/whl-multi-arch/vllm/

.. |VLLM_VERSION_10P| replace:: 0.27
.. |VLLM_DOC_10P| replace:: `vLLM <https://docs.vllm.ai/en/v0.27.0/>`__
.. |VLLM_USAGE_DOC_10P| replace:: `Using vLLM <https://docs.vllm.ai/en/v0.27.0/usage/>`__
.. |VLLM_DOCKER_INSTALL_DOC_10P| replace:: `Set up using Docker (vLLM docs) <https://docs.vllm.ai/en/v0.27.0/getting_started/installation/gpu/#amd-rocm_5>`__
.. |VLLM_PIP_INSTALL_DOC_10P| replace:: `Set up using Python (vLLM docs) <https://docs.vllm.ai/en/v0.27.0/getting_started/installation/gpu/#amd-rocm_3>`__

.. |VLLM_WHL| replace:: https://rocm.frameworks.amd.com/whl-multi-arch/vllm/vllm/vllm-0.27.1.dev5%2Brocm10.0.0.gf46a9dfe2.d20260826-cp314-cp314-linux_x86_64.whl

.. selected:: rocm-ver=10.0.0

   3. Install PyTorch 2.12 in your virtual environment. This should also
      install the ROCm core libraries as a dependency. See
      :doc:`/frameworks/pytorch/install` for full instructions.

      .. selected:: gfx=gfx950

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO| \
                "torch[device-gfx950]==2.12.0+|ROCM_VER|" \
                "torchvision[device-gfx950]==0.27.0+|ROCM_VER|" \
                "torchaudio==2.11.0+|ROCM_VER|"

      .. selected:: gfx=gfx942

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO| \
                "torch[device-gfx942]==2.12.0+|ROCM_VER|" \
                "torchvision[device-gfx942]==0.27.0+|ROCM_VER|" \
                "torchaudio==2.11.0+|ROCM_VER|"

      .. selected:: gfx=gfx1200

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO| \
                "torch[device-gfx1200]==2.12.0+|ROCM_VER|" \
                "torchvision[device-gfx1200]==0.27.0+|ROCM_VER|" \
                "torchaudio==2.11.0+|ROCM_VER|"

      .. selected:: gfx=gfx1201

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO| \
                "torch[device-gfx1201]==2.12.0+|ROCM_VER|" \
                "torchvision[device-gfx1201]==0.27.0+|ROCM_VER|" \
                "torchaudio==2.11.0+|ROCM_VER|"

      .. selected:: gfx=gfx1100

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO| \
                "torch[device-gfx1100]==2.12.0+|ROCM_VER|" \
                "torchvision[device-gfx1100]==0.27.0+|ROCM_VER|" \
                "torchaudio==2.11.0+|ROCM_VER|"

      .. selected:: gfx=gfx1101

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO| \
                "torch[device-gfx1101]==2.12.0+|ROCM_VER|" \
                "torchvision[device-gfx1101]==0.27.0+|ROCM_VER|" \
                "torchaudio==2.11.0+|ROCM_VER|"

      .. selected:: gfx=gfx1102

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO| \
                "torch[device-gfx1102]==2.12.0+|ROCM_VER|" \
                "torchvision[device-gfx1102]==0.27.0+|ROCM_VER|" \
                "torchaudio==2.11.0+|ROCM_VER|"

      .. selected:: gfx=gfx1103

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO| \
                "torch[device-gfx1103]==2.12.0+|ROCM_VER|" \
                "torchvision[device-gfx1103]==0.27.0+|ROCM_VER|" \
                "torchaudio==2.11.0+|ROCM_VER|"

      .. selected:: gfx=gfx1151

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO| \
                "torch[device-gfx1151]==2.13.0+|ROCM_VER|" \
                "torchvision[device-gfx1151]==0.28.0+|ROCM_VER|" \
                "torchaudio==2.11.0.2+|ROCM_VER|"

      .. selected:: gfx=gfx1150

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO| \
                "torch[device-gfx1150]==2.12.0+|ROCM_VER|" \
                "torchvision[device-gfx1150]==0.27.0+|ROCM_VER|" \
                "torchaudio==2.11.0+|ROCM_VER|"

      .. selected:: gfx=gfx1152

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO| \
                "torch[device-gfx1152]==2.12.0+|ROCM_VER|" \
                "torchvision[device-gfx1152]==0.27.0+|ROCM_VER|" \
                "torchaudio==2.11.0+|ROCM_VER|"

      .. selected:: gfx=gfx1152

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO| \
                "torch[device-gfx1153]==2.12.0+|ROCM_VER|" \
                "torchvision[device-gfx1153]==0.27.0+|ROCM_VER|" \
                "torchaudio==2.11.0+|ROCM_VER|"

   4. Install Flash Attention and `AITER <https://github.com/rocm/aiter>`__.

      .. code-block:: bash
         :substitutions:

         python -m pip install --extra-index-url |FW_REPO| \
             "flash-attn==2.8.3" \
             "amd-aiter==0.1.20.post1"

   5. Install the vLLM |VLLM_VERSION_10P| wheel using ``uv pip``.

      .. code-block:: bash
         :substitutions:

         uv pip install |VLLM_WHL|

   6. Set the following environment variables to prevent errors related to ROCm platform and Flash Attention availability when running vLLM.

      .. code-block:: bash
         :substitutions:

         export PYTHONPATH=$VIRTUAL_ENV/lib/python3.14/site-packages/_rocm_sdk_core/share/amd_smi
         export FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE

      To make any of these settings permanent, add it to your shell startup file;
      ``~/.bashrc``, for instance.

   7. Check your installation.

      .. code-block:: bash
         :substitutions:

         python -c "import vllm; print('vLLM version:', vllm.__version__)"
         python -c "import torch; print('PyTorch:', torch.__version__); print('HIP available:', torch.cuda.is_available()); print('HIP built:', torch.backends.hip.is_built() if hasattr(torch.backends, 'hip') else 'N/A')"
         python -c "import flash_attn; print('flash-attn:', flash_attn.__version__)"

   8. After setting up your environment, follow the vLLM |VLLM_VERSION_10P| usage
      documentation to get started: |VLLM_USAGE_DOC_10P|.

   .. seealso::

      |VLLM_PIP_INSTALL_DOC_10P|
