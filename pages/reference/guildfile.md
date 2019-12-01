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

`main` <div id="operation-main"></div>
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

`exec` <div id="operation-exec"></div>
: Operation command (string)

    Guild uses this value to execute a system command.

    Use `exec` to run operations by executing a program. By default,
    flags are not invcluded in the operation command. To include
    flags, specify `${flag_args}` as an argument in the `exec` value.

`steps`
: List of steps to run for workflow (list of string or [steps](#steps))

    See [Workflow](/workflow.md) for more information on
    implementing workflows in Guild.

`flags` <div id="operation-flags"></div>
: Operation flags (mapping of flag name to [Flag](#flags) definition)

`flags-dest` <div id="operation-flags-dest"></div>
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
    `FLAG_UPPER_NAME` variables, where `UPPER_NAME` is the upper case
    flag name. A flag can specify a different environment variable
    name using the [`env-name` flag attribute](#flag-env-name).

`python-requires`
: Requirement specification of Python needed for the operation
  (string)

    The requirement must be specified without a package name using
    only the version portion of a [](ref:pip-reqs).

`python-path`
: Path to use for `PYTHONPATH` when running the operation (string)

`stoppable`
: Indicates whether user-termination of the operation should be
  treated as a success (boolean)

      By default, Guild designated user-terminated operations as
      `terminated`. In some cases, you may may want to designate such
      user-terminated operations as `completed`, in which case, set
      this attribute to `yes`.

`label`
: Label template for the operation (string)

    By default, Guild creates a label that includes user-provided flag
    values. Use the `label` attribute to to define an alternative
    default label template.

    Use ``${FLAG_NAME}`` in the label to include specific flag
    values. For example, to define a label template that includes the
    flag `dropout_rate`, use ``dropout_rate=${dropout_rate}``.

`output-scalars`
: List of output scalar patterns to apply to run standard output (list
  of [output scalar specs](#output-scalar-specs) or `no`)

      By default, Guild captures output scalars using the pattern
      ``^(\key): (\value)``.

      Use the `output-scalars` attribute to customize the way Guild
      captures scalars from standard output.

      To disable capturing of output scalars altogether, specify `no`.

`objective`
: Objective used by sequential optimizers (string or mapping)

    If `objective` is a string, optimizers attempt to minimize the
    specified scalar value for runs.

    If `objective` is a mapping, it uses the following attributes:

    `

`compare`
: List of columns to include for operation runs in [Guild
  Compare](/tools/compare.md) (list of [column specs](#column-specs))

`default-max-trials`
: Default number of max trials when running batches (integer)

    By default, the max trials used when the user doesn't explicitly
    specify `--max-trials` is optimizer-specific --- however, it is
    usually 20.

        self.objective = data.get("objective")
        self.optimizers = _init_optimizers(data, self)
        self.publish = _init_publish(data.get("publish"), self)
        self.sourcecode = _init_sourcecode(
            data.get("sourcecode"), self.guildfile)
        self.default_flag_arg_skip = (
            data.get("default-flag-arg-skip") or False)

### Output Scalar Specs

### Column Specs

## Flags

Flags are defined as mappings under the `flags` operation
attribute. The mapping key is the flag *name*.

A mapping value may either a mapping of attributes or a default
value. Available flag attribute are listed below.

### Flag Attributes

`<mapping key>`
: Flag name (required string)

    The flag name is used when specifing a flag value. When specifying
    a value as an argument to the [run](cmd:run) command, the name is
    used as `NAME=VALUE`.

`description`
: Flag description (string)

    The flag description is used in project and operation help. If the
    flag description contains more than one line, the first line is
    used for operation help.

`type`
: Flag value type

    Flag type is used to both validate and convert flag values when
    set as global variables. Note that all command line arguments and
    environment variables are passed as strings and must be converted
    by the script. Guild uses the type to validate user-provided input
    in all cases.

    By default, Guild converts user-input to values using YAML rules
    for decoding.

    Flag type may be one of:

    `string`
    : Value is converted to string regardless of how it would be
      decoded as YAML.

     `number`
     : Value is converted to an integer when possible, otherwise it is
       converted to a float.

     `float`
     : Value is converted to a float.

     `int`
     : Value is converted to an integer.

     `boolean`
     : Value is converted to a boolean.

     `path`
     : Value is converted to a string and must contain only valid path
       characters.

     `existing-path`
     : Value is converted to a string and checked as an existing path.

`default`
: Default flag value

    By default, flag values are `null`, which means they are not
    passed to the script.

`required`
: Indicates whether or not a flag value is required (boolean)

    By default, flag values are not required.

`arg-name`
: The argument name used when setting the flag value (string)

    If operation `flags-dest` is `args`, this attribute specifies the
    argument option name, used as ``--NAME VALUE``.

    If operation `flags-dest` is `globals`, this attribute specifies
    the global variable name.

    If operation `flags-dest` is `global:PARAM`, this attribute
    specifies the key used when setting the flag in the `PARAM` global
    dict.

`arg-skip`
: Indicates whether the flag is skipped as an argument (boolean)

    By default, all flags are set according to the operations
    `args-dest` attribute. If `arg-skip` is set to `yes` for a flag,
    that flag will not be set.

    This value is used to skip flag arguments that are already
    specified in the `main` or `exec` operation attributes.

`arg-switch`
: A value that, when specified, causes the flag to be set as a boolean
  switch

    By default, flags are set as values. When `arg-switch` is
    specified, they are set as boolean switches if and only if the
    user specifies the `arg-switch` value. A boolean switch is
    specified as a ``--SWITCH`` command line argument and does not
    provide a value. A boolean switch is specified as `True` when set
    as a global variable.

    For example, if `arg-switch` is `yes` for a flag named `test`,
    when the user specifies ``test=yes``, the command line option
    ``--test`` is provided without a value to the script --- or the
    global variable `test` is set to `True` --- depending on the
    operation `flags-dest` setting.

`choices`
: A list of allowed flag values (list of values or mappings)

    Each list item may be either a value, which indicates one of the
    valid choices, or a mapping of choice attributes.

    When specified as a mapping, valid attributes are:

    `value`
    : The choice value

    `description`
    : A description of the choice

        The choice description is used when showing operation help.

`allow-other`
: Indicates whether the user may enter a non-choice value when
  `choices` is specified (boolean)

`env-name` <div id="flag-env-name"></div>
: The environment variable name used for the flag (string)

     By default, Guild provides a flag value as the environment
     variable `FLAG_UPPER_NAME` where `UPPER_NAME` is the flag name in
     upper case. All non-alpha-numeric characters are converted to
     underscores. So a flag named `learning-rate` is made available as
     the environment variable `FLAG_LEARNING_RATE`.

     Use the `env-name` to control the environment variable name used.

`null-label`
: Display label used in operation preview when flag value is `null` (string)

    By default, Guild uses the string ``default`` when showing null
    values in the operation preview. Use this attribute in cases where
    another string would be clearer. For example, if the behavior of a
    script is to auto-detect a value when a `dataset` flag is `null`,
    `null-label` could be set to ``auto detected`` to help convey this
    to the user.

`min`
: Minimum allowed value (number)

    By default, Guild does not check number ranges.

    This value also serves as the default lower bound for values
    chosen by optimizers.

`max`
: Maximum allowed value (number)

    By default, Guild does not check number ranges.

    This value also serves as the default upper bound for values
    chosen by optimizers.

`distribution`
: Distribution used when sampling values for flag

    Legal values are:

    `uniform`
    : Sample from a uniform distribution.

    `log-uniform`
    : Sample from a log uniform distribution.

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
