:selector-toc2: Model
:selector-toc2-icon: fa-solid fa-robot

.. meta::
   :description: How to train a model using Megatron-LM for ROCm.
   :keywords: ROCm, AI, LLM, train, Megatron-LM, megatron, Llama, tutorial, docker, torch

********************************************
Training a model with Primus and Megatron-LM
********************************************

`Primus <https://rocm.docs.amd.com/projects/primus>`__
(`<https://github.com/AMD-AGI/Primus>`__) is a unified training framework
designed to enable efficient training of large-scale foundation models on AMD
GPUs. It supports multiple backends including TorchTitan with full support
for container-based and bare-metal execution.

The following sections explain how to run Primus training through containerized
`<https://github.com/ROCm/MAD>`__ workflows and the
`<https://github.com/ROCm/madengine/>`__ interface for automated benchmarking.

Training flow
=============

The following diagram illustrates the end-to-end flow of how a model is trained
through Primus and ``madengine``, from user CLI commands through the internal
container invocation chain.

.. mermaid::

   flowchart TD
       A["<b>Clone MAD repo</b><br/><i>git clone https://github.com/ROCm/MAD</i>"] --> B["<b>Install madengine</b><br/><i>pip install madengine</i>"]
       A --> C["<b>Initialize Primus submodule</b><br/><i>git submodule update --init --recursive</i>"]
       A --> D["<b>Docker login</b><br/><i>Registry access</i>"]
       B --> F["<b>Build Docker Image</b><br/><i>madengine build --tags</i>"]
       B --> E["<b>Discover configs</b><br/><i>madengine discover --tags</i>"]
       C --> F
       D --> F
       F --> G["<b>Run training</b><br/><i>madengine run --tags</i>"]

Environment setup
=================

1. Clone the MAD repository:

   .. code-block:: bash

      git clone https://github.com/ROCm/MAD
      cd MAD

2. Install ``madengine``:

   .. code-block:: bash

      # Recommended: create and activate a Python virtual environment
      python3 -m venv .venv
      source .venv/bin/activate

      pip install git+https://github.com/ROCm/madengine.git

3. Initialize the Primus submodule:

   .. code-block:: bash

      git submodule update --init --recursive scripts/Primus

4. `Log in to Docker <https://docs.docker.com/reference/cli/docker/login/>`__
   for image registry access:

   .. code-block:: bash

      docker login

Supported models
================

The following models are pre-optimized for performance on AMD Instinct GPUs.
Some instructions, commands, and training recommendations in this documentation
might vary by model. Select one to get started.

.. datatemplate:yaml:: ./data/primus-megatron.yaml

   {% set model_groups = data.model_groups %}

   .. selector:: Model
      :key: model-group

   {% for model_group in model_groups %}
      .. selector-option:: {{ model_group.group }}
         :value: {{ model_group.tag }}
         :width: 4

   {% endfor %}

   {% for model_group in model_groups %}
   .. selector-dropdown:: Variant
      :key: model
      :show-cond: model-group={{ model_group.tag }}

      {% set models = model_group.models %}
      {% for model in models %}
      .. selector-option:: {{ model.model }}
         :value: {{ model.mad_tag }}

      {% endfor %}
   {% endfor %}

.. tip::

   To discover all supported model configurations, try ``madengine``'s model
   discovery feature:

   .. code-block:: bash

      # List all Primus model configs
      madengine discover --tags primus

      # List all MI300X model configs
      madengine discover --tags MI300X

      # List all Megatron configs
      madengine discover --tags megatron

   Or, browse the
   `<https://github.com/AMD-AGI/Primus/tree/main/examples/megatron/configs>`__
   repository for available configs by AMD device architecture.

Single node training
====================

Training with ``madengine`` involves a two-step process: build the Docker
image, then run the model. Complete the preceding environment setup steps and
navigate to the MAD repository root before getting started.

.. note::

   Primus training tags used in the next sections follow the naming
   convention ``primus_train/<backend>_<GPU_ARCH>_<MODEL_CONFIG>``, where:

   - ``<backend>`` is the `Primus backend
     <https://rocm.docs.amd.com/projects/primus/en/latest/01-getting-started/overview.html#supported-backends>`__:
     ``megatron`` or ``torchtitan``
   - ``<GPU_ARCH>`` is the target accelerator (for example, ``MI300X``, ``MI355X``)
   - ``<MODEL_CONFIG>`` matches the YAML filename in the Primus repository
     under ``examples/<backend>/configs/``. See
     `<https://github.com/AMD-AGI/Primus/tree/main/examples/torchtitan/configs>`__
     for available configs.

Build the Docker image
----------------------

Build the Docker image with the desired model configuration. For instance:

.. datatemplate:yaml:: ./data/primus-megatron.yaml

   {% set model_groups = data.model_groups %}
   {% for model_group in model_groups %}
   {% for model in model_group.models %}

   .. selected:: model={{ model.mad_tag }}

      .. tab-set::

         {% for arch, tags in model.train_tags.items() %}
         .. tab-item:: {{ arch }}

            {% for tag in tags %}
            {% set precision = "BF16" if "BF16" in tag else ("FP8" if "FP8" in tag else "") %}
            {% set backend = tag.split('/')[1].split('_')[0] %}
            {% if loop.first %}
            {% if precision %}Use the following command to build the Docker image for training {{ model.model }} with the {{ precision }} precision configuration file using Primus {{ backend }}:{% else %}Use the following command to build the Docker image for training {{ model.model }} using Primus {{ backend }}:{% endif %}
            {% else %}
            To build for {{ model.model }} with {{ precision }} precision, use the following command:
            {% endif %}

            .. code-block:: bash

               madengine build \
                   --tags {{ tag }} \
                   --additional-context '{"gpu_vendor": "AMD", "guest_os": "UBUNTU"}'

            {% endfor %}

         {% endfor %}

   {% endfor %}
   {% endfor %}

The base Docker image is defined in ``docker/primus.ubuntu.amd.Dockerfile``. To use
a different base image (for example, a newer Primus release), edit the
``BASE_DOCKER`` argument at the top of that file:

.. code-block:: dockerfile

   ARG BASE_DOCKER=docker.io/rocm/primus:v26.5

.. note::

   ``MAD_SYSTEM_GPU_ARCHITECTURE`` is automatically detected at runtime via
   ``rocminfo``. You do not need to provide it during the build step.

Run the model
-------------

Run the model with the built image:

.. datatemplate:yaml:: ./data/primus-megatron.yaml

   {% set model_groups = data.model_groups %}
   {% for model_group in model_groups %}
   {% for model in model_group.models %}

   .. selected:: model={{ model.mad_tag }}

      .. tab-set::

         {% for arch, tags in model.train_tags.items() %}
         .. tab-item:: {{ arch }}

            {% for tag in tags %}
            {% set precision = "BF16" if "BF16" in tag else ("FP8" if "FP8" in tag else "") %}
            {% set backend = tag.split('/')[1].split('_')[0] %}
            {% if loop.first %}
            {% if precision %}Use the following command to train {{ model.model }} with the {{ precision }} precision configuration file using Primus {{ backend }}:{% else %}Use the following command to train {{ model.model }} using Primus {{ backend }}:{% endif %}
            {% else %}
            To train {{ model.model }} with {{ precision }} precision, use the following command:
            {% endif %}

            .. code-block:: bash

               madengine run --tags {{ tag }} --live-output

            {% endfor %}

         {% endfor %}

   {% endfor %}
   {% endfor %}

.. note::

   ``--live-output`` is optional. It streams the training logs to your terminal in
   real time.

Passing environment variables to the container
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To pass environment variables into the running container, use the
``docker_env_vars`` field in the ``--additional-context`` mapping:

.. code-block:: bash

   madengine run \
       --tags <tag> \
       --live-output \
       --additional-context '{"docker_env_vars": {"MAD_SECRET_HFTOKEN": "<your_hf_token>", "HSA_NO_SCRATCH_RECLAIM": "1"}}'

.. note::

   The ``MAD_SECRET_HFTOKEN`` environment variable is only required when
   training with real data (that is, ``mock_data: false`` in the config). The
   default configs use mock data and do not require a token. Inside the
   container, this is automatically mapped to ``HF_TOKEN``.

Multi-node training
===================

Multi-node training via ``madengine`` is not yet available. Multi-node support
is planned for a future release.

Further reading
===============

- To learn more about the Primus framework, see the `AMD Primus documentation
  <https://rocm.docs.amd.com/projects/primus/>`__.

- To learn more about MAD and the ``madengine`` CLI, see the `MAD usage guide
  <https://github.com/ROCm/MAD?tab=readme-ov-file#usage-guide>`__.

- To learn more about system settings and management practices to configure your
  system for AMD Instinct MI300X Series GPUs, see `AMD Instinct MI300X Customer
  Acceptance Guide
  <https://instinct.docs.amd.com/projects/system-acceptance/en/latest/gpus/mi300x.html>`_.

Previous versions
=================

See :doc:`/training/recipes/archive/primus-megatron-history`.
