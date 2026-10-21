:selector-toc2: Installation environment
:selector-toc2-icon: fa-solid fa-computer

***************************
llama.cpp inference on ROCm
***************************

`llama.cpp <https://github.com/ggml-org/llama.cpp>`__ is an open-source inference
engine for running LLMs locally. It runs quantized models efficiently on
consumer hardware and has become a pillar of local LLM inference. This page
explains how to set up and run llama.cpp on AMD GPUs and APUs.

.. selector:: ROCm version
   :key: rocm-ver

   .. selector-option:: 10.0.0
      :value: 10.0.0
      :width: 6

   .. selector-option:: 7.14.0
      :value: 7.14.0
      :width: 6

.. selector:: Device family
   :key: fam

   .. selector-option:: AMD Instinct
      :value: instinct
      :width: 4

   .. selector-option:: AMD Radeon
      :value: radeon
      :width: 4

   .. selector-option:: AMD Ryzen
      :value: ryzen
      :width: 4

.. datatemplate:yaml:: /data/gpus.yaml
   :template: gpu-selector.rst.jinja

.. selected:: fam=instinct

   .. selector:: Operating system
      :key: os

      .. selector-option:: Ubuntu 26.04 / 24.04
         :value: ubuntu ubuntu-ver=26.04
         :width: 12

.. selected:: fam=radeon fam=ryzen

   .. selector:: Operating system
      :key: os

      .. selector-option:: Ubuntu 26.04 / 24.04
         :value: ubuntu ubuntu-ver=26.04
         :width: 8

      .. selector-option:: Windows 11
         :value: windows windows-ver=11
         :width: 4

.. selector:: ROCm installation
   :key: i

   .. selector-option:: apt
      :value: pkgman
      :width: 4
      :show-cond: os=ubuntu

   .. selector-option:: pip
      :value: pip
      :width: 4
      :show-cond: os=ubuntu

   .. selector-option:: Tarball
      :value: tar
      :width: 4
      :show-cond: os=ubuntu

   .. selector-option:: pip
      :value: pip
      :width: 6
      :show-cond: os=windows

   .. selector-option:: Tarball
      :value: tar
      :width: 6
      :show-cond: os=windows

----

.. seealso::

   .. selected:: os=ubuntu

      The `<https://github.com/lemonade-sdk/llamacpp-rocm/releases>`__ community
      project publishes nightly llama.cpp builds for Ubuntu that bundle the ROCm
      runtime, in per-architecture packages. With one of those builds you can skip
      installing ROCm and configuring ``LD_LIBRARY_PATH``;
      the AMD GPU driver is still required.

   .. selected:: os=windows

      The `<https://github.com/lemonade-sdk/llamacpp-rocm/releases>`__ community
      project publishes nightly llama.cpp builds for Windows that bundle the ROCm
      runtime, in per-architecture packages. With one of those builds you can skip
      installing ROCm, configuring ``PATH``, and copying the HIP runtime libraries;
      the AMD Software: Adrenalin Edition driver is still required.

.. _llamacpp-sysreqs:

Prerequisites
=============

To run llama.cpp with ROCm, you need the following prerequisites:

.. selected:: os=ubuntu

   - **Operating system:** Ubuntu 26.04 or 24.04

.. selected:: os=windows

   - **Operating system:** Windows 11

- **GPU platform:** AMD Instinct, AMD Radeon, and AMD Ryzen devices supported by
  ROCm. Use the device family and GPU selectors to match your hardware.

.. selected:: os=ubuntu

   - **Group membership:** your user must be a member of the ``video`` and ``render`` groups.

   - **Additional packages:** ``libgomp1`` and ``libcurl4``.

     Install the additional packages if they are not already present:

     .. code-block:: bash

        sudo apt update && sudo apt install libgomp1 libcurl4

.. _llamacpp-install-rocm:

Install ROCm
------------

llama.cpp requires a ROCm installation on the host system.

.. datatemplate:yaml:: /data/gpus.yaml
   :template: rocm-install.rst.jinja

.. selected:: os=ubuntu

   .. important::

      .. selected:: i=pkgman

         When installing via package manager, ROCm is installed system-wide
         under ``/opt/rocm``. This is the installation method the ROCm
         documentation recommends if you are unsure which to choose.

      .. selected:: i=pip

         Install the ``libraries`` extra and the device extra matching your GPU, for example
         ``rocm[libraries,device-gfx1201]``. The ``devel`` extra is not required to run the
         prebuilt llama.cpp binaries; it supplies the ``rocm-sdk`` command-line tool and
         build-time files only.

         Record the path of the virtual environment you create. You need it to
         :ref:`Configure your environment <llamacpp-configure-env>`.

      .. selected:: i=tar

         This guide assumes ``ROCM_PATH`` and ``LD_LIBRARY_PATH`` are set according to the
         ROCm installation via tarball instructions.

.. _llamacpp-install:

Install llama.cpp
=================

AMD does not publish its own binaries for llama.cpp. Download a prebuilt
ROCm-enabled release from the `llama.cpp releases page
<https://github.com/ggml-org/llama.cpp/releases>`__. Release assets are named
in the following format:

.. include:: ./include/llamacpp/rocm10.0.0-llamacpp-install.rst

.. include:: ./include/llamacpp/rocm7.14.0-llamacpp-install.rst

.. note::

   The archive contains only the llama.cpp executables and their ``ggml``
   backend libraries. It does not include the ROCm runtime, which must be
   installed separately as described in the :ref:`previous section <llamacpp-install-rocm>`.

.. _llamacpp-configure-env:

Configure your environment
==========================

.. selected:: os=ubuntu

   llama.cpp loads the ROCm math libraries at run time and must be able to find them.

   .. selected:: i=pkgman

      ROCm libraries are installed in ``/opt/rocm/lib``. This directory is not added to the
      system library search path by the packages, so add it to ``LD_LIBRARY_PATH``:

      .. code-block:: bash

         export LD_LIBRARY_PATH=/opt/rocm/lib:$LD_LIBRARY_PATH

   .. selected:: i=pip

      A pip installation places the ROCm runtime inside the virtual environment, in two
      directories:

      - ``<venv>/lib/python<version>/site-packages/_rocm_sdk_core/lib``
      - ``<venv>/lib/python<version>/site-packages/_rocm_sdk_libraries/lib``

      Add both to ``LD_LIBRARY_PATH``, replacing ``<venv>`` with the path of your virtual
      environment. The Python version in the path is the one you created the environment
      with.

      .. tab-set::

         .. tab-item:: Ubuntu 26.04
            :sync: ub26

            .. code-block:: bash

               SP=<venv>/lib/python3.14/site-packages
               export LD_LIBRARY_PATH="$SP/_rocm_sdk_core/lib:$SP/_rocm_sdk_libraries/lib:$LD_LIBRARY_PATH"

         .. tab-item:: Ubuntu 24.04
            :sync: ub24

            .. code-block:: bash

               SP=<venv>/lib/python3.12/site-packages
               export LD_LIBRARY_PATH="$SP/_rocm_sdk_core/lib:$SP/_rocm_sdk_libraries/lib:$LD_LIBRARY_PATH"

      .. note::

         Activating the virtual environment is not sufficient. It sets ``PATH``, which ROCm's
         own tools use, but not ``LD_LIBRARY_PATH``, which the llama.cpp executables need.

   .. selected:: i=tar

      .. selected:: rocm-ver=10.0.0

         The `tarball installation instructions
         <https://rocm.docs.amd.com/en/docs-10.0.0/install/rocm.html?i=tar>`__
         already set ``LD_LIBRARY_PATH`` to ``$ROCM_PATH/lib``. No further
         configuration is required.

      .. selected:: rocm-ver=7.14.0

         The `tarball installation instructions
         <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?i=tar>`__
         already set ``LD_LIBRARY_PATH`` to ``$ROCM_PATH/lib``. No further
         configuration is required.

   To make any of these settings permanent, update your shell startup file;
   ``~/.bashrc``, for instance.

.. selected:: os=windows

   llama.cpp loads the ROCm math libraries at run time and must be able to find them.

   .. selected:: i=pip

      A pip installation places the ROCm runtime inside the virtual environment in
      two directories:

      - ``<venv>\Lib\site-packages\_rocm_sdk_core\bin``
      - ``<venv>\Lib\site-packages\_rocm_sdk_libraries\bin``

      Add both to your ``PATH`` in the command prompt you use to launch llama.cpp,
      replacing ``<venv>`` with the actual path of your virtual environment, for
      example:

      .. code-block:: bat

         set "PATH=C:\llamacpp\.venv\Lib\site-packages\_rocm_sdk_core\bin;C:\llamacpp\.venv\Lib\site-packages\_rocm_sdk_libraries\bin;%PATH%"

      This setting applies to the current command prompt only. To make it
      permanent, add both directories to your user or system ``PATH`` in your
      Windows settings.

   .. selected:: i=tar

      .. selected:: rocm-ver=10.0.0

         The `tarball installation instructions
         <https://rocm.docs.amd.com/en/docs-10.0.0/install/rocm.html?i=tar&os=windows>`__
         already add ``C:\TheRock\build\bin`` to the system ``PATH``. No further
         configuration is required.

      .. selected:: rocm-ver=7.14.0

         The `tarball installation instructions
         <https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html?i=tar&os=windows>`__
         already add ``C:\TheRock\build\bin`` to the system ``PATH``. No further
         configuration is required.

   If the ROCm libraries are not on your ``PATH``, llama.cpp does not report an
   error. It silently falls back to the CPU backend and runs several times
   slower. Use :ref:`Verify the installation <llamacpp-verify-installation>` to confirm
   the GPU is detected.

.. selected:: os=windows
   :id: llamacpp-copy-runtime-libs
   :heading: Copy the HIP runtime libraries

   .. selected:: i=pip

      Copy the following three files from your ROCm installation into the directory
      that contains ``llama-cli.exe``: ``<venv>\Lib\site-packages\_rocm_sdk_core\bin``

      - ``amdhip64_7.dll``
      - ``rocm_kpack.dll``
      - ``amd_comgr.dll``

      Copy all three files. Copying ``amdhip64_7.dll`` on its own prevents
      llama.cpp from using the GPU: the HIP runtime supplied by ROCm depends on
      the matching ``rocm_kpack.dll`` and ``amd_comgr.dll``, and
      ``rocm_kpack.dll`` is not present in ``System32``.

      .. code-block:: bat

         copy "<venv>\Lib\site-packages\_rocm_sdk_core\bin\amdhip64_7.dll" C:\llamacpp\
         copy "<venv>\Lib\site-packages\_rocm_sdk_core\bin\rocm_kpack.dll" C:\llamacpp\
         copy "<venv>\Lib\site-packages\_rocm_sdk_core\bin\amd_comgr.dll"  C:\llamacpp\

   .. selected:: i=tar

      Copy the following three files from your ROCm installation into the directory
      that contains ``llama-cli.exe``: ``C:\TheRock\build\bin``

      - ``amdhip64_7.dll``
      - ``rocm_kpack.dll``
      - ``amd_comgr.dll``

      .. important::

         Copy all three files. Copying ``amdhip64_7.dll`` on its own prevents
         llama.cpp from using the GPU: the HIP runtime supplied by ROCm depends on
         the matching ``rocm_kpack.dll`` and ``amd_comgr.dll``, and
         ``rocm_kpack.dll`` is not present in ``System32``.

      .. code-block:: bat

         copy "C:\TheRock\build\bin\amdhip64_7.dll" C:\llamacpp\
         copy "C:\TheRock\build\bin\rocm_kpack.dll" C:\llamacpp\
         copy "C:\TheRock\build\bin\amd_comgr.dll"  C:\llamacpp\

   .. note::

      The AMD display driver installs its own copy of ``amdhip64_7.dll`` in
      ``C:\Windows\System32``. Windows searches ``System32`` before ``PATH``, so
      the driver's version is loaded in preference to the one supplied by ROCm,
      even when ROCm is on ``PATH``. Because Windows searches the directory
      containing the executable first, copying these libraries next to
      ``llama-cli.exe`` ensures the ROCm version is used.

.. _llamacpp-verify-installation:

Verify the installation
=======================

.. selected:: os=ubuntu

   List the devices visible to llama.cpp:

   .. code-block:: bash

      # Replace <build> with your llama.cpp build number
      cd llama-<build>
      ./llama-cli --list-devices

   The output shows the detected GPU and its available memory:

   .. code-block::

      Available devices:
        ROCm0: AMD Radeon RX 9070 XT (16304 MiB, 15770 MiB free)

   If ``Available devices`` is empty, the ROCm libraries were not found. Review
   :ref:`Configure your environment <llamacpp-configure-env>`.

   If instead you see ``error while loading shared libraries: libgomp.so.1``, install
   the additional packages listed in :ref:`System requirements <llamacpp-sysreqs>`.

   Listing the devices confirms that the ROCm libraries were found, but it does not confirm
   that computation runs on the GPU. To verify that, run a short benchmark with a model in
   GGUF format; see :ref:`llamacpp-example`.

.. selected:: os=windows

   List the devices visible to llama.cpp. Make sure to ``cd`` into where the llama.cpp
   binaries are located and that you're in the same shell in which you set your ``PATH``.

   .. code-block:: bat

      cd C:\llamacpp
      llama-cli.exe --list-devices

   The output shows the detected GPU and its available memory. For example:

   .. code-block::

      Available devices:
        ROCm0: AMD Radeon RX 7900 XT (20464 MiB, 20315 MiB free)

   .. selected:: i=tar

      If the device is listed but the reported memory is ``0 MiB``, the installation
      is not usable. This occurs when the ``LLVM_PATH`` environment variable is set,
      which the ROCm tarball instructions do system-wide. Copying the HIP runtime
      libraries as described in the :ref:`previous section
      <llamacpp-copy-runtime-libs>` resolves it. Alternatively, clear ``LLVM_PATH``
      before running llama.cpp.

   If no devices are listed at all, the ROCm runtime cannot be found. Review
   :ref:`Configure your environment <llamacpp-configure-env>`.

.. selected:: os=ubuntu
   :heading: Select the GPUs to use

   Systems with both a discrete GPU and an integrated GPU report more than one ROCm device:

   .. code-block::

      Available devices:
        ROCm0: AMD Radeon RX 9070 XT (16304 MiB, 15770 MiB free)
        ROCm1: AMD Radeon Graphics (63199 MiB, 63174 MiB free)

   The integrated GPU reports a large amount of shared system memory and may not be a
   supported ROCm device. To restrict llama.cpp to specific GPUs, set
   ``HIP_VISIBLE_DEVICES`` to a comma-separated list of their indices:

   .. code-block:: bash

      # Use ROCm0 only
      export HIP_VISIBLE_DEVICES=0

      # Use ROCm0 and ROCm1 together, for example two discrete GPUs
      export HIP_VISIBLE_DEVICES=0,1

   The indices refer to the devices as numbered in the ``--list-devices`` output.
   llama.cpp distributes a model across all visible GPUs, so listing more than one
   lets you run models that do not fit in the memory of a single GPU.

   Alternatively, pass the devices to a single command with ``--device``, using the
   names from ``--list-devices`` rather than the indices:

   .. code-block:: bash

      ./llama-cli -m <model>.gguf -ngl 999 --device ROCm0,ROCm1

.. _llamacpp-example:

Run a llama.cpp example
=======================

Once your llama.cpp environment is set up, experiment with the following steps
to run a model and benchmark your installation. The prebuilt llama.cpp
release includes the executables to exercise the functionality of your
installation.

The two most popular use cases are:

* ``llama-cli``: The main executable to run the model interactively or get a response to a prompt.
* ``llama-bench``: Run a benchmark of your model with different configurations.

.. seealso::

   See `Models (llama.cpp docs) <https://llama.app/models>`__ for a list of
   GGUF-formatted models available to download from Hugging Face.

.. selected:: os=ubuntu

   The following examples assume the llama.cpp executables are in your
   ``llama-<build>`` directory from the :ref:`previous installation step
   <llamacpp-install>` and you've downloaded a model in GGUF format to run.

.. selected:: os=windows

   The following examples assume the llama.cpp executables are in ``C:\llamacpp``
   and you've downloaded a model in GGUF format to run.

llama-cli
---------

1. Use the CLI tool to start the client, replacing ``<model>.gguf`` with the path to a model on your system:

   .. selected:: os=ubuntu

      .. code-block:: bash

         # Replace <build> with your llama.cpp build number
         cd llama-<build>
         ./llama-cli -m <model>.gguf -ngl 999

   .. selected:: os=windows

      .. code-block:: bat

         cd C:\llamacpp
         llama-cli.exe -m <model>.gguf -ngl 999

2. A prompt appears when the client is ready, and you can start interacting with the model:

   .. code-block::

      > Explain what a GPU kernel is in one sentence.
      A GPU kernel is a specialized program within a GPU (Graphics Processing Unit) designed to execute
      instructions for rendering graphical content, such as images or video, on a GPU's hardware architecture.

      [ Prompt: 593.4 t/s | Generation: 286.4 t/s ]

3. To exit, enter ``/exit`` or press ``Ctrl+C``.

To send a single prompt and exit instead of starting an interactive session, add the ``-p`` and ``-st`` flags:

.. selected:: os=ubuntu

   .. code-block:: bash

      ./llama-cli -m <model>.gguf -p "Explain what a GPU kernel is in one sentence." -ngl 999 -st

.. selected:: os=windows

   .. code-block:: bat

      llama-cli.exe -m <model>.gguf -p "Explain what a GPU kernel is in one sentence." -ngl 999 -st

.. note::

   .. selected:: os=ubuntu

      Without ``-st``, ``llama-cli`` answers the prompt supplied by ``-p`` and
      then continues waiting for further input. Use ``./llama-completion`` for
      non-interactive generation.

   .. selected:: os=windows

      Without ``-st``, ``llama-cli`` answers the prompt supplied by ``-p`` and
      then continues waiting for further input. Use ``llama-completion.exe`` for
      non-interactive generation.

llama-bench
-----------

1. Use the CLI tool to start the application, replacing ``<model>.gguf`` with the path to a model on your system:

   .. selected:: os=ubuntu

      .. code-block:: bash

         ./llama-bench -m <model>.gguf -p 16,32,64,128,256,512,1024 -n 64,128 -ngl 999

   .. selected:: os=windows

      .. code-block:: bat

         llama-bench.exe -m <model>.gguf -p 16,32,64,128,256,512,1024 -n 64,128 -ngl 999

2. The result of the command above should be similar to the following when running on an AMD Radeon RX 7900 XT system:

   .. selected:: os=ubuntu

      .. code-block::

         ggml_cuda_init: found 1 ROCm devices (Total VRAM: 20464 MiB):
           Device 0: AMD Radeon RX 7900 XT, gfx1100 (0x1100), VMM: no, Wave Size: 32, VRAM: 20464 MiB
         load_backend: loaded ROCm backend from /home/user/llama-b10539/libggml-hip.so
         load_backend: loaded RPC backend from /home/user/llama-b10539/libggml-rpc.so
         load_backend: loaded CPU backend from /home/user/llama-b10539/libggml-cpu-haswell.so

   .. selected:: os=windows

      .. code-block::

         ggml_cuda_init: found 1 ROCm devices (Total VRAM: 20464 MiB):
           Device 0: AMD Radeon RX 7900 XT, gfx1100 (0x1100), VMM: no, Wave Size: 32, VRAM: 20464 MiB
         load_backend: loaded ROCm backend from C:\llamacpp\ggml-hip.dll
         load_backend: loaded RPC backend from C:\llamacpp\ggml-rpc.dll
         load_backend: loaded CPU backend from C:\llamacpp\ggml-cpu-haswell.dll

   .. code-block::

      | model                          |       size |     params | backend    | ngl |            test |                  t/s |
      | ------------------------------ | ---------: | ---------: | ---------- | --: | --------------: | -------------------: |
      | qwen2 1B Q4_K - Medium         | 462.96 MiB |   630.17 M | ROCm       | 999 |            pp16 |     2406.95 ± 704.75 |
      | qwen2 1B Q4_K - Medium         | 462.96 MiB |   630.17 M | ROCm       | 999 |            pp32 |     3842.56 ± 500.15 |
      | qwen2 1B Q4_K - Medium         | 462.96 MiB |   630.17 M | ROCm       | 999 |            pp64 |    7104.29 ± 1218.73 |
      | qwen2 1B Q4_K - Medium         | 462.96 MiB |   630.17 M | ROCm       | 999 |           pp128 |     8628.19 ± 928.69 |
      | qwen2 1B Q4_K - Medium         | 462.96 MiB |   630.17 M | ROCm       | 999 |           pp256 |   16444.29 ± 1662.23 |
      | qwen2 1B Q4_K - Medium         | 462.96 MiB |   630.17 M | ROCm       | 999 |           pp512 |   24628.13 ± 2498.10 |
      | qwen2 1B Q4_K - Medium         | 462.96 MiB |   630.17 M | ROCm       | 999 |          pp1024 |     26143.12 ± 73.58 |
      | qwen2 1B Q4_K - Medium         | 462.96 MiB |   630.17 M | ROCm       | 999 |            tg64 |        373.29 ± 9.81 |
      | qwen2 1B Q4_K - Medium         | 462.96 MiB |   630.17 M | ROCm       | 999 |           tg128 |        375.70 ± 3.49 |

      build: 78ec4c378 (10539)

3. The ``backend`` column shows ``ROCm`` when the GPU is in use. If it shows
   ``CPU``, the ROCm libraries were not found. Review :ref:`Configure your
   environment <llamacpp-configure-env>` to troubleshoot.

You can enable Flash Attention using ``-fa 1``:

.. selected:: os=ubuntu

   .. code-block:: bash

      ./llama-bench -m <model>.gguf -p 512 -n 64 -ngl 999 -fa 1

.. selected:: os=windows

   .. code-block:: bat

      llama-bench.exe -m <model>.gguf -p 512 -n 64 -ngl 999 -fa 1
