sidenav_title: Install

# Install Guild AI

[TOC]

## Requirements

Guild AI has the following requirements:

- macOS, Linux, Windows (Windows requires Python 3)
- Python 2.7, Python 3
- [pip ->](https://pip.pypa.io/en/stable/installing/)
  or [conda ->](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)

## Install Guild AI

### Using pip

To install Guild AI, run the following command:

``` command
pip install --user guildai
```

If you want to install Guild at the system level, omit the `--user`
option and run the command as an administrator:

``` command
sudo pip install guildai
```

If you want the latest pre-release version of Guild AI, use the
``--pre`` option:

``` command
pip install --pre --user guildai
```

### Using conda

If you're using conda, activate your environment:

``` command
conda activate ENV-NAME
```

Next, install Guild using `pip`:

``` command
pip install guildai
```

### With Docker

!!! note
    Installing Guild with Docker requires that you have Docker
    installed. Refer to [About Docker CE
    ->](https://docs.docker.com/install/) for instructions for your
    platform.

Guild AI provides a Docker image that you can install by running:

``` command
docker pull guildai/guildai
```

Start an interactive TTY session using the image by running:

``` command
docker run -it guildai
```

From within the container, you can execute Guild commands.

### From Source Code

!!! note
    This step is an alternative to installing Guild AI with pip
    described above. Install Guild AI from source code if you want a
    specific version from GitHub (e.g. an early release or development
    branch) or if you want to contribute to the project.

Additional required tools for installing from source code:

- [git ->](https://help.github.com/articles/set-up-git/)
- [npm ->](https://www.npmjs.com/get-npm) v5.8.0 or later
- Python development library and headers for your system

To install Guild from source, clone the repository by running:

``` command
git clone https://github.com/guildai/guildai.git
```

Change to the `guild` directory and install the required pip packages:

``` command
cd guildai
pip install -r requirements.txt
```

Build Guild by running:

``` command
python setup.py build
```

Verify Guild by running:

``` command
guild/scripts/guild check
```

If see the message ``NOT INSTALLED (No module named 'tensorflow')``
that's okay - you'll install TensorFlow in the steps below. If you see
other errors, please [](ref:open-an-issue) and we'll help!

You can run the `GUILD_SOURCE_DIR/guild/scripts/guild` executable
directly (where `GUILD_SOURCE_DIR` is the location of your cloned
Guild AI source repository) or modify your environment to make `guild`
available on your PATH using one of these methods:

- Add `GUILD_SOURCE_DIR/guild/scripts` directory to your `PATH` environment
  variable, OR
- Create a symlink to `GUILD_SOURCE_DIR/guild/scripts/guild` that is
  available on your PATH

## Install TensorFlow

!!! important
    Guild requires TensorFlow for integrated TensorBoard
    support only --- you are not required to use TensorFlow in your
    work.

Guild requires TensorFlow but does not install it for
you.[^tf-install] You can use `pip` to install TensorFlow by running:

[^tf-install]:
    TensorFlow is a rapidly evolving software library and is provided as
    both CPU and GPU supported packages. Guild leaves the specific package
    and version of TensorFlow up to the user.

``` command
pip install tensorflow
```

If your system has a GPU, install the GPU enabled package by running:

``` command
pip install tensorflow-gpu
```

For alternative installation methods, refer to [Installing TensorFlow
->](https://www.tensorflow.org/install/).

## Install Optional Libraries

If you system has a GPU or other accelerator supported by TensorFlow,
you will need to install and configure support for your hardware.

### CUDA and cuDNN

If you have an NVIDIA GPU and and want to use the GPU enabled
TensorFlow package, you must install the NVIDIA CUDA and cuDNN
libraries for your system. Refer to the links below for help
installing the libraries.

- [CUDA Toolkit Download ->](https://developer.nvidia.com/cuda-downloads)
- [NVIDIA cuDNN ->](https://developer.nvidia.com/cudnn)

### NVIDIA System Management Interface

Guild uses NVIDIA System Management Interface (`nvidia-smi`) on GPU
accelerated systems to collect GPU metrics. This tool is optional and
Guild will run without it. However, to collect GPU stats on systems
with one or more GPUs, ensure that `nvidia-smi` is installed.

!!! note
    NVIDIA System Management Interface is typically installed with NVIDIA
    GPU drivers. Refer to [NVIDIA System Management Interface
    ->](https://developer.nvidia.com/nvidia-system-management-interface)
    for more information.

## Verify your Installation

Verify that Guild is installed properly by running the
[`check`](docs/commands/check) command:

``` command
guild check
```

If there are problems with your installation, Guild will display the
details and exit with an error.

## Next Steps

Congratulations, you've installed Guild AI! We've outlined some next
steps for you below.

<div class="row match-height mt-4">
<div class="col col-md-4">
<div class="promo left">
<h3>Guild AI Quick Start</h3>
<p class="expand">

Start using Guild to run, track, and compare experiments.

</p>
<a class="btn btn-primary cta" href="/start/"
  >Get Started <i class="fa next"></i></a>
</div>
</div>

<div class="col col-md-6">
<div class="promo left">
<h3>Browse the Docs</h3>
<p class="expand">

If you're interested in a complete picture of Guild AI, browse the
comprehensives documentation.

</p>
<a class="btn btn-primary" href="/docs/">Browse the Docs <i class="fa next"></i></a>
</div>
</div>
</div>
