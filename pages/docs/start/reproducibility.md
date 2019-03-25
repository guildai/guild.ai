tags: get-started

# Reproducibility

In this guide, we introduce the topic of *reproducibility* in Guild by
way of a [Guild file](term:guild-file). Guild files are simple text
files that, when added to a project, support higher level automation
that simplifies the process of running experiments. Guild files also
effectively document the capabilities of a machine learning project to
other users.

Benefits of using Guild files:

- Discover models and operations supports by a project
- Get detailed help on using a project
- Automate running experiments, from downloading required files to
  training to test/evaluation
- Package and share a project

## Requirements

{!start-requirements-3.md!}

Verify that your `guild-start` project structure is:

<div class="file-tree">
<ul>
<li class="is-folder open">guild-start
 <ul>
 <li class="is-file">fashion_mnist_mlp.py</li>
 </ul>
</li>
</ul>
</div>

## Create a Guild file

In the `guild-start` directory, create a file named `guild.yml`.

The file should be:

``` yaml
- model: fashion
  description: Simple classifier for Fashion-MNIST
  operations:
    train:
      description: Train classifier
      main: fashion_mnist_mlp
```

Save your changes to `guild.yml`.

Verify that your `guild-start` project structure is now:

<div class="file-tree">
<ul>
<li class="is-folder open">guild-start
 <ul>
 <li class="is-file">fashion_mnist_mlp.py</li>
 <li class="is-file">guild.yml</li>
 </ul>
</li>
</ul>
</div>

## Get project help

In you haven't done so already, in a command console, change to the
`guild-start` directory:

``` command
cd guild-start
```

While in the directory `guild-start`, show project help by running:

``` command
guild help
```

Guild shows a help screen for the project, which includes models and
operations defined in the Guild file.

Press `q` to exit the help screen.

Guild provides other commands to discover project functionality, in
particular the ability to:

- List available [models](term:model) and their [operations](term:operation)
- Get command help for running specific operations

List available models by running:

``` command
guild models
```

``` output
fashion  Simple classifier for Fashion-MNIST
```

List available operations:

``` command
guild operations
```

``` output
fashion:train  Train classifier
```

You run operations in the same way you run scripts --- with the Guild
[](cmd:run) command. `run` accepts the command line option `--help-op`
that shows help for running the operation:

``` command
guild run fashion:train --help-op
```

``` output
Usage: guild run [OPTIONS] fashion:train [FLAG]...

Train classifier

Use 'guild run --help' for a list of options.

Flags:
  batch_size  (default is 128)
  dropout     (default is 0.2)
  epochs      (default is 5)
  lr          (default is 0.001)
  lr_decay    (default is 0.0)
```

!!! tip
    You can use ``guild run train`` as a short-cut --- or even
    ``guild run`` in this case. Guild needs only enough information to
    uniquely identify the operation defined in the Guild file.

## Run the `train` operation

In a command console, run the `fashion:train` operation defined in the
Guild file:

``` command
guild run
```

``` output
You are about to run fashion:train
  batch_size: 128
  dropout: 0.2
  epochs: 5
  lr: 0.001
  lr_decay: 0.0
Continue? (Y/n)
```

Press `Enter` to train the model.

Note that we omitted the operation name. Guild uses defaults whenever
it can --- in this case the only operation is `fashion:train` so it
can be omitted. This simplifies the work of anyone who wants to use a
project. In simple cases like this, users can simply run ``guild run``
and Guild will do the rest.

List available runs:

``` command
guild runs
```

Note that the new operation ``fashion:train`` appears as the first
run.

You can run any of the run-related commands for this run, For example,
to show run details, use:

``` command
guild runs info
```

## Refine the model interface

In this step, we modify `guild.yml` to include a list of flag
definitions. By default, Guild imports flags from the Python module
specified in the `main` operation attribute:

``` yaml
- model: fashion
  operations:
    train:
      main: fashion_mnist_mlp
```

^ `fashion_mnist_mlp` is the Python module that is executed when
running the operation

When we run ``guild help``, we see that Guild automatically detects
the flags defined in `fashion_mnist_mlp.py`:

- `batch_size`
- `dropout`
- `epochs`
- `lr`
- `lr_decay`

These flags define the *interface* to the train operation. We'd like
to streamline this interface to simplify our users' experience and
minimize misuse of our model.

We can make three types of changes:

- Provide a description of each flag to help the user understand its
  role in the train operation
- Define value ranges to disallow values that we know are ineffective
- Remove flags that do not contribute to improving model accuracy

Using your text editor, modify `guild.yml` to be:

``` yaml
- model: fashion
  description: Simple classifier for Fashion-MNIST
  operations:
    train:
      description: Train classifier
      main: fashion_mnist_mlp
      flags:
        batch_size:
          description: Training batch size
        epochs:
          description: Number of epochs to train
        lr:
          description: Learning rate used to train
          max: 1e-2
        dropout:
          description: Dropout rate used to help prevent overfitting
```

^ Adding `flags`

This change adds a `flags` section to the `train` operation:

- Each flag has a definition to help the user understand its role
- `lr` is constrained to disallow values that we know aren't helpful
- We omitted `lr_decay` because we don't want the user to change the
  default value

Save your changes to `guild.yml`.

Having refined the flag definitions for `train`, view help for the
project:

``` command
guild help
```

Note now that the list of flags for `train` reflect your changes.

Press `q` to exit the help screen.

Verify that high value for learning rate are now allowed:

``` command
guild run lr=0.1
```

``` output
guild: invalid value for lr: out of range (greater than max 0.01)
```

## Exploring dropout

Note that in the last section we omitted a minimum value for
dropout. Surely there's a rate above which dropout is harmful to
learning --- but what is that rate? We might pick a value --- say
`0.5` --- but what rationale do we have for selecting that value?

In this section, we run a grid search to find the point at which
dropout appears to negatively impact learning.

Run the following experiment:

``` command
guild run dropout=[0.7,0.8,0.9,0.95,0.99] epochs=1
```

Press `Enter` to start the experiment.

We train for just one epoch to save time --- we want to see the
relative effect of dropout over some period.

When the operation is finished, compare the results:

``` command
guild compare 1:5 --table -cc =dropout,val_acc
```

This command prints the last five runs (i.e. the runs we generated in
our grid search) and compares only dropout and validation
accuracy.

!!! note
    The syntax `=dropout` means "the dropout flag" --- and is used
    to distinguish flag names from scalars. You can alternatively
    prefix a flag name with ``flag:`` --- e.g. ``-cc
    flag:dropout,val_acc``.

You should see something similar to this:

``` output
run       dropout   val_acc
95eaae5c  0.990000  0.178200
95eaae5b  0.950000  0.370300
95eaae5a  0.900000  0.661000
95eaae59  0.800000  0.795000
95eaae58  0.700000  0.823400
```

This result suggests that dropout starts to negatively effect learning
somewhere above `0.9`. We might opt to set a max for *dropout* at
`0.99` in this case.

## Recreating our dropout experiment

The exercise in the previous section shows potentially helpful
information about dropout in training Fashion MNIST with our simple
neural network. It would be nice to formalize this experiment so that
others can re-run it.

In this section, we further modify `guild.yml` to add a new operation,
which can be used to replicate our dropout experiment.

Using your text editor, modify `guild.yml` to be:

``` yaml
- model: fashion
  description: Simple classifier for Fashion-MNIST
  operations:
    train:
      description: Train classifier
      main: fashion_mnist_mlp
      flags:
        batch_size:
          description: Training batch size
        epochs:
          description: Number of epochs to train
        lr:
          description: Learning rate used to train
          max: 1e-2
        dropout:
          description: Dropout rate used to help prevent overfitting
    dropout-experiment:
      description:
        An experiment that explores the impact of dropout

        We find that dropout above 0.9 starts to negatively impact
        learning. Dropout rates above 0.95 appear to be pathological.

        Use `guild compare 1:5 --table -cc =dropout,val_acc` to
        compare results after running experiment.
      steps:
        - run: train dropout=[0.7,0.8,0.9,0.95,0.99] epochs=1
```

^ Adding `dropout-experiment`

This change adds a new operation: `dropout-experiment`, which uses
`steps` to run the `train` operation with specific values for
*dropout* and *epochs* It also provides a detailed description of the
operation, including its rationale and how to evaluate results.

Save changes to `guild.yml`.

In a command console, view help for the project:

``` command
guild help
```

Note the new operation `dropout-experiment` along with its detailed
description. When users first interact with the project, they can
discover its features using this help facility.

Press `q` to exit the help screen.

Similarly, list the project operations:

``` command
guild operations
```

``` output
fashion:dropout-experiment  An experiment that explores the impact of dropout
fashion:train               Train classifier
```

Finally, verify that `dropout-experiment` indeed replicates the
earlier experiment:

``` command
guild run dropout-experiment
```

Press `Enter` to confirm and start the operation.

When the operation finishes, compare the results:

``` command
guild compare 1:5 --table -cc =dropout,val_acc
```

## Summary

In this guide we created a Guild file that simplifies and automates
the use of our project. In particular, we created an interface for
`train` and an operation that recreates an experiment.

Now when users first explore this project, they can start by running
``guild help`` and proceed to run operations with ``guild run``.

The process for reproducibility is now quite simple:

1. Get project source (e.g. from GitHub, etc.)
2. Change to project directory
3. Run ``guild help`` to discover project models and operations (optional)
4. Use ``guild run`` to run operations, including any operations that
   recreate experiments

## Next steps

{!start-backup-restore.md!}

{!start-remote-train.md!}

{!start-docs.md!}
