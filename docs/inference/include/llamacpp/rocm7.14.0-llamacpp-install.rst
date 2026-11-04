.. selected:: rocm-ver=7.14.0

   .. selected:: os=ubuntu

      .. code-block::

         llama-<build>-bin-ubuntu-rocm-7.14-x64.tar.gz

      For ROCm 7.14, that is any asset containing ``ubuntu-rocm-7.14``, for
      example ``llama-b10628-bin-ubuntu-rocm-7.14-x64.tar.gz``.

      Extract the archive:

      .. code-block:: bash

         tar -xf llama-b10628-bin-ubuntu-rocm-7.14-x64.tar.gz

      The archive extracts into a directory named after the build, for example ``llama-b10628``.

   .. selected:: os=windows

      .. code-block::

         llama-<build>-bin-win-rocm-7.14-x64.zip

      For ROCm 7.14, that is any asset containing ``win-rocm-7.14``, for example
      ``llama-b10628-bin-win-rocm-7.14-x64.zip``.

      Extract the archive. This guide assumes you extract to ``C:\llamacpp``.

      .. code-block:: bat

         tar -xf llama-b10628-bin-win-rocm-7.14-x64.zip -C C:\llamacpp

