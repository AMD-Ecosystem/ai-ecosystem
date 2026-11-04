.. selected:: rocm-ver=10.0.0

   .. selected:: os=ubuntu

      .. code-block::

         llama-<build>-bin-ubuntu-rocm-10.0-x64.tar.gz

      For ROCm 10.0, that is any asset containing ``ubuntu-rocm-10.0``, for
      example ``llama-b10864-bin-ubuntu-rocm-10.0-x64.tar.gz``.

      Extract the archive:

      .. code-block:: bash

         tar -xf llama-b10864-bin-ubuntu-rocm-10.0-x64.tar.gz

      The archive extracts into a directory named after the build, for example ``llama-b10864``.

   .. selected:: os=windows

      .. code-block::

         llama-<build>-bin-win-rocm-10.0-x64.zip

      For ROCm 10.0, that is any asset containing ``win-rocm-10.0``, for example
      ``llama-b10864-bin-win-rocm-10.0-x64.zip``.

      Extract the archive. This guide assumes you extract to ``C:\llamacpp``.

      .. code-block:: bat

         tar -xf llama-b10864-bin-win-rocm-10.0-x64.zip -C C:\llamacpp

