***********************
Model inference recipes
***********************

Model-specific inference recipes for serving large language models on AMD
Instinct GPUs using high-performance inference frameworks.

Each recipe provides day-0 or validated serving configurations, Docker images,
standalone benchmark instructions, and performance tips for a specific model
across one or more inference backends (vLLM, SGLang, ATOM).

Available recipes
=================

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Kimi-K3

      Moonshot AI's 2.8T-parameter MoE (Mixture of Experts) model with
      a 1M-token context window. Day-0 inference on MI350X / MI355X across
      vLLM, SGLang, and ATOM with TP8 serving and standalone benchmark scripts.

Hardware requirements
=====================

Recipes are validated on specific AMD Instinct GPU configurations. Refer to each
recipe's **Hardware requirements** section for the exact GPU count, memory
requirements, and expected topology (for example, TP8).

Quick start with MAD
====================

Most recipes include a `MAD <https://github.com/ROCm/MAD>`__ tag for
one-command launching:

.. code-block:: bash

   madengine run --tags <tag> --keep-model-dir --live-output

See individual recipe pages for the exact tag and any extra context (for
example, pre-downloaded weights or custom mounts).
