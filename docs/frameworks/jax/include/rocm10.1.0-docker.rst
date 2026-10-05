.. |JAX0111_CP314_1010| replace:: rocm/jax:rocm10.1.0_ubuntu26.04_py3.14_jax_release_0.11.1
.. |JAX0111_CP312_1010| replace:: rocm/jax:rocm10.1.0_ubuntu24.04_py3.12_jax_release_0.11.1

.. |JAX0110_CP314_1010| replace:: rocm/jax:rocm10.1.0_ubuntu26.04_py3.14_jax_release_0.11.0
.. |JAX0110_CP312_1010| replace:: rocm/jax:rocm10.1.0_ubuntu24.04_py3.12_jax_release_0.11.0

.. |JAX0102_CP314_1010| replace:: rocm/jax:rocm10.1.0_ubuntu26.04_py3.14_jax_release_0.10.2
.. |JAX0102_CP312_1010| replace:: rocm/jax:rocm10.1.0_ubuntu24.04_py3.12_jax_release_0.10.2

.. selected:: rocm-ver=10.1.0

   .. selected:: i=docker
      :heading: Get started

      .. selected:: jax-ver=0.11.1

         1. Pull the ROCm JAX 0.11.1 Docker image.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash
                     :substitutions:

                     docker pull |JAX0111_CP314_1010|

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash
                     :substitutions:

                     docker pull |JAX0111_CP312_1010|

         2. Start the Docker container.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash
                     :substitutions:

                     docker run -it --rm \
                        --device /dev/kfd \
                        --device /dev/dri \
                        --network=host \
                        --ipc=host \
                        --group-add=video \
                        --cap-add=SYS_PTRACE \
                        --security-opt seccomp=unconfined \
                        |JAX0111_CP314_1010| \
                        bash

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash
                     :substitutions:

                     docker run -it --rm \
                        --device /dev/kfd \
                        --device /dev/dri \
                        --network=host \
                        --ipc=host \
                        --group-add=video \
                        --cap-add=SYS_PTRACE \
                        --security-opt seccomp=unconfined \
                        |JAX0111_CP312_1010| \
                        bash

      .. selected:: jax-ver=0.11.0

         1. Pull the ROCm JAX 0.11.0 Docker image.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash
                     :substitutions:

                     docker pull |JAX0110_CP314_1010|

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash
                     :substitutions:

                     docker pull |JAX0110_CP312_1010|

         2. Start the Docker container.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash
                     :substitutions:

                     docker run -it --rm \
                        --device /dev/kfd \
                        --device /dev/dri \
                        --network=host \
                        --ipc=host \
                        --group-add=video \
                        --cap-add=SYS_PTRACE \
                        --security-opt seccomp=unconfined \
                        |JAX0110_CP314_1010| \
                        bash

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash
                     :substitutions:

                     docker run -it --rm \
                        --device /dev/kfd \
                        --device /dev/dri \
                        --network=host \
                        --ipc=host \
                        --group-add=video \
                        --cap-add=SYS_PTRACE \
                        --security-opt seccomp=unconfined \
                        |JAX0110_CP312_1010| \
                        bash

      .. selected:: jax-ver=0.10.2

         1. Pull the ROCm JAX 0.10.2 Docker image.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash
                     :substitutions:

                     docker pull |JAX0102_CP314_1010|

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash
                     :substitutions:

                     docker pull |JAX0102_CP312_1010|

         2. Start the Docker container.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash
                     :substitutions:

                     docker run -it --rm \
                        --device /dev/kfd \
                        --device /dev/dri \
                        --network=host \
                        --ipc=host \
                        --group-add=video \
                        --cap-add=SYS_PTRACE \
                        --security-opt seccomp=unconfined \
                        |JAX0102_CP314_1010| \
                        bash

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash
                     :substitutions:

                     docker run -it --rm \
                        --device /dev/kfd \
                        --device /dev/dri \
                        --network=host \
                        --ipc=host \
                        --group-add=video \
                        --cap-add=SYS_PTRACE \
                        --security-opt seccomp=unconfined \
                        |JAX0102_CP312_1010| \
                        bash
