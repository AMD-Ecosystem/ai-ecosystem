.. selected:: rocm-ver=10.1.0

   .. selected:: i=pkgman
      :heading: Install MIGraphX 2.18.0 via package manager
      :heading-level: 3

      Use the following steps to install MIGraphX system-wide using your
      distribution's package manager on top of ROCm core libraries.

      .. selector:: Linux distribution
         :key: os

         .. selector-option:: Ubuntu
            :value: ubuntu
            :width: 4

         .. selector-option:: Debian
            :value: debian
            :width: 4

         .. selector-option:: RHEL
            :value: rhel
            :width: 4

         .. selector-option:: Oracle Linux
            :value: oracle-linux
            :width: 4

         .. selector-option:: Rocky Linux
            :value: rocky-linux
            :width: 4

         .. selector-option:: SLES
            :value: sles
            :width: 4

      .. selected:: os=ubuntu

         .. selector:: Ubuntu version
            :key: ubuntu-ver

            .. selector-option:: 26.04.1
               :width: 4

            .. selector-option:: 24.04.5
               :width: 4

            .. selector-option:: 22.04.5
               :width: 4

      .. selected:: os=debian

         .. selector:: Debian version
            :key: debian-ver

            .. selector-option:: 13
               :width: 6

            .. selector-option:: 12
               :width: 6

      .. selected:: os=rhel

         .. selector:: RHEL version
            :key: rhel-ver

            .. selector-option:: 10.2
               :width: 2

            .. selector-option:: 10.0
               :width: 2

            .. selector-option:: 9.8
               :width: 2

            .. selector-option:: 9.6
               :width: 2

            .. selector-option:: 9.4
               :width: 2

            .. selector-option:: 8.10
               :width: 2

      .. selected:: os=oracle-linux

         .. selector:: Oracle Linux version
            :key: oracle-linux-ver

            .. selector-option:: 10
               :width: 4

            .. selector-option:: 9
               :width: 4

            .. selector-option:: 8
               :width: 4

      .. selected:: os=rocky-linux

         .. selector:: Rocky Linux version
            :key: rocky-linux-ver

            .. selector-option:: 9
               :width: 12

      .. selected:: os=sles

         .. selector:: SLES version
            :key: sles-ver

            .. selector-option:: 16
               :width: 6

            .. selector-option:: 15.7
               :width: 6

      .. raw:: html

         <br>

      1. Register the ROCm MIGraphX repository.

         .. selected:: os=ubuntu

            .. selected:: ubuntu-ver=26.04.1

               .. code-block:: bash

                  sudo mkdir --parents --mode=0755 /etc/apt/keyrings
                  wget https://stable.repo.amd.com/rocm/gpg/packages.gpg -O - | \
                      gpg --dearmor | sudo tee /etc/apt/keyrings/amdrocm.gpg > /dev/null
                  sudo tee /etc/apt/sources.list.d/amdrocm-migraphx.sources << 'EOF'
                  X-Repo-Id: amdrocm-migraphx
                  Types: deb
                  URIs: https://stable.repo.amd.com/rocm/migraphx/packages/ubuntu2604/
                  Suites: stable
                  Components: main
                  Architectures: amd64
                  Signed-By: /etc/apt/keyrings/amdrocm.gpg
                  Enabled: yes
                  EOF

                  sudo apt update

            .. selected:: ubuntu-ver=24.04.5

               .. code-block:: bash

                  sudo mkdir --parents --mode=0755 /etc/apt/keyrings
                  wget https://stable.repo.amd.com/rocm/gpg/packages.gpg -O - | \
                      gpg --dearmor | sudo tee /etc/apt/keyrings/amdrocm.gpg > /dev/null
                  sudo tee /etc/apt/sources.list.d/amdrocm-migraphx.sources << 'EOF'
                  X-Repo-Id: amdrocm-migraphx
                  Types: deb
                  URIs: https://stable.repo.amd.com/rocm/migraphx/packages/ubuntu2404/
                  Suites: stable
                  Components: main
                  Architectures: amd64
                  Signed-By: /etc/apt/keyrings/amdrocm.gpg
                  Enabled: yes
                  EOF

                  sudo apt update

            .. selected:: ubuntu-ver=22.04.5

               .. code-block:: bash

                  sudo mkdir --parents --mode=0755 /etc/apt/keyrings
                  wget https://stable.repo.amd.com/rocm/gpg/packages.gpg -O - | \
                      gpg --dearmor | sudo tee /etc/apt/keyrings/amdrocm.gpg > /dev/null
                  sudo tee /etc/apt/sources.list.d/amdrocm-migraphx.sources << 'EOF'
                  X-Repo-Id: amdrocm-migraphx
                  Types: deb
                  URIs: https://stable.repo.amd.com/rocm/migraphx/packages/ubuntu2204/
                  Suites: stable
                  Components: main
                  Architectures: amd64
                  Signed-By: /etc/apt/keyrings/amdrocm.gpg
                  Enabled: yes
                  EOF

                  sudo apt update

         .. selected:: os=debian

            .. selected:: debian-ver=13

               .. code-block:: bash

                  sudo mkdir --parents --mode=0755 /etc/apt/keyrings
                  wget https://stable.repo.amd.com/rocm/gpg/packages.gpg -O - | \
                      gpg --dearmor | sudo tee /etc/apt/keyrings/amdrocm.gpg > /dev/null
                  sudo tee /etc/apt/sources.list.d/amdrocm-migraphx.sources << 'EOF'
                  X-Repo-Id: amdrocm-migraphx
                  Types: deb
                  URIs: https://stable.repo.amd.com/rocm/migraphx/packages/debian13/
                  Suites: stable
                  Components: main
                  Architectures: amd64
                  Signed-By: /etc/apt/keyrings/amdrocm.gpg
                  Enabled: yes
                  EOF

                  sudo apt update

            .. selected:: debian-ver=12

               .. code-block:: bash

                  sudo mkdir --parents --mode=0755 /etc/apt/keyrings
                  wget https://stable.repo.amd.com/rocm/gpg/packages.gpg -O - | \
                      gpg --dearmor | sudo tee /etc/apt/keyrings/amdrocm.gpg > /dev/null
                  sudo tee /etc/apt/sources.list.d/amdrocm-migraphx.sources << 'EOF'
                  X-Repo-Id: amdrocm-migraphx
                  Types: deb
                  URIs: https://stable.repo.amd.com/rocm/migraphx/packages/debian12/
                  Suites: stable
                  Components: main
                  Architectures: amd64
                  Signed-By: /etc/apt/keyrings/amdrocm.gpg
                  Enabled: yes
                  EOF

                  sudo apt update

         .. selected:: os=rhel

            .. selected:: rhel-ver=10.2 rhel-ver=10.0

               .. code-block:: bash

                  sudo tee /etc/yum.repos.d/amdrocm-migraphx.repo <<EOF
                  [amdrocm-migraphx]
                  name=AMD ROCm MIGraphX
                  baseurl=https://stable.repo.amd.com/rocm/migraphx/packages/rhel10/x86_64
                  enabled=1
                  gpgcheck=1
                  gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
                  priority=50
                  EOF
                  sudo dnf clean all

            .. selected:: rhel-ver=9.8 rhel-ver=9.6 rhel-ver=9.4

               .. code-block:: bash

                  sudo tee /etc/yum.repos.d/amdrocm-migraphx.repo <<EOF
                  [amdrocm-migraphx]
                  name=AMD ROCm MIGraphX
                  baseurl=https://stable.repo.amd.com/rocm/migraphx/packages/rhel9/x86_64
                  enabled=1
                  gpgcheck=1
                  gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
                  priority=50
                  EOF
                  sudo dnf clean all

            .. selected:: rhel-ver=8.10

               .. code-block:: bash

                  sudo tee /etc/yum.repos.d/amdrocm-migraphx.repo <<EOF
                  [amdrocm-migraphx]
                  name=AMD ROCm MIGraphX
                  baseurl=https://stable.repo.amd.com/rocm/migraphx/packages/rhel8/x86_64
                  enabled=1
                  gpgcheck=1
                  gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
                  priority=50
                  EOF
                  sudo dnf clean all

         .. selected:: os=oracle-linux

            .. selected:: oracle-linux-ver=10

               .. code-block:: bash

                  sudo tee /etc/yum.repos.d/amdrocm-migraphx.repo <<EOF
                  [amdrocm-migraphx]
                  name=AMD ROCm MIGraphX
                  baseurl=https://stable.repo.amd.com/rocm/migraphx/packages/rhel10/x86_64
                  enabled=1
                  gpgcheck=1
                  gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
                  priority=50
                  EOF
                  sudo dnf clean all

            .. selected:: oracle-linux-ver=9

               .. code-block:: bash

                  sudo tee /etc/yum.repos.d/amdrocm-migraphx.repo <<EOF
                  [amdrocm-migraphx]
                  name=AMD ROCm MIGraphX
                  baseurl=https://stable.repo.amd.com/rocm/migraphx/packages/rhel9/x86_64
                  enabled=1
                  gpgcheck=1
                  gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
                  priority=50
                  EOF
                  sudo dnf clean all

            .. selected:: oracle-linux-ver=8

               .. code-block:: bash

                  sudo tee /etc/yum.repos.d/amdrocm-migraphx.repo <<EOF
                  [amdrocm-migraphx]
                  name=AMD ROCm MIGraphX
                  baseurl=https://stable.repo.amd.com/rocm/migraphx/packages/rhel8/x86_64
                  enabled=1
                  gpgcheck=1
                  gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
                  priority=50
                  EOF
                  sudo dnf clean all

         .. selected:: os=rocky-linux

            .. code-block:: bash

               sudo tee /etc/yum.repos.d/amdrocm-migraphx.repo <<EOF
               [amdrocm-migraphx]
               name=AMD ROCm MIGraphX
               baseurl=https://stable.repo.amd.com/rocm/migraphx/packages/rhel9/x86_64
               enabled=1
               gpgcheck=1
               gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
               priority=50
               EOF
               sudo dnf clean all

         .. selected:: os=sles

            .. selected:: sles-ver=16

               .. code-block:: bash

                  sudo tee /etc/zypp/repos.d/amdrocm-migraphx.repo <<EOF
                  [amdrocm-migraphx]
                  name=AMD ROCm MIGraphX
                  baseurl=https://stable.repo.amd.com/rocm/migraphx/packages/sles16/x86_64
                  enabled=1
                  gpgcheck=1
                  gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
                  priority=50
                  EOF

                  sudo zypper --gpg-auto-import-keys refresh

            .. selected:: sles-ver=15.7

               .. code-block:: bash

                  sudo tee /etc/zypp/repos.d/amdrocm-migraphx.repo <<EOF
                  [amdrocm-migraphx]
                  name=AMD ROCm MIGraphX
                  baseurl=https://stable.repo.amd.com/rocm/migraphx/packages/sles15/x86_64
                  enabled=1
                  gpgcheck=1
                  gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
                  priority=50
                  EOF

                  sudo zypper --gpg-auto-import-keys refresh

      2. Install the MIGraphX packages and ROCm dependencies.

         .. selected:: os=ubuntu os=debian

            .. code-block:: bash

               sudo apt install amdrocm10-migraphx amdrocm10-migraphx-dev

         .. selected:: os=rhel os=oracle-linux os=rocky-linux

            .. code-block:: bash

               sudo dnf install amdrocm10-migraphx amdrocm10-migraphx-devel

         .. selected:: os=sles

            .. code-block:: bash

               sudo zypper install amdrocm10-migraphx amdrocm10-migraphx-devel

      3. Complete the following post-installation steps.

         Configure environment variables so that MIGraphX is added to the
         ``PATH`` and ``LD_LIBRARY_PATH``.

         .. tab-set::

            .. tab-item:: User (~/.bashrc)
               :sync: bashrc

               .. code-block:: bash

                  # MIGraphX Environment Setup
                  tee --append ~/.bashrc << 'EOF'
                  # BEGIN MIGraphX environment configuration
                  export ROCM_PATH=/opt/rocm/core-10.1
                  export MIGRAPHX_PATH=/opt/rocm/extras-10
                  export PATH=$MIGRAPHX_PATH/bin:$PATH
                  export LD_LIBRARY_PATH=$MIGRAPHX_PATH/lib:$ROCM_PATH/lib:$LD_LIBRARY_PATH
                  # END MIGraphX environment configuration
                  EOF

                  source ~/.bashrc

            .. tab-item:: User (~/.profile)
               :sync: profile

               .. code-block:: bash

                  # MIGraphX Environment Setup
                  tee --append ~/.profile << 'EOF'
                  # BEGIN MIGraphX environment configuration
                  export ROCM_PATH=/opt/rocm/core-10.1
                  export MIGRAPHX_PATH=/opt/rocm/extras-10
                  export PATH=$MIGRAPHX_PATH/bin:$PATH
                  export LD_LIBRARY_PATH=$MIGRAPHX_PATH/lib:$ROCM_PATH/lib:$LD_LIBRARY_PATH
                  # END MIGraphX environment configuration
                  EOF

                  source ~/.profile

            .. tab-item:: System-wide
               :sync: system

               .. code-block:: bash

                  # MIGraphX Environment Setup
                  sudo tee /etc/profile.d/set-migraphx-env.sh << 'EOF'
                  export ROCM_PATH=/opt/rocm/core-10.1
                  export MIGRAPHX_PATH=/opt/rocm/extras-10
                  export PATH=$MIGRAPHX_PATH/bin:$PATH
                  export LD_LIBRARY_PATH=$MIGRAPHX_PATH/lib:$ROCM_PATH/lib:$LD_LIBRARY_PATH
                  EOF

                  sudo chmod +x /etc/profile.d/set-migraphx-env.sh
                  source /etc/profile.d/set-migraphx-env.sh

      4. ONNX Runtime accelerates machine learning inference using the MIGraphX
         execution provider on ROCm-supported GPUs. See the :doc:`installation
         <onnxruntime>` guidance.

   .. selected:: i=pkgman
      :heading: Uninstall MIGraphX
      :heading-level: 3

      1. Use your package manager to remove the installed packages.

         .. selected:: os=ubuntu os=debian

            .. code-block:: bash

               sudo apt remove amdrocm10-migraphx amdrocm10-migraphx-dev

         .. selected:: os=rhel os=oracle-linux os=rocky-linux

            .. code-block:: bash

               sudo dnf remove amdrocm10-migraphx amdrocm10-migraphx-devel

         .. selected:: os=sles

            .. code-block:: bash

               sudo zypper remove amdrocm10-migraphx amdrocm10-migraphx-devel

      2. Remove the MIGraphX repository.

         .. selected:: os=ubuntu os=debian

            .. code-block:: bash

               # Remove MIGraphX repository
               sudo rm /etc/apt/sources.list.d/amdrocm-migraphx.sources

               # Clear the cache and clean the system
               sudo apt clean
               sudo apt update

         .. selected:: os=rhel os=oracle-linux os=rocky-linux

            .. code-block:: bash

               # Remove MIGraphX repository
               sudo rm /etc/yum.repos.d/amdrocm-migraphx.repo

               # Clear the cache and clean the system
               sudo dnf clean all

         .. selected:: os=sles

            .. code-block:: bash

               # Remove MIGraphX repository
               sudo rm /etc/zypp/repos.d/amdrocm-migraphx.repo

               # Clear the cache and clean the system
               sudo zypper clean --all
               sudo zypper refresh

      3. Remove the MIGraphX environment configuration.

         .. tab-set::

            .. tab-item:: User (~/.bashrc)
               :sync: bashrc

               If you opted for a user-specific setup during the installation
               process, remove the MIGraphX environment configuration block --
               the lines between the ``BEGIN`` and ``END`` markers -- from
               ``~/.bashrc``.

            .. tab-item:: User (~/.profile)
               :sync: profile

               If you opted for a user-specific setup during the installation
               process, remove the MIGraphX environment configuration block --
               the lines between the ``BEGIN`` and ``END`` markers -- from
               ``~/.profile``.

            .. tab-item:: System-wide
               :sync: system

               If you opted for a system-wide setup during the installation
               process, remove the MIGraphX environment variables.

               .. code-block:: bash

                  sudo rm -f /etc/profile.d/set-migraphx-env.sh
