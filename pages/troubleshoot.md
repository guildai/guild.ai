# Troubleshoot

This guide addresses various issues you may face when using Guild AI.

## Setup

Most setup related errors can be discovered by running ``guild
check``.

Refer to the issues below for help. If you don't see your issue,
[](alias:open-an-issue) and we'll work with you to resolve it.

### CUDA errors

#### Missing libcublas.so

When loading the `tenorflow` Python module, you may see this error:

```
ImportError: libcublas.so.9.0: cannot open shared object file: No such file or directory
```

!!! note
    The version of `libcublas.so` will differ based on the version of
    TensorFlow you're trying to load.

This indicates that TensorFlow cannot load NVIDIA's CUDA library:
either the required version is not installed or it is not
loadable from your shell environment.

Note the version number in the `libcublas.so` filename. This indicates
the required CUDA version.

For instructions on installing CUDA for your system, see [CUDA Toolkit
Documentation ->](http://docs.nvidia.com/cuda/index.html).
