sidenav_title: Commands

# Command Cheatsheet

[TOC]

## Get Command Help

#### Show available Guild commands

``` command
guild
```

#### Command specific help

``` command
guild COMMAND --help
```

## Run a Script

Use the [run](cmd:run) command to run a Python script or executable.

#### Run a Python script

``` command
guild run script.py flag1=val1 flag2=val2
```

#### Run an executable

``` command
guild run script.sh flag1=val flag2=val2
```

## Run an Operation

Use the [run](cmd:run) command to run operations defined in a [Guild
file](ref:guildfile).

#### Show available operations

``` command
guild operations
```

#### Run with default flag values

``` command
guild run train
```

#### Specify flag values

``` command
guild run train flag1=val1 flag2=val2
```

#### Run a batch using flag value lists

The following command generates 4 trials --- one for each combination
of flag values:

``` command
guild run train learning-rate=[0.01,0.1] batch-size=[50,100]
```

For more information, see [Flag Value Lists](ref:flag-value-list).

#### Run a random search

Use [search space functions](term:flag-search-space-function) to
implicitly trigger the use of the `random` optiizer.

``` command
guild run train -m 10 lr=loguniform[1e-5:1e-2] batch_size=50
```

^ Use [`loguniform`](/flags.md#loguniform) to sample from a
log-uniform distribution


``` command
guild run train dropout=uniform[0.1:0.8]
```

^ Use [`uniform`](/flags.md#uniform) to sample from a uniform
distribution

``` command
guild run train dropout=[0.1:0.8]
```

^ When you omit the function name, Guild assumes
[`uniform`](/flags.md#uniform) --- this command is identical to the
previous example

#### Run Bayesian optimization

``` command
guild run train -m 10 -o gp lr=loguniform[1e-5:1e-2] batch_size=50
```

#### Save trials to a batch file

``` command
guild run train dropout=[0.1,0.2,0.3] --save-trials trials.csv
```

#### Use a batch file

``` command
guild run train @trials.csv
```

## Get Project Help

#### List available operations

``` command
guild operations
```

#### View project help

``` command
guild help
```

Get help with running a particular operation:

``` command
guild run operation --help-op
```

## List Runs

``` command
guild runs
```

#### Filter runs by operation

``` command
guild runs -o train
```

#### Filter runs by start time

``` command
guild runs -s today
```

``` command
guild runs -s '1 week ago'
```

``` command
guild runs -s 'last 15 minutes'
```

#### Filter runs by status

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

## Show Run Details

The examples below apply to the latest run. To apply them to another
run, include the run index or run ID in the command.

``` command
guild runs info
```

#### List run files

``` command
guild ls
```

#### List run source code files

``` command
guild ls --sourcecode
```

#### Show run output

``` command
guild cat --output
```

#### Print file contents

``` command
guild cat -p model.txt
```

#### Open a file or directory

``` command
guild open -p plot.png
```

``` command
guild open -p plots
```

## Compare Runs

``` command
guild compare
```

#### Filter runs for compare

``` command
guild compare -o cnn -s today
```

#### Save compare data to a file


``` command
guild compare --csv compare.csv
```

#### Print compare data to the console

``` command
guild compare --csv -
```

#### Compare using alternate tools

``` command
guild compare --tool hiplot
```

^ Copmare runs using [HiPlot](ref:hiplot)

#### Compare runs using TensorBoard

``` command
guild tensorboard
```

#### Compare runs using Guild View

``` command
guild view
```

## Diff Runs

The examples below diff the last two runs. To diff different runs,
include their indexes or IDs in the command in the form `FROM TO`.

#### Diff the last two runs

``` command
guild diff
```

#### Diff specific run information

``` command
guild diff --flags
```

``` command
guild diff --sourcecode
```

``` command
guild diff --output
```

#### Diff a run file or directory

``` command
guild diff -p model.txt
```

``` command
guild diff -p checkpoints
```

#### Diff using alternate commands

``` command
guild diff --cmd meld
```

^ Diff using [Meld](ref:meld)

See [Diff - User Config](/reference/user-config.md#diff) for details
on setting the default command used by [diff](cmd:diff).

## Install Guild AI

``` command
pip install guildai
```

#### Install without admin privileges

``` command
pip install guildai --user
```

#### Install with elevated priviledges (Linux and macOS)

``` command
sudo pip install guildai
```

#### Verify Guild installation

``` command
guild check
```

#### Upgrade Guild

``` command
pip install --upgrade guildai
```

## Debug Operations

#### Show underlying operation command

``` command
guild run train --print-cmd
```

^ Prints the command that Guild uses for `train` and exit without
running the operation

#### Test output scalars

``` command
guild run train --test-output-scalars sample-output.txt
```

^ Apply source code copy rules for `train` to contents of
`sample-output.txt`

``` command
guild run train --test-output-scalars -
```

^ Test interactively --- type a sample output line and press `Enter`
to evaluate it using source code copy rules for `train`

#### Test source code configuration

``` command
guild run train --test-sourcecode
```

#### Stage a run for debugging

``` command
guild run train --stage --run-dir /tmp/staged-run
```
