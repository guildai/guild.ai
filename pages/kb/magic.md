# Magic

[TOC]

## Overview

Guild AI generally adheres to the principles outlined in Tim Peter's
 [PEP 20 -- The Zen of Python
 ->](https://www.python.org/dev/peps/pep-0020/). One of those
 principles is:

> Explicit is better than implicit.

In some cases Guild goes out of its way to support *implicit*
behavior, some of which could be [considered magic
->](https://en.wikipedia.org/wiki/Magic_(programming)).

Magic hides complexity and removes barriers to getting started. When
magic causes unwanted results, its limitations can outweigh its
benefits.

In cases where Guild performs magic, it offers a path to change the
implicit behavior through explicit configuration.

The sections below discuss cases where Guild performs magic and how to
change the behavior.

## Import Flags

By default, Guild AI attempts to detect and import script flags. In
some cases Guild gets this wrong. When it does, you can configure
flags in a [Guild File](ref:guildfiles).

### Motivation

Guild AI attempts to remove barriers to experiment tracking. It's time
consuming to write configuration files and so Guild doesn't require
configuration to start. When you need to be explicit, you can add
configuration in small steps as needed.

### Implementation

Guild inspects the script associated with an operation. It detects
flags in one of two ways. If the script uses Python's
[](pylib:argparse) module, Guild assumes that flags are defined by an
`ArgumentParser` instance. If the script does not use `argparse`,
Guild assumes that script flags are defined as global variables.

In cases where `argparse` is used, Guild runs the script with the
`--help` option and detects parameters that are added to parsers.

To detect global variables, Guild inspects the script for global
assignments of numbers, strings, named constants, `True`, `False`, and
`None`. Guild skips variable names that start with an underscore.

Consider this Python script:

```
import model

data = "iris"
num_classes = 3
learning_rate = 0.1
batch_size = 100

model.train(data, num_classes, learning_rate, batch_size)
```

Because the script does not import `argparse`, Guild inspects the
script's global assignments and finds four.

### Import Specific Flags

In the example above, there are two global variables that a user would
likely want to change: `learning_rate` and `batch_size`. The other two
variables, `data` and `num_classes`, are used in the training
function, but they should not be changed by the user.

To explicitly define the the flags for an operation, use a Guild
File. To import a list of flags, use `flags-import` in the operation
definition:

``` yaml
train:
  flags-import:
    - learning_rate
    - batch_size
```

### Don't Import Specific Flags

Alternatively, you can tell Guild *not* to import the two variables
that aren't flags:

``` yaml
train:
  flags-import-skip:
    - data
    - num_classes
```

### Disable Import Flags

By default, Guild inspects an operation script for flags. Guild caches
the results and updates them when the script changes. Guild is reading
flag information when you see the message:

``` output
Refreshing flags...
```

You can disable the inspection using `flags-import: no` in the Guild
File:

``` yaml
train:
  flags-import: no
```

In this case, you must define each flag explicitly:

``` yaml
train:
  flags-import: no
  flags:
    learning_rate: 0.1
    batch_size: 100
```

## Set Global Variables

When configured to use global variables (see [Import
Flags](#import-flags) above) Guild sets variables to the values of
associated flags.

Consider the following Python script `printx.py`:

``` python
x = 1
print(x)
```

When run directly with Python, the script always prints the value `1`:

``` command
python printx.py
```

``` output
1
```

If you run the script with Guild, specifying a value for `x`, the
script prints the value of `x`:

``` command
guild run printx.py x=2
```

``` output
2
```

Guild sets new values for global variables without requiring changes
to source code.

### Motivation

Guild AI tracks machine learning experiments and does so without
requiring changes to your code. [Dependencies](dependencies.md)
describes the benefit to this approach.

Because a number of machine learning scripts are written without
support for command line interfaces, Guild supports script
configuration by way of global variables. This avoids the need to
modify source code and simplifies the integration of Notebooks.

### Implementation

Guild sets global variables when it runs a script by using a simple
techique:

1. Guild removes applicable global assignments from the script AST.

2. Guild executes the script with a globals namespace containing flag
   values.

This is implemented in the `exec_function` of Guild's
[`python_util`](https://github.com/guildai/guildai/blob/master/guild/python_util.py)
module.

Guild defines a global variable as any assignment to a name defined in
the script root of a number, string, named constant, `True`, `False`,
and `None`. Guild will not attempt to modify variables that are
assigned any other type including other variables, functions, dicts,
and lists.

### Use a Command Line Interface

If a script uses a command line interface using Python's
[](pylib:argparse) module, Guild does not modify global variables.

Consider a modified version of `printx.py` that uses a command line
interface instead of global variables:

``` python
import argparse

p = argparse.ArgumentParser()
p.add_argument("--x", default=1, type=int, help="val to print")

args = p.parse_args()

print(args.x)
```

When you run the script without any arguments, it prints `1` as
before:

``` command
python printx.py
```

``` output
1
```

However, you can now specify values of `x` when running the script:

``` command
python printx.py --x 2
```

``` output
2
```

The script has an *explicit* interface:

``` command
python printx.py --help
```

``` output
usage: printx.py [-h] [--x X]

optional arguments:
  -h, --help  show this help message and exit
  --x X       val to print
```

Guild detects the use of `argparse` in the script and uses script
arguments to set values of `x`. This removes the magic of setting
global variables.

``` command
guild run printx.py x=3
```

``` output
3
```
