tags: concept

# Guild Files

[TOC]

## Overview

Guild files are named `guild.yml` and are located in project
directories. They provide information about your project.

- How to run scripts to generate experiments (operations)
- Input parameters to the script (flags)
- Generated output metrics (scalars)
- Required source code
- Requires input files (dependencies)

See [Get Started - Add a Guild File](start/guildfile.md) for a
hands-on exercise in using a Guild file for a simple project.

See [Guild File Reference](reference/guildfile.md) for a complete list
of configuration options.

See [Guild File Cheatsheet](cheatsheets/guildfile.md) for
configuration examples.

While Guild can run a script directly without explicit configuration,
in such cases Guild makes assumptions about how to run the script. For
systematic machine learning workflows, we recommend using Guild files
to formally define your project operations.

## Operations

An *operation* defines what Guild executes to for a run.

Here's a simple operation, defined in a Guild file:

``` yaml
train:
  main: train
  flags:
    learning-rate: 0.1
    batch-size: 100
```

- The operation is named `train` and can be run using ``guild run train``.

- The main Python module, also named `train`, can be defined in a file
  named `train.py` in the same directory as `guild.yml`.

- The operation defines two flags: `learning-rate` and `batch-size`,
  each with default values.

You can run the operation from a command terminal by changing to the
directory containing `guild.yml` (the project directory) and running:

``` command
guild run train
```

Guild shows a preview of the flags used for the operation and asks you
to confirm the operation by pressing `Enter`. When you confirm the
operation, Guild executes the `train` module with the specified flag
values. Guild generates a *run*, which is a record of the operation
inputs and outputs.

For information about managing runs, see [Runs](runs.md).

### Python Based Operation

### Other Language Based Operations

### Workflows

### Flags

TODO:

- Used as inputs to a run
- Can be defined in both in the script and in the guild file
- Definition in Guild file redefines any imported defs
- Behavior can be disabled for explicit control and to avoid scanning
  scripts

### Source Code

TODO

### Output Scalars

Output scalars are logged scalars generated from script output. Guild
uses regular expressions to match output and associate values with
keys.

By default, Guild looks for the pattern ``^(\key): (\value)``.

`^`
: Indicates the pattern must occur at the start of the line.

`(\key)`
: Captures a pattern matching a legal scalar key.

`(\value)`
: Captires a pattern matching a legal scalar value (a number).

Consider the following output:

``` output
Hello
x: 1.0
y: 2.0
 z: 3.0
```

With the default output scalar configuration, Guild logs the following
scalars:

| key | value | step |
|-----|-------|------|
| `x` | 1.0   | 0    |
| `y` | 2.0   | 0    |

Guild does not log `z` because the line starts with a space.

Note that Guild uses a step value of 0. This value can be controlled
by setting the special key `step`. See [Scalar Step](#scalar-step)
below for more information.

In some cases, Guild applies additional rules to capture scalars
logged by known frameworks. Refer to [Framework
Scalars](#framework-scalars) below for more information.

The sections that follow describe how you can configure Guild's output
scalar behavior.

#### Scalar Step

When logging scalars, Guild associates each value with a current
*step*. This lets you log several values for a key over a number of
steps. For example, it's common to log training *loss* at various
steps during the run.

Guild uses the special scalar key `step` to denote the step used when
logging other scalars.

Consider the following output:

``` output
step: 1
loss: 1.0
step: 2
loss: 0.2
steP: 3
loss: 0.1
```

Using Guild's default capture rule (see above), Guild would log the
following scalar values.

| key | value | step |
|-----|-------|------|
| `x` | 1.0   | 1    |
| `x` | 0.2   | 2    |
| `x` | 0.1   | 3    |

#### Custom Output Scalars

Configure output scalars for an opertion by defining a
`output-scalars` attribute. Guild supports two schemes:

- Pattern mapping
- Pattern list

A pattern mapping associates patterns with scalar keys. Pattern
mappings work well when you have a fixed set of scalars that you want
to capture, and you want to ignore everything.

The following configuration captures scalars using a pattern mapping.

``` yaml
train:
  output-scalars:
    loss: 'Loss: (\value)'
    accuracy: 'Accuracy: (\value)'
    step:
```

#### Disable Output Scalars

If you want to log scalars explicitly (e.g. using a [TensorFlow
summary writer
->](https://www.tensorflow.org/api_docs/python/tf/summary/FileWriter))
you can disable Guild's output summary support by setting
`output-scalars` to `off`.

``` yaml
train:
  output-scalars: off
```

You can control how

#### Keras Scalars

By default, Guild applies the following patterns when running Keras
operations:

`Epoch (?P<step>[0-9]+)`
: Captures `step`

    r" - ([a-z_]+): (\value)"

### Dependencies

TODO

## Models

TODO

## Resources

TODO

## Packages

TODO

## Resuable Config

TODO

## Inheritance

## Including Files
