tags: concept

<!-- TODO

This is a very light weight pass. Think about what's missing below.

-->

# Operations

[TOC]

## Overview

Operations are used to start [runs](term:run). Operations are
specified when calling [run](cmd:run) in the format:

``` command
guild run OPERATION
```

Operations are defined in [Guild files](term:guildfile).

Operations are defined using one of two formats:

- [Operation only](ref:operation-only-format)
- [Full format](ref:full-format)

*Operation only format* defines operations at the top-level of a Guild
file, as mapping items.

``` yaml
train:
  description: Train a model

validate:
  description: Validate a model
```

^ Two operations defined using *operation only* format

*Full format* defines operations under *models*. Models are defined in
the Guild file as top-level list items.

``` yaml
- model: mnist
  operations:
    train:
      description: Train model on MNIST

    validate:
      description: Validate model on MNIST
```

List available operations using [operations](cmd:operations):

``` command
guild operations
```

!!! tip
    The [ops](cmd:ops) command is a short alias for `operations`.

## Python Based Operations

Python based operations are defined in `*.py` files and must be
specified using their *module name* as the `main` operation attribute
in a Guild file.

``` yaml
train:
  main: train_logreg
```

^ Guild file (`guild.yml`) defining operation `train`, implemented in
Python module `train_logreg`.

!!! note
    Do not include the `.py` suffix when specifying `main`. The
    value refers to the module name, not the file name.

Guild loads such modules as `__main__` in the same way that Python
itself loads them when run using ``python -m <module name>`` from the
command line.

You may perform operation tasks directly in the module like this:

``` python
from models import logreg

logreg.train("data.csv")
```

^ Sample Python module --- always executes task when loaded

Alternatively, check the module name and only perform operation tasks
if it `__main__`.

``` python
from models import logref

def main():
    logreg.train("data.csv")

if __name__ == "__main__":
    main()
```

^ Sample Python module --- execute task only when module is loaded as
  `__main__`

## Other Language Operations

Guild supports non-Python based operations with the `exec` operation
attribute. Use `exec` to specify a command that Guild runs, which can
use any executable program.

For example, the following operation uses R to train a model:

``` yaml
train:
  exec: Rscript .guild/sourcecode/train.r
```

The script `train.r` is prefixed with ``.guild/sourcecode/`` because
operations run in the context of a [run directory](term:run-dir), not
the project directory. Guild copies source code files from the project
to the run directory under `.guild/sourcecode` by default. See
[Operation Source Code](#operation-source-code) for more information.

### Flags Interface

When using non-Python languages to implement an operation, you can
access flags using one of two methods:

- Command line arguments
- Environment variables

#### Command Line Arguments

To use command line arguments, you must specify flag arguments in the
`exec` specification. You can specify flag values in one of two ways:

- Individual flag references
- All flag assignments

To include a flag value in the `exec` command, use the format
``${FLAG_NAME}``.

``` yaml
train:
  exec: .guild/sourcecode/train.sh ${learning-rate} ${batch-size}
  flags:
    learning-rate: 0.1
    batch-size: 100
```

When run using default flag values, Guild will start this operation
using the following command:

``` command
train.sh 0.1 100
```

!!! tip
    Use the `--print-cmd` option with [run](cmd:run) to show the
    command Guild uses to start an operation.

### Environment Variables

Guild always provides flag values as environment variables, regardless
of language type. Environment variables provide a convenient way to
access flags as they don't require command line processing.

## Operation Source Code

Guild saves source code for an operation with each run. This ensures
that the run has a record of the source code used and that changes to
project code don't affect runs in progress.

By default, Guild copies text files within the project directory as
source code. As a safe-guard, Guild skips files larger than 1M and
will not copy more than 100 files. Configures these rules using the
`sourcecode` operation attribute.

See [*Guild File Reference - Source Code
Specs*](/reference/guildfile.md#source-code-specs) for information on
configuring rules for source code copies.

See [*Guild File Cheatsheet - Source
Code*](/cheatsheets/guildfile.md#source-code) for examples.

By default, source code is copied to the run directory under
`.guild/sourcecode`. You can change this location using the `dest`
attribute of the source code spec.
