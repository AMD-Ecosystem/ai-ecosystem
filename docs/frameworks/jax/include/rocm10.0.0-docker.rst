.. selected:: rocm-ver=10.0.0

   .. selected:: i=docker
      :heading: Get started

      .. selected:: jax-ver=0.11.0

         1. Pull the ROCm JAX 0.11.0 Docker image.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash

                     docker pull rocm/jax:rocm10.0.0-jax0.11.0-py3.14

               .. tab-item:: Python 3.13
                  :sync: py313

                  .. code-block:: bash

                     docker pull rocm/jax:rocm10.0.0-jax0.11.0-py3.13

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash

                     docker pull rocm/jax:rocm10.0.0-jax0.11.0-py3.12

         2. Start the Docker container.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash

                     docker run -it --rm \
                        --device /dev/kfd \
                        --device /dev/dri \
                        --network=host \
                        --ipc=host \
                        --group-add=video \
                        --cap-add=SYS_PTRACE \
                        --security-opt seccomp=unconfined \
                        rocm/jax:rocm10.0.0-jax0.11.0-py3.14 \
                        bash

               .. tab-item:: Python 3.13
                  :sync: py313

                  .. code-block:: bash

                     docker run -it --rm \
                        --device /dev/kfd \
                        --device /dev/dri \
                        --network=host \
                        --ipc=host \
                        --group-add=video \
                        --cap-add=SYS_PTRACE \
                        --security-opt seccomp=unconfined \
                        rocm/jax:rocm10.0.0-jax0.11.0-py3.13 \
                        bash

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash

                     docker run -it --rm \
                        --device /dev/kfd \
                        --device /dev/dri \
                        --network=host \
                        --ipc=host \
                        --group-add=video \
                        --cap-add=SYS_PTRACE \
                        --security-opt seccomp=unconfined \
                        rocm/jax:rocm10.0.0-jax0.11.0-py3.12 \
                        bash

      .. selected:: jax-ver=0.10.2

         1. Pull the ROCm JAX 0.10.2 Docker image.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash

                     docker pull rocm/jax:rocm10.0.0-jax0.10.2-py3.14

               .. tab-item:: Python 3.13
                  :sync: py313

                  .. code-block:: bash

                     docker pull rocm/jax:rocm10.0.0-jax0.10.2-py3.13

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash

                     docker pull rocm/jax:rocm10.0.0-jax0.10.2-py3.12

               .. tab-item:: Python 3.11
                  :sync: py311

                  .. code-block:: bash

                     docker pull rocm/jax:rocm10.0.0-jax0.10.2-py3.11

         2. Start the Docker container.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash

                     docker run -it --rm \
                        --device /dev/kfd \
                        --device /dev/dri \
                        --network=host \
                        --ipc=host \
                        --group-add=video \
                        --cap-add=SYS_PTRACE \
                        --security-opt seccomp=unconfined \
                        rocm/jax:rocm10.0.0-jax0.10.2-py3.14 \
                        bash

               .. tab-item:: Python 3.13
                  :sync: py313

                  .. code-block:: bash

                     docker run -it --rm \
                        --device /dev/kfd \
                        --device /dev/dri \
                        --network=host \
                        --ipc=host \
                        --group-add=video \
                        --cap-add=SYS_PTRACE \
                        --security-opt seccomp=unconfined \
                        rocm/jax:rocm10.0.0-jax0.10.2-py3.13 \
                        bash

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash

                     docker run -it --rm \
                        --device /dev/kfd \
                        --device /dev/dri \
                        --network=host \
                        --ipc=host \
                        --group-add=video \
                        --cap-add=SYS_PTRACE \
                        --security-opt seccomp=unconfined \
                        rocm/jax:rocm10.0.0-jax0.10.2-py3.12 \
                        bash

               .. tab-item:: Python 3.11
                  :sync: py311

                  .. code-block:: bash

                     docker run -it --rm \
                        --device /dev/kfd \
                        --device /dev/dri \
                        --network=host \
                        --ipc=host \
                        --group-add=video \
                        --cap-add=SYS_PTRACE \
                        --security-opt seccomp=unconfined \
                        rocm/jax:rocm10.0.0-jax0.10.2-py3.11 \
                        bash

      .. selected:: jax-ver=0.10.0

         1. Pull the ROCm JAX 0.10.0 Docker image.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash

                     docker pull rocm/jax:rocm10.0.0-jax0.10.0-py3.14

               .. tab-item:: Python 3.13
                  :sync: py313

                  .. code-block:: bash

                     docker pull rocm/jax:rocm10.0.0-jax0.10.0-py3.13

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash

                     docker pull rocm/jax:rocm10.0.0-jax0.10.0-py3.12

               .. tab-item:: Python 3.11
                  :sync: py311

                  .. code-block:: bash

                     docker pull rocm/jax:rocm10.0.0-jax0.10.0-py3.11

         2. Start the Docker container.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash

                     docker run -it --rm \
                        --device /dev/kfd \
                        --device /dev/dri \
                        --network=host \
                        --ipc=host \
                        --group-add=video \
                        --cap-add=SYS_PTRACE \
                        --security-opt seccomp=unconfined \
                        rocm/jax:rocm10.0.0-jax0.10.0-py3.14 \
                        bash

               .. tab-item:: Python 3.13
                  :sync: py313

                  .. code-block:: bash

                     docker run -it --rm \
                        --device /dev/kfd \
                        --device /dev/dri \
                        --network=host \
                        --ipc=host \
                        --group-add=video \
                        --cap-add=SYS_PTRACE \
                        --security-opt seccomp=unconfined \
                        rocm/jax:rocm10.0.0-jax0.10.0-py3.13 \
                        bash

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash

                     docker run -it --rm \
                        --device /dev/kfd \
                        --device /dev/dri \
                        --network=host \
                        --ipc=host \
                        --group-add=video \
                        --cap-add=SYS_PTRACE \
                        --security-opt seccomp=unconfined \
                        rocm/jax:rocm10.0.0-jax0.10.0-py3.12 \
                        bash

               .. tab-item:: Python 3.11
                  :sync: py311

                  .. code-block:: bash

                     docker run -it --rm \
                        --device /dev/kfd \
                        --device /dev/dri \
                        --network=host \
                        --ipc=host \
                        --group-add=video \
                        --cap-add=SYS_PTRACE \
                        --security-opt seccomp=unconfined \
                        rocm/jax:rocm10.0.0-jax0.10.0-py3.11 \
                        bash
