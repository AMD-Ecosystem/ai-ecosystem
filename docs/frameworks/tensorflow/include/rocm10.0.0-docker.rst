.. selected:: rocm-ver=10.0.0

   .. selected:: i=docker
      :heading: Get started

      .. selected:: tensorflow-ver=2.21

         1. Pull the ROCm TensorFlow 2.21 Docker image.

            .. code-block:: bash
               :substitutions:

               docker pull rocm/tensorflow:rocm10.0-ubuntu22.04-py3.12-tf2.21

      .. selected:: tensorflow-ver=2.20

         1. Pull the ROCm TensorFlow 2.20 Docker image.

            .. code-block:: bash
               :substitutions:

               docker pull rocm/tensorflow:rocm10.0-ubuntu22.04-py3.12-tf2.20

      .. selected:: tensorflow-ver=2.19

         1. Pull the ROCm TensorFlow 2.19.1 Docker image.

            .. code-block:: bash
               :substitutions:

               docker pull rocm/tensorflow:rocm10.0-ubuntu22.04-py3.12-tf2.19.1

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
                  rocm/tensorflow:rocm10.0-ubuntu22.04-py3.12-tf2.21 \
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
                  rocm/tensorflow:rocm10.0-ubuntu22.04-py3.12-tf2.20 \
                  bash

         .. selected:: tensorflow-ver=2.19

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
                  rocm/tensorflow:rocm10.0-ubuntu22.04-py3.12-tf2.19.1 \
                  bash

