sidenav_title: Guild File

# Guild File Cheatsheet

[TOC]

## Operations

#### Default operation

Guild assumes that an operation that does not define `main` or `exec`
is a Python operation implemented in a module with the same name as
the operation.

``` yaml
train:
  description: Python operation implemented in train module
```

!!! note
    Invalid characters in the operation name are converted to
    underscores ``_``. E.g. Guild assumes that the operation
    ``mnist-train`` is implemented in the Python module named
    ``mnist_train``.

#### Python based operation

Use the `main` attribute to specify the main Python module for an
operation:

``` yaml
train:
  main: mnist_train
```

Use standard Python dot notation to reference a module within a package:

``` yaml
train:
  main: mypackage.train
```

If a module is defined in a sub-directory, precede the module name
with the path:

``` yaml
train:
  main: src/train
```

Provide arguments to a module as needed:

``` yaml
train:
  main: main --train
```

!!! note
    Guild automatically appends all flag arguments to the `main`
    spec when the flags interface is `args`. To prevent a flag value
    from appearing as an argument, set its `arg-skip` attribute to
    `yes`.

#### Non-Python based operation

Use `exec` to define a command for running an operation.

``` yaml
train:
  exec: Rscript train.r
```

Flag values are available as environment variables named
`FLAG_<name>`. For example, a flag named `learning_rate` is available
as the environment variable `FLAG_learning_rate`.

Alternatively, use command arguments are needed to pass flag values:

``` yaml
train:
  exec: Rscript train.r --learning-rate ${learning-rate}
  flags:
    learning-rate: 0.1
```

Use ``${flag_args}`` to pass all flags as arguments:

``` yaml
train:
  exec: Rscript train.r ${flag_args}
  flags:
    learning-rate: 0.1
    batch-size: 100
```

## Source Code

!!! important
    Guild executes operation code in new, empty [run
    directories](term:run-dir). Operations must be configured so that
    all required source code is available for a run.

    By default, Guild copies text files under 1M as source code. As a
    safeguard, Guild will not copy more than 1000 files. The examples
    in this sction illustrate how to explicitly configure operation
    source code.

#### Disable source code snapshot

Use to skip the source code snapshot:

``` yaml
train:
  sourcecode: no
```

#### Limit source code to matching patterns

``` yaml
train:
  sourcecode:
    - `*.py`
    - `*.yml`
```

#### Exclude patterns

``` yaml
train:
  sourcecode:
    - exclude: '*.ini'
```

#### Skip matching directories

Guild scans all project directories for matching source code
files. Directories that contain a large number of files may take a
long time to scan.

Exclude these directories using the `dir` attribute of a mapping:

``` yaml
train:
  sourcecode:
    - exclude:
        dir: dir-with-many-files
```

#### Use alternate root for source code

When source code is located outside of the project directory (i.e. the
directory containing `guild.yml`), use the `root` attribute of
`sourcecode`.

``` yaml
train:
  sourcecode:
    root: ../src
```

To specify selection criteria, use the `select` attribute:

``` yaml
train:
  sourcecode:
    root: ../src
    select:
      - '*.yml'
      - '*.py'
```

## Flags

Related help:

- [Flags Overview](/flags.md)
- [Flags - Guild File Reference](/reference/guildfile.md#flags)

### Flag Imports

#### Import all flags

When Guild correctly detects your script flags and you want to import
all of them:

``` yaml
train:
  flags-import: all
```

#### Import some flags

Specify the flags that Guild imports:

``` yaml
train:
  flags-import:
    - learning_rate
    - batch_size
    - dropout
```

If the list is large, consider [importing all flags but skipping
some](#import-all-but-some-flags).

#### Import all but some flags

Use when Guild detects most of the flags correctly but you want to
skip some:

``` yaml
train:
  flags-import: all
  flags-import-skip:
    - not_a_flag_1
    - not_a_flag_1
```

### Flag Interface

By default, Guild automatically detects the flags interface for a
Python script as one of either:

- `globals` --- sets flags via Python global variables
- `args` --- sets flags using command line options

Guild does not automatically support a flags interface for non-Python
scripts --- i.e. scripts run using the `exec` operation attribute.

#### Use global variables for Python scripts

If your script does not import `argparse`, Guild will automatically
use `globals` as the flags interface.

Set `globals` explicitly:

``` yaml
train:
  flags-dest: globals
```

#### Use command line arguments for Python scripts

Use when your script does not import `argparse` or to cause Guild to
skip the check for `argparse` imports:

``` yaml
train:
  flags-dest: args
```

#### Use a global dict for Python scripts

Set flag values as items of the `params` global variable:

``` yaml
train:
  flags-dest: global:params
```

#### Use all flag args with `exec`

Use `exec` for non-Python scripts. Flags may be specified as command
line arguments using ``${flag_args}`` in an `exec` command.

``` yaml
train:
  exec: echo ${flag_args}
  flags:
    msg: hello
```

Example use:

``` command
guild run train
```

``` output
You are about to run test
  msg: hello
Continue? (Y/n)
--msg hello
```

#### Use flag values with `exec`

Include specific flag values in an `exec` command using the format
``${FLAG_NAME}``:

``` yaml
train:
  exec: echo ${msg}
  flags:
    msg: hello
```

Example use:

``` command
guild run train
```

``` output
You are about to run test
  msg: hello
Continue? (Y/n)
hello
```

### Flag Definitions

Flags are defined by the `flags` operation attribute. If a flag is
imported, a flag definition modifies the imported attributes.

#### Simple flag definition

When a flag definition consists of a single value, the value is used
as the default flag value.

``` yaml
train:
  flags:
    learning-rate: 0.1
    batch-size: 100
```

This is equivalent to:

``` yaml
train:
  flags:
    learning-rate:
      default: 0.1
    batch-size:
      default: 100
```

Include a description (used in operation help):

``` yaml
train:
  flags:
    learning-rate:
      description: Learning rate used for training
      default: 0.1
    batch-size:
      description: Batch size used for training
      default: 100
```

#### Required flag value

``` yaml
train:
  flags:
    data:
      description: Location of data file
      required: yes
```

#### Flag choices

``` yaml
train:
  flags:
    optimizer:
      choices:
       - adam
       - sgd
       - rmsprop
      default: sgd
```

Choices with description:

``` yaml
train:
  flags:
    optimizer:
      choices:
       - value: adam
         description: Adam optimizer
       - value: sgd
         description: Stochastic gradient descent optimizer
       - value: rmsprop
         description: RMSProp optimizer
      default: sgd
```

Required choice:

``` yaml
train:
  flags:
    dropout:
      choices: [0.1, 0.2, 0.3]
      required: yes
```

#### Flag types

Related help:

- [Flag Value Types](/flags.md#flag-value-types)
- [Flag Value Decoding](/flags.md#flag-value-decoding)

By default, Guild applies the rules described in [Flag Value
Decoding](/flags.md#flag-value-decoding) when decoding user-provided
flag values. Define a type when you need to validate user input or
explicitly convert values that might be incorrectly decoded.

``` yaml
train:
  flags:
    data:
      type: existing-path
      default: data
    data-digest:
      type: string
      required: yes
    learning-rate:
      type: float
      default: 0.1
```

#### Rename flag arg

``` yaml
train:
  flags:
    learning-rate:
      arg-name: lr
```

If the flag interface is `args` (i.e. command line arguments), the
flag option is ``--lr VAL`` rather than ``--learning-rate VAL``.

Similarly, if the flag interface is `globals`, the target variable
name is `lr`.

## Output Scalars

Related help:

- [Scalars Overview](/scalars.md)
- [Output Scalars Spec - Guild File
  Reference](/reference/guildfile.md#output-scalar-specs)

#### Disable output scalars

Disable output scalars when you log scalars explicitly to summaries:

``` yaml
train:
  output-scalars: no
```

#### Map scalar keys to patterns

Use when you have a limited number of scalars or want to strictly
control what's captured.

``` yaml
train:
  output-scalars:
    step: 'Training epoch (\step)'
    loss: 'Validation loss: (\value)'
```

#### Capture scalar key

Capture both key and value. Use when possible as this method
automatically captures new scalars that match the format.

``` yaml
train:
  output-scalars: ' - (\key): (\value)'
```

!!! note
    The captured key is always the *first group* and value is the
    *second group*. ``\key`` and ``\value`` above are pattern
    templates and are not used to identify what is captured.


#### Named capture groups

Use named capture groups to specify the key for a paricular pattern.

``` yaml
train:
  output-scalars: 'epoch (?P<step>\step) - train loss (?P<loss>\value) - val loss (?P<val_loss>\value)'
```

#### Multiple output scalar specs

Use a list of specs as needed to define output scalars.

``` yaml
train:
  output-scalars:
    - 'Epoch (?P<step>\step)'
    - loss: 'loss: (\value)'
      acc: 'accuracy: (\value)'
    - '(\key)=(\value)'
```


## Resources

### Required Files

#### Require project files and directories

``` yaml
train:
  requires:
    - file: data.csv
```

``` yaml
train:
  requires:
    - file: data-dir
```

Unpack and link to archive contents:

``` yaml
train:
  requires:
    - file: data.tar.gz
```

Link to archive files matching pattern:

``` yaml
train:
  requires:
    - file: data.tar.gz
      select: train/
```

Link to archive without unpacking:

``` yaml
train:
  requires:
    - file: data.tar.gz
      unpack: no
```

### Other Required Resources

#### Verify required Python modules

``` yaml
train:
  requires:
    - module: pandas
    - module: sklearn
    - module: matplotlib
```

!!! note
    Guild will not install modules listed under `requires`. Guild
    verifies the availability of the modules and exits with an error
    message if they cannot be loaded.

#### Configuration files

When resolve, configuration files are re-written to include run flag
values.

``` yaml
train:
  requires:
    - config: config.yml
```

## Other

### Operation Plugins

Enable summary-related plugins, which log additional scalars for each
step.

```yaml
train:
  plugins: summary
```

Explicitly enable each summary-related plugin.

``` yaml
train:
  plugins: [cpu, gpu, disk, memory, perf]
```

{! summary-plugin-support-notice.md !}

---------------

## Operations (OLD)


Include base arguments in the main specification:

``` yaml
train:
  main: model --train
  flags-import: all
```


#### Flags Import

Specify a list of flags to import, skipping any detected flags that
are not specified:

``` yaml
train:
  flags-import:
    - epochs
    - lr
```

To import all flags but a specified list of flags:

``` yaml
train:
  flags-import: all
  flags-import-skip:
    - num_classes
```

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

To force Guild to use a globals interface:

``` yaml
train:
  flags-dest: globals
  flags-import: all
```

To write flag values to a global Python dict named `params`:

``` yaml
train:
  flags-dest: global:params
  flags-import: all
```

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

^ guild.yml

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

^ guild.yml

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

^ guild.yml

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

Use a named optimizer:

``` command
guild run train --optimizer gp
```

Related help topics:

- [`optimizers` operation
  attribute](/reference/guildfile.md#operation-optimizers)

## Required Files (OLD)

Run directories are initially empty. To make files available to
operations, specify [required resources](ref:requirements) using
an operation's `requires` attribute.

Require the unpacked contents of `data.zip`:

``` yaml
train:
  requires:
    - file: data.zip
```



## Packages (OLD)

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
