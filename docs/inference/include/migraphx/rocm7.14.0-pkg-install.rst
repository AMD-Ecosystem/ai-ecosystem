.. selected:: rocm-ver=7.14.0

   .. selected:: i=pkgman
      :heading: Install MIGraphX 2.16.0 via package manager
      :heading-level: 3

      This method installs MIGraphX system-wide via ``.deb`` or ``.rpm`` packages.

      1. Download the packages.

         .. tab-set::

            .. tab-item:: Debian-based distro
               :sync: deb

               .. code-block:: bash

                  wget https://rocm.frameworks.amd.com/deb-multi-arch/amdrocm-migraphx/pool/main/amdrocm-migraphx_2.16.0-3.py312_amd64.deb
                  wget https://rocm.frameworks.amd.com/deb-multi-arch/amdrocm-migraphx/pool/main/amdrocm-migraphx-dev_2.16.0-3.py312_amd64.deb

            .. tab-item:: RPM-based distro
               :sync: rpm

               .. code-block:: bash

                  wget https://rocm.frameworks.amd.com/rpm-multi-arch/amdrocm-migraphx/amdrocm-migraphx-2.16.0-3.x86_64.rpm
                  wget https://rocm.frameworks.amd.com/rpm-multi-arch/amdrocm-migraphx/amdrocm-migraphx-devel-2.16.0-3.x86_64.rpm

      2. Install the packages. Supported Debian-based Linux distributions are
         Ubuntu and Debian. Supported RPM-based distributions are RHEL, Oracle Linux,
         Rocky Linux, and SLES.

         .. tab-set::

            .. tab-item:: Debian-based distro
               :sync: deb

               .. code-block:: bash

                  sudo dpkg -i \
                    amdrocm-migraphx_2.16.0-3.py312_amd64.deb \
                    amdrocm-migraphx-dev_2.16.0-3.py312_amd64.deb

            .. tab-item:: RPM-based distro
               :sync: rpm

               .. code-block:: bash

                  sudo rpm -i \
                    amdrocm-migraphx-2.16.0-3.x86_64.rpm \
                    amdrocm-migraphx-devel-2.16.0-3.x86_64.rpm

      3. ONNX Runtime accelerates machine learning inference using the MIGraphX
         execution provider on ROCm-supported GPUs. See the :doc:`installation
         <onnxruntime>` guidance.

