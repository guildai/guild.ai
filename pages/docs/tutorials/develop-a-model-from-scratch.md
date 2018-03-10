tags: tutorial, developer

# Develop a model from scratch

[TOC]

In this tutorial, we'll develop a model with Guild AI from
scratch. We'll follow this general process:

- Create a training script skeleton
- Implement a model using one of the available TensorFlow model APIs
- Obtain a training dataset
- Iteratively train, evaluate and improve the model

Our final goal is a trained model that predicts classes from the Iris
dataset. We'll use the model architecture outlined in [Getting Started
with TensorFlow
->](https://www.tensorflow.org/get_started/premade_estimators).

## Requirements

This tutorial assumes the following:

- Guild AI is [installed and verified](/install)
- Your [virtual environment is activated](alias:virtualenv-activate)
  (if applicable)
- You have a working Internet connection

While not required, we recommend using a dedicated virtual environment
for this tutorial. To setup your environment, see
[](alias:tut-env-setup).

## Initialize a Guild AI project

Guild projects are directories that contain a [Guild
file](term:guild-file) --- i.e. a file named `guild.yml`. A Guild file
contains information used to train models.

Let's create a new Guild project for our iris classifier by running:

``` command
guild init --project iris
```

Guild asks you to confirm the operation. Press `ENTER` to initialize
the new project.

The commands creates a new directory:

<div class="file-tree">
<ul>
<li class="is-folder open">./iris <i>Project directory</i>
 <ul>
 <li class="is-file">guild.yml<i>Guild file</i></li>
 <li class="is-file">train.py<i>Training script</i></li>
</ul>
</li>
</ul>
</div>

Change to the `iris` directory and run `guild help`:

``` command
cd iris
guild help
```

The help screen displays information in the Guild file
`guild.yml`. We'll look more closely at this file next.

Press `q` to stop viewing the project help.

## Project Guild file

Guild files are named `guild.yml` and are located in the project
directory. Guild files contain the information needed to train your
model.

Before we turn our attention to the model training script, let's make
a quick change to `guild.yml`.

In a text editor, open `./iris/guild.yml`.

``` yaml
- model: iris
  description: A basic model.
  operations:
    train:
      description: Train the model.
      cmd: train
      flags:
        train-steps:
          description: Number of steps to train.
          default: 1000
        batch-size:
          description: Training batch size.
          default: 64
```

Modify the model `description` and replace:

    A basic model.

with:

    DNN classifier for Iris data.

Save `guild.yml`.

!!! note
    Leave `guild.yml` open in your text editor --- we'll make changes
    to it as we go along. If your text editor is a command line
    application, open a [](alias:separate-console) to run commands in.

From a command line in the `./iris` project directory, run:

``` command
guild models
```

You should see this output:

``` output
Limiting models to the current directory (use --all to include all)
./iris  DNN classifier for Iris data
```

The message `Limiting models to the current directory` is displayed
when showing information about models defined in the current
directory. In this case, Guild notices `guild.yml` and infers you're
working on a project. Rather than show you all of the models available
on the system, it limits the results to models defined in the project.

For the remainder of this tutorial, we'll omit this message from the
expected output for brevity.

Next, list the operations available:

``` command
guild operations
```

Guild displays the operations for our model:

``` output
./iris:train  Train the model
```

All of this information is defined in `guild.yml`. Over the course of
this tutorial, we'll evolve this file to support all the features of
our Iris classifier.

## Train the sample model

At this point our model is just a sample --- it doesn't train anything
or know about Iris data. However, we can still run the `train`
operation, which simulates the training process.

From a command line in the `./iris` directory, run:

``` command
guild train
```

Guild prompts you with this message:

``` output
You are about to run ./iris:train
  batch-size: 64
  train-steps: 1000
Continue? (Y/n)
```

This lets you review the [flag values](term:flag) that will be used
for the `train` operation.

Accept the values and start the training by pressing `ENTER`.

Guild runs the sample training operation and exits:

``` output
Sample train: step 0
Sample train: step 100
Sample train: step 200
Sample train: step 300
Sample train: step 400
Sample train: step 500
Sample train: step 600
Sample train: step 700
Sample train: step 800
Sample train: step 900
Sample evaluate: 0.888 accuracy
```

While this is only a stub, we did execute a training run. You can list
runs for a project by running:

``` command
guild runs
```

You should see the completed training run.

Guild runs automatically generated when you run `train`. Each run
contains a record of the operation, which includes information about
the operation along with files generated during the run.

You can show information about the latest run by running:

``` command
guild runs info
```

This shows run details including:

Run ID
: A unique identifier for the run

Run operation
: The model operation that generated the run

Start and stop time
: When the run was started and stopped

Run directory
: The file system directory containing run files

Command details
: The command used to run the operation, its exit status (if it
  exited) and its operation system PID (if it's still running)

We'll revisit runs later in this tutorial.

Next, we'll review our project's training script.

## Review the training script

In your text editor, open `./iris/train.py`, which is the sample
training script that Guild created when you initialized the project.

Here's the script with imports and comments removed for brevity. We'll
look at each part in turn.

``` python
def main():
    args = parse_args()
    data = init_data(args)
    model = init_model(data, args)
    train(model, data, args)
    evaluate(model, data, args)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--train-steps', default=1000, type=int)
    parser.add_argument('--batch-size', default=100, type=int)
    parser.add_argument('--data-dir', default='data')
    parser.add_argument('--model-dir', default='model')
    return parser.parse_args()

def init_data(args):
    train_x, train_y = [], []
    test_x, test_y = [], []
    return (train_x, train_y), (test_x, test_y)

def init_model(data, args):
    return 'sample model'

def train(model, data, args):
    for step in range(args.train_steps):
        if step % 100 == 0:
            print('Sample train: step %s' % step)

def evaluate(model, data, args):
    print('Sample evaluate: 0.888 accuracy')

if __name__ == '__main__':
    main()
```

### Main function

``` python
def main():
    args = parse_args()
    data = init_data(args)
    model = init_model(data, args)
    train(model, data, args)
    evaluate(model, data, args)
```

This function orchestrates the training operation:

- Parse command line arguments
- Initialize data used for training and evaluation
- Initialize the model
- Train the model
- Evaluate the model

We won't modify this function because it already does what we need.

### Parse command line arguments

``` python
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--train-steps', default=1000, type=int)
    parser.add_argument('--batch-size', default=100, type=int)
    parser.add_argument('--data-dir', default='data')
    parser.add_argument('--model-dir', default='model')
    return parser.parse_args()
```

This function parses command line arguments passed to the script.

Rather than hard-code hyperparameter values, consider using command
line arguments. This patterm provides a couple of benefits:

- Users can experiment with different hyperparameter values without
  modifying source code.

- By defining hyperparameters as command line arguments, you document
  values that can be changed without comprimising the model
  architecture.

### Initialize the training and test data

``` python
def init_data(args):
    train_x, train_y = [], []
    test_x, test_y = [], []
    return (train_x, train_y), (test_x, test_y)
```

This function is a stub for loading and initializing data. We'll
modify this function later in this tutorial to load and prepare our
Iris data for training and validation.

### Initialize the model

``` python
def init_model(data, args):
    return 'sample model'
```

This function is a stub for initializing the model. We'll modify it
later in this tutorial to return a `tf.estimator.DNNClassifier` that
can be used to train with the Iris data.


### Train the model

``` python
def train(model, data, args):
    for step in range(args.train_steps):
        if step % 100 == 0:
            print('Sample train: step %s' % step)
```

This function is a stub for the training loop. We'll modify it later
in this tutorial to call the `train` method of our model.

### Evaluate the model

``` python
def evaluate(model, data, args):
    print('Sample evaluate: 0.888 accuracy')
```

Our final function is a stub for evaluating the trained model. We'll
modify it later in this tutorial to call the `evaluate` method of our
model.

### Main handler

``` python
if __name__ == "__main__":
    main()
```

This statement calls `main` only when then module is loaded as a
script.

This pattern serves two purposes:

- The script can be executed from a command line
- The script can also be imported by other Python modules without
  automatically running

It's a good idea to use this pattern because it allows your training
script to be used as a module by other Python programs.

## Load the Iris data

Let's start modifying our training script to work with Iris data.

For our project, we'll use the Iris data prepared by Google for
[Getting Started with TensorFlow
->](https://www.tensorflow.org/get_started/premade_estimators).

### Download `iris_data.py`

Download <a class="ext"
href="https://raw.githubusercontent.com/tensorflow/models/079d67d9a0b3407e8d074a200780f3835413ef99/samples/core/get_started/iris_data.py"
download>iris_data.py</a> and save it in your `./iris` project
directory.

Once you've saved the file, your project directory should look like this:

<div class="file-tree">
<ul>
<li class="is-folder open">./iris
 <ul>
 <li class="is-file">guild.yml</li>
 <li class="is-file">iris_data.py <i><strong>Newly downloaded file</strong></i></li>
 <li class="is-file">train.py</li>
</ul>
</li>
</ul>
</div>

### Import `iris_data`

In your text editor, modify `./iris/train.py` by adding the following
line to the imports section of the file, after the line ``import
tensorflow as tf``:

``` python
import iris_data
```

Your imports should look like this:

``` python
import argparse

import tensorflow as tf

import iris_data   # newly added line
```

### Modify `init_data`

Next, we'll modify the `init_data` function to load the Iris data.

In you text editor, modify `./iris/train.py` to change the `init_data`
function to be this:

``` python
def init_data(_args):
    return iris_data.load_data()
```

Note our changes:

- We're passing through the call to `init_data` to our data module
  without making additional changes to the data. Refer to
  `iris_data.py` for details on how the data is loaded.

- We're not using the `args` argument, so we rename it to
  `_args`. Feel free to remove `args` altogether, but if you do, you
  must also update the `main` function to use ``init_data()``.

### Test your changes

In your text editor, save your changes.

Our script should now load the Iris data but continue the simulated
training and evaluation without using the data. If we have problems
here we can fix them before continuing to the next steps.

From a command line in the `./iris` directory, run:

``` command
guild train -y
```

!!! note
    We use the ``-y`` option here to bypass the prompt, saving us
    a step.

Below are some issues you might experience at this point.

`ImportError: No module named iris_data`
: Verify that you downloaded `iris_data.py` into the project
  directory. See [Download iris_data.py](#download-iris_datapy) above
  for help.

`NameError: global name 'iris_data' is not defined`
: Ensure that you are importing the `iris_data` module. See [Import
  iris_data ](#import-iris_data) above for help.

An error originating from `iris_data.py`
: Verify that you `iris_data.py` was saved correctly.

If the command succeeds, you should see the same result as from our
previous run.

You can list the runs by running:

``` command
guild runs
```

Next, we'll define our model.

## Define the model

In this step, we'll implement a simple deep neural network as
described in [Getting Started with TensorFlow - Instantiate an
estimator
->](https://www.tensorflow.org/get_started/premade_estimators#instantiate_an_estimator).

In your text editor, modify `./iris/train.py` and change the
`init_model` function to be this:

``` python
def init_model(data, args):
    train_x = data[0][0]
    feature_columns = [
        tf.feature_column.numeric_column(key=key)
        for key in train_x.keys()
    ]
    return tf.estimator.DNNClassifier(
        feature_columns=feature_columns,
        hidden_units=[10, 10],
        n_classes=3,
        model_dir=args.model_dir)
```

This is the most complex change to our script, so let's take a moment
to understand it.

The purpose of `init_model` is to return something that can be trained
and evaluated. In this case, we're using the [TensorFlow Estimators
->](https://www.tensorflow.org/programmers_guide/estimators)
high-level framework to create a DNN classifier.

The classifier requires a list of feature columns, which we provide
from the training data.

We also specify `model_dir`, which tells TensorFlow to generate logs
and save the trained model during training. We'll see this in action
later.

In your text editor, save your changes.

Feel free to stop now and test your changes by running:

``` command
guild train -y
```

While we're still not yet training our model, you will see additional
output from the command, which is generated by TensorFlow when we
instantiate the model.

## Implement train and evaluate

In this step, we'll modify our `train` and `evaluate` functions to
perform real work!

In your text editor, modify `./iris/train.py` and change the `train`
function to be:

``` python
def train(model, data, args):
    (train_x, train_y), _ = data
    input_fn = lambda: iris_data.train_input_fn(
        train_x, train_y, args.batch_size)
    model.train(input_fn=input_fn, steps=args.train_steps)

```

Next, change the `evaluate` function to be:

``` python
def evaluate(model, data, args):
    _, (test_x, test_y) = data
    input_fn = lambda: iris_data.eval_input_fn(
        test_x, test_y, args.batch_size)
    eval_result = model.evaluate(input_fn=input_fn)
    print('Test set accuracy: {accuracy:0.3f}\n'.format(**eval_result))
```

Both functions are similar:

- They both call a single method on `model` to perform the work.

- The both use a callback `input_fn` to read batched data.

Note that we're using `args.batch_size` rather than hard-coding a
value. This makes it easy to experiment with different values without
changing the source code.

In your text editor, save your changes.

At this point our training script is ready to train the Iris data!

!!! note
    If you'd like, feel free to delete any remaining `TODO`
    comments.

## Delete the trial runs

Before we proceed, let's delete all of our runs up to this point,
which we won't use because they were just trials. From a command line,
run:

``` command
guild runs delete
```

Guild will ask you to confirm the operation before proceeding. Press
`ENTER` to delete the runs.

!!! note
    Guild lets you restore deleted runs using the [runs
    restore](cmd:runs-restore) command. This can come in handy if you
    accidentally delete something you need!

## Train the DNN

Let's train a real network!

From a command line, run:

``` command
guild train -y
```

You should see real training progress, with updates from TensorFlow
about training loss and other training statistics.

!!! note
    If your script doesn't run as expected, check it against
    [train_premade.py](https://github.com/guildai/examples/blob/master/iris/train_checkpoint_1.py),
    which reflects the changes to `./iris/train.py` up to this point.

When the training is completed, the script prints a final accuracy,
which is calculated using test data. It should be 0.967.

Congratulations - you've just trained a classifier for Iris data!

## View runs

From a command line, run:

``` command
guild view
```

This command opens Guild View in a browser. Use Guild View to explore
your run(s). Click ![View in
TensorBoard](/assets/img/view-in-tensorboard.png) in the upper-right
of the page to view your runs in TensorBoard.

Click the **FILES** tab to view the files generated by the
operation. These include TensorFlow event logs, which are used by
TensorBoard, and the saved trained model.

You can list the files associated with the latest run by running:

``` command
guild runs info --files
```

To see the full path to each file --- for example, to reference the
file in another command --- use the `-P` option:

``` command
guild runs info --files -P
```


## Summary

In this tutorial, we developed a new Guild AI project from scratch,
containing the DNN Iris data classifier defined in [Getting Started
with TensorFlow
->](https://www.tensorflow.org/get_started/premade_estimators).

In this tutoral, we saw the following:

- Guild files (`guild.yml`) define models that can be trained.

- Model operations are wrappers for commands to Python modules.

- Operation flags are passed through to training scripts as command
  line arguments.

- Guild automatically tracks each run.

- Guild provides tools to help you evaluate runs, including
  integration with TensorBoard.
