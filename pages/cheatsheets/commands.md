sidenav_title: Commands

# Command Cheatsheet

[TOC]

## Get Command Help

List Guild commands:

``` command
guild
```

Get help for a command:

``` command
guild command --help
```

## Run a Script

Use Guild to run a Python script to generate a unique experiment.

``` command
guild run script.py flag1=val1 flag2=val2
```

*Command help: [run](cmd:run)*

## Run an Operation

Operations are defined in a [Guild file](ref:guildfiles).

Run an operation with default flag values:

``` command
guild run train
```

Specify flag values:

``` command
guild run train flag1=val1 flag2=val2
```

Run a grid search, which generates trials for each flag combination:

``` command
guild run train learning-rate=[0.01,0.1] batch-size=[50,100]
```

Run 10 trials using random search:

``` command
guild run train -m 10 lr=loguniform[1e-5:1e-2] batch_size=50
```

``` command
guild run train dropout=uniform[0.1:0.8]
```

The previous command can be also run as:

``` command
guild run train dropout=[0.1:0.8]
```

10 trials using Bayesian optimization with gaussian processes:

``` command
guild run train -m 10 -o gp lr=loguniform[1e-5:1e-2] batch_size=50
```

Save trials to a CSV batch file:

``` command
guild run train dropout=[0.1,0.2,0.3] --save-trials trials.csv
```

Use batch file to generate multiple runs:

``` command
guild run train @trials.csv
```

*Command help: [run](cmd:run)*

## Get Operation Help

List available operations:

``` command
guild operations
```

Get help for the current project:

``` command
guild help
```

Get help with running a particular operation:

``` command
guild run operation --help-op
```

*Command help: [operations](cmd:operations), [help](cmd:help), [run](cmd:run)*

## Define an Operation

The examples below can be added to a [Guild file](ref:guildfiles) and
adopted as needed.

Operations defined top-level of `guild.yml` ([operation only
format](ref:operations-only-format)):

``` yaml
prepare-data:
  descrition: Prepare data for training
  main: prepare
  flags:
    val-split:
      description: Percent of examples to use for validation
      default: 0.2

train:
  description: Train a model on prepared data
  main: train
  flags:
    learning-rate:
      description: Learning rate
      default: 0.1
    batch-size:
      description: Batch size
      default: 100
  requires:
    - operation: prepare-data
```

^ Sample operations for guild.yml

Operations defined per model ([full format](ref:full-format)):

``` yaml
- model: cnn
  operations:
    train:
      description: Train the CNN
      main: train
```

^ Sample operation defined for a model in guild.yml

!!! tips
    - Guild automatically imports flags from Python modules so you
      don't need to re-specify them in the Guild file.

    - To only import certain flags, use `flags-import`.

    - To skip importing certain flags, use `flags-import-skip`.

    - To disable importing flags altogether, use `flags-import: no`.

    - When an operation name is the same as the Python module name, you
      can omit `main`.

Refer to [Operations](../reference/guildfile.md#operations) for a full
list of configuration options.

See [Guild File Snippets](#guild-file-snippets) below for more
examples.

## List Runs

``` command
guild runs
```

Show only runs whose operation name contains "train":

``` command
guild runs -o train
```

Show runs that were started within various intervals:

``` command
guild runs -s today
```

``` command
guild runs -s '1 week ago'
```

``` command
guild runs -s 'last 15 minutes'
```

Show runs with various status:

``` command
guild runs --terminated
```

``` command
guild runs --completed
```

``` command
guild runs --terminates --error
```

``` command
guild runs -TE
```

*Command help: [runs list](cmd:runs-list)*

## Show Run Details

The examples below apply to the latest run. To apply them to another
run, include the run index or run ID in the command.

Show latest run metadata including flags:

``` command
guild runs info
```

Include scalars (metrics):

``` command
guid runs info -S
```

List run files:

``` command
guild ls
```

List run source code:

``` command
guild ls --sourcecode
```

Show run output:

``` command
guild cat --output
```

Print a run text file to the console:

``` command
guild cat -p model.txt
```

Open a run file or directory using the desktop file browser:

``` command
guild open -p plot.png
```

``` command
guild open -p plots
```

*Command help: [runs info](cmd:runs-info), [ls](cmd:ls),
[cat](cmd:cat), [open](cmd:open)*

## Compare Runs

``` command
guild compare
```

Compare only runs whose operations contain "cnn" that were started
today:

``` command
guild compare -o cnn -s today
```

Write compare data to a CSV:

``` command
guild compare --csv compare.csv
```

Compare runs using TensorBoard:

``` command
guild tensorboard
```

Compare runs using Guild View:

``` command
guild view
```

*Command help: [compare](cmd:compare), [tensorboard](cmd:tensorboard),
[view](cmd:view)*

## Diff Runs

The examples below diff the last two runs. To diff different runs,
include their indexes or IDs in the command in the form `FROM TO`.

Diff the last two runs:

``` command
guild diff
```

Diff various information of the last two runs:

``` command
guild diff --flags
```

``` command
guild diff --sourcecode
```

``` command
guild diff --output
```

Diff a run file or directory:

``` command
guild diff -p model.txt
```

``` command
guild diff -p checkpoints
```

Use [Meld ->](https://meldmerge.org/) to diff runs:

``` command
guild diff --cmd meld
```

To save Meld as the default program to diff runs, edit
`~/.guild/config.yml` and include this configuration:

``` yaml
diff:
  command: meld
```

^ Snippet for ~/.guild/config.yml

*Command help: [diff](cmd:diff)*

## Install Guild AI

``` command
pip install guildai
```

Install without admin privileges:

``` command
pip install guildai --user
```

Install with elevated priviledges (Linux and macOS):

``` command
sudo pip install guildai
```

Verify that Guild is installed:

``` command
guild check
```

Upgrade Guild:

``` command
pip install --upgrade guildai
```

## Debug Operations

Show the full command that Guild uses when running an operation:

``` command
guild run train --print-cmd
```

Test output scalars:

``` command
guild run train --test-output-scalars -
```

Stage a run directory without running an operation:

``` command
guild run train --stage /tmp/train-stage
```
