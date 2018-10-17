title: Introduction
tags: concepts

# Guild AI introduction

[TOC]

This introduction provides an overview of Guild AI core
functionality. Feel free to follow the steps under each **Example**
section below to get hands-on experience with Guild. The examples
implement the Keras image classifier described in TensorFlow's *[Train
your first neural network: basic classification
->](https://www.tensorflow.org/tutorials/keras/basic_classification)*. Refer
to the [completed
project](https://github.com/guildai/examples/tree/master/fashion) for
the full example.

![Fashion MNIST](/assets/img/fashion-mnist.png)

^ Fashion MNIST images used in examples below

Before running any of the steps below, first [](alias:install-guild).

## Guild projects

A Guild project is a standard TensorFlow or Keras source code project
that contains a file named `guild.yml` in the root directory. We refer
to `guild.yml` as a project [Guild file](term:guild-file).

Guild files supplement TensorFlow and Keras projects. You often don't
need to modify your project source files to take advantage of Guild
features.

Guild files are YAML formatted files that define [models](term:model),
model [operations](term:operation), [resources](term:resource), and
[packages](term:package).

### Example

In this example, we create a simple Guild project that will serve as
the basis for other examples in this introduction.

Start by creating a project directory:

``` command
mkdir sample-project
```

Create a file ``sample-project/guild.yml`` and modify it to be:

``` yaml
model: fashion
description: Basic fashion MNIST image classifier.
```

Save your changes to ``guild.yml``. Confirm that the project structure
is:

<div class="file-tree">
<ul>
<li class="is-folder open">sample-project
 <ul>
 <li class="is-file">guild.yml</li>
 </ul>
</li>
</ul>
</div>

Change to the project directory and list the project models:

``` command
cd sample-project
guild models
```

Guild displays the project models:

``` output
./fashion  Basic fashion MNIST image classifier.
```

Guild models represent the models in your project. In this case, we're
developing a model that predicts the class of an image from the MNIST
fashion dataset. The project is only a skeleton at this point---we
fill in the details in subsequent examples.

## Model operations

Model operations automate model related tasks. A common operation is
`train`, which trains a model from scratch. As we'll see later in this
introduction, operations can be any task that you want to
automate. These might include:

`prepare-data`
: Prepare a dataset for training.

`transfer-learn`
: Train a model using transfer learning.

`finetune`
: Fine tune a trained model.

`evaluate`
: Evaluate a trained model on a hold-out dataset.

`predict`
: Use a trained model to make predictions.

`serve`
: Run a trained model as an inference server.

You're free to define the operations that suit your model---Guild does
not prescribe what a model should or should not support.

Once you define an operation, you run it using the [](cmd:run)
command. As we'll see in the next section, each operation run is
tracked as a separate experiments.

### Example

If you are following the examples, in this section we add a ``train``
operation to our model and run it as an experiment.

Modify ``guild.yml`` to be:

``` yaml
model: fashion
description: Basic fashion MNIST image classifier.
operations:
  train:
    description: Train classifier from scratch.
    main: train
```

In this case, we add a `train` operation with a description and a main
module. We'll see what this means shortly.

Save your changes to ``guild.yml``.

We can use the [ops](cmd:operations) command to list available operations:

``` command
guild ops
```

Guild displays the newly added `train` operation:

``` output
./fashion:train  Train classifier from scratch.
```

You can also view help for the project using the [](cmd:help) command:

``` command
guild help
```

Guild automatically generates help from the Guild file. This
information is useful for effectively working with the project,
especially as it evolves and becomes more complex.

Now that we've defined our train operation, let's run it:

``` command
guild run train
```

Press `Enter` to confirm the operation.

The command fails with the message:

``` output
guild: No module named train
```

That's okay---we expect this error because our project is missing an
important component: the `train` module!

Guild operations are implemented using Python main
modules---i.e. modules that can be executed as a program using
Python's `-m` option (see [Python help
->](https://docs.python.org/3/using/cmdline.html#cmdoption-m) for more
information). This means that any Python script can be used for a
Guild model operation.

Let's create the missing module.

Download [train.py
->](https://raw.githubusercontent.com/guildai/examples/master/fashion/train.py)
and save it to the project directory. If you have `wget` installed,
you can download the file directly to the project directory by
running:

``` command
wget https://raw.githubusercontent.com/guildai/examples/master/fashion/train.py
```

Confirm that the project structure is:

<div class="file-tree">
<ul>
<li class="is-folder open">sample-project
 <ul>
 <li class="is-file">guild.yml</li>
 <li class="is-file">train.py</li>
 </ul>
</li>
</ul>
</div>

The `train` module uses Keras to train a simple image classifer. The
module is derived from the [TensorFlow getting started
tutorial](https://github.com/tensorflow/docs/blob/master/site/en/tutorials/keras/basic_classification.ipynb)
and requires a few additional Python packages:

- matplotlib
- h5py
- numpy

Install those packages now:

``` command
pip install matplotlib h5py numpy
```

Now that ``train.py`` is available, along with its required Python
packages, run the operation again:

``` command
guild run train
```

Press `Enter` to confirm the operation.

Guild runs the train operation by executing ``train.py`` as a Python
main module---the operation is implemented entirely by that
module. Guild however executes the module in a new directory for each
run. We learn more about that in the next section.

## Experiments

Guild tracks each operation run as an isolated experiment using [run
directories](term:run-dir). Files generated by a run are written to a
unique directory and can be accessed as normal files.

Guild provides extensive support for managing and using runs:

- Show run information, including metadata, files, and output
- List by operation, status, and label
- Delete, restore, and purge
- Export and import
- Tag with custom labels
- Push to and pull from remote environments
- Compare run performance
- Diff run metadata, files, and output

For more information about managing runs, see [Runs](/docs/runs/).

### Example

If you are following the examples, in this section we use Guild's run
management facility to examine the runs generated in the previous
section.

List available runs by running:

``` command
guild runs
```

Guild displays the runs so far. You should see two (dates and IDs will
differ):

``` output
[0:19c67a72]  ./fashion:train  2018-10-16 15:57:32  completed
[1:1451e20c]  ./fashion:train  2018-10-16 15:57:23  error
```

The latest run, which is listed first, should have a status of
**completed**, indicating that the operation exited without an
error. The prior run, which is listed second, should have a status of
**error** because the `train` module was not originally available (see
the example above).

Show output for the failed run:

``` command
guild run info --output 1
```

The option ``--output`` tells Guild to include run output. The value
``1`` tells Guild to show information for the run with index ``1``
(see listing above).

You should see information for the failed run (dates and IDs will
differ):

``` output
id: 1451e20cd18611e88f52d017c2ab916f
operation: ./fashion:train
status: error
started: 2018-10-16 15:57:23
stopped: 2018-10-16 15:57:23
run_dir: ~/.guild/runs/1451e20cd18611e88f52d017c2ab916f
command: /usr/bin/python -um guild.op_main train
exit_status: 1
pid:
output:
  guild: No module named train
```

Note the error message in the output. This information is retained as
a part of the tracked experiment.

Let's delete the failed run:

``` command
guild runs rm 1
```

Guild will prompt you before deleting the run. Press `Enter` to
confirm. After deleting the run, you can verify that it was deleted by
running ``guild runs``.

If you make a mistake and delete a run by accident, you can restore it
using [runs restore](cmd:runs-restore).

Let's view the files generated by the successful run:

``` command
guild ls
```

Guild displays these file (IDs and timestamps will differ):

``` output
~/.guild/runs/7d230c98d20811e88f52d017c2ab916f:
  events.out.tfevents.1539779455.local
  weights-0001-13.233.hdf5
  weights-0002-13.080.hdf5
  weights-0003-13.031.hdf5
  weights-0004-12.996.hdf5
  weights-0005-13.007.hdf5
```

These are the operation logs and trained model weights for each
training epoch. They are valuable files---are the output of our
training experiment! Guild tracks them along with all other run
related metadata.

By default the [](cmd:ls) command shows relative file paths for the
latest run. You can show full paths by including the ``-f``
option---this is useful if you want to access a particular file on the
file system.

Guild provides a number of commands to help you view and understand
runs. Try running any of these commands:

``guild view``
: Open the Guild View application.

``guild tensorboard``
: View TensorFlow event logs in TensorBoard.

``guild runs info``
: Show basic run information (try ``guild runs info --help`` for a
  list of additional options).

``guild open``
: Open the run directory in your system file browser.

## End-to-end workflow

Guild operations are used to automate any model related task. While
`train` is a common operation, it is not typically the only operation
that a model supports. Prior to training a model, for example, you
might need to prepare a dataset---i.e. process raw data input into a
format that can be used efficiently for training. Your model might
therefore have a `prepare-data` operation. Similarly, after training
you might need to evaluate a model using a hold-out dataset. You would
add an `evaluate` operation.

The set of operations supported by a model are used to automate
*workflow*.

Consider this sample workflow.

<img style="width:400px" src="/assets/img/workflow-2.png">

- Before you train your model, you run `prepare-data`, which loads raw
  data from a database and processes it using a variety of
  transformation. You can use operation [flags](term:flag) to specify
  which transformations should apply and even how the examples should
  be split between train and validate.

- Once the data is prepared, you train the model by running
  `train`. This is a "train from scratch" operation, which means that
  model weights are initialized with their starting values
  (e.g. randomly generated) without the benefit of prior
  training. This is typically a long running operation that can take
  several hour or even days. As with `prepare-data` you can use flags
  to specify training parameters such as learning rate.

- As the model trains, you run `evaluate` to check its status. This
  can be a time consuming operation, depending on how thorough the
  evaluation is. You run it alongside the train operation so as to not
  slow down model training. You may decide to automate this step and
  stop training early if it's not progressing.

- Once your model is trained, you decide to fine tune it with more
  training---but this time with a lower learning rate. You run
  `finetune`, which initializes the model weights with the values
  from the earlier `train` operation. As with `train` you check in on
  the training by running `evaluate` and stop when the model is no
  longer progressing.

- Finally, it's time to deploy your model, which will be used in a
  mobile application running [TensorFlow Lite
  ->](https://www.tensorflow.org/lite/). You run the `tflite`
  operation to generate a TF Lite file. The operation uses the learned
  weights from the `finetune` operation to create a frozen inference
  model and the corresponding TF Lite file.

This is just one example of a model workflow. Your workflow will be
different based on the type of model and the applications you build
with it.

### Example

If you are following the examples, in this section we add two new
operations to our sample model:

`prepare-data`
: Prepares the fashion MNIST images for training and prediction.

`predict`
: Uses a trained model to make predictions using test images.

With the addition of these operations, our model supports this simple
workflow:

<img style="height:60px" src="/assets/img/workflow-3.png">

Modify ``guild.yml`` to be:

``` yaml
model: fashion
description: Basic fashion MNIST image classifier.
operations:
  train:
    description: Train classifier from scratch.
    main: train
  predict:
    description: Use trained model to make predictions.
    main: predict
    requires: trained-model
resources:
  trained-model:
    path: model
    sources:
      - operation: train
```

This adds a new operation `predict`. It also adds a
[resource](term:resource) named `trained-model`, which is required by
`predict`.

- `predict` requires `trained-model`, which means that all of the
  sources defined for the `trained-model` resource are made available
  to the `predict` operation under the resource path when `predict` is
  run.

- The `trained-model` resource defines one source, which is the output
  generated by the `train` operation. The resource path is `model`,
  which means that each of the resolved source files are located in
  the `model` run subdirectory of requiring operations.

- When `predict` runs, it looks for trained model files in the `model`
  run subdirectory. It uses these to initialize the model variables
  before making any predictions.

Now that we've defined the new `predict` operation, let's download the
Python modules that implement the operation.

Download the following two files and save them to ``sample-project``:

[predict.py ->](https://raw.githubusercontent.com/guildai/examples/master/fashion/predict.py)
: Support for making predictions on test images using a trained model.

[fig.py ->](https://raw.githubusercontent.com/guildai/examples/master/fashion/fig.py)
: Support for generating plots---use by both `prepare_data` and `predict`.

If you are using `wget` you can run these commands from the
`sample-project` directory:

``` command
wget https://raw.githubusercontent.com/guildai/examples/master/fashion/predict.py
wget https://raw.githubusercontent.com/guildai/examples/master/fashion/fig.py
```

When all of the required files are downloaded, your project structure should be:

<div class="file-tree">
<ul>
<li class="is-folder open">sample-project
 <ul>
 <li class="is-file">fig.py</li>
 <li class="is-file">guild.yml</li>
 <li class="is-file">predict.py</li>
 <li class="is-file">train.py</li>
 </ul>
</li>
</ul>
</div>

Save your changes to `guild.yml` and confirm that the new operations
are available:

``` command
guild ops
```

Guild now displays two operations:

``` output
./fashion:predict       Use trained model to make predictions.
./fashion:train         Train classifier from scratch.
```

Let's generate some sample predictions by running `predict`:

``` command
guild run predict
```

Confirm the operation by pressing `Enter`.

Guild runs the operation, which selects five images at random from the
fashion MNIST test dataset and classifies them using the trained
model. The result for each image is displayed in a PNG located in the
operation run directory.

To view the generated files from the `predict` operation, run:

``` command
guild ls
```

Guild shows a list of files that look like this (some file names will
differ):

``` output
~/.guild/runs/bae908a4d25111e88f52d017c2ab916f:
  00618.png
  03100.png
  03975.png
  07868-error.png
  09807.png
  model/
  model/events.out.tfevents.1539810834.dakota
  model/weights-0001-0.494.hdf5
  model/weights-0002-0.373.hdf5
  model/weights-0003-0.332.hdf5
  model/weights-0004-0.310.hdf5
  model/weights-0005-0.292.hdf5
```

Each `*.png` file is an image generated by the `predict`
operation. You can view the images by running `guild view`, clicking
**Files**, and then clicking one of the generated image files.

![Sample predicted image](/assets/img/guild-view-predict.png)

^ Sample predicted image from Guild View

Alternatively, run `guild open` to view the run directory in you
system file browser. From there you can open each of the images in you
image viewer of choice.

If the model misclassifies an image, the image name contains
``error``. Your run may not contain any errors as the images
are randomly selected. Try running the operation a few more times to
see if the model misclassifies an image.

## Model tests

## Packages and code reuse
