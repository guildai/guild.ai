tags: popular, models

# Create an object detector

[TOC]

In this guide we create an object detector using support from
[gpkg.object-detect](pkg:object-detect). We demonstrate a number of
Guild features that accelerate model development and automate
workflow:

- Reuse high-level model configuration from `gpkg.object-detect`
- Automate workflow steps used to train, finetune and deploy a
  state-of-the-art object detector

## Requirements

- [Install Guild AI](alias:install-guild)
- GPU accelerated system

!!! note
    Many of the operations run in this guide are not feasible
    without a GPU accelerated system. If you don't have access to a
    GPU, consider using a GPU accelerated server or container from
    AWS, Google Cloud, Microsoft Azure, and others.

## Create a new project

In this section we create a new Guild project. A Guild project is a
directory that contains a [Guild file](term:guild-file), which is
named `guild.yml` and located in the project root directory.

For the examples, we use the environment variable `PROJECT` to
represent the project directory. For our example, we will create the
project in ``~/sample-object-detector``. Feel free to create the
project in another location. If you use a different location, define
`PROJECT` accordingly.

Define the location of the sample object detector project:

``` command
PROJECT=~/sample-object-detector
```

Create the project directory:

``` command
mkdir $PROJECT
```

In the project directory, create the file `guild.yml` containing:

``` yaml
- model: detector
  description: Sample object detector
```

Ensure this file is named `guild.yml` and is located in the project
directory (i.e. ``$PROJECT/guild.yml``).

Save your changes to `guild.yml`.

From a command line, use Guild to list the project models:

``` command
cd $PROJECT
guild models
```

Guild shows the sample model you just defined in `guild.yml`:

``` output
./detector  Sample object detector
```

If you don't see the `detector` model, verify that the `guild.yml`
above is located in the project directory.

List the model operations:

``` command
guild operations
```

!!! note
    You may alternatively use ``guild ops`` as a shortcut for
    this command. We use this short form for the remainder of this
    guide.

Guild doesn't show anything because model doesn't currently define any
operations. Later we modify the model to add operations. Before we
modify the model, however, we need to install required software into a
project environment.

## Initialize a project environment

For our work in this guide, we'll use a project [Guild
environment](term:guild-env). Environments isolate both installed
packages and runs from the system, ensuring that your work in this
guide is visible only from the project environment.

From the project directory, initialize a Guild environment:

``` command
guild init
```

Press `Enter` to confirm.

Guild creates a new Python virtual environment in the project
directory under `env`. The `env` project directory contains the Python
runtime, installed Python packages, and the project's [Guild
home](term:guild-home), which contains runs generated when the
environment is active.

At this point the environment is created but is not activated. To use
the environment, you must first activate it.

From the project directory, activate the environment:

``` command
source guild-env
```

!!! note
    The command prompt changes when the environment is activated
    to include the environment name. This value is the name of the
    project directory by default but can be set using `--name` when
    running `guild init`.

!!! note
    You must activate the project environment using ``source
    guild-env`` each time you start a new command line session for
    project work.

Before proceeding to the next section, verify the environment using
the [](cmd:check) command:

``` command
guild check
```

Verify that `guild_home` is in the project directory under
``env/.guild``. If `guild_home` is in a different location, verify the
steps above to ensure that your project environment is initialized and
activated.

## Install `gpkg.object-detect`

The sample object detector we create in this guide uses model support
defined in the Guild package `gpkg.object-detect.`

Guild packages are standard Python packages that can be installed
using pip or [guild install](cmd:install).

In this case we'll use Guild. Install `gpkg.object-detect` by running:

``` command
guild install gpkg.object-detect
```

Guild installs `gpkg.object-detect` along with its required packages.

List all installed Guild packages by running:

``` command
guild packages
```

Guild shows the installed `gpkg.object-detect` package.

With `gpkg.object-detect` available, we can use it to extend our model
with a detector model configuration.

## Extend a model configuration

In this step we will modify our sample detector to extend one of the
model configurations defined in the `gpkg.object-detect` package.

`gpkg.object-detect` supports the following configurations:

`faster-rcnn-resnet-50`
: Faster RCNN detector with ResNet-50 backbone.

`faster-rcnn-resnet-101`
: Faster RCNN detector with ResNet-101 backbone.

`ssd-mobilenet-v2`
: SSD detector with MobileNet v1 backbone.

We can apply any of these configurations to our sample detector by
extending it. We'll use `faster-rcnn-renset-50` for our example.

Modify `guild.yml` in the project directory to be:

``` yaml
- model: detector
  description: Sample object detector
  extends:
    - gpkg.object-detect/faster-rcnn-resnet-50
```

Save your changes to `guild.yml`.

By extending `gpkg.object-detect/faster-rcnn-resnet-50` we inherit the
model configuration, which includes a full workflow for building an
object detector.

List operations again:

``` command
guild ops
```

Guild shows the following operations:

``` output
./detector:detect             Detect images using a trained detector
./detector:evaluate           Evaluate a trained detector
./detector:export-and-freeze  Export a detection graph with checkpoint weights
./detector:train              Train detector from scratch
./detector:transfer-learn     Train detector using transfer learning
```

Operations are run in this order:

- `train` or `transfer-learn` - train a model
- `evaluate` - evaluate model performance using validation data
- `detect` - use a trained model to detect objects in am image

Before we can use the model, however, we need to add support for the
dataset we'll train and validate with.

## Add dataset support

Before we can train our detector, we need to modify our model with
dataset support. Dataset support entails two components:

- An operation that prepares the dataset for training and validation

- Information about the prepared data, including the number of
  classes, file patterns for train and validation examples, and human
  readable labels for each example class

Dataset support in `gpkg.object-detect` is flexible---you're free to
provide data from any source, provided the data is prepared as TF
Records split between files for training and validation.

For our detector, we'll implement support for preparing images with
Pascal VOC formatted annotations. As input, we need to provide two
directories:

- Directory containing JPG, PNG, or GIF encoded images
- Directory containing Pascal VOC XML formatted annotations

To add support for preparing a dataset using Pascal VOC formatted
images, we can add
`gpkg.object-detect/voc-annotated-images-directory-support` to our
model's `extends` list.

Modify `guild.yml` to be:

``` yaml
- model: detector
  description: Sample object detector
  extends:
    - gpkg.object-detect/voc-annotated-images-directory-support
    - gpkg.object-detect/faster-rcnn-resnet-50
```

!!! important
    The order that items appear in `extends` is important as
    configuration defined in earlier items in the list take precedance
    over items defined later. Ensure that
    `voc-annotated-images-directory-support` is listed *before*
    `faster-rcnn-resnet-50`.

Save your changes to `guild.yml`.

This change adds a `prepare` operation to our detector.

List model operations:

``` command
guild ops
```

The `prepare` operation is now available:

``` output
./detector:prepare  Prepare images annotated using Pascal VOC format for training
```

Later, we use this operation to prepare our annotated images for
training and validation. First we must obtain some annotated images.

## Obtain annotated images

If you have Pascal VOC annotated images, you may use them to train
your detector.

If you don't have images, you can download one of these datasets (you
need both images and annotations):

<table class="table">
  <tr>
    <td>
      <a href="http://www.robots.ox.ac.uk/~vgg/data/pets/">The Oxford-IIIT Pet Dataset</a>
    </td>
    <td>
      <a href="http://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz">images</a>,
      <a href="http://www.robots.ox.ac.uk/~vgg/data/pets/data/annotations.tar.gz">annotations</a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="http://host.robots.ox.ac.uk/pascal/VOC/voc2008/">Visual Object Classes Challenge 2008</a>
    </td>
    <td>
      <a href="http://host.robots.ox.ac.uk/pascal/VOC/voc2008/VOCtrainval_14-Jul-2008.tar">combined</a>
    </td>
  </tr>
</table>

Once you have obtained annotated images, note the locations of the
image files (e.g. JPG, PNG, GIF files) and of the annotations
(e.g. XML files).

Set the following variables:

``` command
IMAGES=<path to image files>
ANNOTATIONS=<path to annotations>
```

Replace the applicable paths above with the locations of your images
and annotations.

## Prepare dataset

Prepare the dataset for training and validation by running:

``` command
guild run prepare images=$IMAGES annotations=$ANNOTATIONS
```

Guild runs the operation, which processes the annotated images to
prepare train and validation records.

Once prepared, the dataset is available to any operations that needs
training data (e.g. `train` or `transfer-learn`) or validation data
(e.g. `evaluate`).

## Train a detector using transfer learning

Let's begin training our detector using our prepared dataset. To save
time, we'll use transfer learning with model weights that were learned
from training on the ImageNet dataset.

Start the `transfer-learn` operation using this command:

``` command
guild run transfer-learn --gpus 0
```

!!! note
    The use of ``--gpus 0`` ensures that the operation will only
    use the first GPU on the system (ID of `0`). If your system has
    more than one GPU, you'll be able to use it later when running
    `evaluate`.

Press `Enter` to confirm.

The operation is configured to train indefinitely by default. It's
common practice to let models train indefinitely without prescribing a
fixed number of training steps or epochs. While the operation runs,
you routinely evaluate its performance and stop the operation when
it's clear that further training will not sufficiently improve model
performance.

You can stop any operation by pressing `Ctrl-C` or alternatively use
[guild stop](cmd:runs-stop) from another command prompt.

The operation is configured to evaluate accuracy after each
checkpoint. However, we can evaluate at any point by running the
`evaluate` operation.

## Check model accuracy

While the model trains, we can check its accuracy by running the
`evaluate` operation from a second command prompt.

To evaluate the trained model, first initialize a new command console:

- Open a new command console or a new window/pane if using a tmux or
  screen

- Change to the project directory and activate the environment

``` command
cd $PROJECT
source guild-env
```

List project runs:

```
guild runs
```

Guild shows the project runs the `prepare` and `transfer-learn` runs
(IDs and dates will differ):

``` output
[1:ffc693ac]  ./detector:transfer-learn  2018-10-30 16:08:50  running
[2:f93f43da]  ./detector:prepare         2018-10-30 13:45:29  completed
```

If you don't see these runs, confirm that the working directory is
`$PROJECT` and that you have activated the project environment by
running ``source guild-env`` from that directory.

Next, we run the `evaluate` operation, which evaluates the latest
checkpoint saved by the `transfer-learn` operation (run `1` above)
using the validation data from the latest `prepare` operation (run `2`
above).

If your system only has one GPU, you can't use a GPU for the
`evaluate` operation. In this case, start the operation using the
`--no-gpus` option:

``` command
guild run evaluate --no-gpus
```

If your system has more than one GPU, you can use the second GPU for
the `evaluate` operation. In this case, start the operation using the
`--gpus` option:

``` command
guild run evaluate --gpus 1
```

!!! note
    The use of ``--gpus 1`` in the command ensures that the
    operation will only see the second GPU and not try to allocate
    memory on other GPUs.
    <p>
    If you don't explicitly control the visible GPUs with
    `--gpus` and `--no-gpus` options, each TensorFlow operation will
    preemptively consume the memory on all visible GPUs, even if
    they're not used.

The evaluate operation uses the validation records from the prepared
dataset to measure model performance. As we are training an object
detector, performance is measured using COCO mAP metrics.[^mAP]

[^mAP]: For an excellent high-level description of the measuring
    accuracy in object detectors, see [mAP (mean Average Precision)
    for Object Detection
    ->](https://medium.com/@jonathan_hui/map-mean-average-precision-for-object-detection-45c121a31173).

Each time you run `evaluate` a new run is generated, which serves as a
record of your measurement. The run preserves accuracy metrics that
can be viewed in TensorBoard and used by other programs.

You can use Guild Compare by running [](cmd:compare) to view run
performance, including loss and accuracy.

``` command
guild compare
```

You can view run details, including the most recently written scalar
values, by navigating to a run using the `Up` and `Down` keys and
pressing `Enter`. Exit the detail screen by pressing `q`.

Exit Guild Compare by pressing `q`.

## Monitor progress with TensorBoard

In this section we will use TensorBoard to monitor the transfer learn
operation and determine when to stop training.

Using your second command console, from the project directory, start
TensorBoard:

``` command
guild tensorboard
```

Guild starts TensorBoard and opens it in a new browser window. Guild
manages TensorBoard so that changes to project runs automatically
appear in TensorBoard.

In TensorBoard under the **Scalars** tab, type or paste the following
regular expression into the **Filter tags** field at the top of the
page:

``` text
loss|gpu
```

TensorBoard shows matching scalars, including the various training
losses associated with the operation as well as GPU information.

Watch the progress of the losses and use them as a gauge for
determining when to stop training.

![](/assets/img/object-detect-losses.png)

^ Sample training losses from TensorBoard

When losses are no longer decreasing, or are increasing, consider
stopping the transfer learn operation---more training will not likely
improve model performance.

You can stop training at any point, however we recommend training for
at least 10K-20K steps to achieve reasonable accuracy. Use `evaluate`
(see [Check model accuracy](#check-model-accuracy) above) to calculate
model precision to confirm before stopping.

When you are finished monitoring the run, in the second command
console---the console where TensorBoard is running---press `Ctrl-C` to
quit the application.

## Stop training

Stop the transfer learn operation using two methods:

- In the first command console---the console where the
  `transfer-learn` operation is running---press `Ctrl-C`.

- In the second command console, run the command:

``` command
guild stop
```

The [stop](cmd:runs-stop) command stops all active runs by default.

Press `y` and then `Enter` to confirm that you want to stop the
`transfer-learn` operation.

Guild stops the transfer learn operation.

Now that we have a trained object detector, we can use it to detect
objects. First, however, we need to generate a frozen inference graph.

## Export and freeze a trained model

To use our trained object detector for inference, we need to *export*
the model architecture and *freeze* its weights using a
checkpoint. This process generates a *frozen inference graph*, which
is a binary file that can be loaded to initialize the trained model in
TensorFlow.

Run the `export-and-freeze` command:

``` command
guild run export-and-freeze
```

Press `Enter` to confirm.

By default, Guild uses the latest checkpoint from the latest training
run (i.e. the latest `transfer-learn` operation) to generate the
frozen inference graph.

You can specify different runs or checkpoint steps by specifying a
`trained-model` dependency and a `step` flag repectively.

View help for the `export-and-freeze` operation:

``` command
guild run export-and-freeze --help-op
```

Guild shows operation help:

``` output
Usage: guild run [OPTIONS] detector:export-and-freeze [FLAG]...

Export a detection graph with checkpoint weights

Use 'guild run --help' for a list of options.

Dependencies:
  trained-model  Trained model from train or transfer-learn

Flags:
  step  Checkpoint step to use for the frozen graph (latest checkpoint)
```

As needed, you can run the operation using an alternative trained
model and checkpoint step this way:

``` command
guild run export-and-freeze trained-model=<run ID> step=<step>
```

You can view the available checkpoints for a run using the [](cmd:ls)
command:

``` command
guild ls --operation transfer-learn
```

The use of ``--operation transfer-learn`` tells Guild to list files
for the latest `transfer-learn` operation.

Checkpoint steps are shown in files named `train/model.ckpt-STEP.*`
where `STEP` is the available checkpoint step.

## Detect objects in an image

With the frozen inference graph we generated in the previous section,
we can now detect objects in an image.

Create a new directory containing one or more images that you want to
detect.

For this example, we will create a directory in `/tmp`---feel free to
use another location.

``` command
DETECT_IMAGES=/tmp/sample-detect-images
```

Try including images from the original dataset as well as other
images---for example from the Internet or those you've collected
yourself. Images may include zero or more instances of detectable
objects.

Run the `detect` operation, specifying the location of the images you
want to detect:

``` command
guild run detect images=$DETECT_IMAGES
```

Guild uses the inference from the latest `export-and-freeze` operation
to load and initialize the object detector. It runs each image in
`$DETECT_IMAGES` through the model to both classify and locate objects
with bounding boxes.

When the detect operation finishes, you can view the detected objects
using either Guild View---a Guild AI application used to view
runs---or an image viewer installed on your system.

Start Guild View:

``` command
guild view
```

Guild opens a new browser window running Guild View. Guild View
provides a number of helpful features:

- Explore project runs
- Compare runs (similar to [guild compare](cmd:compare))
- View runs in TensorBoard (similar to [guild
  tensorboard](cmd:tensorboard))
- View run files
- Search run output

![](/assets/img/detect-runs.png)

^ Explore project runs in Guild View

Click the **FILES** tab of a `detect` run and click one of the
detected images. Guild opens the image in a file viewer. If the image
contains detected objects, the objects will appear in a bounding box
with the detected class.

![](/assets/img/detected-image.png)

^ View detected image in Guild View

You can also use [guild open](cmd:open) to use your system file
explorer to view run files. To view the run directory of the latest
`detect` operation, run:

``` command
guild open --operation detect
```

From your system file explorer, you can browse detected images and
open them in the image viewer of your choice.

## Deploy a trained model

You can deploy a trained object detector as single frozen inference
graph. This file is generated by the `export-and-freeze` operation.

To obtain this file, use the [](cmd:ls) command:

``` command
guild ls --operation export-and-freeze --path graph
```

Guild shows the files under the `graph` subdirectory of the latest
`export-and-freeze` run (run ID will differ):

``` output
~/sample-object-detector/env/.guild/runs/cb47150edd1111e88f52d017c2ab916f/graph:
  checkpoint
  frozen_inference_graph.pb
  model.ckpt.data-00000-of-00001
  model.ckpt.index
  model.ckpt.meta
  pipeline.config
  saved_model/
  saved_model/saved_model.pb
  saved_model/variables/
```

The first line in the output contains the full path to the `graph`
subdirectory of the `export-and-freeze` run.

You can use the `--full-path` option to show full paths for each file:

``` command
guild ls --operation export-and-freeze --path graph --full-path
```

!!! note
    Guild command options often have short-form alternatives. The
    above command, for example, can also be specified as ``guild ls -o
    export-and-freeze -p graph -f``.
    <p>
    Use `--help` with any command for a full list of options.
