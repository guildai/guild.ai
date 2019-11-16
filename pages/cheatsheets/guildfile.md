# Guild File Snippets

[TOC]

### Import Flags

By default, Guild attempts to import flags from an operation's main
module. If Guild's default behavior is not correct, consider some of
the examples below.

Import specific flags:

``` yaml
train:
  flags-import:
    - lr
    - batch_size
    - epochs
    - dropout
```

^ guild.yml snippet --- import specific flags

Import all flags with some exceptions:

``` yaml
train:
  flags-import-skip:
    - data_dir
    - log_dir
```

^ guild.yml snippet --- import all flags with exceptions

Disable all flag imports:

``` yaml
train:
  flags-import: no
```

^ guild.yml snippet --- disable flag imports

!!! tips
    - Disable flags import to prevent Guild from automatically
      scanning operation modules for flag information.

Related Help Topics:

- [Operations](ref:operations)

### Flags Interface

By default, Guild attempts to detect an operation module's flags
interface. It does this by checking if the module imports
`argparse`. If it does, Guild uses command line arguments to pass flag
values. Otherwise, Guild sets flag values as module global variables.

Explicitly the interface to use command line arguments:

``` yaml
train:
  flags-dest: args
```

^ guild.yml snippet --- use command line arguments to pass flag values

Set flags interface to use global variables:

``` yaml
train:
  flags-dest: globals
```

^ guild.yml snippet --- set flag values as module globals

Set flags interface to set values in a global `params` dict:

``` yaml
train:
  flags-dest: global:params
```

^ guild.yml snippet --- set flag values as items in a global dict

!!! tips
    - Specify a flags interface by setting `flags-dest` to prevent
      Guild from scanning operation modules for interface type.

    - See [Magic](ref:magic) for information on how Guild scans
      modules for interface type and how it sets module global
      variables.

Other Examples:

- [Guild AI Example: Flags Interface
  ->](https://github.com/guildai/examples/tree/master/flags-dest)

Related Help Topics:

- [Operations](ref:operations)

### Define a Flag

Flags must be defined using the `flags` operation attribute. The
samples below are for a hypothetical `train` operation. Change
`FLAG_NAME` and attributes as needed. Delete sections that don't
apply.

``` yaml
train:
  flags:
    FLAG_NAME:
      description: A sample flag
      default: 100

      # List of legal values.
      #choices: [1, 2, blue, shoe]

      # Let user specify a non-choice value when choices are
      # defined.
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

Related Help Topics:

- [Flags](ref:flags)

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
  output-scalars: '^scalar: (\name)=(\value)'
```

Other Examples:

- [Guild AI Example: Customizing Output Scalars
  ->](https://github.com/guildai/examples/tree/master/custom-scalars)

##### Related Help Topics

- [Output Scalars](ref:output-scalars)
- [Operations](ref:operations)

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

Include only Python files and `guild.yml`:

``` yaml
train:
  sourcecode:
    - '*.py'
    - guild.yml
```

Include PNG files in addition to source code files (text files < 1M):

``` yaml
train:
  sourcecode:
    - include: '*.png'
```

Exclude a file or directory:

``` yaml
train:
  sourcecode:
    - exclude: data
    - exclude: dataset.csv
```

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

Copy soucecode from a different root location:

``` yaml
train:
  sourcecode:
    root: src
    # Omit select for default behavior.
    select:
      - guild.yml
      - '*.py'
```

Other Examples:

- [Guild AI Example: Copy Source guild.yml
  ->](https://github.com/guildai/examples/blob/master/copy-source/guild.yml)

Related Help Topics:

- [Source Code](ref:source-code)
- [Operations](ref:operations)

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
