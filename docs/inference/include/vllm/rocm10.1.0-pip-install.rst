.. |PKG_REPO_1010| replace:: https://rocm.frameworks-prereleases.amd.com/whl-multi-arch-staging/
.. |ROCM_VER_1010| replace:: rocm10.1.0rc3
.. |FW_REPO_1010| replace:: https://rocm.frameworks-prereleases.amd.com/whl-multi-arch-staging/vllm/

.. |VLLM_VERSION_1010P| replace:: 0.29
.. |VLLM_DOC_1010P| replace:: `vLLM <https://docs.vllm.ai/en/v0.29.0/>`__
.. |VLLM_USAGE_DOC_1010P| replace:: `Using vLLM <https://docs.vllm.ai/en/v0.29.0/usage/>`__
.. |VLLM_DOCKER_INSTALL_DOC_1010P| replace:: `Set up using Docker (vLLM docs) <https://docs.vllm.ai/en/v0.29.0/getting_started/installation/gpu/#amd-rocm_5>`__
.. |VLLM_PIP_INSTALL_DOC_1010P| replace:: `Set up using Python (vLLM docs) <https://docs.vllm.ai/en/v0.29.0/getting_started/installation/gpu/#amd-rocm_3>`__

.. |VLLM_WHL_1010| replace:: https://rocm.frameworks-prereleases.amd.com/whl-multi-arch-staging/vllm/vllm/vllm-0.29.1.dev0%2Brocm10.1.0rc3.g98dff2a81.d20260928-cp314-cp314-linux_x86_64.whl

.. selected:: rocm-ver=10.1.0

   3. Install PyTorch 2.12 in your virtual environment. This should also
      install the ROCm core libraries as a dependency. See
      :doc:`/frameworks/pytorch/install` for full instructions.

      .. selected:: gfx=gfx950

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1010| \
                "torch[device-gfx950]==2.12.0+|ROCM_VER_1010|" \
                "torchvision[device-gfx950]==0.27.0+|ROCM_VER_1010|" \
                "torchaudio==2.11.0+|ROCM_VER_1010|"

      .. selected:: gfx=gfx942

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1010| \
                "torch[device-gfx942]==2.12.0+|ROCM_VER_1010|" \
                "torchvision[device-gfx942]==0.27.0+|ROCM_VER_1010|" \
                "torchaudio==2.11.0+|ROCM_VER_1010|"

      .. selected:: gfx=gfx1200

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1010| \
                "torch[device-gfx1200]==2.12.0+|ROCM_VER_1010|" \
                "torchvision[device-gfx1200]==0.27.0+|ROCM_VER_1010|" \
                "torchaudio==2.11.0+|ROCM_VER_1010|"

      .. selected:: gfx=gfx1201

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1010| \
                "torch[device-gfx1201]==2.12.0+|ROCM_VER_1010|" \
                "torchvision[device-gfx1201]==0.27.0+|ROCM_VER_1010|" \
                "torchaudio==2.11.0+|ROCM_VER_1010|"

      .. selected:: gfx=gfx1100

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1010| \
                "torch[device-gfx1100]==2.12.0+|ROCM_VER_1010|" \
                "torchvision[device-gfx1100]==0.27.0+|ROCM_VER_1010|" \
                "torchaudio==2.11.0+|ROCM_VER_1010|"

      .. selected:: gfx=gfx1101

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1010| \
                "torch[device-gfx1101]==2.12.0+|ROCM_VER_1010|" \
                "torchvision[device-gfx1101]==0.27.0+|ROCM_VER_1010|" \
                "torchaudio==2.11.0+|ROCM_VER_1010|"

      .. selected:: gfx=gfx1102

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1010| \
                "torch[device-gfx1102]==2.12.0+|ROCM_VER_1010|" \
                "torchvision[device-gfx1102]==0.27.0+|ROCM_VER_1010|" \
                "torchaudio==2.11.0+|ROCM_VER_1010|"

      .. selected:: gfx=gfx1103

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1010| \
                "torch[device-gfx1103]==2.12.0+|ROCM_VER_1010|" \
                "torchvision[device-gfx1103]==0.27.0+|ROCM_VER_1010|" \
                "torchaudio==2.11.0+|ROCM_VER_1010|"

      .. selected:: gfx=gfx1151

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1010| \
                "torch[device-gfx1151]==2.12.0+|ROCM_VER_1010|" \
                "torchvision[device-gfx1151]==0.27.0+|ROCM_VER_1010|" \
                "torchaudio==2.11.0+|ROCM_VER_1010|"

      .. selected:: gfx=gfx1150

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1010| \
                "torch[device-gfx1150]==2.12.0+|ROCM_VER_1010|" \
                "torchvision[device-gfx1150]==0.27.0+|ROCM_VER_1010|" \
                "torchaudio==2.11.0+|ROCM_VER_1010|"

      .. selected:: gfx=gfx1152

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1010| \
                "torch[device-gfx1152]==2.12.0+|ROCM_VER_1010|" \
                "torchvision[device-gfx1152]==0.27.0+|ROCM_VER_1010|" \
                "torchaudio==2.11.0+|ROCM_VER_1010|"

      .. selected:: gfx=gfx1152

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1010| \
                "torch[device-gfx1153]==2.12.0+|ROCM_VER_1010|" \
                "torchvision[device-gfx1153]==0.27.0+|ROCM_VER_1010|" \
                "torchaudio==2.11.0+|ROCM_VER_1010|"

   4. Install Flash Attention and `AITER <https://github.com/rocm/aiter>`__.

      .. code-block:: bash
         :substitutions:

         python -m pip install --extra-index-url |FW_REPO_1010| \
             "flash-attn==2.8.3" \
             "amd-aiter==0.1.20.post1"

   5. Install the vLLM |VLLM_VERSION_1010P| wheel using ``uv pip``.

      .. code-block:: bash
         :substitutions:

         uv pip install |VLLM_WHL_1010|

   6. Upgrade vLLM's ``tensorizer`` dependency as a workaround for
      a :ref:`compatibility issue <vllm-tensorizer-issue>`.

      .. code-block:: bash
         :substitutions:

         python -m pip install --upgrade "tensorizer==2.12.1"

   7. Set the following environment variables to prevent errors related to ROCm platform and Flash Attention availability when running vLLM.

      .. code-block:: bash
         :substitutions:

         export PYTHONPATH=$VIRTUAL_ENV/lib/python3.14/site-packages/_rocm_sdk_core/share/amd_smi
         export FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE

      To make any of these settings permanent, add it to your shell startup file;
      ``~/.bashrc``, for instance.

   8. Check your installation.

      .. code-block:: bash
         :substitutions:

         python -c "import vllm; print('vLLM version:', vllm.__version__)"
         python -c "import torch; print('PyTorch:', torch.__version__); print('HIP available:', torch.cuda.is_available()); print('HIP built:', torch.backends.hip.is_built() if hasattr(torch.backends, 'hip') else 'N/A')"
         python -c "import flash_attn; print('flash-attn:', flash_attn.__version__)"

   9. After setting up your environment, follow the vLLM |VLLM_VERSION_1010P| usage
      documentation to get started: |VLLM_USAGE_DOC_1010P|.

   .. seealso::

      |VLLM_PIP_INSTALL_DOC_1010P|
