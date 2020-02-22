title: Guild Files
tags: concept

<!-- TODO

Keep this about generic concepts and point to other concept docs for
details.

-->

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

- [Get Started - Add a Guild File](/start/guildfile_xxx) --- step-by-step
example creating a simple Guild file
- [Guild File Reference](/reference/guildfile.md) --- complete list of
configuration options
- [Guild File Cheatsheet](/cheatsheets/guildfile.md) --- configuration
examples

## Operations

An *operation* defines what Guild executes to for a run.

Consider this example, which defines a single operation named
``train``:

``` yaml
train:
  description: Train a model using a Python script
  main: train
  flags:
    learning-rate: 0.1
    batch-size: 100
```

The operation is named `train` and can be run using ``guild run
train``.  It runs the `train` Python module, which is specified by the
`main` attribute. The operataion defines two flags: `learning-rate`
and `batch-size`.

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
values. Guild generates a [run](term:run), which is a record of the
operation inputs and outputs.

Guild passes flag values to Python modules by setting global variables
or by passing arguments on the command line. You can configure this
interface or Guild can detect it. For more information, see [*Flags
Interface*](#flags-interface) below.

Guild supports operations in Python as well as other languages. Here's
an operation that runs a shell script:

``` yaml
train:
  description: Train a model using a shell script
  exec: train.sh
```

For more information on running operations with difference languages,
see [*Other Language Operations*](#other-language-operations) below.

### Python Operation

Guild provides special support for Python-based operations. To define
a Python based operation, use the
[`main`](/reference/guildfile.md#operation-main) operation attribute
to specify the Python main module. This is a Python module that runs a
task when loaded by the Python interpreter as ``__main__``.

Consider a script named `train_classifier.py`:

``` python
from models import cnn

def train():
    model = cnn.CNN()
    model.train()

if __name__ == "__main__":
    train()
```



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

### Other Language Operations

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
in several contexts:

- Output from [runs info](cmd:runs-info)
- Columns in [Guild Compare](/tools/compare.md)
- Columns in **Compare Runs** of [Guild View](/tools/view.md)
- Hyperparameters in [Guild TensorBoard](/tools/tensorboard.md)

#### Flags Interface

Guild conveys flag values to a script using various methods:

- Command line arguments
- Environment variables
- Global variables (Python only)

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


##### Flags as Global Variables (Python only)

When `flags-dest` is `globals`, Guild sets flag values as script
global variables.

#### Automatically Import Flags (Python only)

Guild can import flags from Python scripts to avoid duplicating
information in a Guild file. By default, Guild does not attempt to
import flags from Python scripts.

To import flags from a Python script, use the `flags-import` operation
attribute.

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


- Used as inputs to a run
- Can be defined in both in the script and in the guild file
- Definition in Guild file redefines any imported defs
- Behavior can be disabled for explicit control and to avoid scanning
  scripts

### Source Code


### Output Scalars

In some cases, Guild applies additional rules to capture scalars
logged by known frameworks. Refer to [Framework
Scalars](#framework-scalars) below for more information.

The sections that follow describe how you can configure Guild's output
scalar behavior.

#### Custom Output Scalars

Configure output scalars for an operation by defining a
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
: Sets the current `step` used for subsequently logged scalar values

` - ([a-z_]+): (\value)`
: Captures scalar values staring with lower case (skips `ETA`, which
  would otherwise be logged as a scalar)

### Dependencies

### Workflows

TODO

## Models

A *model* defines a set of related operations. Generally models
correspond to the structures that you train, evaluate, and
deploy. However, Guild models may define any operations or even be
used for non-modeling functions.

Models must be defined using [full format](ref:full-format) Guild
files. Models are top-level objects with a `model` attribute.

``` yaml
- model: mnist
  operations:
    train: mnist_train
    validate: mnist_val
```

^ Sample `mnist` model definition with two operations: `train` and `validate`

TODO

- Other attributes - why use models and not just operations?
- Inheritance using config

## Resources


## Packages


## Reusable Config

Guild supports reusable configuration through top-level `config` objects.

Configuration must be defined using [full format](ref:full-format)
Guild files.

Configuration objects may contain any attributes. Attributes are
applied based on how the object is used.

Guild supports two uses of `config` objects:

- [Top-level object inheritance](#inheritance)
- [Attribute includes](#attribute-includes)

Below is a sample `config` object.

``` yaml
- config: base-model
  operations:
    train: '{{ name }}_train'
    validate: '{{ name }}_val'
```

^ Top-level `config` object named `base-model` that defines an
`operations` attribute

This configuration can be referenced using the `extends` attribute of
another top-level object to inherit the configuration attributes.

``` yaml
- model: mnist
  extends: base-model
  params:
    name: mnist
```

^ Top-level `model` object that *extends* `base-model` --- it defines
a `name` param, which resolves references in the inherited attributes

## Inheritance

Guild files support *inheritance* where attributes of one object
(parent) are applied by default to another object (child). A child may
redefine attributes as needed.

Here's an example of a `model` object inheriting the attributes from a
`config` object:

``` yaml
- config: base
  operations
```

## Attribute Includes

TODO

## Including Files

Guild files can include other YAML files by using a top-level
`include` object. The `include` type attribute specifies the path of
the file to include. Paths are considered relative to the including
Guild file.

Here is a sample `guild.yml` file that includes two files.

``` yaml
- include: guild-mnist.yml
- include: guild-cifar.yml
```

^ `guild.yml` --- includes two files

The included files must be valid full format Guild files. Their
contents are included in the Guild including file at the location each
is defined.

``` yaml
- model: mnist
  operations:
    train: mnist_train
    validate: mnist_validate
```

^ `guild-mnist.yml` --- included by `guild.yml` above

``` yaml
- model: cifar
  operations:
    train: cifar_train
    validate: cifar_valuate
```

^ `guild-cifar.yml` --- also included by `guild.yml` above
