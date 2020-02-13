tags: start
sidenav_title: Introduction

# Get Started with Guild AI

[TOC]

## Install Guild AI

If you're familiar with installing Python packages using `pip`, simply
install the `guildai` package.

``` command
pip install guildai --pre
```

Altnernatively, to install to the [user install directory
->](https://pip.pypa.io/en/stable/reference/pip_install/#cmdoption-user):

``` command
pip install guildai --pre --user
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

Guild's primary interface is the [command line](/cli.md). Commands are
run using the format ``guild COMMAND``. Use the `--help` option to
show information for a command.

Show all Guild commands:

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
  -H PATH    Use PATH as Guild home (default is ~/.guild).
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
  select           Select a run and shows its ID.
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

See [Commands Reference](/commands/index.md) for online help.

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

^ Sample script `train.py` [^script-credit]

[^script-credit]: Adapted from [*Bayesian optimization with skopt*
    ->](https://scikit-optimize.github.io/auto_examples/bayesian-optimization.html)

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

Guild runs `train.py`, which prints a simulated loss.

When Guild runs a script, it generates a new experiment, or
[run](term:run). Each run tracks experiment details including results.

!!! highlight
    Guild lets you track experiments without changing your
    scripts. This saves time and keeps your source independent of an
    experiment management framework.

Guild detects two hyperparameters from `train.py`: *noise* and
*x*. Guild refers to these variables as [flags](term:flag). By
default, Guild treats global constants in Python scripts as
flags. This behavior can be controlled through explicit configuration,
which you learn about in later steps.

## View Results

Start the [Guild View](/tools/view.md) application:

``` command
guild view
```

Guild starts the application, and opens a tab in your browser. Guild
View runs in the background in the command terminal.

Use Guild View to browse runs, view run details including metadata,
files, and log output. You can compare run results and run artifacts
in TensorBoard.

![](/assets/img/view-start.png)

^ Guild View --- a web based application for viewing runs and
  comparing results

Return to the command terminal and type `Ctrl-C` to stop Guild View.

### View Results from the Terminal

When working in a command line environment, it's convient to use the
terminal to view run results.

From your terminal, list the current runs:

``` command
guild runs
```

``` output
[1:68f4da74]  train.py  2020-01-14 08:42:54  completed  noise=0.1 x=0.1
```

Guild lists runs, showing the run ID, operation name, start time,
status, and label. As you generate more runs, they appear in this
list.

Information about each run is saved in a [run
directory](term:run-dir), including metadata, flag inputs, and
results.

View information for the latest run:

``` command
guild runs info
```

``` output
id: 68f4da7428bd49b5a8946863909f84dc
operation: train.py
from: ~/Projects/guild-start
status: completed
started: 2020-01-14 08:42:54
stopped: 2020-01-14 08:42:54
marked: no
label: noise=0.1 x=0.1
sourcecode_digest: 9d846ffb2022c9540d7b01a160617881
vcs_commit:
run_dir: ~/.guild/runs/68f4da7428bd49b5a8946863909f84dc
command: /usr/bin/python -um guild.op_main train --noise 0.1 --x 0.1
exit_status: 0
pid:
flags:
  noise: 0.1
  x: 0.1
scalars:
  loss: 0.388010 (step 0)
```

By default, Guild shows information for the latest run.

!!! highlight
    Guild captures detailed information for each run so you
    have a complete record of each result. This information is
    essential for making informed decisions and tracking changes to
    your model.

### Project Source Code

Guild records project source code for each run so you know exactly
what is executed.

List the run source code files with the [ls](cmd:ls) command:

``` command
guild ls --sourcecode
```

``` output
~/.guild/runs/68f4da7428bd49b5a8946863909f84dc:
  .guild/sourcecode/
  .guild/sourcecode/train.py
```

Show the source code for `train.py` with the [cat](cmd:cat) command:

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

!!! highlight
    Guild copies source code files for each run so you have
    an exact record of the code that generated the result.

You can open a run file using a system program.

Open the `train.py` source code file for the latest run:

``` command
guild open --sourcecode --path train.py
```

Guild opens the copy `train.py` used for the run with the default
system program for `py` files.

![](/assets/img/code-start.png)

^ View a run file using the [open](cmd:open) command

## Summary

In this section, you use Guild AI to capture experiments for a sample
training script.

!!! highlights
    - Track experiments without changing your code.

    - Guild is easy to install and use. It doesn't require databases
      or external systems.

    - Guild captures every detail about your run. Use this information
      to optimize your model, catch mistakes, and resolve issues.

In the [next section](/start/optimize.md), you use Guild's built-in
hyperparamter tuning features to find values for `x` that minimize
`loss` for the sample training script.
