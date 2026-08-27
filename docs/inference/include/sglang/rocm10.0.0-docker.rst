.. |SGLANG_VERSION_10| replace:: 0.5.15

.. |SGLANG_DOCKER_TAG_ALL_10| replace:: rocm/sgl-dev:v0.5.15.post1-ubuntu24.04-py3.14-rocm10.0.0

.. |SGLANG_USAGE_DOC_10| replace:: `Basic usage (SGLang docs) <https://docs.sglang.io/docs/basic_usage/overview>`__
.. |SGLANG_DOCKER_INSTALL_DOC_10| replace:: `Using Docker (SGLang docs) <https://docs.sglang.io/docs/hardware-platforms/amd_gpu#install-using-docker-recommended>`__
.. |SGLANG_PIP_INSTALL_DOC_10| replace:: `With pip or uv (SGLang docs) <https://docs.sglang.io/docs/get-started/install#method-1-with-pip-or-uv>`__

.. selected:: rocm-ver=10.0.0

   .. selected:: i=docker
      :heading: Get started

      .. selected:: fam=all

         1. Pull the ROCm SGLang |SGLANG_VERSION_10| Docker image.

            .. code-block:: bash
               :substitutions:

               docker pull |SGLANG_DOCKER_TAG_ALL_10|

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
                  |SGLANG_DOCKER_TAG_ALL_10| \
                  bash

      .. selected:: fam=instinct

         1. Pull the ROCm SGLang |SGLANG_VERSION_10| Docker image.

            .. code-block:: bash
               :substitutions:

               docker pull |SGLANG_DOCKER_TAG_ALL_10|

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
                  |SGLANG_DOCKER_TAG_ALL_10| \
                  bash

      .. selected:: fam=radeon fam=ryzen

         1. Pull the ROCm SGLang |SGLANG_VERSION_10| Docker image.

            .. code-block:: bash
               :substitutions:

               docker pull |SGLANG_DOCKER_TAG_ALL_10|

         2. Start the Docker container. On Radeon GPUs, disable AITER by unsetting
            ``SGLANG_USE_AITER`` and ``SGLANG_ROCM_FUSED_DECODE_MLA``. See the
            :ref:`known issue <sglang-aiter-ki>` for more information.

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
                  -e SGLANG_USE_AITER=false \
                  -e SGLANG_ROCM_FUSED_DECODE_MLA=false \
                  |SGLANG_DOCKER_TAG_ALL_10| \
                  bash

      .. seealso::

         |SGLANG_DOCKER_INSTALL_DOC_10|
