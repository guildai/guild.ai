sidenav_title: Specify Available GPUs
tags: tips

# Specify Available GPUs for a Run

[TOC]

To limit the GPUs available for a run, use the `--gpus` option with
the [](cmd:run) command. This option accepts a comma-separated list of
GPU IDs.

For example, to limit a run to GPU `0`, use:

``` command
guild run train --gpus 0
```

To limit a run to GPUs `0` and `1`, use:

``` command
guild run train --gpus 0,1
```

To disable all GPU access, use `--no-gpus`:

``` command
guild run evaluate --no-gpus
```

This is useful for running operations on CPU that might otherwise fail
(e.g. other GPUs are in use or there isn't enough GPU memory to run
the operation.

!!! note
    Operations that benefit from GPU acceleration will run
    considerably slower on a GPU.

!!! note
    The GPU options only support CUDA devices. To view the list
    of available CUDA devices and their respective IDs, use
    ``nvidia-smi`` ([NVIDIA System Management Interface
    ->](https://developer.nvidia.com/nvidia-system-management-interface))

## Restart an operation with different GPUs

You can stop a run and restart it using a different value for
`--gpus`. For example, if you start a TensorFlow operation without
specifying `--gpus` the operation may preemptively consume all
available memory on all GPUs, preventing you from using GPUs for other
operations. To restart the run, first stop it by pressing `Ctrl-C` in
the run command console or use [guild stop](cmd:stop) from a different
console. Restart the run using `--restart` with the stopped run ID
along the `--gpus` value you want.

!!! important
    Many training operations routinely save trained weights
    to checkpoints and automatically restart from the latest available
    checkpoint, allowing you to stop and restart training where you
    left off. However, if the operation does not routinely save
    checkpoints, you will lose your trained weights if you stop early.

Consider the case where you start a run using this command:

``` command
guild run train
```

By default, this operation will run with all available GPUs,
preventing any other operation from running with the benefit of GPU
acceleration.

Stop the operation by pressing `Ctrl-C`.

Assuming the stopped `train` run ID is `abcd1234`, restart the
operation on the first GPU:

``` command
guild run --restart abcd1234 --gpus 0
```

You can now run other commands with different GPUs. For example:

``` command
guild run evaluate --gpus 1
```
