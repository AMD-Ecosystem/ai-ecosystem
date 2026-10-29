.. |PKG_REPO_1020| replace:: https://stable.repo.amd.com/rocm/whl-next/
.. |ROCM_VER_1020| replace:: rocm10.2.0
.. |FW_REPO_1020| replace:: https://rocm.frameworks.amd.com/whl-multi-arch/vllm/

.. |VLLM_VERSION_1020P| replace:: 0.32
.. |VLLM_USAGE_DOC_1020P| replace:: `Using vLLM <https://docs.vllm.ai/en/v0.32.0/usage/>`__
.. |VLLM_PIP_INSTALL_DOC_1020P| replace:: `Set up using Python (vLLM docs) <https://docs.vllm.ai/en/v0.32.0/getting_started/installation/gpu/#amd-rocm_3>`__

.. |VLLM_WHL_1020| replace:: https://rocm.frameworks.amd.com/whl-multi-arch/vllm/vllm/vllm-0.32.1.dev0%2Bg5df63a720.d20261116.rocm102-cp314-cp314-linux_x86_64.whl

.. selected:: rocm-ver=10.2.0

   2. Install **PyTorch 2.14.0** in your virtual environment. This should also
      install the ROCm core libraries as a dependency. See
      :doc:`/frameworks/pytorch/install` for full instructions; make sure to
      select PyTorch version 2.14.0 on that page.

      .. selected:: gfx=gfx950

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "torch[device-gfx950]==2.14.0+|ROCM_VER_1020|" \
                "torchvision[device-gfx950]==0.29.0+|ROCM_VER_1020|" \
                "torchaudio==2.11.0.3+|ROCM_VER_1020|"

      .. selected:: gfx=gfx942

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "torch[device-gfx942]==2.14.0+|ROCM_VER_1020|" \
                "torchvision[device-gfx942]==0.29.0+|ROCM_VER_1020|" \
                "torchaudio==2.11.0.3+|ROCM_VER_1020|"

      .. selected:: gfx=gfx1200

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "torch[device-gfx1200]==2.14.0+|ROCM_VER_1020|" \
                "torchvision[device-gfx1200]==0.29.0+|ROCM_VER_1020|" \
                "torchaudio==2.11.0.3+|ROCM_VER_1020|"

      .. selected:: gfx=gfx1201

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "torch[device-gfx1201]==2.14.0+|ROCM_VER_1020|" \
                "torchvision[device-gfx1201]==0.29.0+|ROCM_VER_1020|" \
                "torchaudio==2.11.0.3+|ROCM_VER_1020|"

      .. selected:: gfx=gfx1100

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "torch[device-gfx1100]==2.14.0+|ROCM_VER_1020|" \
                "torchvision[device-gfx1100]==0.29.0+|ROCM_VER_1020|" \
                "torchaudio==2.11.0.3+|ROCM_VER_1020|"

      .. selected:: gfx=gfx1101

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "torch[device-gfx1101]==2.14.0+|ROCM_VER_1020|" \
                "torchvision[device-gfx1101]==0.29.0+|ROCM_VER_1020|" \
                "torchaudio==2.11.0.3+|ROCM_VER_1020|"

      .. selected:: gfx=gfx1102

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "torch[device-gfx1102]==2.14.0+|ROCM_VER_1020|" \
                "torchvision[device-gfx1102]==0.29.0+|ROCM_VER_1020|" \
                "torchaudio==2.11.0.3+|ROCM_VER_1020|"

      .. selected:: gfx=gfx1103

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "torch[device-gfx1103]==2.14.0+|ROCM_VER_1020|" \
                "torchvision[device-gfx1103]==0.29.0+|ROCM_VER_1020|" \
                "torchaudio==2.11.0.3+|ROCM_VER_1020|"

      .. selected:: gfx=gfx1151

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "torch[device-gfx1151]==2.14.0+|ROCM_VER_1020|" \
                "torchvision[device-gfx1151]==0.29.0+|ROCM_VER_1020|" \
                "torchaudio==2.11.0.3+|ROCM_VER_1020|"

      .. selected:: gfx=gfx1150

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "torch[device-gfx1150]==2.14.0+|ROCM_VER_1020|" \
                "torchvision[device-gfx1150]==0.29.0+|ROCM_VER_1020|" \
                "torchaudio==2.11.0.3+|ROCM_VER_1020|"

      .. selected:: gfx=gfx1152

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1020| \
                "torch[device-gfx1152]==2.14.0+|ROCM_VER_1020|" \
                "torchvision[device-gfx1152]==0.29.0+|ROCM_VER_1020|" \
                "torchaudio==2.11.0.3+|ROCM_VER_1020|"

   3. Install Flash Attention and `AITER <https://github.com/rocm/aiter>`__.

      .. code-block:: bash
         :substitutions:

         python -m pip install --extra-index-url |FW_REPO_1020| \
             "flash-attn==2.8.3" \
             "amd-aiter==0.1.24.post1"

   4. Install Triton 3.8.0.

      .. code-block:: bash
         :substitutions:

         python -m pip install --extra-index-url |FW_REPO_1020| \
             "triton==3.8.0+git669b31ac"

      This replaces Triton 3.9.0 installed alongside PyTorch in step 2.
      ``pip`` reports the following dependency conflict. The warning is
      expected; you can ignore it.

      .. code-block:: shell-session

         ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
         torch 2.14.0+rocm10.2.0 requires triton==3.9.0+git0a6e13e6.rocm10.2.0, but you have triton 3.8.0+git669b31ac which is incompatible.
         Successfully installed triton-3.8.0+git669b31ac

   5. Install the vLLM |VLLM_VERSION_1020P| wheel using ``uv pip``.

      .. note::

         We recommend using `uv <https://docs.astral.sh/uv/pip/>`__ to install
         the vLLM wheel. It resolves vLLM's many transitive dependencies more
         predictably than pip, which can silently pull incompatible versions
         from PyPI. If you don't have ``uv`` on your system, install it with:

         .. code-block:: bash

            python -m pip install uv

      .. code-block:: bash
         :substitutions:

         cat > overrides.txt <<'EOF'
         triton==3.8.0+git669b31ac
         EOF

         uv pip install --override overrides.txt |VLLM_WHL_1020|

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

         python <<'EOF'
         import vllm
         import torch
         import flash_attn
         from vllm.platforms import current_platform

         print('vLLM version:', vllm.__version__)
         print('vLLM platform:', current_platform.device_name)
         print('Is ROCm:', current_platform.is_rocm())
         print('PyTorch:', torch.__version__)
         print('HIP available:', torch.cuda.is_available())
         print('HIP version:', torch.version.hip)
         print('flash-attn:', flash_attn.__version__)
         for i in range(current_platform.device_count()):
             print(f'Device {i}:', current_platform.get_device_name(i))
         EOF

      You should see output similar to the following with at least one GPU listed:

      .. code-block:: text

         vLLM version: 0.32.1.dev0+g5df63a720.d20261116
         vLLM platform: rocm
         Is ROCm: True
         PyTorch: 2.14.0+rocm10.2.0
         HIP available: True
         HIP version: 7.17.26434
         flash-attn: 2.8.3
         Device 0: <AMD GPU name>

   8. After setting up your environment, follow the vLLM |VLLM_VERSION_1020P| usage
      documentation to get started: |VLLM_USAGE_DOC_1020P|.

   .. seealso::

      |VLLM_PIP_INSTALL_DOC_1020P|
