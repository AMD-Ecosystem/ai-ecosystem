.. |ROCM7141_JAX0100_CP314| replace:: rocm/jax:rocm7.14.1-jax0.10.0-py3.14
.. |ROCM7141_JAX0100_CP313| replace:: rocm/jax:rocm7.14.1-jax0.10.0-py3.13
.. |ROCM7141_JAX0100_CP312| replace:: rocm/jax:rocm7.14.1-jax0.10.0-py3.12
.. |ROCM7141_JAX0100_CP311| replace:: rocm/jax:rocm7.14.1-jax0.10.0-py3.11

.. |ROCM7141_JAX091_CP314| replace:: rocm/jax:rocm7.14.1-jax0.9.1-py3.14
.. |ROCM7141_JAX091_CP313| replace:: rocm/jax:rocm7.14.1-jax0.9.1-py3.13
.. |ROCM7141_JAX091_CP312| replace:: rocm/jax:rocm7.14.1-jax0.9.1-py3.12
.. |ROCM7141_JAX091_CP311| replace:: rocm/jax:rocm7.14.1-jax0.9.1-py3.11

.. selected:: rocm-ver=7.14.1

   .. selected:: i=docker
      :heading: Get started

      .. selected:: jax-ver=0.10.0

         1. Pull the ROCm JAX 0.10.0 Docker image.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_JAX0100_CP314|

               .. tab-item:: Python 3.13
                  :sync: py313

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_JAX0100_CP313|

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_JAX0100_CP312|

               .. tab-item:: Python 3.11
                  :sync: py311

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_JAX0100_CP311|

      .. selected:: jax-ver=0.9.1

         1. Pull the ROCm JAX 0.9.1 Docker image.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_JAX091_CP314|

               .. tab-item:: Python 3.13
                  :sync: py313

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_JAX091_CP313|

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_JAX091_CP312|

               .. tab-item:: Python 3.11
                  :sync: py311

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_JAX091_CP311|

      2. Start the Docker container.

         .. selected:: jax-ver=0.10.0

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
                        |ROCM7141_JAX0100_CP314| \
                        bash

               .. tab-item:: Python 3.13
                  :sync: py313

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
                        |ROCM7141_JAX0100_CP313| \
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
                        |ROCM7141_JAX0100_CP312| \
                        bash

               .. tab-item:: Python 3.11
                  :sync: py311

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
                        |ROCM7141_JAX0100_CP311| \
                        bash

         .. selected:: jax-ver=0.9.1

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
                        |ROCM7141_JAX091_CP314| \
                        bash

               .. tab-item:: Python 3.13
                  :sync: py313

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
                        |ROCM7141_JAX091_CP313| \
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
                        |ROCM7141_JAX091_CP312| \
                        bash

               .. tab-item:: Python 3.11
                  :sync: py311

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
                        |ROCM7141_JAX091_CP311| \
                        bash

