title: Quick Start
pagenav_title: Quick Start
tags: get-started

# Guild AI Quick Start

In this quick start guide, we create a mock training script and run it
with Guild. The script doens't do any actual training, but illustrates
some basic features of Guild.

[TOC]

## Requirements

{!start-requirements.md!}

## Mock training script

The training script we create in this step doesn't actually train
anything, but instead simulates the training process of accepting
hyperparameters as inputs and generating a *[loss
->](https://en.wikipedia.org/wiki/Loss_function)*.

Create a new directory for the project:

``` command
mkdir guild-start
```

Create a file named `train.py`, located in the `guild-start`
directory:

``` python
import numpy as np

x = 0.1
noise = 0.1

loss = (np.sin(5 * x) * (1 - np.tanh(x ** 2)) + np.random.randn() * noise)

print("x: %f" % x)
print("noise: %f" % noise)
print("loss: %f" % loss)
```

^ guild-start/train.py

This mock script simulates a training operation:

- It has two mock hyperparameters: *x* and *noise*
- It calculates a mock *loss* using a "noisy" function [^noisy-credit]

[^noisy-credit]: Credit for "noisy" function: [Gilles Louppe, Manoj
    Kumar
    ->](https://scikit-optimize.github.io/notebooks/bayesian-optimization.html)

Verify that your project structure is:

<div class="file-tree">
<ul>
<li class="is-folder open">guild-start
 <ul>
 <li class="is-file">train.py</li>
 </ul>
</li>
</ul>
</div>

## Run `train.py` with Guild

In a command shell, change to the project directory:

``` command
cd guild-start
```

Run the mock training script `train.py` using Guild:

``` command
guild run train.py
```

Guild shows you a preview of the operation:

``` output
You are about to run train.py
  noise: 0.1
  x: 0.1
Continue? (Y/n)
```

Press `Enter` to confirm and start the operation.

Guild runs the script, which simply calculates a mock loss.

``` output
x: 0.100000
noise: 0.100000
loss: 0.456723
```

!!! note
    The "noisy" function applies a random component to *loss* so
    your result will be different.

Congratulations! You've run your first training script with
Guild. This generated a unique experiment, or a *run*. In the next
section, we examine what was created.

## Examine the run

List available runs by running:

``` command
guild runs
```

Guild shows the recent run for `train.py`:

``` output
[1:25835712]  train.py  2019-03-15 07:45:00  completed
```

The list shows each available run (in this case, we've only run
`train.py` once) with its ID, operation name, start time, and status.

!!! note
    In cases where Guild shows a run ID, the ID will be different
    in your case. That's because each run is assigned a globally
    unique ID to ensure that each run can be tracked as a unique
    experiment, even if it's copied to another system.

Next, show information for the run:

``` command
guild runs info
```

The command displays run details:

``` output
id: 25835712472011e98c3ec85b764bbf34
operation: train.py
status: completed
started: 2019-03-15 07:45:00
stopped: 2019-03-15 07:45:00
marked: no
label:
run_dir: ~/.guild/runs/25835712472011e98c3ec85b764bbf34
command: /usr/bin/python -um guild.op_main train --noise 0.1 --x 0.1
exit_status: 0
pid:
flags:
  noise: 0.1
  x: 0.1
```

Note a few things:

- Each experiment is uniquely identified with a unique ID
- Guild captures a wide range of experiment metadata
- All information associated with the run is stored on disk in a
  directory (see `run_dir` above)

## Train a second time

Run `train.py` again, this time with an explicit value for the
hyperparameter `x`:

``` command
guild run train.py x=0.2
```

Press `Enter` to confirm the operation.

Guild runs `train.py` a second time using the new value for `x`.

``` output
x: 0.200000
noise: 0.100000
loss: 0.817220
```

This demonstrates Guild's core feature: *running experiments*. We
[show later](/docs/start/optimization/) how this basic functionality
is used to automate runs using different sets of hyperparameters.

## Compare runs

Now that we have two runs, let's compare them:

``` command
guild compare
```

This starts [](alias:compare), which is a spreadsheet-like tool for
comparing and exploring runs.

The display should look something like this:

<img class="md terminal" src="/assets/img/compare-2.png" />

^ Comparing two runs --- press `q` to exit this screen

To find the run with the lowest *loss*, use the cursor keys to
navigate to the `loss` column and press `1`. The key `1` tells Guild
to sort the runs in numeric ascending order. For a complete list of
key bindings in Compare, type `?` (the question mark).

Press `q` to exit Guild Compare.

Next, run this command to show the runs sorted by *loss* in
non-interactive mode:

``` command
guild compare --table --min loss
```

The "best" run (i.e. the run with the lowest value for *loss* ---
though this is a contrived example) is listed first.

You can also generate output in CSV format to use in a spreadsheet:

``` command
guild compare --csv
```

## Summary

Contratulations, you've run your first training operation in Guild! It
was a mock training function (with no machine learning whatsoever <i
class="fal fa-smile"></i>) but served to highlight important features
in Guild:

- Run scripts without modification, automatically detecting
  hyperparameters and default values
- Capture each run as a unique experiment including metadata and
  training results
- View and compare results

Guild provides *a lot more* functionality on top of this core --- see
the links below to learn more!

## Next steps

{!start-optimization.md!}

{!start-manage-runs.md!}

{!start-image-classifier.md!}

{!start-reproducibility.md!}

{!start-backup-restore.md!}

{!start-remote-train.md!}
