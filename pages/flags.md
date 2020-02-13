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

Flags may also be defined in [batch files](#batch-files).

## Flags Interface

Guild makes flag values available to a script using a *flags
interface*. Guild supports different interfaces:

- Command line arguments
- Environment variables
- Python global variables

Guild works across platforms and languages using standard interfaces
when possible. Guild does not require changes to script code to
support Guild-specific flag configuration. Guild uses script
inspection and explicit configuration in [Guild files](term:guildfile)
to get flag information.

When Guild does not have explicit configuration (e.g. when a script is
run directly) it attempts to infer the flags interface by inspecting
the script. See [*Default Behavior - Flags
Interface*](/reference/defaults.md#flags-interface) for more
information.

The flags interface is configured for an operation using the
`flags-dest` attribute. See [`flags-dest` in *Guild File
Reference*](/reference/guildfile.md#operation-flags-dest) for
configuration details.

For example of different interfaces, see [*Guild File Cheatsheet -
    Flags Interface*](/cheatsheets/guildfile.md#flag-interface).

### Command Line Arguments

Unless otherwise configured (or inferred by inspecting the script),
Guild uses a command line interface to pass flag values to a script.

This interface can be explicitly configured by setting `flags-dest` to
`args`.

Flag values are included as command line arguments using the format:

```
--FLAG_ARG_NAME ENCODED_FLAG_VALUE
```

By default, `FLAG_ARG_NAME` is the flag name. If the `arg-name`
attribute is specified for a flag definition, Guild uses the attribute
value instead.

`ENCODED_FLAG_VALUE` is the JSON-encoded flag value.

Each non-null flag value is specified as arguments following this
format.

Consider the following command:

``` command
guild run train.py learning-rate=0.1 batch-size=100
```

Guild passes the two flag values to `train.py` this way:

``` command
python -m train --learning-rate=0.1 --batch-size=100
```

The following Guild file configuration changes the argument names for
each flag:


``` yaml
train:
  flags:
    learning-rate:
      arg-name: lr
    batch-size:
      arg-name: bs
```

!!! tip
    Use the `--print-cmd` option with [run](cmd:run) to print the
    full command Guild uses when running an operation. This command
    includes the flag related options as described above.

### Environment Variables

Guild makes flag values available as environment variables to each run
process. Environment variables are named ``FLAG_<upper case flag
name>``.

For example, the value for flag `x` can be read as environment
variable named ``FLAG_X``.

Use the `env-name` attribute to specify a different environment
variable name for a flag.

For example, the following configuration tells Guild to convey `x`
using the environment variable ``X`` instead of ``FLAG_X``.

``` yaml
op:
  flags:
    x:
      env-name: X
```

!!! tip
    Use environment variables from non-Python scripts as a
    convenient way to read flag values without having to process
    command line arguments.

### Python Global Variables

Guild sets flag values as global variables in a Python script when
`flags-dest` is set to ``globals`` or when Guild otherwise [detects
this interface through
inspection](/reference/defaults.md#flags-interface).

Guild only sets global variables when they are already defined in a
script. Guild does not create new variables in a script.

The following operation uses a global variables interface to set
values for flags `x` and `y`:

``` yaml
train:
  flags-dest: globals
  flags-import: [x, y]
```

Here is a Python script that uses `x` and `y`:

``` python
x = 1
y = 2

print("z: %i" % (x + y))
```

^ `train.py` using global variables for flags

You can alternatively set flag values in a Python global dict variable
``global:<variable name>`` for `flags-dest`.

The following configuration sets flag values as items in the `params`
global variable.

``` yaml
train:
  flags-dest: global:params
  flags-import: [x, y]
```

The following Python script shows how `train` might be implemented
using `params`:

``` python
params = {"x": 1, "y": 2}

print("z: %i" % (params["x"] + params["y"]))
```

^ `train.py` using global `param` dict for flags

The variable specified using ``global:<variable>`` must be defined in
the Python module. Guild does not define new variables in modules.

## Import Flags

To avoid duplicating flag definitions in scripts and in Guild files,
Guild lets you *import* flag definitions.

### Flag Detection

To import flags, Guild must inspect a script and look for possible
flag definitions based on the [flags interface](#flags-interface). As
described above, the flags interface may be explicitly
configured. Otherwise Guild attempts to infer the interface.

Guild uses the rules below for inferring flags according to the
specified interface.

*Interface*
: *Flag Detection Method*

`args`
: Guild runs the script with the `--help` option and inspects
  `argparse` generated option. From this Guild infers flag name,
  description, type, available choices, and default value.

`globals`
: Guild inspects the Python module and looks for global variables
  that are assigned numbers, strings, or boolean constants. Guild does
  not import variables that start with ``_``. From this Guild infers
  flag name, type, and default value.

`global:<name>`
: Guild inspects the Python module and looks for the specified global
  variable. Guild infers flags if the variable references a
  dict. Guild infers flags from dict items that are number, string, or
  boolean constants. From these items, Guild infers flag name, type,
  and default value.

Guild does not currently support flag imports for non-Python
scripts. In such cases you must explicitly define each flag and use
command line arguments or environment variables to access flags.

### Flag Import Configuration

Guild supports different import scenarios:

- Disable flag imports
- Import all detected flags
- Import a list of detected flags
- Import all but some detected flags

To disable Guild support for detecting and importing flags, use the
value ``no`` for `flags-import`.

``` yaml
op:
  flags-import: no
```

^ Disable flag imports

In this case, you must explicitly define each flag your script
supports.

!!! tip
    When `flags-import` is ``no``, Guild will not inspect your
    script for flags. Use this value to avoid processing your scripts
    when you don't need to.

To import all detected flags, use the value ``all`` or ``yes`` for
`flags-import`.

``` yaml
op:
  flags-import: all
```

^ Import all flags

To import a list of detected flags, specify the flag names in a list.

```
op:
  flags-import: [x, y, z]
```

^ Import some flags

You may alternatively omit `flags-import` and define the flags.

```
op:
  flags:
    x: 1
    y: 2
    z: 3
```

^ Implicitly import each defined flags --- use `flags-import` or
`flags-import-skip` to control this

You can combine `flags-import: all` with `flags-import-skip` to import
all flags but skip those specified.

``` yaml
op:
  flags-import: all
  flags-import-skip: [x, y]
```

This pattern is useful when Guild mistakenly infers a command line
option or variable as a flag.

## Batch Files

Batch files are files that contain one or more sets of flags to use
for a run.

Specify batch files for a run using one or more arguments with the
syntax ``@PATH``.

For example, to use the batch file `trials.csv` for operation `train`,
run:

``` command
guild run @trials.csv
```

For information on batch file format, see [Batch
Files](/runs.md#batch-files).

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
: Specifies an evenly spaced sequence along a log-linear scale with
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
: Specifies a uniform distribution over a range of values

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

<!-- TODO

## Flag Value Types

-->

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
