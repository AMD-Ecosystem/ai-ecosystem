.. |ROCM_1010_PYT214_CP314| replace:: rocm/pytorch:rocm10.1.0_ubuntu26.04_py3.14_pytorch_release_2.14.0
.. |ROCM_1010_PYT214_CP312| replace:: rocm/pytorch:rocm10.1.0_ubuntu24.04_py3.12_pytorch_release_2.14.0
.. |ROCM_1010_PYT214_CP310| replace:: rocm/pytorch:rocm10.1.0_ubuntu22.04_py3.10_pytorch_release_2.14.0

.. |ROCM_1010_PYT213_CP314| replace:: rocm/pytorch:rocm10.1.0_ubuntu26.04_py3.14_pytorch_release_2.13.0
.. |ROCM_1010_PYT213_CP312| replace:: rocm/pytorch:rocm10.1.0_ubuntu24.04_py3.12_pytorch_release_2.13.0
.. |ROCM_1010_PYT213_CP310| replace:: rocm/pytorch:rocm10.1.0_ubuntu22.04_py3.10_pytorch_release_2.13.0

.. |ROCM_1010_PYT212_CP314| replace:: rocm/pytorch:rocm10.1.0_ubuntu26.04_py3.14_pytorch_release_2.12.0
.. |ROCM_1010_PYT212_CP312| replace:: rocm/pytorch:rocm10.1.0_ubuntu24.04_py3.12_pytorch_release_2.12.0
.. |ROCM_1010_PYT212_CP310| replace:: rocm/pytorch:rocm10.1.0_ubuntu22.04_py3.10_pytorch_release_2.12.0

.. selected:: rocm-ver=10.1.0

   .. selected:: i=docker
      :heading: Get started

      .. selected:: pytorch-ver=2.14.0

         1. Pull the ROCm PyTorch 2.14.0 Docker image.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM_1010_PYT214_CP314|

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM_1010_PYT214_CP312|

               .. tab-item:: Python 3.10
                  :sync: py310

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM_1010_PYT214_CP310|

      .. selected:: pytorch-ver=2.13.0

         1. Pull the ROCm PyTorch 2.13.0 Docker image.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM_1010_PYT213_CP314|

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM_1010_PYT213_CP312|

               .. tab-item:: Python 3.10
                  :sync: py310

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM_1010_PYT213_CP310|

      .. selected:: pytorch-ver=2.12.0

         1. Pull the ROCm PyTorch 2.12.0 Docker image.

            .. tab-set::

               .. tab-item:: Python 3.14
                  :sync: py314

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM_1010_PYT212_CP314|

               .. tab-item:: Python 3.12
                  :sync: py312

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM_1010_PYT212_CP312|

               .. tab-item:: Python 3.10
                  :sync: py310

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM_1010_PYT212_CP310|

      2. Start the Docker container.

         .. selected:: pytorch-ver=2.14.0

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
                        |ROCM_1010_PYT214_CP314| \
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
                        |ROCM_1010_PYT214_CP312| \
                        bash

               .. tab-item:: Python 3.10
                  :sync: py310

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
                        |ROCM_1010_PYT214_CP310| \
                        bash

         .. selected:: pytorch-ver=2.13.0

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
                        |ROCM_1010_PYT213_CP314| \
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
                        |ROCM_1010_PYT213_CP312| \
                        bash

               .. tab-item:: Python 3.10
                  :sync: py310

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
                        |ROCM_1010_PYT213_CP310| \
                        bash

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
                        |ROCM_1010_PYT212_CP314| \
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
                        |ROCM_1010_PYT212_CP312| \
                        bash

               .. tab-item:: Python 3.10
                  :sync: py310

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
                        |ROCM_1010_PYT212_CP310| \
                        bash
