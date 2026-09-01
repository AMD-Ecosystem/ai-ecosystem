.. |ROCM7141_TF221_CP312_UB24| replace:: rocm/tensorflow:rocm7.14.1-ubuntu24.04-py3.12-tf2.21

.. |ROCM7141_TF220_CP312_UB24| replace:: rocm/tensorflow:rocm7.14.1-ubuntu24.04-py3.12-tf2.20

.. |ROCM7141_TF219_CP312_UB24| replace:: rocm/tensorflow:rocm7.14.1-ubuntu24.04-py3.12-tf2.19.1
.. |ROCM7141_TF219_CP312_UB22| replace:: rocm/tensorflow:rocm7.14.1-ubuntu22.04-py3.12-tf2.19.1

.. selected:: rocm-ver=7.14.1

   .. selected:: i=docker
      :heading: Get started

      .. selected:: tensorflow-ver=2.21

         1. Pull the ROCm TensorFlow 2.21 Docker image.

            .. code-block:: bash
               :substitutions:

               docker pull |ROCM7141_TF221_CP312_UB24|

      .. selected:: tensorflow-ver=2.20

         1. Pull the ROCm TensorFlow 2.20 Docker image.

            .. code-block:: bash
               :substitutions:

               docker pull |ROCM7141_TF220_CP312_UB24|

      .. selected:: tensorflow-ver=2.19

         1. Pull the ROCm TensorFlow 2.19.1 Docker image.

            .. tab-set::

               .. tab-item:: Ubuntu 24.04
                  :sync: ub24

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_TF219_CP312_UB24|

               .. tab-item:: Ubuntu 22.04
                  :sync: ub22

                  .. code-block:: bash
                     :substitutions:

                     docker pull |ROCM7141_TF219_CP312_UB22|

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
                  |ROCM7141_TF221_CP312_UB24| \
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
                  |ROCM7141_TF220_CP312_UB24| \
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
                        |ROCM7141_TF219_CP312_UB24| \
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
                        |ROCM7141_TF219_CP312_UB22| \
                        bash

