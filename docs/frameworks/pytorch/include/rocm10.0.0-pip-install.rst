.. |PKG_REPO| replace:: https://stable.repo.amd.com/rocm/whl-next/
.. |ROCM_VER| replace:: rocm10.0.0

.. selected:: rocm-ver=10.0.0

   3. Install the appropriate ROCm-enabled PyTorch libraries for your operating
      system and AMD hardware architecture.

      .. selected:: fam=all

         .. selected:: pytorch-ver=2.13.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-all]==2.13.0+|ROCM_VER|" \
                      "torchvision[device-all]==0.28.0+|ROCM_VER|" \
                      "torchaudio==2.11.0.2+|ROCM_VER|"

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-all]==2.12.0+|ROCM_VER|" \
                      "torchvision[device-all]==0.27.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

            .. selected:: os=windows

               .. code-block:: bat
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| "torch[device-all]==2.13.0+|ROCM_VER|" "torchvision[device-all]==0.28.0+|ROCM_VER|" "torchaudio==2.11.0.2+|ROCM_VER|"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-all]==2.11.0+|ROCM_VER|" \
                      "torchvision[device-all]==0.26.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

      .. selected:: gfx=gfx950

         .. selected:: pytorch-ver=2.13.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx950]==2.13.0+|ROCM_VER|" \
                      "torchvision[device-gfx950]==0.28.0+|ROCM_VER|" \
                      "torchaudio==2.11.0.2+|ROCM_VER|"

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx950]==2.12.0+|ROCM_VER|" \
                      "torchvision[device-gfx950]==0.27.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx950]==2.11.0+|ROCM_VER|" \
                      "torchvision[device-gfx950]==0.26.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

      .. selected:: gfx=gfx942

         .. selected:: pytorch-ver=2.13.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx942]==2.13.0+|ROCM_VER|" \
                      "torchvision[device-gfx942]==0.28.0+|ROCM_VER|" \
                      "torchaudio==2.11.0.2+|ROCM_VER|"

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx942]==2.12.0+|ROCM_VER|" \
                      "torchvision[device-gfx942]==0.27.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx942]==2.11.0+|ROCM_VER|" \
                      "torchvision[device-gfx942]==0.26.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

      .. selected:: gfx=gfx90a

         .. selected:: pytorch-ver=2.13.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx90a]==2.13.0+|ROCM_VER|" \
                      "torchvision[device-gfx90a]==0.28.0+|ROCM_VER|" \
                      "torchaudio==2.11.0.2+|ROCM_VER|"

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx90a]==2.12.0+|ROCM_VER|" \
                      "torchvision[device-gfx90a]==0.27.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx90a]==2.11.0+|ROCM_VER|" \
                      "torchvision[device-gfx90a]==0.26.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

      .. selected:: gfx=gfx908

         .. selected:: pytorch-ver=2.13.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx908]==2.13.0+|ROCM_VER|" \
                      "torchvision[device-gfx908]==0.28.0+|ROCM_VER|" \
                      "torchaudio==2.11.0.2+|ROCM_VER|"

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx908]==2.12.0+|ROCM_VER|" \
                      "torchvision[device-gfx908]==0.27.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

         .. selected:: pytorch-ver=2.11.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx908]==2.11.0+|ROCM_VER|" \
                      "torchvision[device-gfx908]==0.26.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

      .. selected:: gfx=gfx1200

         .. selected:: pytorch-ver=2.13.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1200]==2.13.0+|ROCM_VER|" \
                      "torchvision[device-gfx1200]==0.28.0+|ROCM_VER|" \
                      "torchaudio==2.11.0.2+|ROCM_VER|"

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1200]==2.12.0+|ROCM_VER|" \
                      "torchvision[device-gfx1200]==0.27.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

            .. selected:: os=windows

               .. code-block:: bat
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| "torch[device-gfx1200]==2.13.0+|ROCM_VER|" "torchvision[device-gfx1200]==0.28.0+|ROCM_VER|" "torchaudio==2.11.0.2+|ROCM_VER|"

      .. selected:: gfx=gfx1201

         .. selected:: pytorch-ver=2.13.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1201]==2.13.0+|ROCM_VER|" \
                      "torchvision[device-gfx1201]==0.28.0+|ROCM_VER|" \
                      "torchaudio==2.11.0.2+|ROCM_VER|"

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1201]==2.12.0+|ROCM_VER|" \
                      "torchvision[device-gfx1201]==0.27.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

            .. selected:: os=windows

               .. code-block:: bat
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| "torch[device-gfx1201]==2.13.0+|ROCM_VER|" "torchvision[device-gfx1201]==0.28.0+|ROCM_VER|" "torchaudio==2.11.0.2+|ROCM_VER|"

      .. selected:: gfx=gfx1100

         .. selected:: pytorch-ver=2.13.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1100]==2.13.0+|ROCM_VER|" \
                      "torchvision[device-gfx1100]==0.28.0+|ROCM_VER|" \
                      "torchaudio==2.11.0.2+|ROCM_VER|"

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1100]==2.12.0+|ROCM_VER|" \
                      "torchvision[device-gfx1100]==0.27.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

            .. selected:: os=windows

               .. code-block:: bat
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| "torch[device-gfx1100]==2.13.0+|ROCM_VER|" "torchvision[device-gfx1100]==0.28.0+|ROCM_VER|" "torchaudio==2.11.0.2+|ROCM_VER|"

      .. selected:: gfx=gfx1101

         .. selected:: pytorch-ver=2.13.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1101]==2.13.0+|ROCM_VER|" \
                      "torchvision[device-gfx1101]==0.28.0+|ROCM_VER|" \
                      "torchaudio==2.11.0.2+|ROCM_VER|"

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1101]==2.12.0+|ROCM_VER|" \
                      "torchvision[device-gfx1101]==0.27.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

            .. selected:: os=windows

               .. code-block:: bat
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| "torch[device-gfx1101]==2.13.0+|ROCM_VER|" "torchvision[device-gfx1101]==0.28.0+|ROCM_VER|" "torchaudio==2.11.0.2+|ROCM_VER|"

      .. selected:: gfx=gfx1102

         .. selected:: pytorch-ver=2.13.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1102]==2.13.0+|ROCM_VER|" \
                      "torchvision[device-gfx1102]==0.28.0+|ROCM_VER|" \
                      "torchaudio==2.11.0.2+|ROCM_VER|"

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1102]==2.12.0+|ROCM_VER|" \
                      "torchvision[device-gfx1102]==0.27.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

            .. selected:: os=windows

               .. code-block:: bat
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| "torch[device-gfx1102]==2.13.0+|ROCM_VER|" "torchvision[device-gfx1102]==0.28.0+|ROCM_VER|" "torchaudio==2.11.0.2+|ROCM_VER|"

      .. selected:: gfx=gfx1103

         .. selected:: pytorch-ver=2.13.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1103]==2.13.0+|ROCM_VER|" \
                      "torchvision[device-gfx1103]==0.28.0+|ROCM_VER|" \
                      "torchaudio==2.11.0.2+|ROCM_VER|"

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1103]==2.12.0+|ROCM_VER|" \
                      "torchvision[device-gfx1103]==0.27.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

            .. selected:: os=windows

               .. code-block:: bat
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| "torch[device-gfx1103]==2.13.0+|ROCM_VER|" "torchvision[device-gfx1103]==0.28.0+|ROCM_VER|" "torchaudio==2.11.0.2+|ROCM_VER|"

      .. selected:: gfx=gfx1030

         .. selected:: pytorch-ver=2.13.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1030]==2.13.0+|ROCM_VER|" \
                      "torchvision[device-gfx1030]==0.28.0+|ROCM_VER|" \
                      "torchaudio==2.11.0.2+|ROCM_VER|"

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1030]==2.12.0+|ROCM_VER|" \
                      "torchvision[device-gfx1030]==0.27.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

            .. selected:: os=windows

               .. code-block:: bat
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| "torch[device-gfx1030]==2.13.0+|ROCM_VER|" "torchvision[device-gfx1030]==0.28.0+|ROCM_VER|" "torchaudio==2.11.0.2+|ROCM_VER|"

      .. selected:: gfx=gfx1151

         .. selected:: pytorch-ver=2.13.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1151]==2.13.0+|ROCM_VER|" \
                      "torchvision[device-gfx1151]==0.28.0+|ROCM_VER|" \
                      "torchaudio==2.11.0.2+|ROCM_VER|"

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1151]==2.12.0+|ROCM_VER|" \
                      "torchvision[device-gfx1151]==0.27.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

            .. selected:: os=windows

               .. code-block:: bat
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| "torch[device-gfx1151]==2.13.0+|ROCM_VER|" "torchvision[device-gfx1151]==0.28.0+|ROCM_VER|" "torchaudio==2.11.0.2+|ROCM_VER|"

      .. selected:: gfx=gfx1150

         .. selected:: pytorch-ver=2.13.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1150]==2.12.0+|ROCM_VER|" \
                      "torchvision[device-gfx1150]==0.27.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1150]==2.12.0+|ROCM_VER|" \
                      "torchvision[device-gfx1150]==0.27.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

            .. selected:: os=windows

               .. code-block:: bat
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| "torch[device-gfx1150]==2.13.0+|ROCM_VER|" "torchvision[device-gfx1150]==0.28.0+|ROCM_VER|" "torchaudio==2.11.0.2+|ROCM_VER|"

      .. selected:: gfx=gfx1152

         .. selected:: pytorch-ver=2.13.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1152]==2.13.0+|ROCM_VER|" \
                      "torchvision[device-gfx1152]==0.28.0+|ROCM_VER|" \
                      "torchaudio==2.11.0.2+|ROCM_VER|"

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1152]==2.12.0+|ROCM_VER|" \
                      "torchvision[device-gfx1152]==0.27.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

            .. selected:: os=windows

               .. code-block:: bat
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| "torch[device-gfx1152]==2.13.0+|ROCM_VER|" "torchvision[device-gfx1152]==0.28.0+|ROCM_VER|" "torchaudio==2.11.0.2+|ROCM_VER|"

      .. selected:: gfx=gfx1153

         .. selected:: pytorch-ver=2.13.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1153]==2.13.0+|ROCM_VER|" \
                      "torchvision[device-gfx1153]==0.28.0+|ROCM_VER|" \
                      "torchaudio==2.11.0.2+|ROCM_VER|"

         .. selected:: pytorch-ver=2.12.0

            .. selected:: os=linux

               .. code-block:: bash
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| \
                      "torch[device-gfx1153]==2.12.0+|ROCM_VER|" \
                      "torchvision[device-gfx1153]==0.27.0+|ROCM_VER|" \
                      "torchaudio==2.11.0+|ROCM_VER|"

            .. selected:: os=windows

               .. code-block:: bat
                  :substitutions:

                  python -m pip install --index-url |PKG_REPO| "torch[device-gfx1153]==2.13.0+|ROCM_VER|" "torchvision[device-gfx1153]==0.28.0+|ROCM_VER|" "torchaudio==2.11.0.2+|ROCM_VER|"
