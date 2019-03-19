tags: get-started

# Grid Search

In this guide, we examine Guild's support for performing *[grid search
->](https://en.wikipedia.org/wiki/Hyperparameter_optimization#Grid_search)*.

[TOC]

## Requirements

{!start-requirements-2.md!}

## Grid Search

Grid search --- also referred to as a *parameter sweep* --- is a form
of hyperparameter tuning that uses exhaustive search over a manually
defined set of hyperparameter values.

Grid search in Guild is easy --- simply provide a list of values to
use for any given flag. If you specify lists for multiple flags, Guild
runs trials for each possible flag value combination.

Change to the `guild-start` directory: [^guild-start]

[^guild-start]: If you haven't created `guild-start` yet, follow the
steps in [](alias:quick-start) first).

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

## Summary

In this guide we ran a simple *grid search* --- generating trials over
a narrow search space for two hyperparameters. While our training
operation is contrived, the process illustrates a useful tool in
machine learning, which is to explore manually defined hyperparameter
sets.

## Next Steps

{!start-random-search.md!}

{!start-manage-runs.md!}

{!start-image-classifier.md!}
