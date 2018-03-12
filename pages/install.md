title: Install
pagenav_title: Installing Guild AI
navbar_item: yes
hide_sidenav: yes
hide_pagenav: yes
hide_in_pagenav: yes

# Installing Guild AI

[TOC]

## Requirements

Guild AI has the following requirements:

- Max OS, Linux
- Python 2.7, Python 3
- pip

Guild is installed from PyPI using `pip`. Refer to [Installing pip
->](https://pip.pypa.io/en/stable/installing/) to ensure you have it
installed.

## Install Guild AI

To install Guild AI, run the following on the command line:

``` command
pip install guildai
```

If you need to run `install` with administrative privileges, run:

``` command
sudo pip install guildai
```

You may alternatively install Guild AI in a Python virtual
environment. Refer to the next section for details.

### Install Guild AI using Virtualenv

If you would like to install Guild within a Python [virtual
environment ->](term:https://virtualenv.pypa.io), run the following:

``` command
virtualenv guild
source guild/bin/activate
pip install guildai
```

This has the advantage of isolating Guild AI within a single
directory. For more information on the advantages and disadvantages of
this approach, see [Working with
Virtualenv](/docs/tutorials/working-with-virtualenv/).

### Install Guild AI from source code

!!! note
    This step is an alternative to installing Guild AI with pip
    described above. Install Guild AI from source code if you want a
    specific version from GitHub (e.g. an early release or development
    branch) or if you want to contribute to the project.

Additional required tools for installing from source code:

- [git ->](https://help.github.com/articles/set-up-git/)
- [npm ->](https://www.npmjs.com/get-npm)
- Python development library and headers for your system

To install Guild from source, clone the repository by running:

``` command
git clone https://github.com/guildai/guild.git
```

Change to the `guild` directory and install the required pip packages:

``` command
cd guild
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
other errors, please [](alias:open-an-issue) and we'll help!

You can run the `GUILD_SOURCE_DIR/guild/scripts/guild` executable
directly (where `GUILD_SOURCE_DIR` is the location of your cloned
Guild AI source repository) or modify your environment to make `guild`
available on your PATH using one of these methods:

- Add `GUILD_SOURCE_DIR/guild/scripts` directory to your `PATH` environment
  variable, OR
- Create a symlink to `GUILD_SOURCE_DIR/guild/scripts/guild` that is
  available on your PATH

## Install TensorFlow

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

## Install optional libraries

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

## Verify your installation

Verify that Guild is installed properly by running the
[`check`](docs/commands/check) command:

``` command
guild check
```

If there are problems with your installation, Guild will display the
details and exit with an error. Refer to
[Troubleshooting](/troubleshooting) for assistance.

## Next steps

Congratulations, you've installed Guild AI! We've outlined some next
steps for you below.

<div class="row match-height">
<div class="col col-md-4">
<div class="promo left">
<h3>Train your first model</h3>
<p class="expand">

Dive in and train your first model using Guild AI. This introductory
tutorial will walk you through the basics of Guild and cover most of
its features.

</p>
<a class="btn btn-primary cta" href="/docs/tutorials/train-mnist/"
  >Train your first model <i class="fa next"></i></a>
</div>
</div>

<div class="col col-md-4">
<div class="promo left">
<h3>Discover Guild models</h3>
<p class="expand">

Guild AI provides a catalog of state-of-the-art TensorFlow models that
can be used to build deep learning applications. Start here to see
what developers are building.

</p>
<a class="btn btn-primary cta" href="/models/"
  >Discover Guild models <i class="fa next"></i></a>
</div>
</div>

<div class="col col-md-4">
<div class="promo left">
<h3>Browse the docs</h3>
<p class="expand">

If you're interested in a complete picture of Guild AI, start by
browsing its comprehensives documentation.

</p>
<a class="btn btn-primary" href="/docs/">Browse the docs <i class="fa next"></i></a>
</div>
</div>
</div>
