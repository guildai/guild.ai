tags: popular, models

# Create an object detector

[TOC]

In this guide we create an object detector using support from
[gpkg.object-detect](pkg:object-detect). We demonstrate a number of
Guild features that accelerate model development and automate
workflow:

- Reuse high-level model configuration from `gpkg.object-detect`
- Automate workflow steps used to train, evaluate and deploy a
  state-of-the-art object detector

## Requirements

{!guide-gpu-requirements.md!}

## Create a new project

In this section we create a new Guild project. A Guild project is a
directory that contains a [Guild file](term:guild-file), which is
named `guild.yml` and located in the project root directory.

For the examples, we use the environment variable `PROJECT` to
represent the project directory. For our example, we create the
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

Unless otherwise noted, commands are run from the project
directory. Change to that directory now:

``` command
cd $PROJECT
```

In the project directory, create the file `guild.yml` containing:

``` yaml
- model: detector
  description: Sample object detector
```

Save your changes to `guild.yml`, confirming that it's located in the
project directory (i.e. ``$PROJECT/guild.yml``).

From a command line, use Guild to list the project models:

``` command
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

Guild doesn't show anything because our model doesn't define any
operations. We modify the model later to add operations. First we need
to install required software in a project environment.

## Initialize a project environment

{!guide-init-project-env.md!}

## Install *gpkg.object-detect*

The object detector we create in this guide uses model support defined
in the Guild package `gpkg.object-detect.`

Guild packages are standard Python packages that can be installed
using pip or [guild install](cmd:install).

{!guide-verify-activated-env.md!}

After Verifying that your environment is activated, install
`gpkg.object-detect` the [](cmd:install) command:

``` command
guild install gpkg.object-detect
```

Guild installs `gpkg.object-detect` along with its dependencies.

List installed Guild packages by running:

``` command
guild packages
```

Guild shows the installed `gpkg.object-detect` package along with its
installed dependencies (e.g. `gpkg.slim`).

With `gpkg.object-detect` installed, we can use it to extend our model
with a detector model configuration.

## Extend a model configuration

In this step we modify our detector to extend one of the model
configurations defined in the `gpkg.object-detect` package.

`gpkg.object-detect` supports the following configurations:

[PKG-CONFIG-LIST gpkg/object_detect model-config]

We can apply any of these configurations to our sample detector by
extending it. We use `faster-rcnn-resnet-50` for our detector.

Modify `guild.yml` in the project directory to be:

``` yaml
- model: detector
  description: Sample object detector
  extends:
    - gpkg.object-detect/faster-rcnn-resnet-50
```

Save your changes to `guild.yml`.

By extending `faster-rcnn-resnet-50`, our model inherits its
operations, which support a complete full workflow for building RCNN
object detectors with a ResNet-50 backbone.

List the model operations again:

``` command
guild ops
```

Guild shows the new list of operations, which are inherited from
`faster-rcnn-reset-50`:

``` output
./detector:detect             Detect images using a trained detector
./detector:evaluate           Evaluate a trained detector
./detector:export-and-freeze  Export a detection graph with checkpoint weights
./detector:train              Train detector from scratch
./detector:transfer-learn     Train detector using transfer learning
```

We use these operation to build a trained object detect, running them
as follows:

- `train` or `transfer-learn` to train a model
- `evaluate` to evaluate model performance using validation data
- `detect` to use a trained model to detect objects in am image

Before we can train the model, we need support for a dataset.

## Add dataset support

Train and evaluate operations require a *dataset*. In this section, we
modify our model to include dataset support. Dataset support has two
components:

- A model operation that prepares the dataset for training and
  validation
- Information about the prepared data, including its file format and
  class labels

Dataset support in `gpkg.object-detect` is flexible---you're free to
provide data from any source, provided the data is prepared as TF
Records that are split between training and validation.

For our detector, we add support for images with Pascal VOC formatted
annotations. This type of dataset requires two inputs:

- Directory of JPG, PNG, or GIF images
- Directory of Pascal VOC XML formatted annotations associated with
  the images

To support this scheme, we add
*voc-annotated-images-directory-support* to our model's `extends`
list.

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
    configuration appearing earlier in the list takes precedence over
    configuration appearing later. In the case of our model,
    `voc-annotated-images-directory-support` must appear before
    `faster-rcnn-resnet-50`.

Save your changes to `guild.yml`.

By extending `voc-annotated-images-directory-support` our model
inherits a `prepare` operation.

List model operations:

``` command
guild ops
```

Guild shows the list of operations, which now includes:

``` output
./detector:prepare  Prepare images annotated using Pascal VOC format
```

We use `prepare` to process annotated images, converting them into TF
records that are split between training and validation sets.

Before running `prepare`, we need some annotated images.

## Obtain annotated images

If you have Pascal VOC annotated images, you may use them to train
your detector.

If you don't have images, download one of these datasets:

<table class="table">
  <tr>
    <td>
      <a href="http://www.robots.ox.ac.uk/~vgg/data/pets/">The Oxford-IIIT Pet Dataset</a>
    </td>
    <td>
      <a href="http://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz">images</a><br>
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

!!! note
    You need both images and their associated annotations. If you
    select a dataset that separates images and annotations, ensure
    that you download both source files. If the dataset combines both
    images and annotations, just just need the combined source file.

Once you have the annotated images, note the locations of the image
files (i.e. JPG, PNG, and GIF files) and of the annotations (i.e. XML
files).

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

Press `Enter` to accept the default settings.

Guild runs the operation, which processes the annotated images to
prepare train and validation records.

Once prepared, the dataset is available to any operations that needs
training data (e.g. `train` or `transfer-learn`) or validation data
(e.g. `evaluate`).

Let's take a moment to view the operation results.

When you run an operation, Guild generates a [run](term:run), which is
a file system artifact containing run details, run output, and files
created by the run.

List runs using `guild runs`:

``` command
guild runs
```

Guild shows available runs for the project (IDs and dates will
differ):

``` output
[1:81998e28]  ./detector:prepare  2018-11-02 11:15:25  completed
```

Guild provides a host of run management and discovery features. Refer
to [Runs](/docs/runs) for details.

List files associated with the latest run:

``` command
guild ls
```

Guild shows files associated with the `prepare` operation (files will
differ based on the dataset you prepared):

``` output
~/sample-object-detector/env/.guild/runs/81998e28deba11e8ac6b107b44920855:
  dataset.yml
  deployment/
  labels.pbtxt
  nets/
  object_detection/
  slim/
  train-0001-0941.tfrecord
  train-0942-1898.tfrecord
  train-1899-2833.tfrecord
  train-2834-3568.tfrecord
  val-0001-0973.tfrecord
  val-0974-1528.tfrecord
```

The generated TF records files are those files matching
`train-*.tfrecord` (used for training) and `val-*.tfrecord` (used for
validation). These contain the processed images and annotations.

`dataset.yml` contains information about the prepared dataset,
including the number of processed examples, the number of classes, and
the record storage method.

View `dataset.yml` using the [](cmd:cat) command:

``` command
guild cat dataset.yml
```

Guild shows the contents of `dataset.yml`.

`labels.pbtxt` is a map of annotated object labels to the numeric
values stored in the TF records.

These files are generated by the `prepare` operation and are used by
subsequent operations that need them.

## Train a detector using transfer learning

Having prepared our dataset for training, we're ready to train a
detector.

Our detector supports two train operations:

`train`
: Train the detector from scratch

`transfer-learn`
: Train the detector using transfer learning [^transfer-learning]

[^transfer-learning]:
    See *[A Gentle Introduction to Transfer Learning for Deep Learning
    ->](https://machinelearningmastery.com/transfer-learning-for-deep-learning/)*
    for an overview of transfer learning.

In this guide, we use `transfer-learn`, which saves time and can
improve model accuracy for smaller datasets.

Start the `transfer-learn` operation by running:

``` command
guild run transfer-learn --gpus 0
```

!!! note
    The use of ``--gpus 0`` ensures that the operation only uses
    the first GPU on the system (ID of `0`). If your system has more
    than one GPU, you can use it later when running `evaluate`.

Press `Enter` to accept the default settings and start the operation.

The operation is configured to train indefinitely by default. It's
common practice to let models train indefinitely without prescribing a
fixed number of training steps or epochs. While the operation runs,
you can routinely evaluate its performance and stop the operation when
it's clear that further training is not needed.

You can stop any operation by pressing `Ctrl-C` in the command console
where the operation is running. Alternatively you can run [guild
stop](cmd:runs-stop) from a different command prompt.

## Check model accuracy

While the model trains, we can check its accuracy by running the
`evaluate` operation from a second command prompt.

To evaluate the model during training, open a new command console for
the project:

{!guide-new-project-console.md!}

From the activated project directory, list project runs:

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

Next, run the `evaluate` operation, which evaluates the latest
checkpoint saved by the `transfer-learn` operation (run `1` above)
using the validation data from the latest `prepare` operation (run `2`
above).

If your system only has one GPU, you can't use a GPU for the
`evaluate` operation. In this case, start the operation using the
`--no-gpus` option:

``` command
guild run evaluate --no-gpus
```

Evaluating a model without GPU acceleration can take a long time on
large datasets. To reduce the evaluation time, try setting
`eval-examples` to a number less than 1000. For example:

``` command
guild run evaluate --no-gpus eval-examples=100
```

This measurement is not as comprehensive as using all available
examples (the default setting) but the operation will finish in less
time.

{!stop-run-note.md!}

If your system has more than one GPU, you can use a second GPU for the
`evaluate` operation. In this case, start the operation using the
`--gpus` option:

``` command
guild run evaluate --gpus 1
```

!!! note
    The use of ``--gpus 1`` in the command ensures that the
    operation only sees the second GPU and not try to allocate memory
    on other GPUs. If you don't explicitly control the visible GPUs
    with `--gpus` and `--no-gpus` options, each TensorFlow operation
    preemptively consumes the memory on all visible GPUs, even if
    they're not used.

The evaluate operation uses the validation records from the prepared
dataset to measure model performance. As we are training an object
detector, performance is measured using COCO mAP metrics.[^mAP]

[^mAP]:
    See *[mAP (mean Average Precision) for Object Detection
    ->](https://medium.com/@jonathan_hui/map-mean-average-precision-for-object-detection-45c121a31173)*
    for an overview of measuring accuracy in object detectors.

Each time you run `evaluate`, Guild generates a new run that serves as
a record of your measurement. The run saves accuracy metrics that can
be viewed in TensorBoard and used by other programs.

Use [guild compare](cmd:compare) to view run performance, including
loss and accuracy:

``` command
guild compare
```

You can view run details, including the latest TensorFlow event scalar
values, by navigating to a run using the `Up` and `Down` keys and
pressing `Enter`. Exit the run detail screen by pressing `q`.

Exit Guild Compare by pressing `q`.

While the model continues to train, we monitor its progress with
TensorBoard next.

## Monitor progress with TensorBoard

In this section, we use TensorBoard to monitor the transfer learn
operation and determine when to stop training.

Using a second command console, from the project directory, start
TensorBoard:

``` command
guild tensorboard
```

Guild starts TensorBoard and opens it in a new browser window. Guild
manages TensorBoard so that changes to project runs automatically
appear in TensorBoard.

If you run the `tensorboard` command on a remote server, Guild does
not open TensorBoard in your browser. You must open the link that
Guild shows in the remote command console in your browser manually. If
Guild starts TensorBoard on a port that you cannot access---e.g. due
to firewall restrictions---quit the `tensorboard` command by pressing
`Ctrl-C` and run the command again, specifying a port that you can
access using the `--port` option. For example, if you can access port
`8080` on the remote server, start TensorBoard by running:

``` command
guild tensorboard --port 8080
```

When you have opened TensorBoard in your browser, in the TensorBoard
**Scalars** tab, type or paste the following regular expression into
the **Filter tags** field at the top of the page:

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
at least 10K-20K steps to give the model a chance to transfer
learn. Use `evaluate` (see [Check model
accuracy](#check-model-accuracy) above) to calculate model precision
to confirm before stopping.

When you are finished monitoring the run, in the second command
console---the console where TensorBoard is running---press `Ctrl-C` to
quit TensorBoard.

## Stop training

Stop the transfer learn operation using one of these two methods:

- In the first command console where the `transfer-learn` operation is
  running, press `Ctrl-C`

- Or, in the second command console, use the [stop](cmd:runs-stop)
  command:

``` command
guild stop
```

Press `y` and `Enter` to confirm that you want to stop the
`transfer-learn` operation.

Guild stops the transfer learn operation.

Now that we have a trained object detector, we can use it to detect
objects. First, we need to generate a frozen inference graph.

## Export and freeze a trained model

To use our trained object detector for inference, we need to *export*
the model architecture and *freeze* its weights using a
checkpoint. This process generates a *frozen inference graph*, which
is a binary file used to initialize a trained model in TensorFlow.

Run the `export-and-freeze` command:

``` command
guild run export-and-freeze
```

Press `Enter` to confirm.

By default, Guild uses the latest checkpoint from the latest training
run (i.e. the latest `transfer-learn` operation) to generate the
frozen inference graph.

You can specify different runs or checkpoint steps with
`trained-model` and `step` flags respectively.

To get help for the `export-and-freeze` operation, run:

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

Replace `<run ID>` with the run ID associated with the trained model
and replace `<step>` with the checkpoint step.

To view the available checkpoints for a run using the [](cmd:ls)
command:

``` command
guild ls --operation transfer-learn --path train/model
```

The use of `--operation` tells Guild to list files for the latest
`transfer-learn` operation and the use of `--path` limits the file
listing to the trained model checkpoints.

Checkpoint steps are shown in files named `train/model.ckpt-STEP.*`
where `STEP` is the available checkpoint step.

## Detect objects in an image

With the frozen inference graph generated in the previous section, we
can detect objects in an image.

Create a new directory containing one or more images that you want to
detect.

For this example, we create a directory in `/tmp`---feel free to use
another location.

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

If you are running the command on a remote server, as with
TensorBoard, Guild does not open a window in your browser. You need to
open the link that Guild provides in your browser manually. If you
cannot access the port that Guild uses, specify a port that you can
access using the `--port` option. For example, to run Guild View on
port `8080`, use:

``` command
guild view --port 8080
```

When you have opened Guild View in your browser, click the **FILES**
tab of a `detect` run and click one of the detected images. Guild
opens the image in a file viewer. If the image contains detected
objects, the objects appear in a bounding box with the detected class.

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
~/sample-object-detector/env/.guild/runs/572bdf82df9711e88d57066b64a634d0:
  graph/
  graph/checkpoint
  graph/frozen_inference_graph.pb
  graph/model.ckpt.data-00000-of-00001
  graph/model.ckpt.index
  graph/model.ckpt.meta
  graph/pipeline.config
  graph/saved_model/
  graph/saved_model/saved_model.pb
  graph/saved_model/variables/
```

The first line in the output contains the full path of the run
directory of the latest `export-and-freeze` run.

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

## Summary

In this guide we trained an object detector using a Guild project.

The final Guild project is very simple:

``` yaml
- model: detector
  description: Sample object detector
  extends:
    - gpkg.object-detect/voc-annotated-images-directory-support
    - gpkg.object-detect/faster-rcnn-resnet-50
```

The `detect` model extends two model configurations:
`voc-annotated-images-directory-support` and `faster-rcnn-resnet-50`,
which are both defined in the `gpkg.object-detect` package. These
extensions add various operations to the model that support a workflow
for training, evaluating, and deploying an object detector.
