sidenav_title: Guild File

# Guild File Reference

[TOC]

## Overview

Guild files are named `guild.yml`. They contain project
configuration. This document describes their format and schema.

Guild files are plain text, [YAML ->](https://yaml.org/) formatted
files.

Guild files can be constructed using one of two formats:

- Full format
- Operation-only format

<a id="full-format">*Full*</a> format is used to specify full project
configuration. It contains a list of top-level objects in the format:

``` yaml
- object_type: name
  attr_1: val_1
  attr_2: val_2
  ...

- object_type: name
  attr_1: val_1
  attr_2: val_2
  ...
```

`object_type` is an attribute that implies the object type by its
presence. The type attribute value is the object name.

You can include any of the following types in full mode:

`model`
: Models define operations, which are run to generate experiments. See
  [Models](#models) below.

`config`
: A named mapping of attributes that can be referenced by other
  top-level objects as configuration. See [Config](#config) below.

`package`
: Packages define how Guild generates Python wheel distributions. See
  [Packages](#packages) below.

*Operation-only* format is a simplified format that contains a map of
operations in the format:

``` yaml
operation_name_1:
  attr_1: val_1
  attr_2: val_2
  ...

operation_name_2:
  attr_1: val_1
  attr_2: val_2
  ...
```

Use full format when you want to:

- Specify a model name (operation-only uses an anonymous model)
- Define multiple models
- Define named resources
- Define a package

Use operation-only format when you want to:

- Only define operations, keeping the Guild file as simple as possible

Users often start with operation-only format and move to full format
as needed.

Here's a simple operation-only Guild file:

``` yaml
prepare-data:
  main: prepare
  flags:
    val-split: 0.2

train:
  main: train
  flags:
    learning-rate: 0.1
    batch-size: 100
```

^ Operation-only format --- operations are defined at the top-level

To move to a full format, these operations can be added to a top-level
`model` object:

``` yaml
- model: mlp
  operations:
    prepare-data:
      main: prepare
      flags:
        val-split: 0.2

    train:
      main: train
      flags:
        learning-rate: 0.1
        batch-size: 100
```

^ Full format --- top-level objets defined using type attributes
  (e.g. `model: mlp`)

Full format lets you define models, packages, and reusable
configuration.

## Operations

Operations define what Guild runs when [run](cmd:run) is
executed. Consider the command:

``` command
guild run train
```

Guild looks in the current directory for a Guild file that contains a
`train` operation. Guild uses the configuration to run the operation
and to perform tasks such as validating flag values, snapshotting
source code, and saving metrics.

You can list operations that are available by running:

``` command
guild operations
```

As described above in [Overview](#overview), operations can be defined
at the top-level of a Guild file in a mapping (*operation-only*
format). Alternatively, operations can be defined as values of a
model's `operations` attribute (*full* format).

For a various examples of operations

### Operation Attributes

The attributes listed below describe an operation.

If the Guild file is is operation-only format, the attributes are
applied under a top-level mapping key, which is the operataion name:

``` yaml
<mapping key>:
  <attr>: <val>
  ...
```

If the Guild file is full format, they are applied as attributes of an
`operations` attribute for a model:

``` yaml
- model: <model name>
  operations:
    <mapping key>:
      <attr>: <val>
      ...
```

`<mapping key>`
: Operation name (required string)

    Operation names are specified as the key in a mapping. If the
    Guild file is written in operation-only format, the mapping is
    defined at the top-level of the Guild file. If the Guild file is
    written in full format, the mapping is defined as the value of the
    `operations` attribute for a model.

    Operation names are used when running the operation. If the
    operation is defined for a named model (full format only), it can
    be referenced as `MODEL_NAME:OPERATION_NAME`. Otherwise it can be
    referenced as `OPERATION_NAME`. The model name in this case is
    empty and can be omitted.


`description`
: Operation description (string)

    This value can span multiple lines. By convention, the first line
    is a short description that does not end in a period. Subsequent
    lines, separated by an empty line, should be written using full
    sentences.

    Example of a multi-line description:

        prepare-data:
          description:
            Prepares the data set for training

            Use the flag `val-split` to specify the percentage of
            examples reserved for validation.

            When this operation is completed, run `train`.

`main`
: Operation main Python module (string)

    This value tells Guild what to execute when someone runs the
    operation. The value must be in the format:

    `[MODULE_PATH/]MODULE [ARG...]`

    `MODULE_PATH` is optional. It is the path, relative to the Guild,
    which should be included in the Python system to import the main
    module. `MODULE` is the full module name, including any parent
    Python packages.

    `ARG` may be any argument that should be passed to the
    module. Multiple `ARG` values may be provided.

    Guild appends flag values to the list of `ARG` values in the
    format `--FLAG_NAME FLAG_VAL`.

    You can explicitly specify flag values using the format
    `${FLAG_NAME}`. Guild replaces such references when creating the
    command. Note that unless `arg-skip` is true for referenced flags,
    those values will also be appended as argument as per above.

    Do not include the `.py` extension in the value for `MODULE`.

    `main` is used for Python modules only. To run a program, use
    `exec`.

    `main` must be provided if `exec` is not defined.

`exec`
: Operation command (string)

    Guild uses this value to execute a system command.

    Use `exec` to run operations by executing a program. By default,
    flags are not invcluded in the operation command. To include
    flags, specify `${flag_args}` as an argument in the `exec` value.

`steps`
: List of steps to run for workflow (list of string or [steps](#steps))

    See [Workflow](../workflow.md) for more information on
    implementing workflows in Guild.

`flags`
: Operation flags (mapping of flag name to [Flag](#flag) definition)

`flags-dest`
: Destination for flag values (string)

    This value tells Guild how to communicate flag values to the
    operation script. Guild supports the following flag destinations:

      `args`
      : Provide flag values as command line arguments

      `globals`
      : Set flag values as global variables (Python scripts only)

      `global:DOTTED_NAME`
      : Set flag values as dict values in `DOTTED_NAME`

      `DOTTED_NAME` is a chain of keys, each key separated by a dot
      (`.`). Guild will set each flag value in a dict that is resolved
      by reading module namespace attributes starting with the root
      namespace and proceeding from left-to-right along the chain. For
      example, the value `global:params` sets flag values in a global
      dict named `params`. The value `global:params.train` sets values
      in a dict defined as the attribute or key `train` of the global
      variable `params.

`flags-import`
: List of flags to import (string or list of strings)

    By default, Guild does not import any flags.

    To import all detected flags, use `yes` or `all` for the value.

    To import a list of flags, specify a list of flag names.

    When importing flags, Guild inspects the script specified in the
    `main` attribute to determine how flags are defined. If the Python
    module uses `argparse`, Guild inspects the parser arguments for
    flags, otherwise it inspects the module for global scalar or
    string assignments. This interface can be controlled explicitly
    using the `flags-dest` attribute (see above).

`flags-import-skip`
: List of flags to skip when importing all flags (list of strings)

    Use this attribute when setting `flags-import` to `yes` or `all`
    when it's more convenient to exclude a list of flags than it is to
    list flags to import.

`requires`
: List of operation dependencies (list of [resources](#resources))

    By default run directories are empty, which means that any local
    files that a script needs will not be available by default. To
    ensure that a script has access to required resources, the
    operation must specify the appropriate dependencies using the
    `requires` attribute.

`env`
: Additional environment variables available to the operation process
  (mapping of names to values)

    Note that flag values are always available in the environment as
    `FLAG_*` variables, where `*` is the upper case flag name. A flag
    can specify a different environment variable name using the
    `env-name` flag attribute.

`python-requires`
: Requirement specification of Python needed for the operation
  (string)

    The requirement must be specified without a package name using
    only the version portion of a [](ref:pip-reqs).

`python-path`
: Path to use for `PYTHONPATH` when running the operation (string)

---




        self.disable_plugins = _disable_plugins(data, modeldef.guildfile)
        self.dependencies = _init_dependencies(data.get("requires"), self)
        self.remote = data.get("remote") or False
        self.stoppable = data.get("stoppable") or False
        self.set_trace = data.get("set-trace") or False
        self.label = data.get("label")
        self.compare = data.get("compare")
        self.handle_keyboard_interrupt = (
            data.get("handle-keyboard-interrupt") or False)
        self.flag_encoder = data.get("flag-encoder")
        self.default_max_trials = data.get("default-max-trials")
        self.output_scalars = data.get("output-scalars")
        self.objective = data.get("objective")
        self.optimizers = _init_optimizers(data, self)
        self.publish = _init_publish(data.get("publish"), self)
        self.sourcecode = _init_sourcecode(
            data.get("sourcecode"), self.guildfile)
        self.default_flag_arg_skip = (
            data.get("default-flag-arg-skip") or False)

## Flags

### Examples

## Source Code

## Output Scalars

## Resources

## Steps

## Models

## Packages

A Guild file may contain at most one top-level package object. A
package object is identified by the use of the `package` attribute.

Guild uses package configuration when [package](cmd:package) is
run. If a package object is not defined for a Guild file, Guild uses
default values, which are described below.

Define a package when you want to:

- Distribute your project as a Python distribution (e.g. on PyPI,
  etc.)
- Include additional data files for remote runs
- Control the package name and version associated with remote
  operations

By convention, we recommend that you define the package as the first
object in a Guild file.

### Attributes

`package`
: Package name (string)

    Defaults to name of default model.

`version`
: Package version (string)

      Defaults to `0.0.0`.

`description`
: Package description (string)

    This can be a multi-line description.

`url`
: URL to package website (string)

`author`
: Name of individual or organization author (string)

`author-email`
: Email of package author (string)

`license`
: Name of package license (string)

`tags`
: List of package tags (list of strings)

`python-tag`
: Python tag used in the distribution name (string)

`data-files`
: List of additional data files to include in the distribution (list
  of strings)

    Guild always includes `guild.yml`, `LICENSE.*`, and
    `README.*`. The list of files specified by this attribute is added
    to this list.

    This is another paragraph yop.

`python-requires`
: Version of Python required by the package (string)

`requires`
: Requirements that must be satisfied when the package is installed
  (list of string)

`packages`
: Project Python packages to be included in the distribution (list of
  strings)

    Default is the list of packages returned by
    `setuptools.find_packages()`.

### Examples

``` yaml
- model: hello
  operations:
    say:
      main: say

- package: hello
  description: Simple hello workd package
  version: 1.0
  url: https://github.com/guildai/packages/tree/master/gpkg/hello
  author: Guild AI
  author-email: packages@guild.ai
  license: Apache 2.0
  data-files:
    - msg.txt
```

## Config
