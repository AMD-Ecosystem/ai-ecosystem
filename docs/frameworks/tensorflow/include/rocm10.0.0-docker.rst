.. |TF221_CP312_UB24| replace:: rocm/tensorflow:rocm10.0-ubuntu24.04-py3.12-tf2.21

.. |TF220_CP312_UB24| replace:: rocm/tensorflow:rocm10.0-ubuntu24.04-py3.12-tf2.20

.. |TF219_CP312_UB24| replace:: rocm/tensorflow:rocm10.0-ubuntu24.04-py3.12-tf2.19.1
.. |TF219_CP312_UB22| replace:: rocm/tensorflow:rocm10.0-ubuntu22.04-py3.12-tf2.19.1

.. selected:: rocm-ver=10.0.0

   .. selected:: i=docker
      :heading: Get started

      .. selected:: tensorflow-ver=2.21

         1. Pull the ROCm TensorFlow 2.21 Docker image.

            .. code-block:: bash
               :substitutions:

               docker pull |TF221_CP312_UB24|

      .. selected:: tensorflow-ver=2.20

         1. Pull the ROCm TensorFlow 2.20 Docker image.

            .. code-block:: bash
               :substitutions:

               docker pull |TF220_CP312_UB24|

      .. selected:: tensorflow-ver=2.19

         1. Pull the ROCm TensorFlow 2.19.1 Docker image.

            .. tab-set::

               .. tab-item:: Ubuntu 24.04
                  :sync: ub24

                  .. code-block:: bash
                     :substitutions:

                     docker pull |TF219_CP312_UB24|

               .. tab-item:: Ubuntu 22.04
                  :sync: ub22

                  .. code-block:: bash
                     :substitutions:

                     docker pull |TF219_CP312_UB22|

      2. Start the Docker container.

         .. selected:: tensorflow-ver=2.21

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
                  |TF221_CP312_UB24| \
                  bash

         .. selected:: tensorflow-ver=2.20

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
                  |TF220_CP312_UB24| \
                  bash

         .. selected:: tensorflow-ver=2.19

            .. tab-set::

               .. tab-item:: Ubuntu 24.04
                  :sync: ub24

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
                        |TF219_CP312_UB24| \
                        bash

               .. tab-item:: Ubuntu 22.04
                  :sync: ub22

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
                        |TF219_CP312_UB22| \
                        bash

