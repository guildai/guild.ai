tags: concepts

# Operations

[TOC]

An operation is an action performed on a [](term:model). When run, an
operation generates a [](term:run), which is persistent record of the
operation.

Examples of model operations include:

`train`
: Train a model

`evaluate`
: Evaluate a trained model

`finetune`
: Fine tune a pretrained model

`prepare`
: Prepare a dataset for use in training

`generate`
: Use a model to generate content

While these operations are commonly used, model developers are free to
define different operations as needed. For example, if a model
supports compression (e.g. by using quantization), it might define a
`compress` operation.

## Run an operation

To run an operation, use the [](cmd:run) command:

``` command
guild run OPERATION [ARG...]
```

`OPERATION` must include the complete operation name and may also
include package and model information to disambiguate the operation.

To specify the model along with the operation name, use
`MODEL:OPERATION`. For example, to run the `prepare` operation on a
model named `iris-dataset`, you would run:

``` command
guild run iris-dataset:prepare
```

For more information, see the [](cmd:run) command.

### Operation aliases

Some operations are so common that Guild provides
[aliases](term:operation-alias) for them. Aliases let you run commands
this way:

``` command
guild OPERATION_ALIAS [MODEL] [ARG...]
```

The following operation aliases are supported:

- [](cmd:train)

For example, to run the `train` operation on a model, use:

``` command
guild train MODEL
```

This command is equivalent to running:

``` command
guild run MODEL:train
```

## Get operation help

Operation help is displayed for model help when run ``guild
help``. See [Get model help](/docs/models/#get-model-help) and the
[](cmd:help) command for more information on general model help.

You can get help for a specific operation using the ``--help-op``
option with the `run` command (or an operation alias).

Operation help includes the list of flags you can specify for an
operation. This is useful when you have started to type a run command
and want help on available or required flags.

For example, to view operation help for the `train` operation, run:

``` command
guild train --help-op
```

## List operations

To list available operations, run:

``` command
guild operations
```

For more information, see the [](cmd:operations) command.

## Flags

Flags are operation parameters and are used to specify the behavior of
an operation for a run.

Flags are defined by the model operation. For more information on flag
definitions, see [Flags](/docs/reference/guild-file/#flags) in the
Guild file reference.

Flag values are specified using `NAME=VALUE` arguments to the
[](cmd:run) command (or operation alias).

For example, consider the operation help for
`keras.mnist/mnist-mlp:train`, which we can show by running:

``` command
guild run mlp:train --help-op
```

``` output
Usage: guild run [OPTIONS] mnist-mlp:train [FLAG]...

Train the MLP

Use 'guild run --help' for a list of options.

Flags:
  batch-size  Training batch size (default is 128)
  epochs      Number of epochs to train (default is 20)
```

As described in the operation help, `mnist-mlp:train` supports two
flags: `batch-size` and `epochs`. If we wanted to train the model over
`10` epochs using a batch size of `64`, we would use:

``` command
guild train batch-size=64 epochs=10
```

## Required resources

Operations may require [resources](term:resource). Required resources
are listed in the operation's `requires` attribute.

When Guild starts an operation, it first resolves each required
resource. If a resource cannot be resolved, the operation fails with
an error message.

Resources are resolved by acquiring them (e.g. download a file from
the Internet), verifying them, and finally creating links to resources
files in the run directory. In this way, operations can easily express
"I need these files to run" and ensure that the correct files are
available for each run.

In most cases resources are automatically resolved, but in some cases
an operation may require that the user specify a resource. Resources
can be specified the same way flag values are specified---using
`NAME=VALUE`. In the case of a resource, `VALUE` is the name of the
required resource.

Required resources are described in operation help, if applicable.

## Implementing an operation

Operations are implemented in Python modules. If `main` is specified,
the module must execute when loaded, and should use this pattern:

``` python
def main():
    "Operation code here."

if __name__ == "__main__":
    main()
```

Operations are executed in the context of the current run directory.

Run [flags](term:flag) are provided to the main module as command
arguments, which are accessible in the Python `sys.argv` list. You can
use the Python [argparse
->](https://docs.python.org/library/argparse.html) module to parse
arguments.

<div id="environment-variables"></div>

Operations have access to a number of environment variables.

`CMD_DIR`
: Path where the operation was run. This is the original working
  directory that was changed to `RUN_DIR` for the operation.

`GUILD_HOME`
: Guild install location.

`GUILD_OP`
: Name of the operation including the model.

`GUILD_PLUGINS`
: Comma separated list of active Guild plugins.

`LOG_LEVEL`
: Python log level active for the run.

`MODEL_DIR`
: The directory containing the operation model definition. This is
  where the Guild file is located and can be used to reference
  relative files.

`RUN_DIR`
: Active run directory path. This is the working directory during an
  operation. See `CMD_DIR` for the original working directory -
  i.e. where the operation was run from.

`RUN_ID`
: Active run ID.
