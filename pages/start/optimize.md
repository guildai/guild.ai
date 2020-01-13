tags: start

# Optimize a Model

[TOC]

## Overview

In the [previous section](/start.md) you run a sample training script
`train.py`. In this section, you run the same script with different
hyperparameter values to find lower values of `loss`. This process is
known as [hyperparameter optimization
->](term:https://en.wikipedia.org/wiki/Hyperparameter_optimization),
or hyperparameter tuning.

When you modify your model architecture or train on a new data set,
it's a good idea to optimize your model by tuning
hyperparameters. Guild makes this easy.

Guild supports hyperparameter optimization using various search
methods:

- Manual search
- [Random search ->](term:random-search)
- [Bayesian optimization ->](term:bayesian-optimization)

In this guide, you use each technique to find values for `x` that
minimize `loss`.

## Manual Search

When you are experimenting with hyperparameters, it's often useful to
try values based on experience or intuition.

Guild lets you run multiple trials in a batch by specifying them as a
list in the form ``[VAL1,VAL2,...VALN]``.

Run three trials of `train.py` using different values for `x`:

``` command
guild run train.py x=[-1,0,1]
```

``` output
You are about to run train.py as a batch (max 20 trials, minimize loss)
  noise: 0.1
  x: [-1, 0, 1]
Continue? (Y/n)
```

Press `Enter` to start the trials.

Guild runs `train.py` three times, once for each specified value of
`x`.

Show the runs:

``` command
guild runs
```

``` output
[1:be0f9be1]  train.py   2020-01-13 08:56:18  completed  noise=0.1 x=1
[2:77a92762]  train.py   2020-01-13 08:56:17  completed  noise=0.1 x=0
[3:a7802dc5]  train.py   2020-01-13 08:56:17  completed  noise=0.1 x=-1
[4:4cc17454]  train.py+  2020-01-13 08:56:16  completed
[5:629f7b73]  train.py   2020-01-13 07:27:20  completed  noise=0.1 x=0.1
```

Note that the runs list does not show `loss`. To compare loss across
runs, use the [compare](cmd:compare) command:

``` command
guild compare --min loss
```

Guild starts an interactive application that lets you browse
experiment results. Runs with lower `loss` appear at the top of the
list. Use your arrow keys to navigate. Press `1` to sort by the
current column (ascending) or `2` (descending).

![](/assets/img/compare-start.png)

^ Compare experiment results --- press `?` for a list of commands;
  press `q` to exit

Exit Guild Compare by pressing `q`.

You can specify multiple values for more than one flag. Guild runs
trials for all possible flag value combinations.

Run trials for multiple values of `x` and `noise` (the `noise` flag is
a second sample hyperparameter that determines how much random noise
is used when calculating the mock value for `loss`):

``` command
guild run train.py x=[-0.5,0.5] noise=[0.1,0.2]
```

``` output
You are about to run train.py as a batch (max 20 trials, minimize loss)
  noise: [0.1, 0.2]
  x: [-0.5, 0.5]
Continue? (Y/n)
```

Press `Enter` to start the trials.

Guild runs `train.py` four times, once for each of the four possible
combinations of the specified values.

Compare the results top 3 best runs:

``` command
guild compare --table --min loss --top 3
```

The `--table` option tells Guild to print the results as a table
without running in interactive mode. The `--top` option tells Guild to
show only the top-N results. In this case, we sort by `loss` so it
effecitvely shows the top 3 best runs.

## Random Search

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



---------------------------------------------------

OLD:

In [the previous section](/start.md) you ran a *random search* to
find optimal values for `x`. In this section, you use two other
methods: *grid search* and *Bayesian optimiation*.

For review, here's the loss function used in `train.py`:

``` python
loss = (np.sin(5 * x) * (1 - np.tanh(x ** 2)) + np.random.randn() * 0.1)
```

The relationship between `x` and `loss` is plotted below. We know that
optimal values for `x` will be around -0.3. In a real scenario, we
don't know the optimal hyperparameter values. We have to search for
them.

![](/assets/img/bayesian-optimization.png)

^ Plot of `x` (horizontal axis) to `loss` (vertical axis) [^hparam-plot]

[^hparam-plot]: Image credit: [Bayesian optimization with skopt
    ->](https://scikit-optimize.github.io/notebooks/bayesian-optimization.html)

## Grid Search

[Grid search](term:grid-search) --- also called a *parameter sweep*
--- tries specific values.

To perform a grid search, you could run separate commands for each
value of `x`. However, as you saw in [the previous
section](/start.md), Guild lets you run multiple trials with a
single command.

Run a search over three values of `x`:

``` command
guild run train.py x=[-2,0,2]
```

``` output
You are about to run train.py in a batch
  x: [-2, 0, 2]
Continue? (Y/n)
```

Press `Enter` to confirm.

Guild generates three runs, one for each specified value of `x`.

From the plot above, we expect the `loss` for these runs to be
approximately 0, which is not very close to the minimum.

## Bayesian Optimization

*Bayesian optimization* methods use light weight probabilistic models
that use results from previous runs to suggest promising
hyperparameter values.

Run ten trials using a Bayesian optimizer with gaussian processes:

``` command
guild run train.py --max-trials 10 --optimizer gp x=[-2.0:2.0]
```

``` output
You are about to run train.py with 'gp' optimizer (max 10 trials)
  x: [-2.0:2.0]
Continue? (Y/n)
```

Press `Enter` to confirm.

Guild generates ten trials. The optimizer uses past experience to
explore areas of the search space that have a higher probability of
minimizing `loss`.

With some luck (results are non-deterministic due to random effects),
the search will spend more time exploring values of `x` close to the
optimal value -0.3.

!!! highlight
    Guild uses a standard interface to run scripts using
    variety of methods: *single runs*, *grid search*, *random search*,
    and *Bayesian optimization*.

## Show the Best Runs

Show the five runs with the lowest values for `loss`:

``` command
guild compare --top 5 --min loss --table
```

The `--table` option tells Guild to print the results to standard
output rather than run interactively.

You can also save the comparison data as a CSV file.

``` command
guild compare --csv results.csv
```

## Next Steps

In this section, you ran a grid search and performed Bayesian
optimization to find optimal values of `x`.

In the next section, you learn about more about runs.
