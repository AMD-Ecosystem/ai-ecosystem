.. |ROCM7141_PYT212_CP314| replace:: rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.14_pytorch_release_2.12.0
.. |ROCM7141_PYT212_CP313| replace:: rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.13_pytorch_release_2.12.0
.. |ROCM7141_PYT212_CP312| replace:: rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.12_pytorch_release_2.12.0
.. |ROCM7141_PYT212_CP311| replace:: rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.11_pytorch_release_2.12.0

.. |ROCM7141_PYT211_CP314| replace:: rocm/pytorch:rocm7.14.1_ubuntu26.04_py3.14_pytorch_release_2.11.0
.. |ROCM7141_PYT211_CP313| replace:: rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.13_pytorch_release_2.11.0
.. |ROCM7141_PYT211_CP312| replace:: rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.12_pytorch_release_2.11.0
.. |ROCM7141_PYT211_CP311| replace:: rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.11_pytorch_release_2.11.0

.. |ROCM7141_PYT210_CP314| replace:: rocm/pytorch:rocm7.14.1_ubuntu26.04_py3.14_pytorch_release_2.10.0
.. |ROCM7141_PYT210_CP313| replace:: rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.13_pytorch_release_2.10.0
.. |ROCM7141_PYT210_CP312| replace:: rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.12_pytorch_release_2.10.0
.. |ROCM7141_PYT210_CP311| replace:: rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.11_pytorch_release_2.10.0

.. selected:: rocm-ver=7.14.1

   .. selected:: i=docker
      :heading: Get started

      .. selected:: pytorch-ver=2.12.0

         1. Pull the ROCm PyTorch 2.12.0 Docker image.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_PYT212_CP314|

               .. tab-item:: Python 3.13
                  :sync: py313

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_PYT212_CP313|

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_PYT212_CP312|

               .. tab-item:: Python 3.11
                  :sync: py311

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_PYT212_CP311|

      .. selected:: pytorch-ver=2.11.0

         1. Pull the ROCm PyTorch 2.11.0 Docker image.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_PYT211_CP314|

               .. tab-item:: Python 3.13
                  :sync: py313

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_PYT211_CP313|

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_PYT211_CP312|

               .. tab-item:: Python 3.11
                  :sync: py311

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_PYT211_CP311|

      .. selected:: pytorch-ver=2.10.0

         1. Pull the ROCm PyTorch 2.10.0 Docker image.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_PYT210_CP314|

               .. tab-item:: Python 3.13
                  :sync: py313

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_PYT210_CP313|

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_PYT210_CP312|

               .. tab-item:: Python 3.11
                  :sync: py311

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_PYT210_CP311|

      2. Start the Docker container.

         .. selected:: pytorch-ver=2.12.0

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
                        |ROCM7141_PYT212_CP314| \
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
                        |ROCM7141_PYT212_CP313| \
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
                        |ROCM7141_PYT212_CP312| \
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
                        |ROCM7141_PYT212_CP311| \
                        bash

         .. selected:: pytorch-ver=2.11.0

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
                        |ROCM7141_PYT211_CP314| \
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
                        |ROCM7141_PYT211_CP313| \
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
                        |ROCM7141_PYT211_CP312| \
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
                        |ROCM7141_PYT211_CP311| \
                        bash

         .. selected:: pytorch-ver=2.10.0

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
                        |ROCM7141_PYT210_CP314| \
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
                        |ROCM7141_PYT210_CP313| \
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
                        |ROCM7141_PYT210_CP312| \
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
                        |ROCM7141_PYT210_CP311| \
                        bash
