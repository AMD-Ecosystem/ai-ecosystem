.. |TARBALL_1010| replace:: amdrocm10-migraphx-2.18.0.tar.gz
.. |TARBALL_URL_1010| replace:: https://stable.repo.amd.com/rocm/migraphx/tarball/amdrocm10-migraphx-2.18.0.tar.gz

.. selected:: rocm-ver=10.1.0

   .. selected:: i=tar
      :heading: Install MIGraphX 2.18.0 using tarball
      :heading-level: 3

      After installing ROCm, install MIGraphX using the tarball method.

      1. Download the MIGraphX tarball.

         .. code-block:: bash
            :substitutions:

            wget |TARBALL_URL_1010|

      2. Extract the tarball.

         MIGraphX is part of the ROCm Extras set of tools that work with the
         ROCm Core SDK and requires configuring the location of a ROCm
         installation. Set the ``ROCM_INSTALL_PATH`` variable to the install
         directory of ROCm. For example, if you installed the ROCm Core SDK
         using your Linux distribution's package manager, set it to
         ``/opt/rocm/core-10.1``. If ROCm was installed via tarball to a custom
         location, set ``ROCM_INSTALL_PATH`` to that location, for example
         ``$HOME/therock-tarball/install``.

         ``MIGRAPHX_INSTALL_PATH`` is set to the installation of MIGraphX to an
         extras location within the ROCm installation.

         .. code-block:: bash
            :substitutions:

            # Set installation paths
            ROCM_INSTALL_PATH="$HOME/therock-tarball/install"
            MIGRAPHX_INSTALL_PATH="$HOME/therock-tarball/install/extras-10"

            # Extract to the MIGraphX directory
            mkdir -p $MIGRAPHX_INSTALL_PATH
            tar -xzf |TARBALL_1010| -C $MIGRAPHX_INSTALL_PATH

         .. note::

            The installation path for MIGraphX above assumes ROCm was installed
            to ``$HOME/therock-tarball/install``.

      3. Complete the following post-installation steps.

         Configure environment variables so that MIGraphX is added to the
         ``PATH`` and ``LD_LIBRARY_PATH``. ``MIGRAPHX_PATH`` and ``ROCM_PATH``
         are set to the values used during extraction.

         .. tab-set::

            .. tab-item:: User (~/.bashrc)
               :sync: bashrc

               .. code-block:: bash

                  # MIGraphX Environment Setup
                  tee --append ~/.bashrc << EOF
                  # BEGIN MIGraphX environment configuration
                  export ROCM_PATH=$ROCM_INSTALL_PATH
                  export MIGRAPHX_PATH=$MIGRAPHX_INSTALL_PATH
                  export PATH=\$MIGRAPHX_PATH/bin:\$PATH
                  export LD_LIBRARY_PATH=\$MIGRAPHX_PATH/lib:\$ROCM_PATH/lib:\$LD_LIBRARY_PATH
                  # END MIGraphX environment configuration
                  EOF

                  source ~/.bashrc

            .. tab-item:: User (~/.profile)
               :sync: profile

               .. code-block:: bash

                  # MIGraphX Environment Setup
                  tee --append ~/.profile << EOF
                  # BEGIN MIGraphX environment configuration
                  export ROCM_PATH=$ROCM_INSTALL_PATH
                  export MIGRAPHX_PATH=$MIGRAPHX_INSTALL_PATH
                  export PATH=\$MIGRAPHX_PATH/bin:\$PATH
                  export LD_LIBRARY_PATH=\$MIGRAPHX_PATH/lib:\$ROCM_PATH/lib:\$LD_LIBRARY_PATH
                  # END MIGraphX environment configuration
                  EOF

                  source ~/.profile

            .. tab-item:: System-wide
               :sync: system

               .. code-block:: bash

                  # MIGraphX Environment Setup
                  sudo tee /etc/profile.d/set-migraphx-env.sh << EOF
                  export ROCM_PATH=$ROCM_INSTALL_PATH
                  export MIGRAPHX_PATH=$MIGRAPHX_INSTALL_PATH
                  export PATH=\$MIGRAPHX_PATH/bin:\$PATH
                  export LD_LIBRARY_PATH=\$MIGRAPHX_PATH/lib:\$ROCM_PATH/lib:\$LD_LIBRARY_PATH
                  EOF

                  sudo chmod +x /etc/profile.d/set-migraphx-env.sh
                  source /etc/profile.d/set-migraphx-env.sh

      4. Verify your installation.

         Confirm that ``migraphx-driver`` is on your ``PATH`` and reports the
         expected version.

         .. code-block:: bash

            migraphx-driver --version

         .. tip::

            If the command isn't found, the environment variables from the
            previous step aren't set in your current shell. Re-run the
            ``source`` command or open a new shell session.

   .. selected:: i=tar
      :heading: Uninstall MIGraphX
      :heading-level: 3

      1. Remove the installation directory.

         To uninstall MIGraphX, remove your MIGraphX installation directory.

         .. important::

            The following command assumes you're working with the
            ``MIGRAPHX_INSTALL_PATH`` directory set to
            ``$HOME/therock-tarball/install/extras-10``. If you chose a
            different directory when installing MIGraphX, adjust the command
            accordingly.

         .. code-block:: bash

            rm -rf "$HOME/therock-tarball/install/extras-10"

      2. Remove the MIGraphX environment configuration.

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
