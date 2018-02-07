tags: support

# Troubleshooting

[TOC]

This guide addresses various issues you may face when using Guild AI.

Most setup related errors can be discovered by running ``guild
check``.

Refer to the issues below for help. If you don't see your issue,
[](alias:open-an-issue) and we'll work with you to resolve it.

## TensorFlow

### TensorFlow is not installed

When you run ``guild check``, you may see this error:

```
tensorflow_version: NOT INSTALLED (No module named 'tensorflow')
```

The `tensorflow` Python module must be available for Guild training
scripts. You can test whether this module is available directly by
running:

``` command
python -m tensorflow
```

If the command exits without an error, TensorFlow is available but is
not visible to Guild. In this case [](alias:open-an-issue) and we'll
help you resolve it.

If the command exits with the message ``No module named tensorflow``
you must install TensorFlow.

Refer to [Installing TensorFlow
->](https://www.tensorflow.org/install/) for instructions for your
system.

In most cases, you can install TensorFlow by running:

``` command
pip install tensorflow
```

If your system has a GPU, run:

``` command
pip install tensorflow-gpu
```

## CUDA and cuDNN errors

### Missing libcublas.so

When loading the `tensorflow` Python module, you may see this error:

```
ImportError: libcublas.so.9.0: cannot open shared object file: No such file or directory
```

!!! note
    The version of `libcublas.so` will differ based on the version of
    TensorFlow you're trying to load.

This indicates that TensorFlow cannot load NVIDIA's CUDA library
because either the required version is not installed or it's not
loadable from your shell environment.

Note the version number in the `libcublas.so` filename. This indicates
the required CUDA version.

For instructions on installing CUDA for your system, see [CUDA Toolkit
Documentation ->](http://docs.nvidia.com/cuda/index.html).

### Missing libcudnn.so

When loading the `tensorflow` Python module, you may see this error:

```
ImportError: libcudnn.so.7: cannot open shared object file: No such file or directory
```

!!! note
    The version of `libcudnn.so` will differ based on the version of
    TensorFlow you're trying to load.

This indicates that TensorFlow cannot load NVIDIA's cuDNN library
because either the required version is not installed or it's not
loadable from your shell environment.

Note the version number in the `libcudnn.so` filename. This indicates
the required cuDNN version.

For instructions on installing cuDNN for your system, see [Deep
Learning SDK Documentation
->](http://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html).

## GPU stats

### NVML library version mismatch

When training on a GPU enabled system, you may see this error printed
to the console:

```
ERROR: [guild.gpu] reading GPU stats (smi output: '[['Failed to initialize NVML: Driver/library version mismatch']]')
```

This indicates that `nvidia-smi` is installed but the CUDA library
version is incompatible.

Ensure that your version of `nvidia-smi` is compatible with the
version of CUDA installed.

You can get the CUDA version by running:

``` command
guild check | grep cuda
```
