tags: start

# Add a Classifier

[TOC]

## Overview

In the [previous section](/start/guildfile.md), you use a Guild file
to define a `train` operation. In this section, you enhance the
project by adding a real-world classifier.

You learn how to:

- Support multiple [models](term:model) in a single project
- Use Guild [environments](term:environment) to isolate project work

## Download Classifier Script

[Download
`plot_iris_exercise.py`](ext:https://raw.githubusercontent.com/guildai/examples/master/iris-svm/plot_iris_exercise.py)
and save it to the `guild-start` directory.

The script [^iris-script] trains a model on the Iris benchmark data set.

[^iris-script]: The classifier added in this section is adapted from
[*scikit-learn SVM Exercise*
->](https://scikit-learn.org/stable/auto_examples/exercises/plot_iris_exercise.html)

The `guild-start` directory should look like this:

<div class="file-tree">
<ul>
<li class="is-folder open">guild-start
 <ul>
 <li class="is-folder">archived-runs</li>
 <li class="is-file">guild.yml</li>
 <li class="is-file">plot_iris_exercise.py</li>
 <li class="is-file">train.yml</li>
 </ul>
</li>
</ul>
</div>

## Add `iris-svm` Model to guild.yml

In the `guild-start` directory, modify `guild.yml` by adding the
`iris-svn` model below.

The final modified `guild.yml` should be:

``` yaml
- model: sample
  description: A sample model
  operations:
    train:
      description: Sample training script
      main: train
      flags-dest: globals
      flags-import:
        - noise
        - x
      output-scalars: '(\key): (\value)'

- model: iris-svm
  description: Iris classifier using a support vector machine (SVM)
  operations:
    train:
      description: Train SVM model on Iris data set
      main: plot_iris_exercise
      flags:
        kernel:
          description: SVM kernel type
          default: rbf
          choices: [linear, poly, rbf]
        test_split:
          description: Percentage of examples held out for test
          default: 0.2
        random_seed:
          description: Seed used for shuffling data
          default: 0
        degree:
          description: Degree of the poly kernel function
          default: 3
        gamma:
          description: Kernel coefficient for rbf and poly
          default: 10
      output-scalars:
        train_accuracy: 'Train accuracy: (\value)'
        test_accuracy: 'Test accuracy: (\value)'
```

^ `guild.yml` after adding `iris-svm` model

Note the changes to `guild.yml`:

- The format changes from a mapping of operations to a list of
  top-level objects. Guild supports these two formats for Guild files:
  [operation only format](term:operation-only-format) and [full
  format](term:full-format).

- The file defines two models: `sample` and `iris-svm`. The `sample`
  model defines the `train` operation from the [previous
  step](/start/guildfile.md). The `iris-svm` is a new model, which you
  add in this section.

Verify that the two operations are available:

``` command
guild ops
```

``` output
iris-svm:train  Train SVM model on Iris data set
sample:train    Generate a sample loss
```

If you don't see `iris-svm:fit` in the list above, verify that
`guild.yml` is the same as above and that you're running the command
from `guild-start`.

Show the project models:

``` command
guild models
```

``` output
iris-svm  Iris classifier using a support vector machine (SVM)
sample    A sample model
```

Finally, show help for the project:

``` command
guild help
```

``` output
OVERVIEW

    You are viewing help for operations defined in the current directory.

    To run an operation use 'guild run OPERATION' where OPERATION is one
    of options listed below. If an operation is associated with a model,
    include the model name as MODEL:OPERATION when running the operation.

    To list available operations, run 'guild operations'.

    Set operation flags using 'FLAG=VALUE' arguments to the run command.
    Refer to the operations below for a list of supported flags.

    For more information on running operations, try 'guild run --help'.
    For general information, try 'guild --help'.

MODELS

    iris-svm

      Iris classifier using a support vector machine (SVM)

      Operations:

        train
          Train SVM model on Iris data set

          Flags:
            degree       Degree of the poly kernel function (default is 3)
            gamma        Kernel coefficient for rbf and poly (default is 10)
            kernel       SVM kernel type (default is rbf)

                         Choices:  linear, poly, rbf

            random_seed  Seed used for shuffling data (default is 0)
            test_split   Percentage of examples held out for test (default is 0.2)

    sample

      A sample model

      Operations:

        train
          Sample training script

          Flags:
            noise  (default is 0.1)
            x      (default is 0.1)

```

!!! highlight
    Update your project Guild file to reflect your project
    features. This is not just useful documentation. You can *run*
    each operation to generate experiments.

## Create a Guild Environment

Up to this point, you run experiments in the default Guild
environment, which stores runs under your user directory.

In this section, we create a project-specific environment to keep
project libraries and runs separate from other projects. See [*Use
project specific virtual
environments*](/guides/tips-and-techniques.md#use-project-specific-virtual-environments)
in [Tips & Techniques](/guides/tips-and-techniques.md) for the
rationale for using project environments.

### Create `requirements.txt`

Guild uses `requirements.txt` to install required packages when
creating an environment.

In the `guild-start` project directory, create a file named
`requirements.txt` that specifies the Python packages required by the
project. `requirements.txt` should be:

``` txt
matplotlib
scikit-learn
```

^ `requirements.txt` --- specifies Python packages required by the
project

Your project directory should look like this:

<div class="file-tree">
<ul>
<li class="is-folder open">guild-start
 <ul>
 <li class="is-folder">archived-runs</li>
 <li class="is-file">guild.yml</li>
 <li class="is-file">plot_iris_exercise.py</li>
 <li class="is-file">requirements.txt</li>
 <li class="is-file">train.yml</li>
 </ul>
</li>
</ul>
</div>

### Initialize the Environment

Initialize the environment using [init](cmd:init):

``` command
guild init
```

Guild prompts with the environment settings. Press `Enter` to create
the environment.

Guild initializes a virtual environment in the project under a `venv`
subdirectory.

Your project directory should look like this:

<div class="file-tree">
<ul>
<li class="is-folder open">guild-start
 <ul>
 <li class="is-folder">archived-runs</li>
 <li class="is-folder">venv</li>
 <li class="is-file">guild.yml</li>
 <li class="is-file">plot_iris_exercise.py</li>
 <li class="is-file">requirements.txt</li>
 <li class="is-file">train.yml</li>
 </ul>
</li>
</ul>
</div>

### Activate the Environment

To use an environment, you must *activate* it within each terminal
session that uses it.

Activate the environment:

``` command
source guild-env
```

When you activate an environment, software libraries and runs are
isolated within the environment.

The command prompt is modified to reflect the activated environment.

!!! note
    You can alternatively use the traditional method, which is to
    source the virtual environment script `bin/activate` --- for
    example, by running ``source venv/bin/activate``.

Verify that the environment is activated using [check](cmd:check):

``` command
guild check
```

Note the location of ``guild_home`` --- it should be under the project
directory in ``venv/.guild``.

List the current runs:

``` command
guild runs
```

The list is empty beause you haven't generated any runs in current
environment.

## Train the Classifier

In the activated environment, run the `iris-svm:train` operation:

``` command
guild run iris-svm:train
```

``` output
You are about to run iris-svm:train
  degree: 3
  gamma: 10
  kernel: rbf
  random_seed: 0
  test_split: 0.2
Continue? (Y/n)
```

Press `Enter` to start the operation.

Guild runs the operation, which is implemented by the
[`plot_iris_exercise` Python module
->](https://raw.githubusercontent.com/guildai/examples/master/iris-svm/plot_iris_exercise.py).

Guild uses the default flag values defined for the operation in
`guild.yml` (see above).

Run `mnist-svm:train` again using each of the other kernels:

``` command
guild run iris-svm:train kernel=[linear,poly]
```

``` output
You are about to run iris-svm:train as a batch (2 trials)
  degree: 3
  gamma: 10
  kernel: [linear, poly]
  random_seed: 0
  test_split: 0.2
Continue? (Y/n)
```

Press `Enter` to confirm.

Guild runs `iris-svm:train` twice --- once for each specified kernel.

## Compare Runs

Use [compare](cmd:compare) to list results:

``` command
guild compare
```

Use the arrow keys to scroll to the right and view the values for
`test_accuracy`. Note that the `linear` kernel performs better the
other two, at least with the default hyperparameters.

Press `q` to exit Guild Compare.

## Summary

In this section you added a new model `iris-svm` to your project. The
model defines a `train` operation, which runs the Python module
`plot_iris_exercise` to fit a support vector machine to the Iris data
set.

In the next section, you add a new operation to `iris-svm` that
automates a more complete search.
