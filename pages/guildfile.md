tags: concept

# Guild Files

[TOC]

## Overview

Guild files are named `guild.yml` and are located in project
directories. They provide information about your project.

- Scripts used to generate experiments
- User input parameters
- Generated metrics
- Script source code
- Requires input files

While Guild can run scripts directly without explicit configuration,
in such cases Guild makes assumptions about how to run each
script. For all but simple cases, we recommend using Guild files to
formally define your project operations.

More about Guild files:

- [Get Started - Add a Guild File](/start/guildfile.md) --- step-by-step
example creating a simple Guild file

- [Guild File Reference](/reference/guildfile.md) --- complete list of
configuration options

- [Guild File Cheatsheet](/cheatsheets/guildfile.md) --- configuration
examples

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

- The operation is named `train` and can be run using ``guild run
  train``

- The main Python module, also named `train`, is defined in a file
  named `train.py` in the same directory as `guild.yml`

- The operation defines two flags: `learning-rate` and `batch-size`

You can run the operation from a command terminal by changing to the
directory containing `guild.yml` (the project directory) and running:

``` command
guild run train
```

``` output
You are about to run train
  batch-size: 100
    learning-rate: 0.1
    Continue? (Y/n)
```

Guild shows a preview of the flags used for the operation and asks you
to confirm the operation by pressing `Enter`. When you confirm the
operation, Guild executes the `train` module with the specified flag
values. Guild generates a *run*, which is a record of the operation
inputs and outputs.

For information on managing runs, see [Runs](/runs.md).

### Python Operation

Guild provides special support for Python-based operations. To define
a Python based operation, use the `main` operation attribute. The
`main` attribute specifies the Python main module. This is a Python
module that performs some task when loaded by the Python interpreter
as `__main__`.

Consider a script named `train_classifier.py` that is run using Python
as follows:

``` command
python train_classifier.py
```

In this case, the `main` module name is `train_classifier` and is
specified in a Guild file operation as follows:

``` yaml
train:
  main: train_classifier
```

!!! note
    Do not include the file name extension when specifying a main
    module for an operation. The attribute value specifies a Python
    *module* and not a file name.

See also:

- [`main` attribute reference](/reference/guildfile.md#operation-main)
- [Simple Operations - Guild File
  Cheatsheet](/cheatsheets/guildfile.md#simple-operations)

### Other Language Based Operations

To run a non-Python based operation, use the `exec` operation
attribute. The value for `exec` is a command available on the `PATH`
environment variable or a path to an executable program.

The following example runs a Java program, provided as a JAR file:

``` yaml
train:
  exec: java -jar train.jar
  requires:
    - file: train.jar
```

Any files needed by the operation --- e.g. programs, etc. --- must be
specified as dependencies using the `requires` attribute. Refer to
[Dependencies](#dependencies) below for information on specifying
required files for an operation.

See also:

- [`exec` attribute reference](/reference/guildfile.md#operation-exec)

### Flags

*Flags* are user inputs to an operation. Flags define model and
training hyperparameters as well other script inputs, such as data set
information, user defined input paths, deployment endpoints, etc.

Flags are defined for each operation using the `flags` attribute.

``` yaml
train:
  flags:
    learning-rate: 0.1
    batch-size: 100
```

^ Use flags to define operation inputs such as *learning rate* and
  *batch size*

When running an operation, a user sets flag values using
`FLAG_NAME=VALUE` arguments to the [run](cmd:run) command.

``` command
guild run train learning-rate=0.01 batch-size=1000
```

^ Specify flag values as `FLAG_NAME=VALUE` arguments

See [Flags Interface](#flags-interface) below for information on how
Guild conveys flag values to a script.

Guild records flag values used for each run. Flag values are displayed
in serveral contexts:

- Output from [runs info](cmd:runs-info)
- Columns in [Guild Compare](/tools/compare.md)
- Columns in **Compare Runs** of [Guild View](/tools/view.md)
- Hyperparameters in [Guild TensorBoard](/tools/tensorboard.md)

#### Flags Interface

Guild conveys flag values to a script using various methods:

- Command line arguments
- Environment variables
- Global variables (Python scripts only)

For Python based operations, Guild detects the flags interface by
inspecting the `main` module. If the module uses Python's [`argparse`
package](ext:https://docs.python.org/library/argparse.html), Guild
assumes that the script uses command line arguments to read flag
values. Otherwise, Guild assumes the script uses global variables for
flags.

Specify the interface using the `flags-dest` operation attribute
(short for *flags destination*).

When `flags-dest` is set, Guild does not inspect the file to detect
the flags interface.

See also:

- [`flags-dest` attribute
  reference](/reference/guildfile.md#operation-flags-dest)

##### Flags as Command Line Arguments

To indicate that flags should be passed as command line arguments use
`args`:

```
train:
  flags:
    learning-rate: 0.1
    batch-size: 100
  flags-dest: args
```

^ Flags conveyed to a script using command line arguments

In this case, Guild runs the command ``python -m train --learning-rate
0.1 --batch-size 100``. The script `train.py` must parse these command
lines to read the specified flag values.

By default Guild uses the flag name as the argument name. To use a
different value, specify the `arg-name` flag attribute.

See also:

- [`arg-name` attribute
  reference](/reference/guildfile.md#flag-arg-name)


##### Flags as Global Variables (Python scripts only)

When `flags-dest` is `globals`, Guild sets flag values as script global variables.

#### Automatically Import Flags (Python scripts only)

Guild can import flags from Python scripts to avoid duplicating
information in a Guild file. By default, Guild does not attempt to
import flags from Python scripts.

To import flags from a Python script, use the `flags-import` operation
attribute.


```
```



#### Default Values

#### Flag Data Type

#### Required Flags

#### Flag Value Choices

#### Flag Value Distribution

#### Flag Help

        self.default = _data.pop("default", None)
        self.description = _data.pop("description", None) or ""
        self.type = _data.pop("type", None)
        self.required = bool(_data.pop("required", False))
        self.arg_name = _data.pop("arg-name", None)
        self.arg_skip = _data.pop("arg-skip", None)
        self.arg_switch = _data.pop("arg-switch", None)
        self.choices = _init_flag_choices(_data.pop("choices", None), self)
        self.allow_other = _data.pop("allow-other", False)
        self.env_name = _data.pop("env-name", None)
        self.null_label = _data.pop("null-label", None)
        self.min = _data.pop("min", None)
        self.max = _data.pop("max", None)
        self.distribution = data.pop("distribution", None)
        self.extra = _data


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

### Workflows

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
