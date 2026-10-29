.. |PKG_REPO_1000| replace:: https://stable.repo.amd.com/rocm/whl-next/
.. |ROCM_VER_1000| replace:: rocm10.0.0
.. |FW_REPO_1000| replace:: https://rocm.frameworks.amd.com/whl-multi-arch/vllm/

.. |VLLM_VERSION_10P| replace:: 0.27
.. |VLLM_USAGE_DOC_10P| replace:: `Using vLLM <https://docs.vllm.ai/en/v0.27.0/usage/>`__
.. |VLLM_PIP_INSTALL_DOC_10P| replace:: `Set up using Python (vLLM docs) <https://docs.vllm.ai/en/v0.27.0/getting_started/installation/gpu/#amd-rocm_3>`__

.. |VLLM_WHL| replace:: https://rocm.frameworks.amd.com/whl-multi-arch/vllm/vllm/vllm-0.27.1.dev5%2Brocm10.0.0.gf46a9dfe2.d20260826-cp314-cp314-linux_x86_64.whl

.. selected:: rocm-ver=10.0.0

   2. Install **PyTorch 2.12** in your virtual environment. This should also
      install the ROCm core libraries as a dependency. See
      :doc:`/frameworks/pytorch/install` for full instructions; make sure to
      select PyTorch version 2.12.0 on that page.

      .. selected:: gfx=gfx950

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1000| \
                "torch[device-gfx950]==2.12.0+|ROCM_VER_1000|" \
                "torchvision[device-gfx950]==0.27.0+|ROCM_VER_1000|" \
                "torchaudio==2.11.0+|ROCM_VER_1000|"

      .. selected:: gfx=gfx942

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1000| \
                "torch[device-gfx942]==2.12.0+|ROCM_VER_1000|" \
                "torchvision[device-gfx942]==0.27.0+|ROCM_VER_1000|" \
                "torchaudio==2.11.0+|ROCM_VER_1000|"

      .. selected:: gfx=gfx1200

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1000| \
                "torch[device-gfx1200]==2.12.0+|ROCM_VER_1000|" \
                "torchvision[device-gfx1200]==0.27.0+|ROCM_VER_1000|" \
                "torchaudio==2.11.0+|ROCM_VER_1000|"

      .. selected:: gfx=gfx1201

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1000| \
                "torch[device-gfx1201]==2.12.0+|ROCM_VER_1000|" \
                "torchvision[device-gfx1201]==0.27.0+|ROCM_VER_1000|" \
                "torchaudio==2.11.0+|ROCM_VER_1000|"

      .. selected:: gfx=gfx1100

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1000| \
                "torch[device-gfx1100]==2.12.0+|ROCM_VER_1000|" \
                "torchvision[device-gfx1100]==0.27.0+|ROCM_VER_1000|" \
                "torchaudio==2.11.0+|ROCM_VER_1000|"

      .. selected:: gfx=gfx1101

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1000| \
                "torch[device-gfx1101]==2.12.0+|ROCM_VER_1000|" \
                "torchvision[device-gfx1101]==0.27.0+|ROCM_VER_1000|" \
                "torchaudio==2.11.0+|ROCM_VER_1000|"

      .. selected:: gfx=gfx1102

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1000| \
                "torch[device-gfx1102]==2.12.0+|ROCM_VER_1000|" \
                "torchvision[device-gfx1102]==0.27.0+|ROCM_VER_1000|" \
                "torchaudio==2.11.0+|ROCM_VER_1000|"

      .. selected:: gfx=gfx1103

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1000| \
                "torch[device-gfx1103]==2.12.0+|ROCM_VER_1000|" \
                "torchvision[device-gfx1103]==0.27.0+|ROCM_VER_1000|" \
                "torchaudio==2.11.0+|ROCM_VER_1000|"

      .. selected:: gfx=gfx1151

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1000| \
                "torch[device-gfx1151]==2.12.0+|ROCM_VER_1000|" \
                "torchvision[device-gfx1151]==0.27.0+|ROCM_VER_1000|" \
                "torchaudio==2.11.0+|ROCM_VER_1000|"

      .. selected:: gfx=gfx1150

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1000| \
                "torch[device-gfx1150]==2.12.0+|ROCM_VER_1000|" \
                "torchvision[device-gfx1150]==0.27.0+|ROCM_VER_1000|" \
                "torchaudio==2.11.0+|ROCM_VER_1000|"

      .. selected:: gfx=gfx1152

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1000| \
                "torch[device-gfx1152]==2.12.0+|ROCM_VER_1000|" \
                "torchvision[device-gfx1152]==0.27.0+|ROCM_VER_1000|" \
                "torchaudio==2.11.0+|ROCM_VER_1000|"

   3. Install Flash Attention and `AITER <https://github.com/rocm/aiter>`__.

      .. code-block:: bash
         :substitutions:

         python -m pip install --extra-index-url |FW_REPO_1000| \
             "flash-attn==2.8.3" \
             "amd-aiter==0.1.20.post1"

   4. Install the vLLM |VLLM_VERSION_10P| wheel using ``uv pip``.

      .. note::

         We recommend using `uv <https://docs.astral.sh/uv/pip/>`__ to install
         the vLLM wheel. It resolves vLLM's many transitive dependencies more
         predictably than pip, which can silently pull incompatible versions
         from PyPI. If you don't have ``uv`` on your system, install it with:

         .. code-block:: bash

            python -m pip install uv

      .. code-block:: bash
         :substitutions:

         uv pip install |VLLM_WHL|

   5. Upgrade vLLM's ``tensorizer`` dependency as a workaround for
      a :ref:`compatibility issue <vllm-tensorizer-issue>`.

      .. code-block:: bash
         :substitutions:

         python -m pip install --upgrade "tensorizer==2.12.1"

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

   8. After setting up your environment, follow the vLLM |VLLM_VERSION_10P| usage
      documentation to get started: |VLLM_USAGE_DOC_10P|.

   .. seealso::

      |VLLM_PIP_INSTALL_DOC_10P|
