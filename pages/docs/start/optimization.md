tags: get-started

# Hyperparameter Optimization

In this guide, we look more closely at Guild's support for
[hyperparameter optimization
->](https://en.wikipedia.org/wiki/Hyperparameter_optimization). Specifically,
we look at a progession of techiques, starting with grid search and
random search and moving to more sophisticated methods using Bayesian
algorithms.

[TOC]

## Requirements

{!start-requirements-2.md!}

## Grid search

[Grid search
->](https://en.wikipedia.org/wiki/Hyperparameter_optimization#Grid_search)
--- also referred to as a *parameter sweep* --- is a form of
hyperparameter tuning that uses exhaustive search over a manually
defined set of hyperparameter values.

To perform a grid search in Guild, simply provide a list of values to
use for any given flag. If you specify lists for multiple flags, Guild
runs trials for each possible flag value combination.

To illustrate, first change to the `guild-start` directory:
[^guild-start]

[^guild-start]: If you haven't created `guild-start` yet, follow the
steps in [](alias:quick-start) first.

``` command
cd guild-start
```

Run a grid search over five values for *x*:

``` command
guild run train.py x=[-0.5,-0.4,-0.3,-0.2,-0.1]
```

Press `Enter` to confirm the operation.

Guild runs `train.py` for each of the specified values.

Compare the last five runs:

``` command
guild compare 1:5 --table --min loss
```

This command tells Guild to compare runs from index `1` to index `5`
(the last five runs) sorted in ascending order by *loss*. Note that
the loss is lowest where `x=-0.3`&nbsp; [^loss]

[^loss]: For background on the function generating *loss*, see
[](alias:quick-start).

Next, run a search that includes two values for *x* and two values for
*noise*:

``` command
guild run train.py x=[-0.25,-0.30,-0.35] noise=[0.0,0.1]
```

This operation generates a total of 6 trials --- the Cartesian product
of the values specified for *x* and *noise*.

Press `Enter` to start the grid search.

After the 6 trials have completed, compare them by running:

``` command
guild compare 1:6 -T -m loss
```

Here are each of the arguments to [](cmd:compare) and what they mean:

`1:6`
: Compare runs starting with index `1` and ending with index `6`

`-T`
: Print results as a table rather than run as an interactive
  application (short form of ``--table``)

`-m loss`
: Sort results by the `loss` column in ascending order (short form of
  ``--min loss``)

## Random search

Random search is a method used in machine learning to explore
hyperparamter spaces at random. Random search is a surprisingly
effective technique to find optimal hyperparameter values when you can
spend enough time searching.

For costly operations, consider [Bayesian
optimization](/docs/guides/bayesian-optimization/) as an alternative
to random search.

Guild performs a random search whenever you specify a flag value in the form `[LOW:HIGH]`:

- The value must start and end with square brackets
- Low and high values may be either integer or float values and must
  be separated by a colon

!!! note
    The form `[LOW:HIGH]` is a short version of
    `uniform[LOW:HIGH]`, which samples from a uniform distribution.
    Guild also supports `loguniform`, which samples from a log-uniform
    distribution.

Run a random search over the range `-0.4` and `-0.2` for *x*:

``` command
guild run train.py noise=0 x=[-0.4:-0.2]
```

``` output
You are about to run train.py with random optimizer (max 20 trials)
  noise: 0.1
  x: [-0.4:-0.2]
Continue? (Y/n)
```

We set *noise* to `0` so we can search for the true minimum loss.

List the best 5 runs over the last 20 runs:

``` command
guild compare 1:20 -T -m loss -t 5
```

The arguments to [](cmd:compare) are:

`1:20`
: Compare runs starting with index `1` and ending with index `20` ---
  i.e. the last 20 runs

`-T`
: Print results as a table rather than run as an interactive
  application (short form of ``--table``)

`-m loss`
: Sort results by the `loss` column in ascending order (short form of
  ``--min loss``)

`-t 5`
: Show the top five runs

This is a fairly complex command, though it shows the flexibility of
the `compare` command. If you prefer, simply run ``guild compare`` and
iteratively explore the current list of runs. This will include runs
from previous guides.

## Bayesian optimization

You've seen Guild's ability to run a script and capture results for
comparison. In this step we use Guild to automate a common practice:
*hyperparameter optimization*.

Our mock training script takes two (slightly contrived)
hyperparameters: *x* and *noise*. Let's try to find a value for *x*
that minimize *loss*.

Because we're using a simple function to simulate a training
operation, we can plot the relationship between *x* and *loss* for a
given value of *noise*. It looks something like this:

![](/assets/img/bayesian-optimization.png)

^ Relationship between hyperparameter *x* and *loss*&nbsp; [^plot]

[^plot]: Image credit: [Bayesian optimization with skopt
->](https://scikit-optimize.github.io/notebooks/bayesian-optimization.html)

From the plot, we can see that the true minimum for *loss* is where is
around `-0.3`.

In real life of course we don't know this! So we run experiments to
find (or to confirm) the hyperparameters that give us the best result.

Use Guild's built-in Bayesian optimizer to multiple trials over a
range of *x* with the goal of minimizing loss:

``` command
guild run train.py x=[-2.0:2.0] --optimizer bayesian
```

``` output
You are about to run train.py with gp optimizer (max 20 trials)
  noise: 0.1
  x: [-2.0:2.0]
Continue? (Y/n)
```

Press `Enter` to start the operation.

Guild runs 20 trials --- the default number if the command line option
`--max-trials` is not specified --- each time with a different value
for *x* over the range <code>-2.0</code> to <code>2.0</code>.

When the operation is finished, view the top five runs to see which
values for *x* perform better:

``` command
guild compare --top 5 --min loss --table
```

The `--table` option tells Guild to print the results as a table
rather than run the interactive spreadsheet application.

You should see that loss is lowest when *x* is near `-0.3`. If the
search process didn't find minimums around this value, you can restart
the Bayesian optimization operation to run for another 20 trials by
running:

``` command
guild run --restart gp
```

Guild picks up where it left off, using the 20 previous trials as data
for minimizing loss.

!!! note
    The value `gp` in the restart command is the name of the
    Bayesian optimizer operation --- Guild restarts the last operation
    with this name. You can alternatively specify the run ID with
    `--restart`.

## Summary

In this guide we looked at three hyperparameter optimization techniques:

- Grid search
- Random search
- Bayesian optimization

## Next steps

{!start-manage-runs.md!}

{!start-image-classifier.md!}
