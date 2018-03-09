tags: tutorial, developer

# Develop a model from scratch

[TOC]

In this tutorial we'll develop a model with Guild AI from
scratch. Model development in Guild AI follows the same general
process as developing any Python based deep learning model:

- Create a training script skeleton
- Implement a model using one of the available TensorFlow model APIs
- Obtain a training dataset
- Iteratively train, evaluate and improve the model

Guild AI provides some additional help in this process:

- Automatically track training runs
- Easily compare runs
- Package and distribute models

We'll follow the general outline presented in [Getting Started with
TensorFlow
->](ttps://www.tensorflow.org/get_started/premade_estimators), which
creates a basic classifier for the Iris dataset.

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
contains information about what's in the project.

We can use the [](cmd:init) command to initialize a new project.

Since we're creating a classifier for the Iris dataset, let's call our
project "iris" (feel free to use a different name --- just modify the
values below accordingly).

Initialize a new Guild project by running:

``` command
guild init --project iris
```

Guild generates the following project files:

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
model:

- Model information such as name and description
- Model [operations](term:operation), which define actions such as "train"
- Model [resources](term:resource) needed by operations, such as datasets

In a text editor, open `./iris/guild.yml`.

``` yaml
- model: iris
  description:
    TODO - model description
  operations:
    train:
      description: Train the model
      cmd: train
      flags:
        epochs:
          description: Number of epochs to train
          default: 20
        batch-size:
          description: Training batch size
          default: 64
        learning-rate:
          description: Learning rate
          default: 0.01
      requires:
        - data
  resources:
    data:
      descrition: Data for training and validation
      sources:
        - url: http://pub.guild.ai.s3.amazonaws.com/samples/data.csv
          sha256: 6be6b1203f3d51df0b553a70e57b8a723cd405683958204f96d23d7cd6aea659

```

Modify the model `description` and replace:

    TODO - model description

with:

    DNN classifier for Iris data

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
expected output.

Next, list the operations available:

``` command
guild operations
```

Guild will display the operations for our model:

``` output
./iris:train  Train the model
```

All of this information is defined in `guild.yml`. Over the course of
this tutorial, we'll evolve this file to support all the features of
our Iris classifier.

## Train the sample model

At this point our model is just a sample --- it doesn't train anyting
or know about Iris data! But we can still run the `train` operation,
which simulates the training process.

From a command line in the `./iris` directory, run:

``` command
guild train
```

Guild will prompt you with this message:

``` output
You are about to run ./iris:train
  batch-size: 64
  epochs: 20
  learning-rate: 0.01
Continue? (Y/n)
```

This prompt lets you review the [flag values](term:flag) that will be
used for the `train` operation. These are flags defined in the sample
model --- we'll modify them later.

For now, accept the values and start the training by pressing `ENTER`.

Guild downloads a sample data file (the file is very small and won't
take long to download) and runs a similated training, printing status
updates.

``` output
Resolving data dependency
Starting new HTTP connection (1): pub.guild.ai.s3.amazonaws.com
Downloading http://pub.guild.ai.s3.amazonaws.com/samples/data.csv
Training sample model (batch-size: 64, learning-rate: 0.01): epoch 1
...
```

Remember, this is a sample training that doesn't train anything at
all! We'll change this later.

## Training script

Let's look at `train.py`, which is the script used to train the
model. In your text editor, open `train.py`.

Here's the script, minus some imports and comments, which are removed
for bervity:

``` python
def main():
    args = parse_args()
    model = init_model(args)
    train(model, args)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", default=20, type=int)
    parser.add_argument("--batch-size", default=64, type=int)
    parser.add_argument("--learning-rate", default=0.01, type=float)
    return parser.parse_args()

def init_model(args):
    return (
        "sample model (batch-size: {}, learning-rate: {})".format(
        args.batch_size, args.learning_rate)
    )

def train(model, args):
    for i in range(args.epochs):
        print("Training %s: epoch %i" % (model, i + 1))
        import time; time.sleep(0.05)

if __name__ == "__main__":
    main()
```

While this is only a sample and doesn't train anything, it does
reflect the core structure of most training scripts. Let's look at
each part.

### Main handler

Training scripts must be runnable from the command line. Nearly all
TensorFlow training examples support this and our sample is no
exception.

The following block checks if the module is being loaded as a script
and, if it is, calls a `main` function.

``` python
if __name__ == "__main__":
    main()
```

This pattern serves two
purposes:

- The script can be executed from a command line
- The script can also be imported by other Python modules without
  automatically running

The second point is important and many TensorFlow scripts, including
the Keras sample models, don't use this pattern. Scripts that always
execute are not reusable,[^1] short of modifying them.

[^1]: It is technically possible to reuse scripts that execute on
    import --- Guild does this in its Keras support. However, it's not
    practical as a general pattern as it's far simpler to modify the
    script in question to use the Main handler pattern shown above.

### Main function

Skipping to the top of the script, we see the `main` function:

```
def main():
    args = parse_args()
    model = init_model(args)
    train(model, args)
```

This is a simple function that performs three tasks:

- Parses the script command line arguments
- Initialize the model
- Train the model

Most training scripts follow these steps, though many omit the first
task --- parsing command line arguments. This is an important
consideration in model development as we'll see in the next section.

Model initialization is logically separate from training, and that
distinction is reflected in our sample script by using functions ---
`init_model` to initialize the model and `train` to train it.

### Command line arguments

Many TensorFlow scripts hard-code important values such as training
epochs, batch size, learning rates, and dataset location. Hard coding
these values makes it hard to use the model as it forces users to edit
source code.

As a model developer, it's a good idea to build scripts that can be
used without modification. To do that effectively, you need to support
command line argumets. Fortunately, it's easy. Here's the function in
our sample script that handles command line arguments:

``` python
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", default=20, type=int)
    parser.add_argument("--batch-size", default=64, type=int)
    parser.add_argument("--learning-rate", default=0.01, type=float)
    return parser.parse_args()
```

Here we see that three arguments are supported: `epochs`,
`batch-size`, and `leaning-rate`. Each of these variables has a
default value that can be easily changed by the user when running the
scripts.

For example, to use a batch size of 100, a user could run:

```
python train.py --batch-size 100
```

As we proceed in this tutoral, we'll revisit this function and modify
it to support the parameters that we need for our Iris classifier.

### Model definition

TensorFlow models can be defined using a variety of APIs. In [Getting
Started with TensorFlow
->](https://www.tensorflow.org/get_started/premade_estimators) --- our
template for the Iris classifier --- the author uses the [TF Estimator
->](https://www.tensorflow.org/programmers_guide/estimators) framework
to define a simple DNN (deep neural network) model.

Our sample script doesn't attempt to guess which API you want to use
and instead provides a place-holder:

``` python
def init_model(args):
    return (
        "sample model (batch-size: {}, learning-rate: {})".format(
        args.batch_size, args.learning_rate)
    )
```

As you can see, our model is nothing more than a string! We'll fix
this later.

### Training loop

Machine learning models are trained iteratively using batches of
training data. This iteration is often referred to as a *training
loop*. Our sample model provides a training loop simulation, which
iterates over *epochs*, which are training iterations performed over
all training examples.

``` python
def train(model, args):
    for i in range(args.epochs):
        print("Training %s: epoch %i" % (model, i + 1))
        import time; time.sleep(0.05)
```

As with the other sample functions, our training loop is a phony!
We'll fix that as well.
