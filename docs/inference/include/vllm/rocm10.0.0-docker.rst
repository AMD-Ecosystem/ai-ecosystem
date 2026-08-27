.. |VLLM_VERSION_10D| replace:: 0.27

.. |VLLM_DOCKER_TAG_CDNA_10D| replace:: rocm/vllm:rocm10.0.0_cdna_ubuntu24.04_py3.14_pytorch_2.12.0_vllm_0.27.0
.. |VLLM_DOCKER_TAG_RDNA_10D| replace:: rocm/vllm:rocm10.0.0_rdna_ubuntu24.04_py3.14_pytorch_2.12.0_vllm_0.27.0

.. |VLLM_DOC_10D| replace:: `vLLM <https://docs.vllm.ai/en/v0.27.0/>`__
.. |VLLM_USAGE_DOC_10D| replace:: `Using vLLM <https://docs.vllm.ai/en/v0.27.0/usage/>`__
.. |VLLM_DOCKER_INSTALL_DOC_10D| replace:: `Set up using Docker (vLLM docs) <https://docs.vllm.ai/en/v0.27.0/getting_started/installation/gpu/#amd-rocm_5>`__

.. selected:: rocm-ver=10.0.0

   .. selected:: i=docker
      :heading: Get started

      .. selected:: fam=instinct

         1. Pull the ROCm vLLM |VLLM_VERSION_10D| Docker image.

            .. code-block:: bash
               :substitutions:

               docker pull |VLLM_DOCKER_TAG_CDNA_10D|

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
                  |VLLM_DOCKER_TAG_CDNA_10D| \
                  bash

      .. selected:: fam=radeon fam=ryzen

         1. Pull the ROCm vLLM |VLLM_VERSION_10D| Docker image.

            .. code-block:: bash
               :substitutions:

               docker pull |VLLM_DOCKER_TAG_RDNA_10D|

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
                  |VLLM_DOCKER_TAG_RDNA_10D| \
                  bash

      .. seealso::

         |VLLM_DOCKER_INSTALL_DOC_10D|

      3. After setting up your environment, follow the vLLM |VLLM_VERSION_10D| usage
         documentation to get started: |VLLM_USAGE_DOC_10D|.
