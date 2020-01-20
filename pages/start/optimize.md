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

When you change a model implementation or train on a new data set,
it's a good idea to optimize your training objective (e.g. *loss*,
*accuracy*, etc.) by tuning hyperparameters.

Guild supports hyperparameter optimization using various search
methods:

- Manual search
- [Grid Search ->](term:grid-search)
- [Random search ->](term:random-search)
- [Bayesian optimization ->](term:bayesian-optimization)

You use each of these methods below to find optimal values for `x`.

For review, here's the loss function used in `train.py`:

``` python
loss = (np.sin(5 * x) * (1 - np.tanh(x ** 2)) + np.random.randn() * noise)
```

The relationship between `x` and `loss` is plotted below. We know that
optimal values for `x` will be around -0.3. In a real scenario, we
don't know the optimal hyperparameter values.

![](/assets/img/bayesian-optimization.png)

^ Plot of `x` (horizontal axis) to `loss` (vertical axis) [^hparam-plot]

[^hparam-plot]: Image credit: [Bayesian optimization with skopt
    ->](https://scikit-optimize.github.io/notebooks/bayesian-optimization.html)

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
[1:1933bdcb]  train.py   2020-01-14 09:38:15  completed  noise=0.1 x=1
[2:83dc048d]  train.py   2020-01-14 09:38:14  completed  noise=0.1 x=0
[3:468bb240]  train.py   2020-01-14 09:38:14  completed  noise=0.1 x=-1
[4:bfcff413]  train.py+  2020-01-14 09:38:13  completed
[5:68f4da74]  train.py   2020-01-14 08:42:54  completed  noise=0.1 x=0.1
```

Run 4, named `train.py+`, is a [batch](term:batch) run and denoted by
a ``+`` in its name. Batch runs are responsible for running
trials. Runs 1 through 3 are the trials.

To compare `loss` across runs, use the [compare](cmd:compare) command:

``` command
guild compare --min loss
```

Guild starts an interactive application that lets you browse
experiment results. Runs with lower `loss` appear at the top of the
list. Use your arrow keys to navigate. Press `1` to sort by the
current column in ascending order or `2` to sort in descending
order. Press `?` for a list of supported commands.

![](/assets/img/compare-start.png)

^ Compare experiment results --- press `?` for a list of commands, `q`
  to exit

Exit Guild Compare by pressing `q`.

When you specify lists for more than one flag, Guild runs trials for
each flag value combination (the cartesian product of flag values).

The following command generates four runs --- one for for each unique
combination of flag values:

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

Show the top-3 best runs:

``` command
guild compare --table --min loss --top 3
```

The `--table` option tells Guild to show results without running in
interactive mode. The `--top` option tells Guild to show only the
top-N runs based on the sort order. In this case, we use `--min loss`
to sort by loss in ascending order.

Note that runs where `x` is `-0.5` have the lowest `loss`. This is
consistent with our expectation from the plot above.

Next, use TensorBoard to compare runs. Start TensorBoard using Guild
by running:

``` command
guild tensorboard
```

Guild starts TensorBoard and opens a new tab in your browser.

Select the **HPARAMS** tab and then select the **PARALLEL COORDINATES
VIEW** subtab.

## Grid Search

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

Guild opens TensorBoard in your browser.

Click the **HPARAMS** tab to compare run performance.

You can visualize the runs using **PARALLEL COORDINATES VIEW** and
**SCATTER PLOT MATRIX VIEW** by clicking the applicable tab.

![](/assets/img/tb-hparams.png)

^ Compare runs using Parallel Coordinates View --- click-and-drag over
  a vertical axis to highlight runs for a particular range of values
  (e.g. runs with the lowest loss)

The *Parellal Coordinates View* in particular is useful for
highlighting runs that perform better along various axes. For example,
click-and-drag along the `loss` axis to highlight runs with the lowest
values.

In addition to hyperparameters (`x` and `noise`) and generated metrics
(`loss`), Guild includes axes for `time` and `sourcecode`. The `time`
axis shows how long a run took to execute. Generally speaking, runs
that take less time are preferred to runs that take longer time, other
factors held constant. The `sourcecode` axis diffentiates source code
digests, helping to avoid hyperparameter comparisons across
potentially different model implementations.

## Grid Search

*Grid search* is a systematic search across a search space. If every
hyperparameter has a finite list of discrete values, it's possible to
conduct an exhaustive search over every combination of values, thereby
ensuring optimal values. However, in most cases, hyperparameters are
either continuous or it would take too long to conduct an exhaustive
search.

As you saw in the previous section, Guild supports *batch* runs for
sets of flag values. You can conduct grid searches by manually
specifying sets of flag values that cover the target search
space. Alternatively, you can use [flag sequence
functions](term:flag-sequence-function) to specify a sequence of
values.



## Random Search

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
