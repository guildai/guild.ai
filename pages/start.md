navbar_item: yes
tags: start

# Quick Start

[TOC]

## Install Guild AI

If you're familiar with installing Python packages using `pip`, simply
install the `guildai` package.

``` command
pip install guildai
```

or to install to the user install directory:

``` command
pip install guildai --user
```

For detailed installation instructions, see [Install Guild
AI](/install.md).

When Guild is installed, check the environment:

``` command
guild check
```

For help troubleshooting, [ask for help](ref:slack) on the Guild AI
Slack workspace.

## Get Command Help

This guide focuses on Guild's [command line
interface](/cli.md). Commands are run using the format ``guild
COMMAND``. Use the `--help` option to show information for a command.

To show all available commands, run:

``` command
guild --help
```

``` output
Usage: guild [OPTIONS] COMMAND [ARGS]...

  Guild AI command line interface.

Options:
  --version  Show the version and exit.
  -C PATH    Use PATH as current directory for referencing guild files
             (guild.yml).
  -H PATH    Use PATH as Guild home (default is /home/garrett/.guild).
  --debug    Log more information during command.
  --help     Show this message and exit.

Commands:
  cat              Show contents of a run file.
  check            Check the Guild setup.
  compare          Compare run results.
  diff             Diff two runs.
  download         Download a file resource.
  export           Export one or more runs.
  help             Show help for a path or package.
  import           Import one or more runs from ARCHIVE.
  init             Initialize a Guild environment.
  install          Install one or more packages.
  label            Set run labels.
  ls               List run files.
  mark             Mark a run.
  models           Show available models.
  open             Open a run path.
  operations, ops  Show model operations.
  package          Create a package for distribution.
  packages         Show or manage packages.
  publish          Publish one or more runs.
  pull             Copy one or more runs from a remote location.
  push             Copy one or more runs to a remote location.
  remote           Manage remote status.
  remotes          Show available remotes.
  run              Run a model operation.
  runs             Show or manage runs.
  search           Search for a package.
  shell            Start a Python shell for API use.
  stop             Stop one or more runs.
  sync             Synchronize remote runs.
  sys              System utilities.
  tensorboard      Visualize runs with TensorBoard.
  tensorflow       Collection of TensorFlow tools.
  uninstall        Uninstall one or more packages.
  view             Visualize runs in a local web application.
  watch            Watch run output.
```

See [Commands](/commands/index.md) for online help.

## Create a Sample Training Script

In the steps below, you create a sample training script and run it to
generate experiments.

Create a new project directory:

``` command
mkdir guild-start
```

Change to the project directory:

``` command
cd guild-start
```

In the project directory, create a file named `train.py` that contains
this Python code:

``` python
import numpy as np

# Hyperparameters
x = 0.1
noise = 0.1

# Simulated training loss
loss = (np.sin(5 * x) * (1 - np.tanh(x ** 2)) + np.random.randn() * noise)

print("loss: %f" % loss)
```

^ Sample script `train.py`

This script simulates a loss function. It accepts hyperparameters `x`
and `noise` and prints the resulting `loss`.

The project directory should look like this:

<div class="file-tree">
<ul>
<li class="is-folder open">guild-start
 <ul>
 <li class="is-file">train.py</li>
 </ul>
</li>
</ul>
</div>

## Run the Script

Use Guild to run `train.py`:

``` command
guild run train.py
```

``` output
You are about to run train.py
  noise: 0.1
  x: 0.1
Continue? (Y/n)
```

Press `Enter` to start the operation.

Guild runs `train.py`, which prints a simulated loss. Guild lets you
run any unmodified script this way.

When Guild runs a script, it generates a new experiment, or
[run](term:run). Each run tracks experiment details including results.

## View Run Results

Show the current runs:

``` command
guild runs
```

``` output
[1:50cec0c8]  train.py  2020-01-09 15:55:15  completed  noise=0.1 x=0.1
```

Guild shows available runs, including the run ID, operation name,
start time, status, and label.

Information about each run is saved in a [run
directory](term:run-dir), including metadata and results.

View information for the latest run:

``` command
guild runs info
```

``` output
id: 50cec0c8513c40e7883e1d76f9828f6c
operation: train.py
from: ~/Projects/guild-start
status: completed
started: 2020-01-09 15:55:15
stopped: 2020-01-09 15:55:15
marked: no
label: noise=0.1 x=0.1
sourcecode_digest: 9d846ffb2022c9540d7b01a160617881
vcs_commit:
run_dir: ~/.guild/runs/50cec0c8513c40e7883e1d76f9828f6c
command: /usr/bin/python -um guild.op_main train --noise 0.1 --x 0.1
exit_status: 0
pid:
flags:
  noise: 0.1
  x: 0.1
scalars:
  loss: 0.432132 (step 0)
```

List the source code files used for the run:

``` command
guild ls --sourcecode
```

``` output
~/.guild/runs/50cec0c8513c40e7883e1d76f9828f6c:
  .guild/sourcecode/
  .guild/sourcecode/train.py
```

Show the source code for the `train.py` module:

``` command
guild cat --sourcecode --path train.py
```

``` output
import numpy as np

# Hyperparameters
x = 0.1
noise = 0.1

# Simulated training loss
loss = (np.sin(5 * x) * (1 - np.tanh(x ** 2)) + np.random.randn() * noise)

print("loss: %f" % loss)
```

Guild captures important details associated with a run:

- Run metadata: operation name, flags, OS process status, start time,
  source code digest, etc.
- Run scalars (i.e. metrics generated by the run)
- Files generated by the run (in this case our sample does not generate files)
- Source code files

There are many benefits to capturing this information:

- Formally track your model development progress
- Document metrics used when evaluating model performance
- Create an audit trail for models that you deploy
- Compare differences across runs

In the steps that follow, you use Guild to optimize hyperparameter and
compare run results.

## Optimize Training Loss

Guild has built-in support for hyperparameter optimization using
various search methods:

- [Random search ->](term:random-search)
- [Grid search ->](term:grid-search)
- [Bayesian optimization ->](term:bayesian-optimization)

In this section, you use each technique to find values for `x` that
minimize `loss`.

### Random Search

To search over a range of values, specify a flag value in the format
`[MIN:MAX]`. By default, Guild runs 20 trials using randomly chosen
values within the specified range. Use `--max-trials` to specify the
number of trials to run.

Start a random search over `x` using ten trials:

``` command
guild run train.py x=[-2.0:2.0] --max-trials 10
```

``` output
You are about to run train.py with random search (max 10 trials, minimize loss)
  x: [-2.0:2.0]
Continue? (Y/n)
```

Press `Enter` to start the operation.

Guild runs `train.py` ten times using values for `x` that randomly
sampled from a uniform distribution from -2.0 to 2.0.

Show the runs:

``` command
guild runs
```

### Grid Search

To run trials with specific values, specify a flag value in the format
`[VAL1,VAL2,...,VALN]`. When you specify values using this format for
multiple flags, Guild runs trials over the cartesian product of
specified values.

Run four trials over values for `x` and `noise`:

``` command
guild run train.py x=[-1,1] noise=[0,0.1]
```

## Compare Runs

Use [guild compare](cmd:compare) to start a spreadsheet-like
application to compare run results.

``` command
guild compare --min loss
```

Guild starts an interactive application that lets you browse
experiment results. Runs with lower `loss` appear at the top of the
list. Use your arrow keys to navigate. Press `1` to sort by the
current column (ascending) or `2` (descending).

![](/assets/img/compare-start.png)

^ Compare experiment results --- press `q` to exit

Your results will differ as values for `x` are randomly generated.

Exit Guild Compare by pressing `q`.

## View Runs in TensorBoard

View your runs using TensorBoard:

``` command
guild tensorboard
```

Guild opens TensorBoard in your browser. Click the **HPARAMS** tab to
compare run performance. You can visualize the runs using **PARALLEL
COORDINATES VIEW** and **SCATTER PLOT MATRIX VIEW** by clicking the
applicable tab.

![](/assets/img/tb-hparams.png)

^ Compare runs using Parallel Coordinates View

## Delete Runs

Use [guild runs delete](cmd:runs-delete) (or its alias ``guild runs
rm``) to delete runs. By default, Guild saves deleted runs so they can
be restored using [guild runs restore](cmd:runs-restore).

Delete all of the current runs (don't worry, you will restore these
runs later):

``` command
guild runs rm
```

Press `Enter` to delete the runs.

Guild deletes all of the runs.

Show deleted runs by specifying the `--deleted` option:

``` command
guild runs --deleted
```

Restore

You can restore deleted runs using [guild runs
restore](cmd:runs-restore).
