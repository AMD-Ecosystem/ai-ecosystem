:no-search:
:orphan:

**************************************************************
Primus TorchTitan training performance testing version history
**************************************************************

This table lists previous releases of the Primus AI training Docker image. The
following documentation archives use Primus with the TorchTitan backend and
demonstrate training performance testing. You can find tagged previous releases
of the ``ROCm/primus`` Docker image on `Docker Hub
<https://hub.docker.com/r/rocm/primus/tags>`__.

.. list-table::
   :header-rows: 1

   * - Image version
     - Components
     - Resources

   * - v26.4
     -
       * ROCm 7.14.0a20260608
       * PyTorch 2.12.0+git7e98855
     -
       * :doc:`Documentation <primus-megatron-v26-4>`
       * `Docker Hub <https://hub.docker.com/layers/rocm/primus/v26.4/images/sha256-c3d9033c55440f3650a24b26377f3630a0b1bf1b48a6509a4b8fdd8900b2bbcb>`__

   * - v26.3
     -
       * ROCm 7.2.1
       * PyTorch 2.10.0+git94c6e04
     -
       * `Primus PyTorch training documentation <https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/primus-pytorch-v26.3.html>`__
       * `Docker Hub <https://hub.docker.com/layers/rocm/primus/v26.3/images/sha256-da50bfe9dc4bb70ad683d3ee4a176dccb66f596f48d30e8e52323b41892759b1>`__

   * - v26.2
     -
       * ROCm 7.2.0
       * PyTorch 2.10.0+git94c6e04
     -
       * `Primus PyTorch training documentation <https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/primus-pytorch-v26.2.html>`__
       * `Docker Hub <https://hub.docker.com/layers/rocm/primus/v26.2/images/sha256-9148d1bfcd579bf92f44bd89090e0d8c958f149c134b4b34b9674ab559244585>`__

   * - v26.1
     -
       * ROCm 7.1.0
       * PyTorch 2.10.0.dev20251112+rocm7.1
     -
       * `Primus PyTorch training documentation <https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/primus-pytorch-v26.1.html>`__
       * `Docker Hub <https://hub.docker.com/layers/rocm/primus/v26.1/images/sha256-4fc8808bdb14117c6af7f38d79c809056e6fdbfd530c1fabbb61d097ddaf820d>`__

   * - v25.11
     -
       * ROCm 7.1.0
       * PyTorch 2.10.0.dev20251112+rocm7.1
     -
       * `Primus PyTorch training documentation <https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/primus-pytorch-v25.11.html>`__
       * `PyTorch training (legacy) documentation <https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/pytorch-training-v25.11.html>`__
       * `Docker Hub <https://hub.docker.com/layers/rocm/primus/v25.11/images/sha256-71aa65a9bfc8e9dd18bce5b68c81caff864f223e9afa75dc1b719671a1f4a3c3>`__

   * - v25.10
     -
       * ROCm 7.1.0
       * PyTorch 2.10.0.dev20251112+rocm7.1
     -
       * `Primus PyTorch training documentation <https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/primus-pytorch-v25.10.html>`__
       * `PyTorch training (legacy) documentation <https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/pytorch-training-v25.10.html>`__
       * `Docker Hub <https://hub.docker.com/layers/rocm/primus/v25.10/images/sha256-140c37cd2eeeb183759b9622543fc03cc210dc97cbfa18eeefdcbda84420c197>`__

   * - v25.9
     -
       * ROCm 7.0.0
       * Primus 0.3.0
       * PyTorch 2.9.0.dev20250821+rocm7.0.0.lw.git125803b7
     -
       * `Primus PyTorch training documentation <https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/primus-pytorch-v25.9.html>`__
       * `PyTorch training (legacy) documentation <https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/pytorch-training-v25.9.html>`__
       * `Docker Hub (gfx950) <https://hub.docker.com/layers/rocm/primus/v25.9_gfx950/images/sha256-1a198be32f49efd66d0ff82066b44bd99b3e6b04c8e0e9b36b2c481e13bff7b6>`__
       * `Docker Hub (gfx942) <https://hub.docker.com/layers/rocm/primus/v25.9_gfx942/images/sha256-df6ab8f45b4b9ceb100fb24e19b2019a364e351ee3b324dbe54466a1d67f8357>`__

   * - v25.8
     -
       * ROCm 6.4.3
       * PyTorch 2.8.0a0+gitd06a406
     -
       * `Primus PyTorch training documentation <https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/primus-pytorch-v25.8.html>`__
       * `PyTorch training (legacy) documentation <https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/pytorch-training-v25.8.html>`__
       * `Docker Hub <https://hub.docker.com/layers/rocm/pytorch-training/v25.8/images/sha256-5082ae01d73fec6972b0d84e5dad78c0926820dcf3c19f301d6c8eb892e573c5>`__

   * - v25.7
     -
       * ROCm 6.4.2
       * PyTorch 2.8.0a0+gitd06a406
     -
       * `Documentation <https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/pytorch-training-v25.7.html>`__
       * `Docker Hub <https://hub.docker.com/layers/rocm/pytorch-training/v25.7/images/sha256-cc6fd840ab89cb81d926fc29eca6d075aee9875a55a522675a4b9231c9a0a712>`__

   * - v25.6
     -
       * ROCm 6.3.4
       * PyTorch 2.8.0a0+git7d205b2
     -
       * `Documentation <https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/pytorch-training-v25.6.html>`__
       * `Docker Hub <https://hub.docker.com/layers/rocm/pytorch-training/v25.6/images/sha256-a4cea3c493a4a03d199a3e81960ac071d79a4a7a391aa9866add3b30a7842661>`__

   * - v25.5
     -
       * ROCm 6.3.4
       * PyTorch 2.7.0a0+git637433
     -
       * `Documentation <https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/pytorch-training-v25.5.html>`__
       * `Docker Hub <https://hub.docker.com/layers/rocm/pytorch-training/v25.5/images/sha256-d47850a9b25b4a7151f796a8d24d55ea17bba545573f0d50d54d3852f96ecde5>`__

   * - v25.4
     -
       * ROCm 6.3.0
       * PyTorch 2.7.0a0+git637433
     -
       * `Documentation <https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/pytorch-training-v25.4.html>`__
       * `Docker Hub <https://hub.docker.com/layers/rocm/pytorch-training/v25.4/images/sha256-fa98a9aa69968e654466c06f05aaa12730db79b48b113c1ab4f7a5fe6920a20b>`__

   * - v25.3
     -
       * ROCm 6.3.0
       * PyTorch 2.7.0a0+git637433
     -
       * `Documentation <https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/training/benchmark-docker/previous-versions/pytorch-training-v25.3.html>`__
       * `Docker Hub <https://hub.docker.com/layers/rocm/pytorch-training/v25.3/images/sha256-0ffdde1b590fd2787b1c7adf5686875b100980b0f314090901387c44253e709b>`__
