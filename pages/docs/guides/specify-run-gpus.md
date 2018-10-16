sidenav_title: Specify available GPUs
tags: tip

# Specifying available GPUs for a run

To limit the GPUs available for a run, use the `--gpus` option with
the [](cmd:run) command. This option accepts a comma-separated list of
GPU IDs.

For example, to limit a run to GPU `0`, use:

``` command
guild run train --gpus 0
```

You can disable all GPU access by using `--no-gpus`:

``` command
guild run evaluate --no-gpus
```

This is useful for running operations on CPU that might otherwise fail
(e.g. other GPUs are in use or there isn't enough GPU memory to run
the operation.

!!! note
    Operations that benefit from GPU acceleration will likely
    run considerably slower on a GPU.

!!! note
    The GPU options only support CUDA devices. To view the list of
    available CUDA devices and their respective IDs, use
    ``nvidia-smi``---the [NVIDIA System Management Interface
    ->](https://developer.nvidia.com/nvidia-system-management-interface)
