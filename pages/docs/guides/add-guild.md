tags: get-started, guide

# Add Guild to a project

[TOC]

This guide provides instructions for adding Guild AI support to an
existing project.

To demonstrate the process, we use the [SRGAN TensorLayer project
->](https://github.com/tensorlayer/srgan) as our starting point and
incementally build Guild support in each step. Our final project
supports these operations:

`train`
: Train the SRGAN.

`evaluate`
: Evaluate a trained SRGAN.

By following the steps in this guide, you become familiar with Guild
features and how they are added to existing projects.

## Requirements

Before running the steps in the guide, ensure that the following
requirements are met:

- [Guild AI is installed and verified](alias:install-guild)

## Background

Guild AI integrates with existing projects without requiring changes
to project code.

Our goal in adding Guild support is to define project models and their
operations in a [Guild file](ref:guild-file), which is a file named
`guild.yml` in the project root directory. Once modela and operations
are defined, project developers and users can perform these tasks
using Guild:

- Run an operation, automatically capturing run output and generated
  files as a unique experiment
- Study and compare run results
- Run an operation remotely to take advantage of compute capacity
- Backup and restore runs to the cloud
- Test model implementation

## Clone sample project

In this guide, we add Guild to the project [SRGAN TensorLayer project
->](https://github.com/tensorlayer/srgan).

Clone the repository on GitHub:

``` command
git clone https://github.com/tensorlayer/srgan.git
```

!!! note
    We don't commit changes to this repository in this guide. If
    you want to commit your changes, first fork the project and clone
    your fork instead of the TensorLayer project.

The SRGAN project provides two artifacts in particular that we look at
in this guide:

[README.md](https://github.com/tensorlayer/srgan/blob/master/README.md)
: Describes the goals of the project, cites the original paper, and
  provides step by step instructions for using the model. We use this
  file to understand the project at a high level and identify the
  models and operations it may support.

[main.py](https://github.com/tensorlayer/srgan/blob/master/main.py)
: Python main module that runs project commands. We use this file to
  study supported commands and their interfaces.

## Create `guild.yml`

Create a file named `guild.yml` in the project root directory.

The file should be:

``` yaml
- model: srgan
  description: SRGAN implementation using TensorLayer
  references:
    - https://arxiv.org/abs/1609.04802
```

Save your changes to `guild.yml`.

This is a basic model definition in Guild. It provides a name, a
description, and a reference. It's good practice to include the
original paper as a reference in your Guild files.

In a command console, change to the project directory and use Guild to
list project models:

``` command
cd srgan
guild models
```

Guild displays the model information that you just defined in
`guild.yml`:

``` output
./srgan  SRGAN implementation using TensorLayer
```

Next use Guild to display help for the project:

``` command
guild help
```

Guild displays project help, which contains the model details up to
this point:

``` output
...

MODELS

    srgan

      SRGAN implementation using TensorLayer

      Operations:

        No operations defined for this model

      References:

        - https://arxiv.org/abs/1609.04802
```

Note from the help that the model doesn't have operations. We define
those next.

## Define operations

In this section we define operations for our SRGAN model. To do this
we need to identify the tasks that can be performed for a model---each
of these becomes a Guild operation.

What tasks can be performed for the SRGAN model?

In looking at `README.md` under
[Run](https://github.com/tensorlayer/srgan#run), we see the use of two
commands:

> Start training.
>
>     python main.py
>
> Start evaluation.
>
>     python main.py --mode=evaluate

We can verify these two operations in `main.py` in the
[lines](https://github.com/tensorlayer/srgan/blob/13607e275baf3ec6052ecd90f3403433f4271977/main.py#L309-L314):

``` python
if tl.global_flag['mode'] == 'srgan':
    train()
elif tl.global_flag['mode'] == 'evaluate':
    evaluate()
else:
    raise Exception("Unknow --mode")
```

By looking at the source, it's clear that the project supports two
operations: *train* and *evaluate*.

Modify `guild.yml` to be:

``` yaml
- model: srgan
  description: SRGAN implementation using TensorLayer
  references:
    - https://arxiv.org/abs/1609.04802
  operations:
    train:
      description: Train the model
      main: main
    evaluate:
      description: Evaluate the model
      main: main --mode=evaluate
```

This is a basic Guild file. It contains one model with two
operations.

List available operations by running:

``` command
guild operations
```

!!! note
    You can use `ops` as a shortcut for
    [operations](cmd:operations). We use the short form through the
    rest of this guide.

Guild shows:

``` output
./srgan:evaluate  Evaluate the model
./srgan:train     Train the model
```

You can all use Guild help again:

``` command
guild help
```

Next, we initialize a Guild environment to manage runs.

## Initialize Guild environment

A [Guild environment](term:guild-env) is a Python virtual environment
that isolated Guild runs and installed packages. We recommend using
environments whenever running model operations for a project.

Initialize a Guild environment in the project directory:

``` command
guild init
```

Press `Enter` to confirm. Guild creates an environment in the `env`
project subdirectory.

When the environment is created, activate it:

``` command
source guild-env
```

After creating a new environment and activating it, we recommend
running [](cmd:check):

``` command
guild check
```

If there are any errors, resolve them before continuing. If you need
help solving a problem, [](alias:open-an-issue).

The final step in initializing the environment is to install packages
required by the SRGAN project:

``` command
pip install tensorlayer easydict
```

With the Guild environment initialized and activated, we can run our
first operation.

## Run `train` operation - take 1

In this section we run the `train` operation using the [](cmd:run)
command.

Guild runs operations by executing the main module defined for the
operation in the Guild file.

The `train` operation in `guild.yml` is currently:

``` yaml
train:
  description: Train the model
  main: main
```

When Guild runs this operation, it executes the `main`
module---i.e. the module defined in `main.py`.

You can see the command that Guild uses for an operation by running
[](cmd:run) with the `--print-cmd` option:

``` command
guild run train --print-cmd
```

Guild shows:

``` output
python -um main
```

!!! note
    The full path of the `python` executable is omitted above for
    brevity. Guild always displays the full path to the Python
    executable when showing run commands.

At this point we're naively running `main.py` to see what the script
does.

Run the `train` operation:

``` command
guild run train
```

Press `Enter` to confirm the operation.

After a few seconds, the operation exits with an error:

``` error
...
FileNotFoundError: [Errno 2] No such file or directory: 'data2017/DIV2K_train_HR/'
```

This is okay---we are only just experimenting with `main.py` to see
what happens. We'll resolve the issue using the error.

Before we troubleshoot the error, let's look at what the operation
generated.

Guild generates a unique [run](term:run) when it runs an
operation. Runs can be viewed and managed using a variety of Guild
commands.

List the current runs for the project:

``` command
guild runs
```

Guild shows the failed run (ID and timestamp will differ):

``` output
[1:bae4aeb2]  ./srgan:train  2018-10-24 12:53:35  error
```

Next, view run information, including its output:

``` command
guild runs info --output
```

Guild shows additional run details including the error message.

List files associated with the run:

``` guild
guild ls
```

Guild shows (top-level directory may differ):

``` output
~/srgan/env/.guild/runs/bae4aeb2d7b511e88f52d017c2ab916f:
  checkpoint/
  samples/
  samples/srgan_gan/
  samples/srgan_ginit/
```

This is a complete list of files and directories created during the
operation. The top-level directory (specified on the first line of the
output) is the [run directory](term:run-dir). A run directory is a
unique directory that Guild creates for each run. Guild runs the main
module in the run directory so that all relative paths used by the
script are relative to that directory.

We can see that `main.py` created four directories before exiting.

With this information, let's troubleshoot the error.

We can see from the error traceback that `main.py` is failing at this
[line](https://github.com/tensorlayer/srgan/blob/13607e275baf3ec6052ecd90f3403433f4271977/main.py#L41):

``` python
 train_hr_img_list = sorted(tl.files.load_file_list(path=config.TRAIN.hr_img_path, regx='.*.png', printable=False))
```

What's going on? The train script is looking for a directory
`data2017/DIV2K_train_HR/` but can't find it. Indeed, we can see from
the result of running [](cmd:ls) (see above) that the run directory is
missing this directory.

To resolve this issue, we need to somehow provide the missing files to
the script in the expected location in the run directory. We'll do
this in the next step.

## Add required resources

In this section, we resolve this issue using Guild
[resources](term:resource). A resource is a named set of sources that
Guild resolves within a run directory before executing the operation
main module.

In `README.md` we see in [Prepare Data and Pre-trained
VGG](https://github.com/tensorlayer/srgan#prepare-data-and-pre-trained-vgg)
that the train script requires some files---it's no surprise that the
train operation failed!

In the case of our SRGAN model, we see there are two required
resources:

- Pretrained VGG19 model
- High resolution images for training

We can modify the Guild file to define these resources and to indicate
that `train` requires both. We need the URLs for each of the
resources.

From the `README.md`, the training images are available from these URL
sources:

- [http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_HR.zip](http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_HR.zip)
- [https://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_LR_bicubic_X4.zip](https://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_LR_bicubic_X4.zip)
- [https://data.vision.ee.ethz.ch/cvl/DIV2K/validation_release/DIV2K_valid_HR.zip](https://data.vision.ee.ethz.ch/cvl/DIV2K/validation_release/DIV2K_valid_HR.zip)
- [https://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_valid_LR_bicubic_X4.zip](https://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_valid_LR_bicubic_X4.zip)

The pretrained VGG 19 model is here:

- [https://github.com/tensorlayer/pretrained-models/raw/master/models/vgg19.npy](https://github.com/tensorlayer/pretrained-models/raw/master/models/vgg19.npy)

Guild resources are defined in a `resources` section for each
model. Each resource has a list of sources. In our case, we have two
resources and define them as follows:

``` yaml
resources:
  pretrained-model:
    sources:
      - url: https://github.com/tensorlayer/pretrained-models/raw/master/models/vgg19.npy
        sha256: ???
  training-images:
    path: data2017
    sources:
      - url: http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_HR.zip
        sha256: ???
      - url: https://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_LR_bicubic_X4.zip
        sha256: ???
      - url: https://data.vision.ee.ethz.ch/cvl/DIV2K/validation_release/DIV2K_valid_HR.zip
        sha256: ???
      - url: https://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_valid_LR_bicubic_X4.zip
        sha256: ???
```

Note that each URL source has an undefined `sha256` attribute. These
values are used to verify the integrity of downloaded files. It's a
good practice to always use verified SHA 256 digests when defining
required sources.

You can pre-download each source to get its SHA 256 digest using the
[](cmd:download) command. Guild stores downloaded resources in
`~/.guild/cache/resources`. If a file is already downloaded, Guild
uses the local file rather than download it again.

We provide SHA 256 digests below, so you don't need to explicitly
download anything now---Guild downloads them as needed when you run an
operation.

Guild automatically unpacks archives when it resolves sources, so the
contents of each image zip file are available to the script in the run
directory.

Note that `training-images` defines a `path` value of
``data2017``. This indicates that resolved sources should be located
in a subdirectory `data2017`. This is where the script looks for the
images (e.g. see error message above: ``No such file or directory:
'data2017/DIV2K_train_HR/``).

With the two resources defined, we can indicate that `train` requires
them as follows:

``` yaml
train:
  description: Train the model
  main: main
  requires:
    - pretrained-model
    - training-images
```

This indicates tells Guild that each of the specified resources must
be resolved before executing the `main` module.

Let's add all of this to our Guild file.

Modify `guild.yml` to be:

``` yaml
- model: srgan
  description: SRGAN implementation using TensorLayer
  references:
    - https://arxiv.org/abs/1609.04802
  operations:
    train:
      description: Train the model
      main: main
      requires:
        - pretrained-model
        - images
    evaluate:
      description: Evaluate the model
      main: main --mode=evaluate
  resources:
    pretrained-model:
      sources:
        - url: https://github.com/tensorlayer/pretrained-models/raw/master/models/vgg19.npy
          sha256: 230f8aac6679445545743fa5ea3839f963677a38e008846f13364e6caa594f60
    images:
      path: data2017
      sources:
        - url: http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_HR.zip
          sha256: 9d0b9c463f6e35b6c62cc6a930ee2224f670b34c1df841a57670f9acf0f6c335
        - url: https://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_LR_bicubic_X4.zip
          sha256: f006b837f4eb52b82909aa01478e6d6d199eefce932179491d0c9dbb706dde3a
        - url: https://data.vision.ee.ethz.ch/cvl/DIV2K/validation_release/DIV2K_valid_HR.zip
          sha256: 20dd31fd84d777bc1cf5d6b7654a3f569c0aec74458ae094122ad1d0489900fc
        - url: https://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_valid_LR_bicubic_X4.zip
          sha256: a50a5d1c4b88de4e8d300d8fb2b904c52fe93b2b298a4899697760d7cbb6d553
```

Save your changes to `guild.yml`.

At this point the Guild file is ready for training.

## Run `train` operation - take 2

Now that we've configured resources for `train`, let's run it again:

``` command
guild run train
```

Press `Enter` to start the operation.

!!! note
    If you did not pre-download the required resources, the
    operation initially takes time to download the sources. When the
    files are downloaded, Guild unpacks them and make them available
    to the operation within the active run directory.

The project `main` module performs the training. Guild adds a few
steps to the process, which streamlines training:

- Download required resources
- Create a new directory for each run to capture run output as a
  unique experiment
- Setup the run directory with files needed by the main module
- Provide tools for inspecting and managing runs

The train operation should begin running through first the initial
epochs and then the training epochs (100

The train operation runs for 100 epochs. It progresses as `main`
iteratively trains the RSGAN model using the downloaded test data. The
process can take anywhere from an hour to several hours depending on
your hardware.

You can inspect the active run from another command console by running
any of these commands:

[guild runs](cmd:runs)
: List runs, showing status for each. Use this to see what's running.

[guild runs info](cmd:runs-info)
: Show info for the most recent run. You can include additional
  options to show more information such as `--output` and `--files`.

[guild open](cmd:open)
: Use your system file browser to open the latest run directory. This
  is useful for browsing files associated with a run.

[guild open -p PATH](cmd:open)
: Open a run file or directory `PATH`. The program used to open files
  is system specific.

[guild view](cmd:view)
: Start [Guild View](term:guild-view) and open a browser window for
  it. Guild View is a visual application provided with Guild for
  exploring runs, run files, and output.

[guild runs rm -E](cmd:runs-delete)
: Delete failed runs.
