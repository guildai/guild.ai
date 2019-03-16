title: Quick Start
pagenav_title: Quick Start
tags: get-started

# Guild AI Quick Start

## Requirements

{!start-requirements.md!}

## A mock training script

In this quick start guide, you create a mock training script and run
it with Guild. The script doens't do any actual training, but
illustrates some basic features of Guild.

Frist, create a new directory for the project:

``` command
mkdir simple-project
```

Create a file named `train.py`, located in the `simple-project`
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

^ sample-project/train.py

This mock script simulates a training operation:

- It has two mock hyperparameters: *x* and *noise*
- It calculates a mock *loss* using a "noisy" function [^noisy-credit]

[^noisy-credit]: Credit for "noisy" function: [Gilles Louppe, Manoj Kumar ->](https://scikit-optimize.github.io/notebooks/bayesian-optimization.html)

Verify that your project structure is:

<div class="file-tree">
<ul>
<li class="is-folder open">sample-project
 <ul>
 <li class="is-file">train.py</li>
 </ul>
</li>
</ul>
</div>

## Run `train.py` with Guild

In a command shell, change to the project directory:

``` command
cd simple-project
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

Press `Enter` to confirm the operation.

Guild runs the script, which simply calculates a mock loss.

``` output
x: 0.100000
noise: 0.100000
loss: 0.456723
```

!!! note
    Because the "noisy" function introduces a random component,
    your result will be different.

Congratulations! You've run your first training script with
Guild. This generated a unique experiment, or a *run*.

## Examine the run

In a command shell, run:

``` command
guild runs
```

This command lists available runs.

``` output
[1:25835712]  train.py  2019-03-15 07:45:00  completed
```

The list displays a single run with *ID*, *operation name* (i.e. the
script name), *start time*, and *status*.

!!! note
    In cases where Guild shows a run ID, the ID will be
    different in your case. That's because each run is assigned a
    globally unique ID to ensure that each run can be tracked as a
    unique experiment, even if it's copied to another system.

    Similarly, dates and time will differ.

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

We learn more about these details later.

Next, list files generated for the run:

``` command
guild ls
```

This command lists files associated with the run:

``` output
~/.guild/runs/25835712472011e98c3ec85b764bbf34
```

In our mock training script, we don't generate any files so the list
is empty. We generate files in later examples so knowing this command
is useful.

## Train a second time

Run `train.py` again, but with an explicit value for the
hyperparameter `x`:

``` command
guild run train.py x=0.2
```

Guild shows a preview of the run. Press `Enter` to continue.

Guild runs `train.py` a second time using the new value for `x`.

``` output
x: 0.200000
noise: 0.100000
loss: 0.817220
```

This demonstrates Guild's core feature: *running experiments*. We
later show how this basic functionality is used to build better models
in less time!

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
key bindings in Compare, press `?` (question mark).

Press `q` to exit Guild Compare.

## Run Bayesian optimization

You've seen Guild's ability to run a script and capture results for
comparison. This is Guild's core functionality, but it only starts
there. In this step you'll use Guild to automate a common practice:
hyperparameter optimization.

Our mock training script takes two (rather contrived) hyperparameters:
*x* and *noise*. Let's try to find a value for *x* that minimize
*loss*.

Because we're using a simple function to simulate a training
operation, we can plot the relationship between *x* and *loss* for a
given value of *noise*. It looks something like this:

![](/assets/img/bayesian-optimization.png)

^ Relationship between hyperparameter *x* and *loss* [^plot]

[^plot]: Credit for "noisy" plot: [Bayesian optimization with skopt ->](https://scikit-optimize.github.io/notebooks/bayesian-optimization.html)

From the plot, we can see that the true minimum for *loss* is where is
around `-0.3`.

In real life of course we don't know this! So we run experiments to
find (or to confirm) the hyperparameters that give us the best result.

Let's use Guild's built-in Bayesian optimizer to multiple trials over
a range of *x* with the goal of minimizing loss:

``` command
guild run train.py x=[-2.0:2.0] --optimizer bayesian
```

Guild prompts with:

``` output
You are about to run train.py with gp optimizer (max 20 trials)
  noise: 0.1
  x: [-2.0:2.0]
Continue? (Y/n)
```

Press `Enter` to start the operation.

Guild runs twenty trials (the default number if the command line
option `--max-trials` is not specified), each time with a different
value for over the range <code>-2.0</code> to <code>2.0</code>.

When the operation is finished, view the top five runs to see which
values for *x* perform better:

``` command
guild compare --top 5 --min loss --table
```

The `--table` option tells Guild to print the results as a table
rather than run the interactive spreadsheet application.

You should see that loss is lowest when *x* is near `-0.3`.

!!! note
    The *noise* parameter introduces random "noise" to the loss
    function, so results vary across runs.

## Summary

Contratulations &mdash; you've run your first training operation in
Guild! It was totally fake, but it served to illustrate some important
features in Guild:

- Runs scripts without modification, automatically detecting
  hyperparameters and default values
- Capture each run as a unique experiment
- View and management experiments
- Optimize hyperparameters with a single command

## Next Steps

To continue learning about Guild, select one of the Get Started guides
below.

{!start-grid-search.md!}

{!start-random-search.md!}

{!start-reproducibility.md!}

{!start-image-classifier.md!}
