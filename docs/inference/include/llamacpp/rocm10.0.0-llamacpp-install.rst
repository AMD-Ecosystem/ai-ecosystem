.. selected:: rocm-ver=10.0.0

   .. selected:: os=ubuntu

      .. code-block::

         llama-<build>-bin-ubuntu-rocm-10.0-x64.tar.gz

      For ROCm 10.0, that is any asset containing ``ubuntu-rocm-10.0``, for
      example ``llama-b10864-bin-ubuntu-rocm-10.0-x64.tar.gz``.

      Verify the checksum of the downloaded file against the digest shown for the asset, then
      extract the archive:

      .. code-block:: bash

         sha256sum llama-b10864-bin-ubuntu-rocm-10.0-x64.tar.gz
         tar -xf llama-b10864-bin-ubuntu-rocm-10.0-x64.tar.gz

      The archive extracts into a directory named after the build, for example ``llama-b10864``.

   .. selected:: os=windows

      .. code-block::

         llama-<build>-bin-win-rocm-10.0-x64.zip

      For ROCm 10.0, that is any asset containing ``win-rocm-10.0``, for example
      ``llama-b10864-bin-win-rocm-10.0-x64.zip``.

      Verify the checksum of the downloaded file against the digest shown for the
      asset, then extract the archive. This guide assumes you extract to ``C:\llamacpp``.

      .. code-block:: bat

         certutil -hashfile llama-b10864-bin-win-rocm-10.0-x64.zip SHA256
         tar -xf llama-b10864-bin-win-rocm-10.0-x64.zip -C C:\llamacpp

