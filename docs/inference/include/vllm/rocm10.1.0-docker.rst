.. |VLLM_VERSION_1010D| replace:: 0.29

.. |VLLM029_PYT213_CP314_1010| replace:: rocm/vllm:rocm10.1.0_ubuntu24.04_py3.14_pytorch_2.13.0_vllm_0.29.0

.. |VLLM_DOC_1010D| replace:: `vLLM <https://docs.vllm.ai/en/v0.29.0/>`__
.. |VLLM_USAGE_DOC_1010D| replace:: `Using vLLM <https://docs.vllm.ai/en/v0.29.0/usage/>`__
.. |VLLM_DOCKER_INSTALL_DOC_1010D| replace:: `Set up using Docker (vLLM docs) <https://docs.vllm.ai/en/v0.29.0/getting_started/installation/gpu/#amd-rocm_5>`__

.. selected:: rocm-ver=10.1.0

   .. selected:: i=docker
      :heading: Get started

      1. Pull the ROCm vLLM |VLLM_VERSION_1010D| Docker image.

         .. code-block:: bash
            :substitutions:

            docker pull |VLLM029_PYT213_CP314_1010|

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
               |VLLM029_PYT213_CP314_1010| \
               bash

      .. seealso::

         |VLLM_DOCKER_INSTALL_DOC_1010D|

      3. After setting up your environment, follow the vLLM |VLLM_VERSION_1010D| usage
         documentation to get started: |VLLM_USAGE_DOC_1010D|.
