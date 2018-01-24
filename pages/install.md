title: Install
pagenav_title: Get started with Guild AI
navbar_item: yes
hide_sidenav: yes

# Get started with Guild AI

## Requirements

Before installing Guild, review the requirements below.

- Windows, Max OS, Linux
- Python 2.7, Python 3
- pip

Guild is installed from PyPI using the `pip` command. Refer to
[Installing pip ->](https://pip.pypa.io/en/stable/installing/) to
ensure you have pip installed.

## Installation

In a console, run the following:

``` shell
pip install guildai
```

!!! note
    You may need to run `pip` as a privileged user, in which case
    run the above command as `sudo pip install guildai`. If you
    would prefer to install Guild as an unpriviledged user, we
    recommend using a Python virtual environment. Refer to
    [Install using Virtualenv](#install-using-virtualenv) below.

### Install using Virtualenv

You may alternatively install Guild within a Python virtual
environment. This has the advantage of isolating Guild and its
requirements in a single directory.

``` shell
virtualenv guild
source guild/bin/activate
pip install guildai
```

!!! note
    If you install Guild in a virtual environment, you must activate the
    environment before using Guild using the command `source
    VIRTUAL_ENV_DIR/bin/activate`.

For more information refer to the [Virtualenv documentation
->](https://virtualenv.pypa.io/en/stable/).

## Install TensorFlow

Guild requires TensorFlow but does not install it for
you. [^tf-install] You can use `pip` to install TensorFlow by running
this command:

[^tf-install]:
    TensorFlow is a rapidly evolving software library and is provided as
    both CPU and GPU supported packages. Guild leaves the specific package
    and version of TensorFlow up to the user.

``` shell
pip install tensorflow
```

If your system has a GPU, you can install the GPU enabled package by
running:

``` shell
pip install tensorflow-gpu
```

For alternative installation method, refer to [Installing TensorFlow
->](https://www.tensorflow.org/install/).

## Install optional libraries

### CUDA and cuDNN

To run the GPU enabled TensorFlow package, you must also install
Nvidia's CUDA cuDNN libraries for your system. Refer to the links
below for more information.

- [CUDA Toolkit Download ->](https://developer.nvidia.com/cuda-downloads)
- [NVIDIA cuDNN ->](https://developer.nvidia.com/cudnn)

### NVIDIA System Management Interface

Guild uses the NVIDIA System Management Interface on GPU systems to
collect GPU stats. This tool is optional --- Guild will run without it
--- however, to collect GPU stats on systems with one or more GPUs,
ensure that `nvidia-smi` is available on your system.

!!! note
    NVIDIA System Management Interface is typically installed with NVIDIA
    GPU drivers. More information is available at [NVIDIA System
    Management Interface ->](https://developer.nvidia.com/nvidia-system-management-interface).

## Verify your installation

Verify that Guild is installed propery by running the
[`check`](docs/commands/check) command:

``` shell
guild check
```

If there are problems with your installation, Guild will display the
details and exit with an error.

Below are some common issues with the Guild installation.

TensorFlow is not installed
: See [Install TensorFlow](#install-tensorflow) above.

CUDA or cuCNN are not installed
: This is not a problem if your system does not have a GPU. If your
  system does have a GPU and there are problems with CUDA or cuDNN,
  you must resolve these issues before running TensorFlow
  operations. Refer to [CUDA and cuDNN](#cuda-and-cudnn) amd [NVIDIA
  System Management Interface](#nvidia-system-management-interface)
  above for links to NVIDIA's website.
