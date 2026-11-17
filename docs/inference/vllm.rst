:selector-toc2: Installation environment
:selector-toc2-icon: fa-solid fa-computer

**********************************
vLLM inference and serving on ROCm
**********************************

vLLM is an open-source library for fast, memory-efficient LLM inference
and serving. This page describes how to set up and run vLLM on AMD GPUs and
APUs using either a prebuilt Docker image (recommended) or pip. It applies to
`supported AMD GPUs and platforms <https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support>`__.

.. selector:: ROCm version
   :key: rocm-ver

   .. selector-option:: 10.2.0
      :width: 20%

   .. selector-option:: 10.1.0
      :width: 20%

   .. selector-option:: 10.0.0
      :width: 20%

   .. selector-option:: 7.14.1
      :width: 20%

   .. selector-option:: 7.14.0
      :width: 20%

.. selector:: Device family
   :key: fam

   .. selector-option:: AMD Instinct™
      :value: instinct w=compute
      :width: 4
      :toc-label: AMD Instinct

   .. selector-option:: AMD Radeon™
      :value: radeon w=compute
      :width: 4
      :toc-label: AMD Radeon

   .. selector-option:: AMD Ryzen™
      :value: ryzen w=compute
      :width: 4
      :toc-label: AMD Ryzen

.. ================================================================ GPU / APU ==

.. selected:: fam=instinct fam=radeon fam=ryzen

   .. selector-dropdown:: Instinct GPU
      :key: gpu
      :show-cond: fam=instinct
      :sort: desc

      .. selector-option:: AMD Instinct MI355X (gfx950)
         :value: mi355x gfx=gfx950

      .. selector-option:: AMD Instinct MI350X (gfx950)
         :value: mi350x gfx=gfx950

      .. selector-option:: AMD Instinct MI350P (gfx950)
         :value: mi350p gfx=gfx950

      .. selector-option:: AMD Instinct MI325X (gfx942)
         :value: mi325x gfx=gfx942

      .. selector-option:: AMD Instinct MI300X (gfx942)
         :value: mi300x gfx=gfx942

      .. selector-option:: AMD Instinct MI300A (gfx942)
         :value: mi300a gfx=gfx942

   .. selector-dropdown:: Radeon GPU
      :key: gpu
      :show-cond: fam=radeon
      :sort: desc

      .. selector-option:: AMD Radeon AI PRO R9700S (gfx1201)
         :value: ai-r9700s gfx=gfx1201

      .. selector-option:: AMD Radeon AI PRO R9700 (gfx1201)
         :value: ai-r9700 gfx=gfx1201

      .. selector-option:: AMD Radeon AI PRO R9600D (gfx1201)
         :value: ai-r9600d gfx=gfx1201

      .. selector-option:: AMD Radeon AI PRO R9600 (gfx1201)
         :value: ai-r9600 gfx=gfx1201

      .. selector-option:: AMD Radeon RX 9070 XT (gfx1201)
         :value: rx-9070-xt gfx=gfx1201

      .. selector-option:: AMD Radeon RX 9070 GRE (gfx1201)
         :value: rx-9070-gre gfx=gfx1201

      .. selector-option:: AMD Radeon RX 9070 (gfx1201)
         :value: rx-9070 gfx=gfx1201

      .. selector-option:: AMD Radeon RX 9060 XT LP (gfx1200)
         :value: rx-9060-xt-lp gfx=gfx1200

      .. selector-option:: AMD Radeon RX 9060 XT (gfx1200)
         :value: rx-9060-xt gfx=gfx1200

      .. selector-option:: AMD Radeon RX 9060 (gfx1200)
         :value: rx-9060 gfx=gfx1200

      .. selector-option:: AMD Radeon RX 9050 (4GB) (gfx1200)
         :value: rx-9050-4gb gfx=gfx1200

      .. selector-option:: AMD Radeon RX 9050 (gfx1200)
         :value: rx-9050 gfx=gfx1200

      .. selector-option:: AMD Radeon PRO W7900 Dual Slot (gfx1100)
         :value: w7900-dual-slot gfx=gfx1100

      .. selector-option:: AMD Radeon PRO W7900 (gfx1100)
         :value: w7900 gfx=gfx1100

      .. selector-option:: AMD Radeon PRO W7800 48GB (gfx1100)
         :value: w7800-48gb gfx=gfx1100

      .. selector-option:: AMD Radeon PRO W7800 (gfx1100)
         :value: w7800 gfx=gfx1100

      .. selector-option:: AMD Radeon RX 7900 XTX (gfx1100)
         :value: rx-7900-xtx gfx=gfx1100

      .. selector-option:: AMD Radeon RX 7900 XT (gfx1100)
         :value: rx-7900-xt gfx=gfx1100

      .. selector-option:: AMD Radeon RX 7900 GRE (gfx1100)
         :value: rx-7900-gre gfx=gfx1100

      .. selector-option:: AMD Radeon PRO W7700 (gfx1101)
         :value: w7700 gfx=gfx1101

      .. selector-option:: AMD Radeon RX 7800 XT (gfx1101)
         :value: rx-7800-xt gfx=gfx1101

      .. selector-option:: AMD Radeon RX 7700 XT (gfx1101)
         :value: rx-7700-xt gfx=gfx1101

      .. selector-option:: AMD Radeon RX 7700 (gfx1101)
         :value: rx-7700 gfx=gfx1101

      .. selector-option:: AMD Radeon PRO V710 (gfx1101)
         :value: v710 gfx=gfx1101

      .. selector-option:: AMD Radeon RX 7600 (gfx1102)
         :value: rx-7600 gfx=gfx1102

   .. selector-dropdown:: Ryzen APU
      :key: gpu
      :show-cond: fam=ryzen
      :sort: desc

      .. selector-option:: AMD Ryzen AI Max+ PRO 495 (gfx1151)
         :value: max-plus-pro-495 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max PRO 490 (gfx1151)
         :value: max-pro-490 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max PRO 485 (gfx1151)
         :value: max-pro-485 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max+ PRO 395 (gfx1151)
         :value: max-pro-395 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max PRO 390 (gfx1151)
         :value: max-pro-390 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max PRO 385 (gfx1151)
         :value: max-pro-385 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max PRO 380 (gfx1151)
         :value: max-pro-380 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max+ 395 (gfx1151)
         :value: max-395 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max+ 392 (gfx1151)
         :value: max-392 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max+ 388 (gfx1151)
         :value: max-388 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max 390 (gfx1151)
         :value: max-390 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI Max 385 (gfx1151)
         :value: max-385 gfx=gfx1151

      .. selector-option:: AMD Ryzen AI 9 HX PRO 475 (gfx1150)
         :value: ai-9-hx-pro-475 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 9 HX PRO 470 (gfx1150)
         :value: ai-9-hx-pro-470 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 9 PRO 465 (gfx1150)
         :value: ai-9-pro-465 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 7 PRO 450 (gfx1152)
         :value: ai-7-pro-450 gfx=gfx1152

      .. selector-option:: AMD Ryzen AI 5 PRO 440 (gfx1152)
         :value: ai-5-pro-440 gfx=gfx1152

      .. selector-option:: AMD Ryzen AI 9 HX 475 (gfx1150)
         :value: ai-9-hx-475 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 9 HX 470 (gfx1150)
         :value: ai-9-hx-470 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 9 465 (gfx1150)
         :value: ai-9-465 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 7 450 (gfx1152)
         :value: ai-7-450 gfx=gfx1152

      .. selector-option:: AMD Ryzen AI 9 HX PRO 375 (gfx1150)
         :value: 9-hx-pro-375 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 9 HX PRO 370 (gfx1150)
         :value: 9-hx-pro-370 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 7 PRO 350 (gfx1152)
         :value: ai-7-pro-350 gfx=gfx1152

      .. selector-option:: AMD Ryzen AI 5 PRO 340 (gfx1152)
         :value: ai-5-pro-340 gfx=gfx1152

      .. selector-option:: AMD Ryzen AI 9 HX 375 (gfx1150)
         :value: 9-hx-375 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 9 HX 370 (gfx1150)
         :value: 9-hx-370 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 9 365 (gfx1150)
         :value: 9-365 gfx=gfx1150

      .. selector-option:: AMD Ryzen AI 7 350 (gfx1152)
         :value: ai-7-350 gfx=gfx1152

      .. selector-option:: AMD Ryzen AI 7 345 (gfx1152)
         :value: ai-7-345 gfx=gfx1152

      .. selector-option:: AMD Ryzen AI 5 340 (gfx1152)
         :value: ai-5-340 gfx=gfx1152

      .. selector-option:: AMD Ryzen AI 5 330 (gfx1152)
         :value: ai-5-330 gfx=gfx1152

      .. selector-option:: AMD Ryzen 7 PRO 253 (gfx1103)
         :value: 7-pro-253 gfx=gfx1103

      .. selector-option:: AMD Ryzen 7 PRO 250 (gfx1103)
         :value: 7-pro-250 gfx=gfx1103

      .. selector-option:: AMD Ryzen 7 PRO 249 (gfx1103)
         :value: 7-pro-249 gfx=gfx1103

      .. selector-option:: AMD Ryzen 7 PRO 217 (gfx1103)
         :value: 7-pro-217 gfx=gfx1103

      .. selector-option:: AMD Ryzen 5 PRO 230 (gfx1103)
         :value: 5-pro-230 gfx=gfx1103

      .. selector-option:: AMD Ryzen 5 PRO 225 (gfx1103)
         :value: 5-pro-225 gfx=gfx1103

      .. selector-option:: AMD Ryzen 5 PRO 224 (gfx1103)
         :value: 5-pro-224 gfx=gfx1103

      .. selector-option:: AMD Ryzen 5 PRO 220 (gfx1103)
         :value: 5-pro-220 gfx=gfx1103

      .. selector-option:: AMD Ryzen 5 PRO 216 (gfx1103)
         :value: 5-pro-216 gfx=gfx1103

      .. selector-option:: AMD Ryzen 5 PRO 215 (gfx1103)
         :value: 5-pro-215 gfx=gfx1103

      .. selector-option:: AMD Ryzen 3 PRO 210 (gfx1103)
         :value: 3-pro-210 gfx=gfx1103

      .. selector-option:: AMD Ryzen 3 PRO 205 (gfx1103)
         :value: 3-pro-205 gfx=gfx1103

      .. selector-option:: AMD Ryzen 9 270 (gfx1103)
         :value: 9-270 gfx=gfx1103

      .. selector-option:: AMD Ryzen 7 260 (gfx1103)
         :value: 7-260 gfx=gfx1103

      .. selector-option:: AMD Ryzen 7 253 (gfx1103)
         :value: 7-253 gfx=gfx1103

      .. selector-option:: AMD Ryzen 7 250 (gfx1103)
         :value: 7-250 gfx=gfx1103

      .. selector-option:: AMD Ryzen 7 249 (gfx1103)
         :value: 7-249 gfx=gfx1103

      .. selector-option:: AMD Ryzen 7 217 (gfx1103)
         :value: 7-217 gfx=gfx1103

      .. selector-option:: AMD Ryzen 5 240 (gfx1103)
         :value: 5-240 gfx=gfx1103

      .. selector-option:: AMD Ryzen 5 230 (gfx1103)
         :value: 5-230 gfx=gfx1103

      .. selector-option:: AMD Ryzen 5 225 (gfx1103)
         :value: 5-225 gfx=gfx1103

      .. selector-option:: AMD Ryzen 5 224 (gfx1103)
         :value: 5-224 gfx=gfx1103

      .. selector-option:: AMD Ryzen 5 220 (gfx1103)
         :value: 5-220 gfx=gfx1103

      .. selector-option:: AMD Ryzen 5 216 (gfx1103)
         :value: 5-216 gfx=gfx1103

      .. selector-option:: AMD Ryzen 3 210 (gfx1103)
         :value: 3-210 gfx=gfx1103

      .. selector-option:: AMD Ryzen 3 205 (gfx1103)
         :value: 3-205 gfx=gfx1103

      .. selector-option:: AMD Ryzen 9 180 (gfx1103)
         :value: 9-180 gfx=gfx1103

      .. selector-option:: AMD Ryzen 7 165 (gfx1103)
         :value: 7-165 gfx=gfx1103

      .. selector-option:: AMD Ryzen 7 155 (gfx1103)
         :value: 7-155 gfx=gfx1103

      .. selector-option:: AMD Ryzen 5 125 (gfx1103)
         :value: 5-125 gfx=gfx1103

.. selector:: vLLM version
   :key: vllm-ver

   .. selector-option:: 0.32
      :value: 0.32
      :width: 12
      :show-cond: rocm-ver=10.2.0

   .. selector-option:: 0.29
      :value: 0.29
      :width: 12
      :show-cond: rocm-ver=10.1.0

   .. selector-option:: 0.27
      :value: 0.27
      :width: 12
      :show-cond: rocm-ver=10.0.0

   .. selector-option:: 0.23
      :value: 0.23
      :width: 12
      :show-cond: rocm-ver=7.14.1 rocm-ver=7.14.0

.. selector:: Installation method
   :key: i

   .. selector-option:: Docker
      :value: docker
      :width: 6

   .. selector-option:: pip
      :value: pip
      :width: 6

Prerequisites
=============

.. selected:: i=docker

   .. selected:: fam=instinct fam=radeon

      .. selected:: rocm-ver=10.2.0

         * Ensure your host system has the AMD GPU Driver (amdgpu) installed.
           See the `ROCm compatibility matrix (ROCm 10.2.0)
           <https://rocm.docs.amd.com/en/docs-10.2.0/compatibility/compatibility-matrix.html>`__
           for driver support information. For installation instructions, see
           the `AMD GPU Driver documentation
           <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.70.0/index.html>`__.

      .. selected:: rocm-ver=10.1.0

         * Ensure your host system has the AMD GPU Driver (amdgpu) installed.
           See the `ROCm compatibility matrix (ROCm 10.1.0)
           <https://rocm.docs.amd.com/en/docs-10.1.0/compatibility/compatibility-matrix.html>`__
           for driver support information. For installation instructions, see
           the `AMD GPU Driver documentation
           <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.60.0/index.html>`__.

      .. selected:: rocm-ver=10.0.0

         * Ensure your host system has the AMD GPU Driver (amdgpu) installed.
           See the `ROCm compatibility matrix (ROCm 10.0.0)
           <https://rocm.docs.amd.com/en/docs-10.0.0/compatibility/compatibility-matrix.html>`__
           for driver support information. For installation instructions, see
           the `AMD GPU Driver documentation
           <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/index.html>`__.

      .. selected:: rocm-ver=7.14.1

         * Ensure your host system has the AMD GPU Driver (amdgpu) installed.
           See the `ROCm compatibility matrix (ROCm 7.14.1)
           <https://rocm.docs.amd.com/en/docs-7.14.1/compatibility/compatibility-matrix.html>`__
           for driver support information. For installation instructions, see
           the `AMD GPU Driver documentation
           <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html>`__.

      .. selected:: rocm-ver=7.14.0

         * Ensure your host system has the AMD GPU Driver (amdgpu) installed.
           See the `ROCm compatibility matrix (ROCm 7.14.0)
           <https://rocm.docs.amd.com/en/docs-7.14.0/compatibility/compatibility-matrix.html>`__
           for driver support information. For installation instructions, see
           the `AMD GPU Driver documentation
           <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html>`__.

      * Ensure the host system has `Docker Engine
        <https://docs.docker.com/engine/install/>`__ installed. For more guidance
        on running ROCm workloads in Docker containers, see `Run ROCm Docker
        containers
        <https://rocm.docs.amd.com/en/latest/install/docker-containers.html>`__.

   .. selected:: fam=ryzen

      * Ensure the host system has `Docker Engine
        <https://docs.docker.com/engine/install/>`__ installed. For more guidance
        on running ROCm workloads in Docker containers, see `Run ROCm Docker
        containers
        <https://rocm.docs.amd.com/en/latest/install/docker-containers.html>`__.

.. selected:: i=pip

   .. selected:: fam=instinct fam=radeon

      .. selected:: rocm-ver=10.2.0

         * Ensure your host system has the AMD GPU Driver (amdgpu) installed.
           See the `ROCm compatibility matrix (ROCm 10.2.0)
           <https://rocm.docs.amd.com/en/docs-10.2.0/compatibility/compatibility-matrix.html>`__
           for driver support information. For installation instructions, see
           the `AMD GPU Driver documentation
           <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.70.0/index.html>`__.

      .. selected:: rocm-ver=10.1.0

         * Ensure your host system has the AMD GPU Driver (amdgpu) installed.
           See the `ROCm compatibility matrix (ROCm 10.1.0)
           <https://rocm.docs.amd.com/en/docs-10.1.0/compatibility/compatibility-matrix.html>`__
           for driver support information. For installation instructions, see
           the `AMD GPU Driver documentation
           <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.60.0/index.html>`__.

      .. selected:: rocm-ver=10.0.0

         * Ensure your host system has the AMD GPU Driver (amdgpu) installed.
           See the `ROCm compatibility matrix (ROCm 10.0.0)
           <https://rocm.docs.amd.com/en/docs-10.0.0/compatibility/compatibility-matrix.html>`__
           for driver support information. For installation instructions, see
           the `AMD GPU Driver documentation
           <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/index.html>`__.

      .. selected:: rocm-ver=7.14.1

         * Ensure your host system has the AMD GPU Driver (amdgpu) installed.
           See the `ROCm compatibility matrix (ROCm 7.14.1)
           <https://rocm.docs.amd.com/en/docs-7.14.1/compatibility/compatibility-matrix.html>`__
           for driver support information. For installation instructions, see
           the `AMD GPU Driver documentation
           <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html>`__.

      .. selected:: rocm-ver=7.14.0

         * Ensure your host system has the AMD GPU Driver (amdgpu) installed.
           See the `ROCm compatibility matrix (ROCm 7.14.0)
           <https://rocm.docs.amd.com/en/docs-7.14.0/compatibility/compatibility-matrix.html>`__
           for driver support information. For installation instructions, see
           the `AMD GPU Driver documentation
           <https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html>`__.

   * Ensure your system has `Python 3.14
     <https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support>`__
     and its development package are installed and accessible, along with
     ``libgomp``.

     .. tab-set::

        .. tab-item:: apt

           .. code-block:: bash

              sudo apt update && sudo apt install python3.14-dev libgomp1

        .. tab-item:: dnf

           .. code-block:: bash

              sudo dnf install python3.14-devel libgomp

        .. tab-item:: zypper

           .. code-block:: bash

              sudo zypper install python3-devel libgomp1

   * If your system has a separate ROCm installation and you set the ``ROCM_PATH``
     or ``LD_LIBRARY_PATH`` environment variables, for example after installing ROCm
     via tarball, unset them before running vLLM as they can interfere with vLLM's ROCm
     platform detection.

     .. code-block:: bash

        unset ROCM_PATH LD_LIBRARY_PATH

     If you don't need the tarball installation, you can remove it instead. See
     `Uninstalling ROCm
     <https://rocm.docs.amd.com/en/latest/install/rocm.html?i=tar#uninstalling>`__,
     which removes the installation directory and its environment
     configuration. Step 2 of this guide installs ROCm core libraries using pip
     alongside PyTorch.

.. datatemplate:yaml:: /data/docker-tags/vllm.yaml
   :template: vllm-docker.rst.jinja

.. selected:: i=pip
   :heading: Install vLLM using pip

   1. Set up and activate your Python virtual environment.

      .. code-block:: shell

         python3.14 -m venv .venv
         source .venv/bin/activate

   .. include:: ./include/vllm/rocm10.2.0-pip-install.rst

   .. include:: ./include/vllm/rocm10.1.0-pip-install.rst

   .. include:: ./include/vllm/rocm10.0.0-pip-install.rst

   .. include:: ./include/vllm/rocm7.14.1-pip-install.rst

   .. include:: ./include/vllm/rocm7.14.0-pip-install.rst

.. _vllm-tensorizer-issue:

.. selected:: fam=instinct

   .. selected:: i=pip

      .. selected:: rocm-ver=10.1.0 rocm-ver=10.0.0 rocm-ver=7.14.1 rocm-ver=7.14.0
         :heading: Known issues

         * An incompatibility with vLLM's ``tensorizer`` dependency results in
           errors when running vLLM. As a workaround, manually bump the
           ``tensorizer`` version in your virtual environment.

           .. code-block:: bash

              python -m pip install --upgrade "tensorizer==2.12.1"

.. selected:: fam=radeon fam=ryzen
   :heading: Known issues

   .. selected:: i=pip

      .. selected:: rocm-ver=10.1.0 rocm-ver=10.0.0 rocm-ver=7.14.1 rocm-ver=7.14.0

         * An incompatibility with vLLM's ``tensorizer`` dependency results in
           errors when running vLLM. As a workaround, manually bump the
           ``tensorizer`` version in your virtual environment.

           .. code-block:: bash

              python -m pip install --upgrade "tensorizer==2.12.1"

   .. selected:: rocm-ver=7.14.1 rocm-ver=7.14.0

      * Significantly longer warmup times might be observed in some large language
        model inference workloads on AMD Radeon GPUs using vLLM versions v0.21.0
        through v0.25.0. As a workaround, use a vLLM release earlier than v0.21.0
        or upgrade to vLLM v0.26.0 or later, which includes a fix for this issue.
