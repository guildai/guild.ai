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

## Miscellaneous

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
