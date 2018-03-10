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

Note that this is only a sample --- nothing has been actually been trained!

We'll fix that next.

## Training script

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
