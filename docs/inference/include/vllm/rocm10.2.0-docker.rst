.. |VLLM_VERSION_1020D| replace:: 0.32

.. |VLLM032_PYT214_CP314_1020| replace:: rocm/vllm:rocm10.2.0_ubuntu24.04_py3.14-pytorch_2.14.0_vllm-0.32.0

.. |VLLM_USAGE_DOC_1020D| replace:: `Using vLLM <https://docs.vllm.ai/en/v0.32.0/usage/>`__
.. |VLLM_DOCKER_INSTALL_DOC_1020D| replace:: `Set up using Docker (vLLM docs) <https://docs.vllm.ai/en/v0.32.0/getting_started/installation/gpu/#amd-rocm_5>`__

.. selected:: rocm-ver=10.2.0

   .. selected:: i=docker
      :heading: Get started

      1. Pull the ROCm vLLM |VLLM_VERSION_1020D| Docker image.

         .. code-block:: bash
            :substitutions:

            docker pull |VLLM032_PYT214_CP314_1020|

      2. Start the Docker container.

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
               -v <path/to/your/models>:/app/models \
               -e HF_HOME="/app/models" \
               |VLLM032_PYT214_CP314_1020| \
               bash

      .. seealso::

         |VLLM_DOCKER_INSTALL_DOC_1020D|

      3. After setting up your environment, follow the vLLM |VLLM_VERSION_1020D| usage
         documentation to get started: |VLLM_USAGE_DOC_1020D|.
