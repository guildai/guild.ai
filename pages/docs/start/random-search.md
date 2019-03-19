tags: get-started

# Random Search

In this guide, we examine Guild's support for performing *[random
search
->](https://en.wikipedia.org/wiki/Hyperparameter_optimization#Random_search)*.

[TOC]

## Requirements

{!start-requirements-2.md!}

## Random Search

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

Change to the `guild-start` directory: [^guild-start]

[^guild-start]: If you haven't created `guild-start` yet, follow the
steps in [](alias:quick-start) first).

``` command
cd guild-start
```

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

## Summary

In this guide we ran a simple *random search* over a narrow range for
*x*. Random search can be an effective way to find good and even
optimal hyperparameters, especially when used in conjunction with
[grid search](/docs/start/grid-search/) and [Bayesian
optimization](/docs/guides/bayesian-optimization/).

## Next Steps

{!start-manage-runs.md!}

{!start-image-classifier.md!}
