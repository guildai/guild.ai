navbar_item: yes
tags: start

# Quick Start

## Install Guild AI

In an activated [virtualenv
->](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
or [conda
->](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
environment, install Guild AI by running:

``` command
pip install guildai
```

When Guild is installed, check the environment:

``` command
guild check
```

Refer to [Install Guild AI](install.md) for detailed install
instructions or [ask for help](ref:slack).

## Get Help

Guild is a command line tool. Commands are run using the format
``guild COMMAND``. Use the `--help` option to show information for a
command.

Show available commands:

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

See [Command Reference](commands/index.md) for online help.

## Create a Sample Training Script

Create a new directory:

``` command
mkdir guild-start
```

Change to the new directory:

``` command
cd guild-start
```

In the new directory, create a file named `train.py` that contains
this Python code:

``` python
import numpy as np

x = 0.1

loss = (np.sin(5 * x) * (1 - np.tanh(x ** 2)) + np.random.randn() * 0.1)

print("loss: %f" % loss)
```

^ Sample training script `train.py`

This script simulates a loss function. It accepts a hyperparameter `x`
and prints the resulting `loss`.

The new directory should look like this:

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
  x: 0.1
  Continue? (Y/n)
```

Press `Enter` to confirm.

Guild runs `train.py`, which prints a simulated loss. Guild lets you
run any unmodified script this way.

When Guild runs a script, it generates a new experiment, or
[run](term:run). Each run tracks experiment details including results.

List available runs:

``` command
guild runs
```

``` output
[1:91a5d7e1]  train.py  2019-09-17 06:19:40  completed
```

Information about each run is saved in a *run directory*, including
metadata and results. Guild [does not use databases](ref:no-databases)
to save results.

View information for the latest run:

``` command
guild runs info
```

``` output
id: 91a5d7e1adb54291a1cb2fab97cfac23
operation: train.py
from: ~/guild-start
status: completed
started: 2019-09-17 06:19:40
stopped: 2019-09-17 06:19:40
marked: no
label:
sourcecode_digest: 3b323a26ebfe99fbad95095d2b4adfd1
run_dir: ~/Env/guild-start/.guild/runs/91a5d7e1adb54291a1cb2fab97cfac23
command: ~/Env/guild-start/bin/python3.7 -um guild.op_main train --x 0.1
exit_status: 0
pid:
flags:
  x: 0.1
scalars:
  loss: 0.592545 (step 0)
```

^ Information captured by Guild --- your output will differ slightly

Guild provides a number of tools to leverage experiment data, which
you learn about later.

!!! highlight
    - No code changes
    - No system daemons (databases, web services, etc.)

## Search for Better Results

In the pervious step, you ran `train.py` with the default value for
`x` of 0.1. This results in a `loss` of approximately 0.5 (plus or
minus some random noise).

Let's try to find values `x` that result in lower `loss`.

Run ten new experiments:

``` command
guild run train.py x=uniform[-2.0:2.0] --max-trials 10
```

``` output
You are about to run train.py with random search (max 10 trials)
  x: uniform[-2.0:2.0]
Continue? (Y/n)
```

Press `Enter` to confirm.

Guild runs `train.py` ten times using different values for `x`. Values
are randomly sampled from a uniform distribution from -2.0 to
2.0. This is a [random search](term:random-search). Guild supports
other search types including [grid search](term:grid-search) and
[Bayesian optimization](term:bayesian-optimization). You use these in
later steps.

## Compare Runs

Compare your experiment results in a console-based spreadsheet
application:

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

^ Compare runs using parallel coordinates

!!! highlight
    Guild gives you tools to optimize your models.

    - Automate hyperparameter search
    - Study and compare results in various ways

## Next Steps

In this section, you ran a sample training script and compared results
using various methods.

In the next section, you use *grid search* and *Bayesian optimization*
to further explore the relationship between `x` and `loss`.
