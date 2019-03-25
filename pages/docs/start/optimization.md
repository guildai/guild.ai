tags: get-started

# Hyperparameter Optimization

In this guide, we look more closely at Guild's support for
[hyperparameter optimization
->](https://en.wikipedia.org/wiki/Hyperparameter_optimization). Specifically,
we look at a progession of techiques, starting with **grid search**
and **random search** and moving to more sophisticated methods using
**Bayesian algorithms**.

## Requirements

{!start-requirements-2.md!}

## Grid search

[Grid search
->](https://en.wikipedia.org/wiki/Hyperparameter_optimization#Grid_search)
--- also referred to as a *parameter sweep* --- is a form of
hyperparameter tuning that uses exhaustive search over a manually
defined set of hyperparameter values.

To perform a grid search in Guild, provide a list of values to use for
any given flag. If you specify lists for multiple flags, Guild runs
trials for each possible flag value combination.

If you haven't already done so, open a command console and change to
the `guild-start` directory: [^guild-start]

[^guild-start]: If you haven't created `guild-start` yet, follow the
steps in [](alias:quick-start) before processing.

``` command
cd guild-start
```

Run grid search over five values for *x*:

``` command
guild run train.py x=[-0.5,-0.4,-0.3,-0.2,-0.1]
```

``` output
You are about to run train.py in a batch
  noise: 0.1
  x: [-0.5, -0.4, -0.3, -0.2, -0.1]
Continue? (Y/n)
```

Press `Enter` to confirm the operation.

Guild runs `train.py` for each of the specified values.

Compare the current runs:

``` command
guild compare
```

Use your cursor keys to navigate to different columns. You can sort a
column in numeric ascending order by pressing the `1` key while the
cursor is in the column. For example, move to the far right column to
sort by *loss*.

Note the run with the lowest value for *loss*. Based on our function,
[^loss] loss should be lowest where *x* is near `-0.3`.

[^loss]: For background on the function generating *loss*, see
[](alias:quick-start).

!!! note
    Because the loss function introduces a random component
    ("noise") the lowest loss is not always where *x* is near `-0.3`.

Press `q` to exit the Compare application.

By default, Guild compares all runs --- you see runs in the list from
previous guides as well as the last five. To compare only the last
five runs, use:

``` command
guild compare 1:5 --table
```

This tells Guild to compare runs starting with index `1` (the latest
run) up to and including index `5`. The `--table` option runs the
command in non-interactive mode, printing the results to the console.

If you want to sort the results so that runs with the lowest loss
appear first, run:

``` command
guild compare --table --min loss
```

If you want to show only the top 3 runs, use:

``` command
guild compare --table --min loss --top 3
```

For a complete list of options, see the [](cmd:compare) command.

Next, run a search that includes two values for *x* and two values for
*noise*:

``` command
guild run train.py x=[-0.25,-0.30,-0.35] noise=[0.0,0.1]
```

This operation generates a total of 6 trials --- the Cartesian product
of the values specified for *x* and *noise*. We narrowed our range for
*x* based on our previous results, using both automated grid search
and intuition to find an optimal value for *x*.

!!! tip
    While Guild supports AutoML features, it still provides
    complete control over the model development process.

Press `Enter` to start the search.

After the 6 trials have completed, compare the runs:

``` command
guild compare --table --min loss
```

By now, we've accumlated enough runs to show that values of *x* near
`-0.3` are indeed optimal with respect to minimizing *loss*.

## Random search

Random search is a method used in machine learning to explore
hyperparamter spaces at random. Random search is a surprisingly
effective technique to find optimal hyperparameter values when you can
spend enough time searching.

For costly operations, consider [Bayesian
optimization](#bayesian-optimization) (shown below) as an alternative
to random search.

Guild performs a random search by default when you specify a flag
value in the form `[LOW:HIGH]`:

- The value must start and end with square brackets
- Low and high values may be either integer or float values and must
  be separated by a colon

!!! note
    The form `[LOW:HIGH]` is a short version of
    `uniform[LOW:HIGH]`, which samples from a uniform distribution.
    Guild also supports `loguniform`, which samples from a log-uniform
    distribution.

Run a random search over the range `-0.35` and `-0.25` for *x*:

``` command
guild run train.py noise=0 x=[-0.35:-0.25] --max-trials 5
```

``` output
You are about to run train.py with random optimizer (max 5 trials)
  noise: 0.1
  x: [-0.35:-0.25]
Continue? (Y/n)
```

We set *noise* to `0` so we can search for the true minimum loss.

When the operation is finished, compare the last 5 runs:

``` command
guild compare --table --min loss 1:5
```

The argument `1:5` tells Guild to show only runs starting with index
`1` and ending with index `5` --- i.e. the last five runs.

!!! note
    The argument `1:5` is applied before the list is sorted by
    *loss* so that the result shows the last 5 runs rather than the
    top 5 runs. To view the top 5 runs, replace use ``--top
    5`` instead of ``1:5``.

## Bayesian optimization

In the steps above, we used grid and random search methods to find
values for *x* that correspond with low *loss*. This illustrates a
common problem in machine learning: finding hyperparmeter values that
are optimal for a given model and data set.

Here's a plot that shows the relationship between *x* and *loss* for
our `train.py` script:

![](/assets/img/bayesian-optimization.png)

^ Relationship between hyperparameter *x* and *loss*&nbsp; [^plot]

[^plot]: Image credit: [Bayesian optimization with skopt
->](https://scikit-optimize.github.io/notebooks/bayesian-optimization.html)

Of course in a real scenario, we don't have this information! And
while we can use grid and random search to explore the search space of
*x*, practical machine learning application present two challenges:

- The search space across all hyperparameters is often too large to
  cover, even with substantial computing power.

- Large models, in particular neural networks, are expensive to
  evaluate, taking hours or even days to generate a single result.

To address the problem of hyperparameter optimization in these cases,
we turn to *Bayesian optimization*. Bayesian optimizers use light
weight models as surrogates for the target model --- surrogates that
can be evaluated quickly to recommend likely optimal hyperparameter
values --- and update those models using results from real
trials. [^optimization]

[^optimization]: For more complete coverage, see:<p>[Sequential
    Model-Based Optimization for General Algorithm Configuration
    ->](https://www.cs.ubc.ca/~hutter/papers/10-TR-SMAC.pdf) by Frank
    Hutter et al.<p>[A Tutorial on Bayesian Optimization
    ->](https://arxiv.org/abs/1807.02811)* by Peter Frazier.

Run `train.py` with Guild's built-in Bayesian optimizer, which uses a
Gaussian process:

``` command
guild run train.py x=[-2.0:2.0] --optimizer bayesian --max-trials 20
```

``` output
You are about to run train.py with gp optimizer (max 20 trials)
  noise: 0.1
  x: [-2.0:2.0]
Continue? (Y/n)
```

!!! note
    The argument `bayesian` in the command is an alias for `gp`,
    which is Bayesian optimizer that uses Gaussian processes. Note the
    use of `gp` in the command preview. Guild supports three Bayesian
    optimizers: `gp`, `forest` and `gbrt`. See below for more
    information on supported optimizers.

Press `Enter` to start the operation.

Guild runs 20 trials, each time using the results from previous trials
to suggest values of *x* that are more likely to minimize *loss*.

Note that we provide a wide range for *x*, not knowing (in this case,
pretending not to know!) where to search. We rely on the optimizer to
spend more time exploring high potential ranges to find a value for
*x* that minimizes *loss*.

When the operation is finished, compare the runs:

``` command
guild compare
```

Runs that are generated by the default Bayesian optimizer (i.e. using
Gaussian processes) are labeled starting with ``gp``. In some cases,
the optimizer recommends values that have already been tried, in which
case Guild intervenes and uses random values within the search space
--- these trials are labeled starting with ``gp+random``.

To sort a column in ascending order, navigate using the cursor keys to
the target column and press `1` --- e.g. use this technique to sort
runs by *loss* so that low values are listed first.

!!! note
    Bayesian methods are not guaranteed to find optimal values
    for *x*, though they can do reasonably well with enough trials. To
    ensure that you find optimal hyperparameters, you must use grid
    search, though as stated before, this is an intractable problem
    for large search spaces or expensive evaluations.

Guild supports three Bayesian optimizers, any of which can be
specified for the `--optimizer` command line option for the
[](cmd:run) command:

`gp`
: Uses Gaussian processes. You can alternatively use `bayesian` or
  `gaussian` to specify this optimizer.

`forest`
: Uses decision trees.

`gbrt`
: Uses gradient boosted regression tree.

!!! note
    Guild uses the excellent [Scikit-Optimize
    ->](https://scikit-optimize.github.io/) library for its built-in
    support of Bayesian optimization. Guild can further be extended
    to use your own optimizer and will be enhanced over time to
    support a wider range of optimizers.

Each optimizer has supports options that can be specified using `oF`
or `--opt-flag` options in the format ``--op-flag NAME=VALUE``. For
help with an optimizer, including a complete list of options, run
``guild OPTIMIZER --help-op``.

For example, to show help for the `gp` optimizer, run:

``` command
guild run gp --help-op
```

Feel free to experiment with different optimizers and optimizer
flags. For example, to run 20 trials using Gaussian proceses (i.e. the
`gp` optimizer) using *negative expected improvement* and an explicit
value for *noise*, use:

``` command
guild run train.py \
  x=[-2.0:2.0] \
  --optimizer gp \
  --opt-flag acq-func=EI \
  --opt-flag noise=0 \
  --label ei-1
```

This command includes the `--label` command line option, which helps
to identify trials associated with the optimization. You can filter
runs containing ``ei-1`` in the label this way:

``` command
guild compare --label ei-1
```

## Summary

In this guide we looked at three hyperparameter optimization techniques:

- Grid search
- Random search
- Bayesian optimization

## Next steps

{!start-manage-runs.md!}

{!start-image-classifier.md!}
