# Cheatsheet

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

Operations are defined in [Guild files](ref:guild-files).

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

The examples below can be added to [`guild.yml`](ref:guild-files) and
adopted as needed.

Operations at the top-level of `guild.yml` ([operation only
format](reference/guildfile.md#operation-only-format)):

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

When using [full format](reference/guildfile.md#full-format), define
operations under a model's `operations` attribute:

``` yaml
- model: cnn
  operations:
    train:
      description: Train the CNN
      main: train
```

Hints:

- Guild automatically imports flags from Python modules so you don't
  need to re-specify them in the Guild file.

- To only import certain flags, use `flags-import`.

- To skip importing certain flags, use `flags-import-skip`.

- To disable importing flags altogether, use `flags-import: no`.

- When an operation name is the same as the Python module name, you
  can omit `main`.

Refer to [Operations](reference/guildfile.md#operations) for a full
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

!!! note
    The examples below apply to the latest run. To apply them to
    another run, include the run index or run ID in the command.

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

!!! note
    The examples below diff the last two runs. To diff different
    runs, include their indexes or IDs in the command in the form
    `FROM TO`.

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

^ `~/.guild/config.yml`

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

Test output scalars:

``` command
guild run train --test-output-scalars -
```

Stage a run directory without running an operation:

``` command
guild run train --stage /tmp/train-stage
```

## Guild File Snippets

### Flag

``` yaml
flags:
  NAME:
    description: A sample flag
    default: 100

    # List of legal values.
    #choices: [1, 2, blue, shoe]

    # Let user specify a non-choice value when choices are
    # defined.
    #allow-other: yes

    # Indicate if a value is required for the operation.
    #required: yes

    # Use a different command line argument or variable name.
    #args-name: NAME_2

    # Value that, when set, causes flag to appear as a 'switch'
    # command line option - i.e. an option with no value. E.g.
    # NAME=yes results in '--NAME' and not '--NAME True' to be
    # used as the flag argument.
    #arg-switch: yes

    # Don't include flag in command line arguments. Use when
    # referencing the flag in `main` as `${NAME}` to avoid
    # flag from appearing twice.
    #arg-skip: yes

    # Label to use when `null` value (default if not defined
    # above) is specified.
    #null-label: Default behavior
```

### Output Scalars

Examples below define `output-scalars` under a hypothetical `train`
operation. Apply them to your operations as needed.

Output scalars control how Guild logs scalar values from run
output. Patterns are defined as [regular
expressions](https://docs.python.org/3/library/re.html#regular-expression-syntax). Scalar
values are captured using a regular expression capturing group. The
special escape values `\key`, `\value`, and `\step` can be used to
match keys, values, and step values respectively.

By default, Guild detects scalars from output in the format `KEY:
NUMBER` where `KEY` occurs at the start of the line.

The special `step` key is used to capture the current step.

Disable output scalar logging (e.g. you're logging scalars directly
using a TF Event summary writer):

``` yaml
train:
  output-scalars: no
```

Specify patterns as a mapping of scalar key to output pattern:

``` yaml
train:
  output-scalars:
    step: 'Training epoch (\step)'
    loss: 'Validation loss: (\value)'
    acc: 'Accuracy: (\value)'
```

Modify the default pattern:

``` yaml
train:
  output-scalars: '^scalar: (\name)=(\value)'
```

Other Examples:

- [Guild AI Example: Customizing Output Scalars
  ->](https://github.com/guildai/examples/tree/master/custom-scalars)

### Source Code

The `sourcecode` attribute determines which files Guild copies as
source code for a run. Configuration can be specified for an operation
or for a model. Model configuration applies to all operation defined
for the model. Operation level configuration extends, rather than
replaces, any model level configuration.

Examples below apply source code configuration to a hypothetical
`train` operation. Apply them to your own operations as needed.

Disable source code snapshots:

``` yaml
train:
  sourcecode: no
```

Include only Python files and `guild.yml`:

``` yaml
train:
  sourcecode:
    - '*.py'
    - guild.yml
```

Include PNG files in addition to source code files (text files < 1M):

``` yaml
train:
  sourcecode:
    - include: '*.png'
```

Exclude a file or directory:

``` yaml
train:
  sourcecode:
    - exclude: data
    - exclude: dataset.csv
```

Model and operation level configuration:

``` yaml
- model: cnn
  sourcecode:
    - exclude: data
    - exclude: '*.csv'

  operations:
    train:
      sourcecode:
        # Rules here are applied to those defined for model above.
        - include: train-config.csv
```

Copy soucecode from a different root location:

``` yaml
train:
  sourcecode:
    root: src
    # Omit select for default behavior.
    select:
      - guild.yml
      - '*.py'
```

Other Examples:

- [Guild AI Example: Copy Source guild.yml
  ->](https://github.com/guildai/examples/blob/master/copy-source/guild.yml)

## Required Files

Run directories are initially empty. To make files available to
operations, specify [requirements](ref:requirements) using `requires`.

Require a file named `data.zip`, which exists in the same directory as
`guild.yml`.

``` yaml

```
