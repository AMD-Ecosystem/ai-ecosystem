.. |PKG_REPO_1010| replace:: https://stable.repo.amd.com/rocm/migraphx/whl-next/
.. |WHL_1010| replace:: "migraphx==2.18.0+rocm10.1.0"
.. |WHL_LIBS_1010| replace:: "migraphx-libs==2.18.0+rocm10.1.0"

.. selected:: rocm-ver=10.1.0

   .. selected:: i=pip
      :heading: Install MIGraphX 2.18.0 using pip
      :heading-level: 3

      After installing ROCm, install MIGraphX. This method installs MIGraphX into
      a Python virtual environment.

      1. Create and activate a virtual environment or activate an existing ROCm 10.1.0 environment.

         .. tab-set::

            .. tab-item:: Python 3.12
               :sync: py312

               .. code-block:: bash

                  python3.12 -m venv .venv
                  source .venv/bin/activate

      2. Install the MIGraphX and ``migraphx-libs`` wheels.

         .. code-block:: bash
            :substitutions:

            python -m pip install --index-url |PKG_REPO_1010| \
                |WHL_1010| |WHL_LIBS_1010|

      3. **If you installed ROCm 10.1.0 using your Linux distribution's package
         manager** instead of pip, importing MIGraphX fails with
         ``libhsa-runtime64.so.1: cannot open shared object file``. As
         a workaround, update ``LD_LIBRARY_PATH`` to link to the required ROCm
         libraries in your installation path:

         .. tab-set::

            .. tab-item:: Active session
               :sync: active

               Set the environment variable for the current shell session
               only. To keep this setting across sessions, use System-wide
               setup or User setup.

               .. code-block:: bash

                  # MIGraphX Environment Setup
                  export ROCM_PATH=/opt/rocm/core-10.1
                  export LD_LIBRARY_PATH=$ROCM_PATH/lib:$LD_LIBRARY_PATH

            .. tab-item:: System-wide setup
               :sync: system

               Create a profile script so that all users inherit the
               MIGraphX environment variables when they start a shell
               session.

               .. code-block:: bash

                  # MIGraphX Environment Setup
                  sudo tee /etc/profile.d/set-migraphx-env.sh << 'EOF'
                  export ROCM_PATH=/opt/rocm/core-10.1
                  export LD_LIBRARY_PATH=$ROCM_PATH/lib:$LD_LIBRARY_PATH
                  EOF

                  sudo chmod +x /etc/profile.d/set-migraphx-env.sh
                  source /etc/profile.d/set-migraphx-env.sh

            .. tab-item:: User setup
               :sync: user

               Configure the MIGraphX environment for your user by updating
               your shell startup configuration file.

               .. tab-set::

                  .. tab-item:: .bashrc
                     :sync: bashrc

                     .. code-block:: bash

                        # MIGraphX Environment Setup
                        tee --append ~/.bashrc << 'EOF'
                        # BEGIN MIGraphX environment configuration
                        export ROCM_PATH=/opt/rocm/core-10.1
                        export LD_LIBRARY_PATH=$ROCM_PATH/lib:$LD_LIBRARY_PATH
                        # END MIGraphX environment configuration
                        EOF

                        source ~/.bashrc

                  .. tab-item:: .profile
                     :sync: profile

                     .. code-block:: bash

                        # MIGraphX Environment Setup
                        tee --append ~/.profile << 'EOF'
                        # BEGIN MIGraphX environment configuration
                        export ROCM_PATH=/opt/rocm/core-10.1
                        export LD_LIBRARY_PATH=$ROCM_PATH/lib:$LD_LIBRARY_PATH
                        # END MIGraphX environment configuration
                        EOF

                        source ~/.profile

      4. Verify your installation.

         Confirm that ``migraphx-driver`` and the ``migraphx`` Python module are
         available in your virtual environment and report the expected version.

         .. code-block:: bash

            migraphx-driver --version
            python -c "import migraphx; print(migraphx.__version__)"

         You should see MIGraphX 2.18.0 in the output:

         .. code-block:: text

            2026-11-16 18:09:10.434107 [INFO] [/app/AMDMIGraphX/src/driver/main.cpp:1345] MIGraphX Version: 2.18.0.20250912-17-754-g95672916e
            2.18.0+rocm10.1.0

      5. ONNX Runtime accelerates machine learning inference using the MIGraphX
         execution provider on ROCm-supported GPUs. See the :doc:`installation
         <onnxruntime>` guidance.

   .. selected:: i=pip
      :heading: Uninstall MIGraphX
      :heading-level: 3

      1. Remove the virtual environment containing MIGraphX.

         .. code-block:: bash

            deactivate
            rm -rf .venv

      2. Remove the MIGraphX environment configuration.

         If you added the ``LD_LIBRARY_PATH`` workaround as part of the
         installation, remove it.

         .. tab-set::

            .. tab-item:: System-wide setup
               :sync: system

               If you opted for a system-wide setup during the installation
               process, remove the MIGraphX environment variables.

               .. code-block:: bash

                  sudo rm -f /etc/profile.d/set-migraphx-env.sh

            .. tab-item:: User setup
               :sync: user

               .. tab-set::

                  .. tab-item:: .bashrc
                     :sync: bashrc

                     If you opted for a user-specific setup during the installation
                     process, remove the MIGraphX environment configuration block --
                     the lines between the ``BEGIN`` and ``END`` markers -- from
                     ``~/.bashrc``.

                  .. tab-item:: .profile
                     :sync: profile

                     If you opted for a user-specific setup during the installation
                     process, remove the MIGraphX environment configuration block --
                     the lines between the ``BEGIN`` and ``END`` markers -- from
                     ``~/.profile``.
