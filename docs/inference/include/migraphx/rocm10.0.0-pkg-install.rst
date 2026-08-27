.. |DEB_REPO| replace:: https://rocm.frameworks-prereleases.amd.com/deb-multi-arch-staging/
.. |RPM_REPO| replace:: https://rocm.frameworks-prereleases.amd.com/rpm-multi-arch-staging/

.. |WGET_DEB| replace:: amdrocm-migraphx_2.17.0%2Brocm10.0.0rc4.becdb3d_amd64.deb
.. |WGET_DEV_DEB| replace:: amdrocm-migraphx-dev_2.17.0%2Brocm10.0.0rc4.becdb3d_amd64.deb
.. |DEB| replace:: amdrocm-migraphx_2.17.0+rocm10.0.0rc4.becdb3d_amd64.deb
.. |DEV_DEB| replace:: amdrocm-migraphx-dev_2.17.0+rocm10.0.0rc4.becdb3d_amd64.deb

.. |RPM| replace:: amdrocm-migraphx-2.17.0.rocm10.0.0rc4.becdb3d-1.el8.x86_64.rpm
.. |DEV_RPM| replace:: amdrocm-migraphx-devel-2.17.0.rocm10.0.0rc4.becdb3d-1.el8.x86_64.rpm

.. selected:: rocm-ver=10.0.0

   .. selected:: i=pkgman
      :heading: Install MIGraphX 2.17.0 via package manager
      :heading-level: 3

      This method installs MIGraphX system-wide via ``.deb`` or ``.rpm`` packages.

      1. Download the packages.

         .. tab-set::

            .. tab-item:: Debian-based distro
               :sync: deb

               .. code-block:: bash
                  :substitutions:

                  wget |DEB_REPO||WGET_DEB|
                  wget |DEB_REPO||WGET_DEV_DEB|

            .. tab-item:: RPM-based distro
               :sync: rpm

               .. code-block:: bash
                  :substitutions:

                  wget |RPM_REPO||RPM|
                  wget |RPM_REPO||DEV_RPM|

      2. Install the packages. Supported Debian-based Linux distributions are
         Ubuntu and Debian. Supported RPM-based distributions are RHEL, Oracle Linux,
         Rocky Linux, and SLES.

         .. tab-set::

            .. tab-item:: Debian-based distro
               :sync: deb

               .. code-block:: bash
                  :substitutions:

                  sudo dpkg -i \
                    |DEB| \
                    |DEV_DEB|

            .. tab-item:: RPM-based distro
               :sync: rpm

               .. code-block:: bash
                  :substitutions:

                  sudo rpm -i \
                    |RPM| \
                    |DEV_RPM|

      3. ONNX Runtime accelerates machine learning inference using the MIGraphX
         execution provider on ROCm-supported GPUs. See the :doc:`installation
         <onnxruntime>` guidance.

