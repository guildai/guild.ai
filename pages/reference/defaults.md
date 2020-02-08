# Default Behavior

[TOC]

## Overview

This document describes the assumptions that Guild makes in the
absence of explicit configuration.

In general, Guild must know the following about an operation:

- [Flags interface](ref:flags-interface)
- List of [flags](ref:flags)
- [Output scalars](ref:output-scalars)

If this information is not defined explicitly in a [Guild
file](ref:guildfile), Guild attempts to infer the information using
rules based on what you run.

## Python Scripts

Unless otherwise configured in a Guild file, Guild makes some
assumptions when running Python scripts. This includes cases when a
script is run directly and when a script is defined using the `main`
operation attribute.

#### Flags Interface

If the `flags-dest` attribute, which specifies the [flags
interface](ref:flags-interface), is not defined for an operation,
Guild attempts to detect the interface by inspecting the operation
Python module.

- If the module imports the [`argparse` module
  ->](https://docs.python.org/library/argparse.html), Guild assumes
  that flags are set using command line arguments and uses ``args``
  for `flags-dest`.

- If the main module does not import `argparse`, Guild assumes that
  flags are defined in global variables and uses ``globals`` for
  `flags-dest`.

If you set `flags-dest` for an operation, Guild will inspect the
Python main module to infer the flags interface.

##### Example: Command Line Arguments

Consider the following Python module `train`:

``` python
import argparse

p = argparse.ArgumentParser()
p.add_argument("--learning-rate", type=float, default=0.1)
p.add_argument("--batch-size", type=int, default=100)

args = p.parse_args()

# Use args to train model, etc.
```

^ Module imports `argparse` --- Guild assumes `flags-dest` is ``args``

Unless `flags-dest` is configured for the operation, Guild inspects
the module and detects the import of `argparse` and uses ``args``.

``` yaml
train:
  flags-dest: args
```

^ Explicit `flags-dest` for `train`

##### Example: Global Variables

The following version of `train` does not import `argparse` but
instead defines flags as global variables.

``` yaml
learning_rate = 0.1
batch_size = 100

# Use globals to train model, etc.
```

Unless otherwise configured, when Guild inspects this module, it uses
``globals`` as the value for `flags-dest`.

``` yaml
train:
  flags-dest: globals
```

#### List of Flags

The list of operation flags is defined by the `flags` operation
attribute.

Guild infers the list of flags based on the *flags interface*.

If the interface is defined by `argparse



#### Output Scalars

If


## Keras Scripts
