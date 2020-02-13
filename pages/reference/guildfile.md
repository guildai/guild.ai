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

### Full Format

*Full format* is used to specify full project configuration. It
contains a list of top-level objects in the format:

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

### Operation Only Format

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

`<mapping key>` <div id="operation-name"></div>
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


`description` <div id="operation-description"></div>
: Operation description (string)

    This value can span multiple lines. By convention, the first line
    is a short description that does not end in a period. Subsequent
    lines, separated by an empty line, should be written using full
    sentences.

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

`steps` <div id="operation-steps"></div>
: List of steps to run for workflow (list of string or [steps](#steps))

    Steps are used to implement sequential work flow in Guild. Refer
    to [Steps](#steps) below for details.

`flags` <div id="operation-flags"></div>
: Operation flags (mapping of flag name to [flag](#flags))

    Flags define the user-interface for an operation. Mapping keys are
    flag names. See [Flags](#flags) for a list of flag attributes.

    Guild supports the special `$include` mapping key, which may be a
    string or list of strings. Each string may refer to either a model
    operation or a config object.

    See [Reuse Flag Definitions](#reuse-flag-definitions) below for
    .

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

`flags-import` <div id="operation-flags-import"></div>
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

`flags-import-skip` <div id="operation-flags-import-skip"></div>
: List of flags to skip when importing all flags (list of strings)

    Use this attribute when setting `flags-import` to `yes` or `all`
    when it's more convenient to exclude a list of flags than it is to
    list flags to import.

`requires` <div id="operation-requires"></div>
: List of operation dependencies (list of [resources](#resources))

    By default run directories are empty, which means that any local
    files that a script needs will not be available by default. To
    ensure that a script has access to required resources, the
    operation must specify the appropriate dependencies using the
    `requires` attribute.

    Refer to [Dependencies](#dependencies) below for details on
    specifying this value.

`sourcecode` <div id="operation-sourcecode"></div>
: Specification used to copy source code files ([source code
  spec](#source-code-specs))

    Guild copies source code for each run to provide a record
    associated with the run. Furthermore, Python based operations are
    isolated from their upstream project source code and rely on
    copied source code.

    By default, Guild copies text files that are less than 1M up to
    100 files. Guild shows warnings for files that exceed these
    limits.

    When the `sourcecode` attribute is defined, Guild does not apply
    these checks and will not show sauch warnings.

`output-scalars` <div id="operation-output-scalars"></div>
: List of output scalar patterns to apply to run standard output (list
  of [output scalar specs](#output-scalar-specs) or `no`)

      By default, Guild captures output scalars using the pattern
      ``^(\key): (\value)``.

      Use the `output-scalars` attribute to customize the way Guild
      captures scalars from standard output.

      To disable capturing of output scalars altogether, specify `no`.

`env` <div id="operation-env"></div>
: Additional environment variables available to the operation process
  (mapping of names to values)

    Note that flag values are always available in the environment as
    `FLAG_UPPER_NAME` variables, where `UPPER_NAME` is the upper case
    flag name. A flag can specify a different environment variable
    name using the [`env-name` flag attribute](#flag-env-name).

`python-requires` <div id="operation-python-requires"></div>
: Requirement specification of Python needed for the operation
  (string)

    The requirement must be specified without a package name using
    only the version portion of a [](ref:pip-reqs).

`python-path` <div id="operation-python-path"></div>
: Path to use for `PYTHONPATH` when running the operation (string)

`stoppable` <div id="operation-stoppable"></div>
: Indicates whether user-termination of the operation should be
  treated as a success (boolean)

      By default, Guild designated user-terminated operations as
      `terminated`. In some cases, you may may want to designate such
      user-terminated operations as `completed`, in which case, set
      this attribute to `yes`.

`label` <div id="operation-label"></div>
: Label template for the operation (string)

    By default, Guild creates a label that includes user-provided flag
    values. Use the `label` attribute to to define an alternative
    default label template.

    Use ``${FLAG_NAME}`` in the label to include specific flag
    values. For example, to define a label template that includes the
    flag `dropout_rate`, use ``dropout_rate=${dropout_rate}``.

`compare` <div id="operation-compare"></div>
: List of columns to include for operation runs in [Guild
  Compare](/tools/compare.md) (list of [column specs](#column-specs))

`default-max-trials` <div id="operation-default-max-trials"></div>
: Default number of max trials when running batches (integer)

    By default, the max trials used when the user doesn't explicitly
    specify `--max-trials` is optimizer-specific --- however, it is
    usually 20.

`objective` <div id="operation-objective"></div>
: Objective used by sequential optimizers (string or mapping)

    If `objective` is a string, optimizers attempt to minimize the
    specified scalar value for runs.

    As an alternative, to minimize a scalar, use the mapping
    `minimize: SCALAR`.

    Use a mapping of `maximize: SCALAR` to maximize a scalar value
    when optimizing.

`optimizers` <div id="operation-optimizers"></div>
: Mapping of named optimizers associated with the operation

    The mapping consists of default optimizer flags used when the
    optimizer is specified for a run.

    An optimizer defined in this section can be specified for a run
    using its name with the `--optimizer` option.

    By default, the optimizer operation is the same as the mapping
    key. To use a different operation, use the special attribute
    `algorithm`.

    To designate an optimizer as the *default*, use the special
    attribute `default` with a value of `yes`. Default optimizers as
    used when the `--optimize` option is used with [run](cmd:run).

    See [Optimizers - Guild File
    Cheatsheet](/cheatsheets/guildfile.md#optimizers) for examples.

`plugins` <div id="operation-plugins"></div>
: List of plugins to enable for the operation

    Use the value `all` to enable all plugins. To enable all
    summary-related plugins (`cpu`, `gpu`, `disk`, `memory`, and
    `perf`) use the value `summary`. See
    [Plugins](/reference/plugins.md) for more information.

### Flags

Flags are defined as mappings under the `flags` operation
attribute. The mapping key is the flag *name*.

A mapping value may either a mapping of attributes or a default
value. Available flag attribute are listed below.

`<mapping key>` <div id="flag-name"></div>
: Flag name (required string)

    The flag name is used when specifing a flag value. When specifying
    a value as an argument to the [run](cmd:run) command, the name is
    used as `NAME=VALUE`.

`description` <div id="flag-description"></div>
: Flag description (string)

    The flag description is used in project and operation help. If the
    flag description contains more than one line, the first line is
    used for operation help.

`type` <div id="flag-type"></div>
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

`default` <div id="flag-default"></div>
: Default flag value

    By default, flag values are `null`, which means they are not
    passed to the script.

`required` <div id="flag-required"></div>
: Indicates whether or not a flag value is required (boolean)

    By default, flag values are not required.

`arg-name` <div id="flag-arg-name"></div>
: The argument name used when setting the flag value (string)

    If operation `flags-dest` is `args`, this attribute specifies the
    argument option name, used as ``--NAME VALUE``.

    If operation `flags-dest` is `globals`, this attribute specifies
    the global variable name.

    If operation `flags-dest` is `global:PARAM`, this attribute
    specifies the key used when setting the flag in the `PARAM` global
    dict.

`arg-skip` <div id="flag-arg-skip"></div>
: Indicates whether the flag is skipped as an argument (boolean)

    By default, all flags are set according to the operations
    `args-dest` attribute. If `arg-skip` is set to `yes` for a flag,
    that flag will not be set.

    This value is used to skip flag arguments that are already
    specified in the `main` or `exec` operation attributes.

`arg-switch` <div id="flag-arg-switch"></div>
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

`choices` <div id="flag-choices"></div>
: A list of allowed flag values (list of values or mappings)

    Each list item may be either a value, which indicates one of the
    valid choices, or a mapping of choice attributes.

    When specified as a mapping, valid attributes are:

    `value`
    : The choice value

    `description`
    : A description of the choice

        The choice description is used when showing operation help.

`allow-other` <div id="flag-allow-other"></div>
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

`null-label` <div id="flag-null-label"></div>
: Display label used in operation preview when flag value is `null` (string)

    By default, Guild uses the string ``default`` when showing null
    values in the operation preview. Use this attribute in cases where
    another string would be clearer. For example, if the behavior of a
    script is to auto-detect a value when a `dataset` flag is `null`,
    `null-label` could be set to ``auto detected`` to help convey this
    to the user.

`min` <div id="flag-min"></div>
: Minimum allowed value (number)

    By default, Guild does not check number ranges.

    This value also serves as the default lower bound for values
    chosen by optimizers.

`max` <div id="flag-max"></div>
: Maximum allowed value (number)

    By default, Guild does not check number ranges.

    This value also serves as the default upper bound for values
    chosen by optimizers.

`distribution` <div id="flag-distribution"></div>
: Distribution used when sampling values for flag

    Legal values are:

    `uniform`
    : Sample from a uniform distribution.

    `log-uniform`
    : Sample from a log uniform distribution.

### Dependencies

An operation may require *resources* to run. Required resources are
referred to as *dependencies*.

Dependencies are specified using the `requires` attribute. The value
for `requires` is list of dependencies.

Dependencies may be *inline* or *named*. An inline resource is defined
as part of the `requires` operation attribute. A named resource is
defined as a model resource and is referenced using the resource name.

When defining an inline resource, you may specify any supported
resource attributes. In addition, you may include a `name` attribute,
which is used when referencing the inline resource. By default, Guild
generates a unique name using the resource source URIs.

The following defines a list of both inline and named dependencies:

``` yaml
train:
  required:
    - prepared-data     # named resource
    - file: config.yml  # inline resource
```

See [Resources](#resources) below for resource types and supported
attributes.

See [Required Files - Guild File
Cheatsheet](/cheatsheets/guildfile.md#required-files) for more
examples.

### Source Code Specs

The operation [`sourcecode` attribute](#operation-sourcecode)
specifies how source code is copied for a run.

The `sourcecode` attribute value may be a list or a mapping. If the
value is a mapping, it has the following attributes:

`root` <div id="sourcecode-root"></div>
: An alternative root from which to copy source code (string)

    By default, Guild copies source relative to the Guild file
    defining the operation. Use `root` to specify an alternative path.

    This value may use `../` to reference source code outside the
    Guild file directory.

    Note that paths that refer to locations outside the Guild file
    directory may break if the project is copied to another system.

`select` <div id="sourcecode-select"></div>
: A list of select rules

    See below for a description of select rules.

`digest` <div id="sourcecode-digest"></div>
: Indicates whether or not Guild generates a digest for copied source
  code (boolean)

    By default Guild generates digests of copied source code. The
    digest can be used to determine if source code used by two runs is
    different.

    In some cases, it may be too expensive to compute a digest and the
    source code version may be available through an explicit
    version. In such cases, you can disable the digest by setting this
    attribute to `no`.

If the `sourcecode` attribute is a list, it is treated as the value
for `select` above and the Guild file directory is treated as `root`.

Each select list item is an *include* or *exclude* rule. Each rule is
either a string or a mapping.

If the rule is a mapping, it must contain a type attribute of either
`include` or `exclude`. The type attribute value is a [glob style
->](https://en.wikipedia.org/wiki/Glob_(programming)) patterns or list
of patterns.

If the rule is a string, it implies a mapping type of `include` where
the string is the rule pattern.

When at least one rule pattern matches a path relative to the Guild
file location, Guild applies the rule with the effect of including or
excluding the path.

Rules are applied in the order specified. Subsequent rules override
previous rules.

In addition to glob patterns, defined as the type attribute, you may
specify additional mapping attributes, which are listed below.

`type`
: The type of path to match

    This information is applied to the selection test, along with the
    rule path pattern.

    Type may be one of the following values:

    `text`
    : Matches only text files

    `binary`
    : Matches only binary files (i.e. non-text)

    `dir`
    : Matches only directories

        Excluding `dir` types has a performance benefit as Guild will
        not scan the contents of excluded directories.

See [Source Code - Guild File
Cheatsheet](/cheatsheets/guildfile.md#source-code) for examples on how
to configure source code for an operation.

### Output Scalar Specs

*Output scalars* are numeric values that are written to standard
output or standard error streams and logged during a run. Output
scalar values correspond to a *key* and an optional *step*.

Guild supports output scalars as an alternative to explicit logging to
event logs. Use output scalars to log results by printing them as
script output.

Output is matched using [regular expressions](term:regex). Values are
captured using capture groups. The special escape values ``\key``,
``\value``, and ``\step`` can be used to match keys, values, and step
values respectively.

By default, Guild logs output written in the format:

``` output
key: value
```

- `key` must not be preceded by any white space
- `value` must be a value that can be decoded as number
- Guild treats the key literal ``step`` as a special value, which is
  used to set the *step* associated with subsequently logged values

This scheme is designed for simple cases and can be modified using the
`output-scalars` operation attribute.

The `output-scalars` attribute may be a mapping of scalar keys to
capturing pattern or a list of capturing patterns. If the value of
`output-scalars` is a mapping, the mapping keys correspond to scalar
keys and each value is a pattern that captures a numeric value as a
group.

``` yaml
train:
  output-scalars:
    loss: 'test_loss=(\value)'
    acc: 'test_acc=(\value)'
    step: 'epoch=(\step)'
```

^ Sample mapping attribute --- keys are scalar keys and values are
  capturing regular expression patterns

If the value of `output-scalars` is a list, each item may be a mapping
of keys to capturing patterns, which is treated identically as the
mapping described above, or as strings. If an item is a string, it
must define two capture groups. By default, the first capture group is
the scalar key and the second capture group is the scalar value. Named
capture groups may be used to reverse this order, using `key` and
`value` group names for the captured key and value respectively.

``` yaml
train:
  output-scalars:
    - step: 'Results for \(step (\step)\):'
    - '  (\key)=(\value)'
```

^ Sample list attribute --- items may be mappings of scalar keys to
  capturing patterns or strings that capture both keys and values

Patterns must be valid [regular expression](ref:regex).

The special templates ``\key``, ``\value``, and ``\step`` may be used
to represent regular expressions for valid keys, numeric values, and
step values respectively.

!!! tip
    Use the `--test-output-scalars` option to [run](cmd:run) to
    test strings from generated output. You can test a file or
    interatively test strings that you type into the console (use
    ``-`` as the file name to read from standard intput).

See [Output Scalars - Guild File
Cheatsheet](/cheatsheets/guildfile.md#output-scalars) for additional
examples of output scalar capture patterns.

### Column Specs

By default Guild shows all flags and root output scalars for an
operation run in [Guild Compare](/tools/compare.md). Use the `columns`
operation attribute to define an alternative set of columns.

Guild supports a special syntax for specifying columns, which is
defined by the following grammar:

```
['first'|'last'|'min'|'max'|'total'|'avg'] SCALAR_KEY ['step'] ['as' DISPLAY_NAME]

'=' FLAG_NAME ['as' DISPLAY_NAME]

'.' RUN_ATTRIBUTE ['as' DISPLAY_NAME]
```

All columns can be named by appending `` as DISPLAY_NAME`` to the
expression.

To show *scalars*, specify the scalar key. You may optionally qualify
which scalar value to show by preceding the expression with one of the
qualifiers listed above. Scalars are logged per *step* and so there
may be multiple values, each associated with a step value. Qualifiers
indicate how a scalar should be presented as a single value. By
default, the last scalar value is used --- the value associated with
the largest step value.

To show a run *flag*, precede the flag name with an equals sign ``=``.

To show a run *attribute*, precede the run attribute name with a dot
``.``. For a list of attributes, use ``guild ls -a -p .guild/attrs
RUN`` for a run.

For example:

``` yaml
train:
  compare:
    - max loss as max_loss
    - max loss step as max_loss_step
    - min loss as min_loss
    - min loss step as min_loss_step
```

^ Use the `compare` operation attribute to define the columns shown in
  [Guild Compare](/tools/compare.md)

!!! note
    Column specs are used with any column-spec command
    option. For example, use the above syntax for `STEPS` in `guild
    compare --columns SPECS`.

### Steps

Steps are used to implement sequential work flow in Guild. The `steps`
attribute specifies a list of operations to run.

Operations that define steps are referred to as *stepped operations*
or *workflows*.

The `step` attribute is a list of steps. Each step may be a string or
a mapping. If a step item is a string, it is treated as a `run`
command.

A step mapping may have the following attributes:

`run` <div id="step-run"></div>
: An operation to run for the step (string)

    You may include flag values as arguments to the
    operation. Alternatively, use the `flags` attribute to list flag
    assignments.

`name` <div id="step-name"></div>
: An alternative name used for the step (string)

    By default, the operation name specified for `run` (or as the step
    value if it is a string) is used as the name.

    Names are used as links within the stepped run.

`flags` <div id="step-flags"></div>
: A list of flag assignment strings (list of strings)

    Each string must be in the form ``NAME=VALUE``.

`checks` <div id="step-checks"></div>
: A list of checks to perform on the step (list of [step checks](#step-check))

    Use checks to validate a step. Checks are used to implement tests
    in Guild.

`label` <div id="step-label"></div>
: The label template for the step (string)

    The label template overrides the `label` template defined for the
    step operation. See [`label` operation
    attribute](#operation-label) for details on how label templates
    are applied.

        self.checks = _init_checks(data)
        self.label = _resolve_param(params, "label", parent_flags)
        self.gpus = _resolve_param(params, "gpus", parent_flags)
        self.no_gpus = params["no_gpus"]
        self.stop_after = params["stop_after"]
        self.needed = params["needed"]
        self.optimizer = params["optimizer"]
        self.opt_flags = params["opt_flags"]
        self.max_trials = params["max_trials"]
        self.random_seed = params["random_seed"]

### Step Check

A *step check* is a test that Guild applies to an operation step.

Checks are identified by a type attribute, which may be one of the
following:

`file`
: Tests a file generated by an operation.

    See [`file` check attributes](#file-check-attributes) below for
    additional attributes.

`output`
: Tests operation output.

    See [`output` check attributes](#output-check-attributes) below
    for additional attributes.

Each check type supports a different set of attributes, which are
described below.

#### `file` Check Attributes

`<mapping key>`
: File path to check (required string)

    Paths are considered relative to the step run directory.

`compare-to`
: Compares the run file to another file (string)

    If the run file is different from the file specified by
    `compare-to`, the check fails.

    Guild assumes that the `compare-to` file is relative to the step
    run directory.

`contains`
: Checks the run file for matching text (string)

    `contains` must be a valid [regular expression](ref:regex).

    If the run file output does not contain text that matches this
    attribute value, the check fails.

#### `output` Check Attributes

`pattern`
: Pattern to search for in run output (required string)

    If the run did not generate output that matches this value, the
    check fails.

## Models

In Guild AI, a *model* is a set of related operations.

Models are defined in [full format](term:full-format) Guild files
using the `model` type attribute.

``` yaml
- model: svm
  operations:
    train:
      main: train_svm
```

^ Sample model `svm` defined in using [full format](term:full-format)

Model attribute include:

`description`
: Description of the model (multiline string)

    Use `description` to provide a single line description as well as
    multiline descriptions. The first line of a model description is
    used in [models](cmd:models) output. Additional lines are used to
    show model help.

`extends`
: One or more models or config objects to extend (string or list of
  strings)

    Use `extends` to inherit the a model definition from a `model` or
    `config` top-level object.

    For more information, see [Inheritance](#inheritance)
    below.

`params`
: A mapping of parameter names to values

    Use `params` to define or redefine parameter values used in
    configuration.

    For more information, see [Parameters](#parameters).

`references`
: List of model sources and attributions (list of strings)

    Guild includes model references in model help.

`operations`
: Model operations (mapping of [operations](#operations)

    Use `operations` to define supported model operations. Mapping
    keys are operation names. See [Operations](#operations) for
    operation attributes.

    Model operations are run using ``guild run MODEL:OPERATION`` where
    `MODEL` is the model name and `OPERATION` is the operation name.

`resources`
: Resources defined for the model (mapping of [resources](#resources))

    Use `resources` to define named resources, which may be referenced
    by operations as dependencies using the resource name. Mapping
    keys are resource names. See [Resources](#resources) for resource
    attributes.

`sourcecode`
: Source code specification used for model operations ([source code
  spec](#source-code-spec))

    The `sourcecode` spec defined at the model level applies to all
    model operations. Operation level `sourcecode` specs *extend* the
    model level spec by effectively appending spec items to the end of
    the model items.

`python-requires`
: Default Python requirement for model operations ([](ref:pip-reqs)

    Operations may redefine this value as needed using their own
    `python-requires` attribute.

## Resources

Resources are files used by operations. Resources are specified as
operation *dependencies* using the [`requires` operation
attribute](#operation-requires).

Resources may be defined *inline* as a item in `requires` or may be
defined for a model under the `resources` attribute. In either case,
resource attributes, which are described below, may be used.

Resources define *sources*, which specify information about the files
to resolve.

Refer to [Resource Sources](#resource-sources) for supported
attributes.

Resources may refer to multiple files, as in the case of a local
directory, an archive file, or run-generated files. In such cases, the
resource may *select* required files using one or more regular
expression patterns. See [`select` resource
attribute](#resource-select) below for more information.

A resource item may be a mapping or a list. If the resource is a
mapping, the keys are assumed to be [*resource
attributes*](#resource-attributes). If the value is a list, the list
is assumed to be [*resource sources*](#resource-sources).

Here's a resource definition mapping where sources are defined under
the `sources` resource attribute:

``` yaml
- model: resnet
  resources:
    pretrained-model:
      path: model
      sources:
        - url: http://my.co/models/resnet.tar.gz
```

Here's a resource definition list, which defines sources as list
items:

``` yaml
- model: resnet
  resources:
    pretrained-model:
      - url: http://my.co/models/resnet.tar.gz
```

To specify any resource attribute other than `sources`, you must use a
mapping to define the resource.

See [Required Files - Guild File
Cheatsheet](/cheatsheets/guildfile.md#required-files) for examples.

### Resource Attributes

The following attribute may be used when defining a resoure using a
mapping.

`<mapping key>`
: Resource name, when defined as a model resource (required)

`flag-name`
: Flag name used when setting resource source values using flags (string)

    In cases where a user may configure a resource value, Guild uses
    the resource name by default to reference the resource. In some
    cases, it might be clearer to use an alternative name.

    This value can also be used to associated the resource to a flag
    definition of the same name. Use flag expose resources to users
    through project help and run preview.

`description`
: Resource description (string)

    This value is used to annotate the resource in the Guild file. It
    is not otherwise used by Guild.

`path`
: Path to create resolved resources under (string)

    By default, Guild creates links to resolved resource in the run
    directory. `path` may be used to specify a subpath to create links
    in.

    This value serves as a default for resource sources, which may
    define their own `path` attributes.

`default-unpack`
: Whether or not to unpack source archives by default (boolean)

    By default, Guild unpacks resolved archives. Each resource source
    may define `unpack`, which controls this
    behavior. `default-unpack` may be used to define the default used
    by sources.

`sources`
: Sources that define the resources to resolve (list of [resource
  source](#resource-sources))

### Resource Sources

A resource source is specified by a type attribute, which may be one
of the following:

`file`
: A local path relative to the Guild file location.

    A file may refer to a file or a directory. The value of `file`
    types is a local file path.

`url`
: A network accessible file.

    The value for `url` types is a valid URL.

`operation`
: Files generated by an operation run.

    The value for `operation` types is an operation name or a regular
    expression pattern used match operation names.

`config`
: A required configuration file.

    The value for `config` is a project-relative path to a file.

    The file must be a supported type: JSON, YAML.

    Guild resolves config sources by re-writing the files with the run
    flag values that are different from those defined in the original
    file.

`module`
: A required software library.

    The value for `module` types is a module name.

    Guild resolves module types by verifying that the module is
    available for a run.

In addition to the type attribute, resource sources support these
attributes:

`name`
: An optional name used to reference the source (string)

    By default, Guild uses the type attribute value to generate a name
    for the source.

    Source names are used to set modify type attribute values using
    flags.

`path`
: The path under the run directory in which to create resolved source
  links (string)

    By default, Guild creates links in the run directory. Use `path`
    to specify a subpath.

`sha256`
: An optional digest used to validate a source file (string)

    If specified, Guild will compare the resolved file to the
    specified digest and generate an error if it does not match.

    If the source is a directory, Guild ignores this value and prints
    a warning message.

`unpack`
: Indicates whether or not Guild unpacks resolved archives (boolean)

    By default, Guild unpacks resolved archives. Set this value to
    `yes` disable unpacking.

    If this attribute is not specified, Guild uses the resource
    `default-unpack` attribute, if defined.

`select`
: A list of patterns used to select files from an archive or directory
  (string or list of strings)

    If a file path within an archive or directory matches one of the
    specified select patterns, that file is selected, otherwise the
    file is not selected.

    Archives must be unpacked to select files.

    This setting is ignored for single file sources.

`select-min` and `select-max`
: A pattern used to select a file matching minimum or maximum captured
  value (string)

    Use o select one file from a list of archive or directory files
    using a captured group value. For example, if a directory contains
    `file-1` and `file-2`, the `select-min` value ``file-([0-9]+)``
    will select `file-1`. Similarly, `select-max` would select
    `file-2`.

    This attribute is often used with the `operation` type to select
    trained models that are saved in files containing performance
    values such as *loss* and *accuracy*.

`rename`
: Specification for renaming resolved files (string or mapping)

    If the value is a string, it must be in the form `PATTERN REPL`
    where `PATTERN` is a regular expression to match and `REPL` is the
    value used to replace matched patterns.

    If the value is a mapping, it must define the following
    attributes:

    `pattern`
    : The pattern to match (string)

    `repl`
    : The value to replace matching patterns (string)

`post-process`
: A command to run once to process a resource (string)

    When Guild first resolves a resource, it runs `post-process` if
    specified. This command is run once per command value. If the
    value is changed, Guild will re-run the command when resolving the
    resoure.

    Use this value to perform tasks on a resolved resource. For
    example, to apply patches, compile source, etc.

`help`
: A message to show the user if the resouce cannot be resolved
  (string)

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

Package attributes are listed below.

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

Refer to [Packages - Guild File
Cheatsheet](/cheatsheets/guildfile.md#packages) for examples.

## Config

A `config` top-level object can be used to create reusable
configuration within a Guild file.

Use config objects to:

- Define config that can be inherited by models
- Define reusable sets of flags
- Define reusable sets of operations

## Inheritance

A `model` object may used the `extends` attribute to extend one or
more top-level objects. `extends` may be a string or a list of
strings, each string referring to the top-level object name being
inherited.

``` yaml
- model: child
  extends: parent
```

^ Inheriting from a single parent

``` yaml
- model: child
  extends:
    - parent-1
    - parent-2
```

^ Inheriting from multiple parents

## Parameters

Parent configuration may use *parameters* in both attribute name and
values. A parameter reference uses the format ``{{ NAME }}``.

Parameter values are defined using the `params` attribute. Parameters
are inherited and may be redefined by children.

The following example illustrates the use of parameters to define flag
value defaults.

``` yaml
- model: base
  params:
    default-lr: 0.1
    default-dropout: 0.2
  operations:
    train:
      flags:
        lr: '{{ default-lr }}'
        dropout: '{{ default-dropout }}'

- model: a
  extends: base

- model: b
  extends: base
  params:
    default-lr: 0.01
    default-dropout: 0.3
```

^ Use parameters to define flag value defaults

!!! important
    YAML formatting rules require that `{{...}}` be quoted
    when used at the start of a value. Note the single-quotes used in
    the example above.

## Mapping Includes

### Reuse Flag Definitions

### Reuse Operation Definitions

## Guild File Includes
