tags: concept

# Flags

[TOC]

## Overview

Flags are user-specifies inputs to an operation. Flags may define any
type of information. They are commonly used for:

- Hyperparameters
- Data file locations
- Data set names

Flags are specified for an operation using ``NAME=VALUE`` arguments to
the [run](cmd:run) command.

The following command sets two flag values:

``` command
guild run train learning-rate=0.1 batch-size=100
```

Flags may also be defined in [batch files](def:batch-file).

## Flags Interface

TODO

## Flag Imports

### Flag Detection

### Import All Flags

### Import Some Flags

### Skip Some Flags

------------------------
OLD - need to merge ^
------------------------

## Flags Interface

XXX


## Explicit Flag Configuration

## Command Line Arguments

## Batch Files

## Special Flag Values

Guild supports a number of special flag value types that influence the
way Guild runs an operation.

[*Value list*](#value-lists)
: Used in manual searches to generate runs for a list of values.

[*Sequence function*](#sequence-functions)
: Used in grid search to generate a sequential list of values.

[*Search space function*](#search-space-functions)
: Used in random search and other optimizers to specify a search space.

Refer to the sections below for details on each flag value type.

### Value Lists

Value lists are specified in the format ``[VAL1,VAL2,...]`` where each
value is a number, a string, or boolean value.

If an optimizer is specified for a run (e.g. using the `--optimize` or
`--optimizer` option), a value list is treated as a search space
containing a discrete number of choices.

If an optimizer is not specified, a list of values indicates that a
run should be generated for each value appearing in the list. If a
list is specified for multiple flag, Guild runs the operation for each
unique combination of flag values.

The following command runs the `train` operation a total of *nine*
times --- one for each combination of flag values:

``` command
guild run train lr=[0.001,0.01,0.1] batch-size=[100,500,1000]
```

### Sequence Functions

Sequence functions are specified in the format ``NAME[ARGS]`` where
``NAME`` is one of the functions below and ``ARGS`` is a list of
values separated by a colon ``:``.

[`range`](#range)
: Specifies a range with *start*, *end*, and an optional step size.

[`linspace`](#linspace)
: Specifies an evenly spaced sequence along a linear scale with
  *start*, *end*, and an optional value count.

[`logspace`](#logspace)
: Specifies an evently spaced sequence along a log-linear scale with
  *start*, *end*, an optional value count, and an optional logarithmic
  base.

Refer to the sections below for details on each function.

#### `range`

Usage:

    range[START:END:STEP=1]

Generates a list of values starting with `START` and ending with `END`
in increments of `STEP`. `STEP` may be omitted, in which case the
value `1` is used.

*Example*
: *Sequence*

`range[1:4]`
: `[1, 2, 3, 4]`

`range[1:4:2]`
: `[1, 3]`

`range[0:0.3:0.1]`
: `[0.0, 0.1, 0.2, 0.3]`

#### `linspace`

Usage:

    linspace[START:END:COUNT=5]

Generates `COUNT` values that are evenly spaced between `START` and
`END` inclusively.

*Example*
: *Sequence*

`linspace[1:5]`
: `[1.0, 2.0, 3.0, 4.0, 5.0]`

`linspace[1:5:3]`
: `[1.0, 3.0, 5.0]`

#### `logspace`

Usage:

    logspace[LOW:HIGH:COUNT=5:BASE=10]

Generates `COUNT` values along a logarithmic scale between `BASE ^
LOW` and `BASE ^ HIGH` inclusively.

*Example*
: *Sequence*

`logspace[1:5]`
: `[10.0, 100.0, 1000.0, 10000.0, 100000.0]`

`logspace[0:4:3]`
: `[1.0, 100.0, 10000.0]`

`logspace[-4:-1:4]`
: `[0.0001, 0.001, 0.01, 0.1]`

`logspace[0:2:3:2]`
: `[1.0, 2.0, 4.0]`

### Search Space Functions

Search space functions are specified in the format ``NAME[ARGS]``
where `ARGS` is a list of values separated by a colon.

[`uniform`](#uniform)
: Specifies a uniform distrbution over a range of values

[`loguniform`](#loguniform)
: Specifies a log-uniform distribution over a range of values.

Refer to the sections below for details on each function.

#### uniform

    uniform[START:END]

Alternative syntax (omits function name):

    [START:END]

Search space from `START` to `END` from a uniform distribution.

#### loguniform

    loguniform[START:END]

Search space from `START` to `END` from a log-uniform distribution.

## Flag Value Types

TODO: merge smartly




## Flag Value Decoding

TODO: Need to merge smartly above

Guild uses the [YAML spec ->](https://yaml.org/spec/) for decoding
strings to values.

Below are examples of various conversions.

| String Value | Decoded Type |
|--------------|--------------|
| hello        | string       |
| 1            | int          |
| 1.0          | float        |
| 1e2          | float        |
| '1e2'        | string       |
| [1,2,3]      | list         |

Guild provides an exception in cases where a string that appears to be
a run ID but would otherwise be treated by YAML as scientific
notation.

| String Value | Decoded Type |
|--------------|--------------|
| 1e10         | string       |
| 67217e15     | string       |

In cases where a flag must interpret these values as floats, specify
the `type` attribute as `float` for the flag definition.

For example:

``` yaml
train:
  flags:
    learning-rate:
      type: float
```

In this case, Guild will explicitly decode string input to `float`.


## Python Global Variables

TODO: merge into above where it belongs

Guild is designed to avoid changes to your code.
