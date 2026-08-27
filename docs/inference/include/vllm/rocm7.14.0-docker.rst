.. |VLLM_VERSION_714D| replace:: 0.23

.. |VLLM_DOCKER_TAG_CDNA_714D| replace:: rocm/vllm:rocm7.14.0_cdna_ubuntu24.04_py3.14_pytorch_2.11.0_vllm_0.23.0
.. |VLLM_DOCKER_TAG_RDNA_714D| replace:: rocm/vllm:rocm7.14.0_rdna_ubuntu24.04_py3.14_pytorch_2.11.0_vllm_0.23.0

.. |VLLM_DOC_714D| replace:: `vLLM <https://docs.vllm.ai/en/v0.23.0/>`__
.. |VLLM_USAGE_DOC_714D| replace:: `Using vLLM <https://docs.vllm.ai/en/v0.23.0/usage/>`__
.. |VLLM_DOCKER_INSTALL_DOC_714D| replace:: `Set up using Docker (vLLM docs) <https://docs.vllm.ai/en/v0.23.0/getting_started/installation/gpu/#amd-rocm_5>`__

.. selected:: rocm-ver=7.14.0

   .. selected:: i=docker
      :heading: Get started

      .. selected:: fam=instinct

         1. Pull the ROCm vLLM |VLLM_VERSION_714D| Docker image.

            .. code-block:: bash
               :substitutions:

               docker pull |VLLM_DOCKER_TAG_CDNA_714D|

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
                  |VLLM_DOCKER_TAG_CDNA_714D| \
                  bash

      .. selected:: fam=radeon fam=ryzen

         1. Pull the ROCm vLLM |VLLM_VERSION_714D| Docker image.

            .. code-block:: bash
               :substitutions:

               docker pull |VLLM_DOCKER_TAG_RDNA_714D|

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
                  |VLLM_DOCKER_TAG_RDNA_714D| \
                  bash

      .. seealso::

         |VLLM_DOCKER_INSTALL_DOC_714D|

      3. After setting up your environment, follow the vLLM |VLLM_VERSION_714D| usage
         documentation to get started: |VLLM_USAGE_DOC_714D|.
