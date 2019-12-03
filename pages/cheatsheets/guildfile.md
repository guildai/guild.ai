sidenav_title: Guild File

# Guild File Cheatsheet

[TOC]

## Operations

### Python Based Operations

#### Simple Operations

Run an operation implemented in the Python `train` module
(e.g. defined locally in `train.py`):

``` yaml
train:
  flags-import: all
```

^ Run Python `train` module and import all auto-detected flags

In this case, Guild imports all available flags defined in the `train`
module. By default, Guild inspects the module for an appropriate flags
interface: argument passing or global variables. Based on the detected
interface, Guild detects available flags. See [Flags
Interface](#flags-interface) below for examples on defining this
explicitly.

Use the `main` attribute to be explicit or to use a value different
from the operation name.

``` yaml
train:
  main: train_model
  flags-import: all
```

^ Use `main` to explicitly define the Python main module

Run a script defined in a subdirectory:

``` yaml
train:
  main: src/train_model
  flags-import: all
```

^ Use a path to reference modules defined in directories

If the script is located in a package (i.e. the subdirectory contains
`__init__.py`) use Python's package notation:

``` yaml
train:
  main: my_package.train_model
  flags-import: all
```

Include base arguments in the main specification:

``` yaml
train:
  main: model --train
  flags-import: all
```

^ Specify base (non flag) arguments to the module as needed

#### Flags Import

Specify a list of flags to import, skipping any detected flags that
are not specified:

``` yaml
train:
  flags-import:
    - epochs
    - lr
```

^ Import only specific flags

To import all flags but a specified list of flags:

``` yaml
train:
  flags-import: all
  flags-import-skip:
    - num_classes
```

^ Import all but some flags

!!! note
    The values `all` and `yes` for `flags-import` are
    synonymous. Use the value that you feel is clearest for the
    context.

#### Flags Interface

For background, see [Flags Interface - Guild
File](/guildfile.md#flags-interface).

To force Guild to use an argument passing interface:

``` yaml
train:
  flags-dest: args
  flags-import: all
```

^ Pass flag values to `train` module as arguments

To force Guild to use a globals interface:

``` yaml
train:
  flags-dest: globals
  flags-import: all
```

^ Set flag values as `train` module global variables

To write flag values to a global Python dict named `params`:

``` yaml
train:
  flags-dest: global:params
  flags-import: all
```

^ Set flag values as elements of global dict `params` in `train` module

!!! tip
    By specifying `flags-dest` and not importing all flags, you
    disable Guild's automatic flags detection scan.  See
    [Auto-detecting Flags](ref:autodetect-flags) for information on
    how Guild scans modules for interface type and how it sets module
    global variables.

### Other Language Operations

Examples below show operations implemented in non-Python languages
using the `exec` operation attribute.

#### All Flag Values as Arguments

Pass all flag arguments using getopt long-form `--NAME VAL` for each
argument:

``` yaml
train:
  exec: java -jar train.jar ${flag_args}
  flags:
    lr: 0.1
    epochs: 100
    activation: relu
  requires:
    - file: train.jar
```

^ Use `${flag_args}` in `exec` to insert flag values as long-form
  getopt args

``` command
guild run train --print-cmd
```

``` output
java -jar train.jar --activation relu --epochs 100 --lr 0.1
```

#### Specific Flag Values as Arguments

Include flag argument explicitly:

``` yaml
train:
  exec: java -jar train.jar ${epochs}
  flags:
    epochs: 100
  requires:
    - file: train.jar
```

^ Specify value for `epochs` flag as a command argument

``` command
guild run train --print-cmd
```

``` output
java -jar train.jar 1000
```

### Flags

Flags must be defined using the `flags` operation attribute.

#### Basic Flag Definitions

The most basic flag configuration is a single default value.

``` yaml
train:
  flags:
    lr: 0.1
    epochs: 100
```

^ Flags defined using their default values

All other flag configurations require a mapping.

``` yaml
train:
  flags:
    lr:
      description: Learning rate
      default: 0.1
    epochs:
      description: Number of epochs to train
      default: 100
```

^ Flags with descriptions and default values

#### Required Values

Require that the user specify a value for a flag using the `required`
attribute.

``` yaml
train:
  flags:
    dataset:
      description: Path to data set
      required: yes
```

#### Flag Value Types

Guild automatically detects number types and converts them accordingly
when setting global values. All command arguments, however, are passed
as strings and must be processed by the script.

Use the `type` flag attribute to validate user input and convert that
input to the specified type.

``` yaml
train:
  flags:
    epochs:
      default: 100
      type: int
    lr:
      default: 0.1
      type: float
    data-path:
      default: data.csv
      type: existing-path

```

See

#### Flag Choices

Limit to a list of valid choices using the `choices` attribute.

``` yaml
train:
  flags:
    activation:
      description: Activation layer
      default: relu
      choices:
        - relu
        - sigmoid
        - linear
```

^ Use choices to limit flag values

Provide descriptions for each choice to help the user understand each.

``` yaml
train:
  flags:
    activation:
      description: Activation layer
      choices:
        - value: relu
          description: Rectified linear unit
        - value: sigmoid
          description: Non-linear transform
        - value: linear
          description: No transform
```

^ Choices with descriptions --- used to display help to the user

``` command
guild run train --help-op
```

``` output
Usage: guild run [OPTIONS] train [FLAG]...

Use 'guild run --help' for a list of options.

Flags:
  activation  Activation layer

              Choices:
                relu     Rectified linear unit
                sigmoid  Non-linear transform
                linear   No transform
```

Allow a value not listed in `choices`:

``` yaml
train:
  flags:
    layers:
      description: Number of hidden layers
      choices: [1, 5, 10]
      allow-other: yes
```

xxx

``` yaml
train:
  flags:
    FLAG_NAME:
      description: A sample flag
      default: 100

      #allow-other: yes

      # Indicate if a value is required for the operation.
      #required: yes

      # Use a different command line argument or variable name.
      #args-name: NAME_2

      # Value that, when set, causes flag to appear as a 'switch'
      # command line option - i.e. an option with no value. E.g.
      # NAME=yes results in '--NAME' and not '--NAME True' to be
      # used as the flag argument.
      #arg-switch: yes

      # Don't include flag in command line arguments. Use when
      # referencing the flag in `main` as `${NAME}` to avoid
      # flag from appearing twice.
      #arg-skip: yes

      # Label to use when `null` value (default if not defined
      # above) is specified.
      #null-label: Default behavior
```

^ guild.yml snippet --- sample flag

!!! tips
    - Flag descriptions are used to show help when running ``guild
      help`` and ``guild run OP --help-op``. Descriptions can contain
      multiple lines to provide detailed help. Refer to
      [Flags](ref:flags) for details.

Related help topics:

- [Flags](ref:flags)


----------------------------

### Source Code

The `sourcecode` attribute determines which files Guild copies as
source code for a run. Configuration can be specified for an operation
or for a model. Model configuration applies to all operation defined
for the model. Operation level configuration extends, rather than
replaces, any model level configuration.

Examples below apply source code configuration to a hypothetical
`train` operation. Apply them to your own operations as needed.

Disable source code snapshots:

``` yaml
train:
  sourcecode: no
```

^ Disable source code for an operation

Include only Python files and `guild.yml`:

``` yaml
train:
  sourcecode:
    - '*.py'
    - guild.yml
```

^ Use a list of strings to include only those patterns

Include PNG files in addition to source code files (text files < 1M):

``` yaml
train:
  sourcecode:
    - include: '*.png'
```

^ Extend the selection rules by adding `include` rules

Exclude a file or directory:

``` yaml
train:
  sourcecode:
    - exclude: data
    - exclude: dataset.csv
```

^ Restrict selections by adding `exclude` rules

Model and operation level configuration:

``` yaml
- model: cnn
  sourcecode:
    - exclude: data
    - exclude: '*.csv'

  operations:
    train:
      sourcecode:
        # Rules here are applied to those defined for model above.
        - include: train-config.csv
```

^ Define model-level source code rules, which apply by default to operations

Copy souce code from a different root location:

``` yaml
train:
  sourcecode:
    root: src
```

^ Use a mapping to provide additional source code attributes like
  `root` --- see [Source Code Specs - Guild File
  Reference](/reference/guildfile.md#source-code-specs) for more
  information

Copy source code from a different location and define selection rules:

``` yaml
train:
  sourcecode:
    root: src
    select:
      - guild.yml
      - '*.py'
```

^ Use `select` to define the selection rules when specifying
  additional attributes like `root`

Other examples:

- [Guild AI Example: Copy Source guild.yml
  ->](https://github.com/guildai/examples/blob/master/copy-source/guild.yml)

Related help topics:

- [Source Code](ref:source-code)
- [Operations](ref:operations)

### Output Scalars

Examples below define `output-scalars` under a hypothetical `train`
operation. Apply them to your operations as needed.

Output scalars control how Guild logs scalar values from run
output. Patterns are defined as [regular
expressions](https://docs.python.org/3/library/re.html#regular-expression-syntax). Scalar
values are captured using a regular expression capturing group. The
special escape values `\key`, `\value`, and `\step` can be used to
match keys, values, and step values respectively.

By default, Guild detects scalars from output in the format `KEY:
NUMBER` where `KEY` occurs at the start of the line.

The special `step` key is used to capture the current step.

Disable output scalar logging (e.g. you're logging scalars directly
using a TF Event summary writer):

``` yaml
train:
  output-scalars: no
```

Specify patterns as a mapping of scalar key to output pattern:

``` yaml
train:
  output-scalars:
    step: 'Training epoch (\step)'
    loss: 'Validation loss: (\value)'
    acc: 'Accuracy: (\value)'
```

Modify the default pattern:

``` yaml
train:
  output-scalars: '^scalar: (\key)=(\value)'
```

Other examples:

- [Guild AI Example: Customizing Output Scalars
  ->](https://github.com/guildai/examples/tree/master/custom-scalars)

Related help topics:

- [Output Scalars](ref:output-scalars)
- [Operations](ref:operations)

### Optimizers

The `optimizers` operation attribute can be used to specify default
optimizer flags, define a default optimizer, and create alternative
named optimizers.

``` yaml
train:
  optimizers:
    gp:
      default: yes
      kappa: 1.5
      noise: 0.001
    gp-2:
      algorithm: gp
      kappa: 1.8
      noise: gaussian
      xi: 0.1
```

^ Define a default optimizer and an alternative named optimizer

By default, optimizer names reference a Guild *operation*. In the
example above, `gp` is a built-in operation that uses gaussian
processes for Bayesian optimization. To use a different name, specify
the the `algorithm` attribute as the optimizer operation. For example,
the `gp-2` optimizer above uses the `algorithm` attribute to indicate
that its operation is `gp`.

Use the default optimizer:

``` command
guild run train --optimize
```

^ Use the default optimizer defined for an operation

Use a named optimizer:

``` command
guild run train --optimizer gp
```

^ Use a named optimizer

Related help topics:

- [`optimizers` operation
  attribute](/reference/guildfile.md#operation-optimizers)

## Required Files

Run directories are initially empty. To make files available to
operations, specify [required resources](ref:requirements) using
an operation's `requires` attribute.

Require the unpacked contents of `data.zip`:

``` yaml
train:
  requires:
    - file: data.zip
```



## Packages

Package configuration is used by Guild when running
[package](cmd:package).

See [Packages - Guild File
Reference](/reference/guildfile.md#packages) for a full list of
supported package attributes.

``` yaml
- package: hello
  description: Simple hello workd package
  version: 1.0
  url: https://github.com/guildai/packages/tree/master/gpkg/hello
  author: Guild AI
  author-email: packages@guild.ai
  license: Apache 2.0
  data-files:
    - msg.txt

- model: hello
  operations:
    say:
      main: say
      requires:
        - file: msg.txt
```

^ Use a single `package` top-level object to define the Guild file
  package
