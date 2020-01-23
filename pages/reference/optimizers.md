sidenav_title: Optimizers

# Optimizer Reference

[TOC]

## Overview

An *optimizer* is a Guild [batch operation](ref:batch) that attempts
to optimize an objective by adjusting flag values over a series of
trials.

Below is a list of supported optimizers.

[`gp`](#gp)
: Sequential optimizer using guassian processes.

[`forest`](#forest)
: Sequential optimizer using decision trees.

[`gbrt`](#gbrt)
: Sequential optimizer using gradient boosted regression trees.

[`random`](#random)
: Batch processor using randomly selected values.

Refer to [Optimizers](#optimizers) below for details on each
optimizer.

## Usage

Use the default optimizer for an operation by specifying the
`--optimize` option to [run](cmd:run). The default optimizer may be
specified in the operation definition.

Specify a named optimizer with the `--optimizer` option to
[run](cmd:run). A name may be one of the optimizers below or may be
the name of an optimizer defined for the operation.

Refer to help on [`optimizers` operation
attribute](/reference/guildfile.md#operation-optimizers) for details
on defining optimizers for an operation.

Optimizer flags may be set using `--opt-flag` or `-Fo`. Optimizer
flags are specified like other flags using the format ``NAME=VALUE``.

For example, run the default optimizer for `train`:

``` command
guild run train --optimize
```

Use the `forest` optimizer:

``` command
guild run train --optimizer forest
```

For more examples, see [Optimizers - Guild File
Cheatsheet](/cheatsheets/guildfile.md#optimizers).

## Optimizers

### gp

Bayesian optimizer using Gaussian processes.

Refer to [skopt API
documentation](https://scikit-optimize.github.io/#skopt.gp_minimize)
for details on this algorithm and its flags.

Aliases: `gaussian`, `bayesian`

Flags:

`acq-func`
: Function to minimize over the gaussian prior (default is `gp_hedge`)

    Choices:

    `LCB`
    : Lower confidence bound

    `EI`
    : Negative expected improvement

    `PI`
    : Negative probability of improvement

    `gp_hedge`
    : Probabilistically use LCB, EI, or PI at every iteration

    `EIps`
    : Negative expected improvement per second

    `PIps`
    : Negative probability of improvement per second

`kappa`
: Degree to which variance in the predicted values is taken into
  account (default is `1.96`)

`noise`
: Level of noise associated with the objective (default is `gaussian`)

    Use `gaussian` if the objective returns noisy observations,
    otherwise specify the expected variance of the noise.

`random-starts`
: Number of trials using random values before optimizing (default is `3`)

`xi`
: Improvement to seek over the previous best values (default is `0.05`)

### forest

Sequential optimization using decision trees. Refer to [skopt API
documentation](https://scikit-optimize.github.io/#skopt.forest_minimize)
for details on this algorithm and its flags.

Flags:

`kappa`
: Degree to which variance in the predicted values is taken into
  account (default is `1.96`)

`random-starts`
: Number of trials using random values before optimizing (default is
  `3`)

`xi`
: Improvement to seek over the previous best values (default is
  `0.05`)

### gbrt

Sequential optimization using gradient boosted regression trees.

Refer to [skopt API
documentation](https://scikit-optimize.github.io/#skopt.gbrt_minimize)
for details on this algorithm and its flags.

Flags:

`kappa`
: Degree to which variance in the predicted values is taken into
  account (default is `1.96`)

`random-starts`
: Number of trials using random values before optimizing (default is
  `3`)

`xi`
: Improvement to seek over the previous best values (default is
  `0.05`)

### random

Batch processor supporting random flag value generation.

Values are selected from the search space distribution specified for
each flag value.

This optimizer does not attempt to optimize an objective.

It does not support any flags.
