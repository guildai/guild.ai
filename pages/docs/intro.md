title: Introduction
tags: get-started

# Guild AI introduction

[TOC]

This introduction provides an overview of Guild AI core
functionality. Follow the steps under the each *Example* section below
to get hands-on experience with Guild. By following the examples, you
will implement a Keras image classifier as described in TensorFlow's
*[Train your first neural network: basic classification
->](https://www.tensorflow.org/tutorials/keras/basic_classification)*.

Refer to the [completed
project](https://github.com/guildai/examples/tree/master/fashion) for
the full example.

![Fashion-MNIST](/assets/img/fashion-mnist.png)

^ Fashion-MNIST dataset used in examples below

## Projects

Guild features are be enabled for a TensorFlow or Keras project by
adding a file named `guild.yml` to the project root directory. We
refer to `guild.yml` as a project [Guild file](term:guild-file).

Guild files supplement TensorFlow and Keras projects. You often don't
need to modify your project source files to take advantage of Guild
features.

Guild files are YAML formatted files that define [models](term:model),
model [operations](term:operation), model [resources](term:resource),
[tests](term:test), and [packages](term:package).

### Example

In this example, we create a Guild project that contains a basic model
definition.

If you haven't already done so, [](alias:install-guild).

To create a project, start by creating its directory:

``` command
mkdir sample-project
```

!!! tip
    In any command example, you can click the word *`COMMAND`* in
    the upper right corner to copy the example text to your clipboard,
    which you can paste into your console.

Create the file ``sample-project/guild.yml`` and modify it to be:

``` yaml
- model: fashion
  description: Basic Fashion-MNIST image classifier.
```

!!! tip
    As with command examples, you can click the word *`YAML`* to
    copy the example to your clipboard, which you can paste into your
    text editor.

Save your changes to ``guild.yml``.

Confirm that the project structure is:

<div class="file-tree">
<ul>
<li class="is-folder open">sample-project
 <ul>
 <li class="is-file">guild.yml</li>
 </ul>
</li>
</ul>
</div>

Change to the project directory and use Guild to list the project
models:

``` command
cd sample-project
guild models
```

Guild shows the project models:

``` output
./fashion  Basic Fashion-MNIST image classifier.
```

The value ``./fashion`` is the model source and name. The source
``./`` means that the model is defined in the current directory. Both
the model name and description come from the Guild file you just
created.

Guild model definitions represent the TensorFlow or Keras models in
your project. In the examples that follow, we fill in details to
create a fully functional classifier for the Fashion-MNIST dataset.

## Model operations

Model operations automate model related tasks. A common operation is
*train*, which trains a model from scratch. As we'll see later in this
introduction, operations can be any task that you want to
automate. These may include:

*prepare-data*
: Prepare a dataset for training.

*transfer-learn*
: Train a model using transfer learning.

*finetune*
: Fine tune a trained model.

*evaluate*
: Evaluate a trained model on a test/validation dataset.

*quantize*
: Quantize a trained model to use 8 bit integers.

*predict*
: Use a trained model to make predictions.

*serve*
: Run a trained model as an inference server.

You're free to define the operations that suit your model---Guild does
not prescribe a set of operations that must be supported.

You run an operation using the [](cmd:run) command. As we'll see in
the next section, each operation run is tracked as a separate
experiment.

### Example

If you are following the examples, in this section we add a ``train``
operation to our model and run that operation as an experiment.

Modify ``guild.yml`` to be:

``` yaml
- model: fashion
  description: Basic Fashion-MNIST image classifier.
  operations:
    train:
      description: Train classifier from scratch.
      main: train
```

This change adds a `train` operation to the model with a description
and a main module.

Save your changes to ``guild.yml``.

Use the [operations](cmd:operations) command to list available operations:

``` command
guild operations
```

!!! tip

    You can use `ops` as a short cut to the `operations` command. We use
    `ops` through the rest of this introduction.

Guild displays the newly added `train` operation:

``` output
./fashion:train  Train classifier from scratch.
```

The value ``./fashion:train`` is the full operation name, which
contains the model as well as the operation name.

You can view help for the project using the [](cmd:help) command:

``` command
guild help
```

Guild automatically generates help from the Guild file. This
information is useful for working with the project, especially as it
becomes more complex over time.

Press ``q`` to exit the help screen.

Next, run the operation:

``` command
guild run train
```

Press `Enter` to confirm the operation.

The command fails with the message:

``` error
guild: No module named train
```

This is okay---we expect this error because our project is missing the
`train` module.

Guild operations are implemented using Python main
modules---i.e. Python modules that can be executed as a program (see
[Python help
->](https://docs.python.org/3/using/cmdline.html#cmdoption-m) for
details). Any Python script can therefore be used for a Guild model
operation.

Let's create the missing module.

Download [train.py
->](https://raw.githubusercontent.com/guildai/examples/master/fashion/train.py)
and save it to the project directory. If you have `wget` installed,
you can download the file directly to the project directory by
running:

``` command
wget https://raw.githubusercontent.com/guildai/examples/master/fashion/train.py
```

Confirm that the project structure is now:

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

The `train` module uses Keras to train a simple image classifier. The
module is derived from the [TensorFlow getting started tutorial
Notebook
->](https://github.com/tensorflow/docs/blob/master/site/en/tutorials/keras/basic_classification.ipynb). The
neural network used in `train` consists of three layers:

- Input layer used to read images
- Fully connected hidden layer
- Fully connected output layer used generate image classes

For details on the network architecture, see [Build the model
->](https://www.tensorflow.org/tutorials/keras/basic_classification#build_the_model)
in the TensorFlow basic classification example.

Before we can train our model, we need to install the following Python
packages, which are required by the `train` module:

- matplotlib
- h5py
- numpy

Install those packages using pip:

``` command
pip install matplotlib h5py numpy
```

With the ``train`` module now available, run the operation again:

``` command
guild run train
```

Press `Enter` to confirm the operation.

Guild runs the train operation by executing the ``train`` module as a
program---the operation is implemented by that module.

The operation run is captured as an *experiment*. We examine
experiments in the next section.

## Experiments

Guild tracks each operation run as an isolated experiment that can be
managed and used. Files generated by a run are written to their
associated [run directory](term:run-dir) and can be accessed as normal
files. Guild saves operation metadata, process output, and process
exit status for each run.

Guild provides extensive support for managing and using runs:

- View metadata, files, and output
- List by operation, status, and label
- Delete, restore, and purge
- Export and import
- Tag with custom labels
- Copy to and from remote environments
- Compare run performance
- Diff run metadata, files, and output

Files generated by a run can be used as input to other runs. For
example, model checkpoints saved during a *train* operation can be
used as input to an *evaluate* operation.

For information on managing runs, see [Runs](/docs/runs/).

### Example

If you are following the examples, in this section we use Guild's run
management facility to examine the runs generated in the previous
example.

First, list available runs:

``` command
guild runs
```

Guild shows the two runs from the previous section (dates and IDs will
differ):

``` output
[1:19c67a72]  ./fashion:train  2018-10-16 15:57:32  completed
[2:1451e20c]  ./fashion:train  2018-10-16 15:57:23  error
```

The latest run is listed first and should have a status of
`completed`, indicating that the operation exited without an
error. The previous run is listed second and should have a status of
`error` because the `train` module was not originally available (see
previous section).

Next, show output for the failed run:

``` command
guild runs info --output 2
```

The option ``--output`` tells Guild to include run output. The value
``2`` tells Guild to show information for the run with index `2` (see
listing above).

Guild shows information for the failed run (dates and IDs will
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

Next, delete the failed run (we don't need it):

``` command
guild runs rm 2
```

As with the `runs info` command, the value ``2`` is a reference to the
second run in the list.

Guild prompts you before deleting the run. Press `Enter` to
confirm. After deleting the run, you can verify that it was deleted by
running ``guild runs``.

If you make a mistake and delete a run by accident, you can restore it
using [runs restore](cmd:runs-restore). For a list of deleted runs,
use ``guild runs --deleted``.

Next, view the files generated by the successful run:

``` command
guild ls
```

We can omit a reference to the run in this case---Guild assumes you
want to show files for the latest run.

Guild show these files (file names will differ):

``` output
~/.guild/runs/7d230c98d20811e88f52d017c2ab916f:
  events.out.tfevents.1539779455.local
  weights-0001-13.233.hdf5
  weights-0002-13.080.hdf5
  weights-0003-13.031.hdf5
  weights-0004-12.996.hdf5
  weights-0005-13.007.hdf5
```

These are the log file and trained model weights. Guild tracks these
files along with all other run related metadata.

!!! tip

    By default [](cmd:ls) shows relative file paths. You can show full
    paths by including the `-f` option. This is useful if you need to
    access a particular file on the file system.

Guild provides a number of commands for viewing runs. Try any of these
commands from the `sample-project` directory:

``guild view``
: Open [Guild View](term:guild-view).

``guild tensorboard``
: View TensorFlow event logs in [TensorBoard](term:tensorboard).

``guild runs info``
: Show basic run information (try ``guild runs info --help`` for a
  list of options).

``guild open``
: Open the run directory in your system file browser.

!!! note

    For the commands ``guild view`` and ``guild tensorflow``, you must
    press `Ctrl-C` in the console to quit the application and return to a
    command prompt.

![Fashion MNIST in TensorBoard](/assets/img/fashion-tb.png)

^ Fashion MNIST in TensorBoard

## End-to-end workflow

Guild operations automate model related tasks. While *train* is a
common operation, it's not the only operation a model may support. For
example, prior to training a model, you may need to prepare a dataset
by processing raw data into a format that can be used efficiently for
training and validation. Your model may therefore have a
*prepare-data* operation that automates that task. Similarly, after
training you may need to evaluate a trained model with test or
validation data---your model may have an *evaluate* operation.

By running various operations, you use Guild to automate your
workflow.

Consider the following worflow, which generates TensorFlow Lite files
for deployment to mobile devices:

<img class="md" style="width:400px" src="/assets/img/workflow-2.png">

Each step can be automated using an operation:

- Before training a model, run `prepare-data`, which loads raw data
  from a database and processes it using various transformations. You
  can use operation [flags](term:flag) to specify which
  transformations should apply and how examples should be split
  between train and validate.

    ```
    $ guild run prepare-data transforms=all validation-split=20
    ```

- Once the data is prepared, run `train`. This is a "train from
  scratch" operation, which means that model weights are initialized
  with their starting values (e.g. randomly generated) without the
  benefit of prior training. This is typically a long-running
  operation that can take several hour or even days. As with
  `prepare-data` you can use flags to specify training parameters such
  as learning rate.

    ```
    $ guild run train learning-rate=0.001
    ```

- As the model trains, run `evaluate` to check its status. This can be
  a time consuming operation, depending on how thorough the evaluation
  is. Run it alongside the train operation without having to stop
  training.

    ```
    $ guild run evaluate
    ```

- Once a model is trained, you can fine-tune it with additional
  training---but with different parameters, such as a lower learning
  rate. You run `finetune`, which initializes the model weights with
  the values from a previous `train` operation. As with `train` you
  can check progress by running `evaluate` and stop operation when
  model accuracy is no longer improving.

    ```
    $ guild run finetune learning-rate=0.0001
    ```

- When it's time to deploy a trained model for use in a mobile
  application, run the `tflite` operation to generate a [TF Lite
  ->](https://www.tensorflow.org/lite/) file. The operation uses the
  learned weights from the `finetune` operation to create a frozen
  inference model and corresponding TF Lite file.

    ```
    $ guild run tflite
    ```

This is just one example of a model workflow. Your workflow will be
different based on the type of model and the applications you build
with it.

### Example

If you are following the examples, in this section we add a `predict`
operation to our Fashion-MNIST model. With the addition of this
operation, our model supports this simple workflow:

<img class="md" style="width:220px" src="/assets/img/workflow-3.png">

Modify ``guild.yml`` to be:

``` yaml
- model: fashion
  description: Basic Fashion-MNIST image classifier.
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
`predict`. Resources are used to resolve source files needed by an
operation. In this example, the `predict` operation needs files
generated by the `train` operation.

Here's how it works:

- `predict` requires `trained-model`, which means that all of the
  sources defined for the `trained-model` resource must be available
  to the `predict` operation when `predict` is run.

- The `trained-model` resource defines a single *source*, which is the
  output generated by the `train` operation.

- The `trained-model` resource *path* is ``model``, which means that
  each of source files are located in the `model` run subdirectory of
  requiring operations.

- When `predict` runs, it looks for trained model files in a run
  subdirectory named `model`. It uses these to initialize the model
  variables before making any predictions.

Next, we need to create the `predict` module. We'll download it along
with a second module `fig`, which is required by `predict`.

Download the following two files and save them to ``sample-project``:

[predict.py ->](https://raw.githubusercontent.com/guildai/examples/master/fashion/predict.py)
: The `predict` module.

[fig.py ->](https://raw.githubusercontent.com/guildai/examples/master/fashion/fig.py)
: A module required by `predict`.

If you are using `wget` you can download the file directly to the
project directory by running:

``` command
wget https://raw.githubusercontent.com/guildai/examples/master/fashion/predict.py
wget https://raw.githubusercontent.com/guildai/examples/master/fashion/fig.py
```

When the required files are downloaded, your project structure should
be:

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

Next, generate predictions by running `predict`:

``` command
guild run predict
```

Press `Enter` to confirm.

Guild runs the operation, which selects five images at random from the
Fashion-MNIST test dataset and classifies them using the trained
model. The prediction for each image is plotted in a `png` file
located in the operation run directory.

To view the generated files from the `predict` operation, run:

``` command
guild ls
```

Guild shows these files (file names will differ):

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

Each `png` file is an image generated by the `predict` operation.

The files under the `models` subdirectory
(e.g. `model/weights-*.hdf5`) are generated by the previous `train`
operation. The `predict` operation uses these files to initialize the
model weights. Guild makes these files available when it resolves the
`trained-model` resource.

You can view generated predict images using Guild View:

``` command
guild view
```

Clicking the **FILES** tab, and then click one of the `png` files.

<img class="md" style="width:660px" src="/assets/img/guild-view-predict.png">

^ Sample predicted image from Guild View

Press `Ctrl-C` in the console to quit Guild View and return to a
command prompt.

Alternatively, run `guild open` to view the run directory in you
system file browser. From there you can open images in the image
viewer of choice.

If the model misclassifies an image, the image name contains the text
``error``. Your run may not have errors as the images are randomly
selected---try running the operation a few more times to see if the
model misclassifies an image.

## Model tests

Guild provides a test facility to verify model behavior. The primary
method of testing is to run operations and to check the contents of
generated files.

For more information, see [Tests](term:test).

### Example

If you are following the examples, in this section we add a test to
our project that can be run to verify model behavior.

Modify ``guild.yml`` to be:

``` yaml
- model: fashion
  description: Basic Fashion-MNIST image classifier.
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

- test: fashion
  steps:
    - run: train
    - run: predict
```

This adds a *test* named `fashion` to the Guild file, which is used to
check the model's `train` and `predict` operations. If the operations
complete successfully the test will pass, otherwise it will fail.

Save your changes to `guild.yml`.

Next, run the test:

``` command
guild test
```

Press `Enter` to confirm.

Guild runs `train` and `predict`---the operations should complete
without error and Guild shows ``All tests passed``.

## Packages

Guild supports packaging and distribution your models, which allow
others to use your models by simply installing a package. Once
installed, packaged models and their operations are available just
like project models.

You can install and use models developed by others.

For more information, see [Packages](term:package).

### Example

If you're following the examples, in this section we package our model
for use by others.

Modify `guild.yml` to be:

``` yaml
- model: fashion
  description: Basic Fashion-MNIST image classifier.
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

- test: fashion
  steps:
    - run: train
    - run: predict

- package: fashion
  version: 1.0
  requires:
    - matplotlib
    - h5py
    - numpy
```

This adds a `package` element to `guild.yml` that provides information
Guild uses to generate a package. We include the list of required
packages to ensure that those packages are available when our package
is installed.

Next, create a package by running:

``` command
guild package
```

Guild creates a file `dist/fashion-1.0.0-py2.py3-none-any.whl`. This
is a Python [distribution archive
->](https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives)
that is used to install the fashion model.

You can distribute this file to friends and colleagues who want to use
your model. For example, upload the package as a [release on GitHub
->](https://help.github.com/articles/creating-releases/).

To install the package, a user runs [guild install](cmd:install),
specifying the path to `fashion-1.0.0-py2.py3-none-any.whl`.

### Install and use packaged model (optional)

The steps in this section are optional---follow them to experiment
with your packaged model.

To simulate a user's experience when installing and using your
packaged model, create a [Python virtual environment
->](https://docs.python.org/3/tutorial/venv.html) that isolates the
package and its requirements. Use a temporary environment directory
(you can delete the directory after you complete the steps below):

``` command
virtualenv /tmp/sample-package-test
```

Next, activate the virtual environment:

``` command
source /tmp/sample-package-test/bin/activate
```

Within the activated virtual environment, install Guild AI,
TensorFlow, and the `fashion` package:

``` command
pip install guildai tensorflow dist/fashion-1.0-py2.py3-none-any.whl
```

Change to the environment directory:

``` command
cd /tmp/sample-package-test
```

!!! note

    The last step is not required to use the installed `fashion`
    package. However, by changing out of the project directory
    (i.e. `sample-project`) you avoid displaying its Guild file contents
    in the commands below.

With the `fashion` package installed, list available models:

``` command
guild models
```

Guild shows the available models:

``` output
fashion/fashion  Basic Fashion-MNIST image classifier.
```

The value ``fashion/fashion`` is the full model name including the
model source. In this case the model is defined in the ``fashion``
package.

Next, show available operations:

``` command
guild ops
```

Guild shows the model operations, again indicating that they are
defined in the ``fashion`` package:

``` output
fashion/fashion:predict  Use trained model to make predictions.
fashion/fashion:train    Train classifier from scratch.
```

Next, test the model---this runs both the `train` and `predict`
operations:

``` command
guild test fashion
```

In this case you must specify the package to test.

Press `Enter` to continue. Guild runs the two operations associated
with test.

When the two operations are completed, you may use the various Guild
run management commands to view the results.

List runs:

``` command
guild runs
```

Use Guild View to explore the run files, including prediction images:

``` command
guild view
```

Press `Ctrl-C` to quit Guild View and return to a command prompt.

Use TensorBoard to view training logs:

``` command
guild tensorboard
```

Press `Ctrl-C` to quit TensorBoard and return to a command prompt.

These steps simulate a user's experience when installing and using
your Fashion-MNIST image classifier. Once you package your model, you
need only distribute the package archive
(e.g. `fashion-1.0.0-py2.py3-none-any.whl`) to users for them to
install and use your model.

## Summary

In this introduction we present Guild AI core functionality with
step-by-step examples for hands-on experience with the toolset.

Guild AI supports TensorFlow and Keras model automation and provides a
comprehensive set of features to improve developer productivity and
facilitate model reuse for application development.

Guild models can be both project based and package based. Project
based models are defined in Guild files (i.e. files named `guild.yml`)
that reside in a project root directory. Guild files contain model
definitions, including operations and resources used by
operations. Guild files can also contain tests and package
definitions.

Guild packages are used to distribute models to other users. Packages
are standard Python package archives that can be installed with
pip. Package dependencies (e.g. `numpy`, `matplotlib`, etc.) are
automatically installed with Guild packages, ensuring that operations
work without additional installation steps.

Guild supports experiment tracking and management. Experiments are
created for each operation runs and can be viewed in various ways
using Guild commands, including visualization tools for exploring runs
and training logs.

### Next steps

- [More step-by-step guides](/docs/guides/)
- [Browse Guild AI documentation](/docs/)
