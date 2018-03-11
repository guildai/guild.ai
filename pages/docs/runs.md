tags: concepts

# Runs

[TOC]

## Overview

Runs are generated in Guild AI by running an [](term:operation).

When you train a model, you generate a *run*, which contains the
trained model as well as training logs and other artifacts associated
with the operation.

Similarly, when you fine tune a model, you generate a run. When you
test a model, you generate a run. In fact, any operation that you run
generates a distinct run. This is how Guild manages your work.

Here is a common work flow:

- Find and install a model
- Run an operation on that model (e.g. `train`)
- Monitor the progress of the operation (e.g. `view`)
- Run another operation with different hyper-parameters (flags)
- Compare runs
- Delete runs that you're no longer interested in
- Select successful runs for deployment or use in other operations

The work centers on *runs* --- creating, comparing, and selecting.

## Concepts

As you work with runs in Guild it's important to understand some core
concepts. If you'd prefer to skip this conceptual material, jump to
[Start a run](#start-a-run) below.

### Run directory

A *run directory* is a file system directory (or folder) that contains
artifacts associated with a run. Guild creates a unique run directory
for every run. This directory contains a variety of important data:

- Run metadata
- Run sources such as datasets
- Run output such as event logs and saved models

Run directories are located in `GUILD_HOME/runs`. For more information
see [Guild home](/docs/reference/guild-home/).

Run related operations interact with run directories in various ways:

- ``guild run`` creates a new run directory
- ``guild runs info`` prints information read from a run directory
- ``guild runs list`` enumerates run directories
- ``guild runs delete`` deletes run directories

### Limiting runs

Over time you'll generate a large number of runs. This list can become
unwieldy, especially when you're interested in a small subset ---
e.g. runs associated with a particular model you're working with. For
this reason, Guild provides two ways of limiting the runs that apply
to run related commands:

- Limit to runs associated with a model defined in the current
  directory
- Limit to runs that match a filter

#### Run scope

The first limit is known as *run scope*. Scope can be either *local*
or *global*. By default, scope is local when the current directory
contains a [model definition](term:model-def), otherwise scope is
global. Local scope limits runs to those associated with models
defined in the current directory. Global scope displays all runs.

Global scope can be applied using the ``--all`` (or ``-a``) option.

Run scope is applied based on the directory that Guild commands are
run in. Consider the following directory structure:

<div class="file-tree">
<ul>
<li class="is-folder open">Home<i>Does not contain a model definition &mdash; global scope applies</i>
<li class="is-folder open">Models
 <ul>
 <li class="is-folder open">mnist <i>Contains a model definition &mdash; local scope applies</i>
  <ul>
  <li class="is-file">MODELS <i>Model definition</i></li>
  </ul>
 </li>
 </ul>
</li>
</ul>
</div>

Commands run the from `/Home` have *global* run scope because `/Home`
doesn't contain a model definition. Commands run from `/Models/mnist`
however have *local* scope because that directory contains a model
definition (`/Models/mnist/MODELS`).

Run scope defaults to *local* when a model definition is exists
because Guild assumes that the user is working on models defined at
that location and is not interested in other runs, at least by
default. This follows the pattern of command line tools such as `git`
that apply operations locally when they find a project, repository,
etc. in the current directory.

When a command is run in local scope, Guild prints a message to
indicate that results are limited:

    Limiting runs to the current directory (use --all to include all)

#### Run filtering

The other limit is *run filtering*. Filters are applied with command
line options that specify run attributes, which may include:

- Operation
- Run status
- Deleted status

Run filtering is applied *after* run scope (see above).

For example, to view runs that are associated with the `train`
operation, use the ``--op`` (or ``-o``) option:

``` command
guild runs --op train
```

If the command is in local scope, Guild will limit runs to those
associated with models in the current directory otherwise it will use
all runs. It will then filter those runs, limiting the result to those
associated with operations containing the string "train".

### Selecting runs

Some run related commands let you select one or more runs:

- [](category:/docs/commands/#runs-select)

For these commands, runs can be specified in various ways:

- Index as returned by ``guild runs`` or ``guild runs list``
- Run ID (full or partial if unique)

Additionally, a range may be specified using run indexes in the form:

    [START]:[STOP]

`STOP` and `START` are inclusive --- runs are selected beginning with
the `STOP` index up to and including those with the `START` index.

Both `STOP` and `START` are optional. If `START` is omitted it is
assumed to be ``0`` (i.e. the first run in the list). If `STOP` is
omitted it is assumed to be the index of the last run.

!!! important
    Run indexes are relative to the list of runs returned by ``guild
    runs`` or ``guild runs list`` for a given scope and filter (see
    [Limiting runs](#limiting-runs) above). The run associated with index
    ``0`` for one listing may not be the same run for another
    listing. Always verify the selected runs before proceeding with a
    command.

    When in doubt, use a run ID to select a run.

#### Examples

Consider this output from ``guild runs``:

```
Limiting runs to the current directory (use --all to include all)
[0:9734f85e]   ./slim-resnet-101:train        2017-12-14 07:56:32  terminated
[1:d8cde0fc]   ./slim-resnet-50:export        2017-12-13 13:14:31  completed
[2:0df943ac]   ./slim-resnet-50:predict       2017-12-06 11:51:15  completed
[3:e150e44a]   ./slim-resnet-50:predict       2017-12-06 11:50:00  completed
```

!!! note
    The [run scope](term:#run-scope) in the above command is *local*. If
    the user had run ``guild runs --all`` the scope would be *global* ---
    the list and run indexes would likely be different.

Below are various operations with run selectors applied to this
list.

``guild runs rm 0``
: Delete run `9734f85e` (you can always use index ``0`` to select the
  most recently started run in the list)

``guild runs rm 1:2``
: Delete runs `d8cde0fc` and `0df943ac`

``guild runs rm :``
: Delete all runs

``guild runs rm 0df943ac e150e44a``
: Delete runs `0df943ac` and `e150e44a`

!!! note
    The following assumptions must hold for the above examples that use
    run indexes:

    - Commands must be executed in the same directory as the command
      that generated the list and without scope modifiers or filters

    - The runs themselves must not change --- i.e. runs cannot be deleted
      or started

## Start a run

To start a run, use the [](cmd:run) command. The basic format of a
`run` command looks like this:

```
guild run OPERATION
guild run MODEL:OPERATION
guild run PACKAGE/MODEL:OPERATION
```

You can list available operations using the [](cmd:operations)
command.

In general, you can omit information about an operation name as long
as Guild can uniquely identify the operation.

For example, if the output of `operations` looks like this:

``` output
iris/iris-cnn:train
iris/iris-cnn:finetune
iris/iris-cnn:test
```

You can start the `finetune` operation by running:

``` command
guild run finetune
```

You can always provide the model or package. For example, this form
will also start `finetune`:

``` command
guild run iris-cnn:finetune
```

You use part of the operation specification as long as Guild can
uniquely identify the operation. For example, you can run the `test`
on `iris-cnn` using:

```
guild run cnn:train
```

### Operation aliases

Some operations are so common that Guild provides *alias*
commands. Aliases currently include:

- [](cmd:train)

Aliases are used to start operation using these forms:

```
guild ALIAS_CMD
guild ALIAS_CMD MODEL
guild ALIAS_CMD PACKAGE/MODEL
```

The `train` alias is used to run the `train` operation. In the example
above, the following commands can be used to train the iris model:

```
guild train
guild train iris-cnn
guild train cnn
```

## Flag values

Specify operation flag values as `NAME=VALUE` arguments to [](cmd:run).

To get help on available and required flags for an operation, run:

``` command
guild run OPERATION --help-op
```

You can also view help for models defined in the current directory by
running:

``` command
guild help
```

To get help for a packaged model, run:


``` command
guild help PACKAGE
```

If you omit a required flag, the `run` command (or applicable alias)
will exit with an error message.

## List runs

To list Guild runs, use the [](cmd:runs) or [runs list](cmd:runs-list)
command.

``guild runs`` is shorthand for ``guild runs list``.

When listing runs, be aware of [run scope](term:#run-scope) and [run
filtering](term:#run-filtering) --- these effect the runs that are
displayed.

``guild runs``
: List all runs with the run scope. If the current directory contain a
  [model definition](term:model-def) the list is limited to runs
  associated with the locally defined models, otherwise the list will
  contain all runs.

``foo``
: Another thing yo.

The command:

```
guild runs
```

will display different lists depending on the directory it's run
in. If the directory contains a model definition, runs will be limited
to those associated with the locally defined models. If the directory
does not contain a model definition, all runs are displayed.

## Get run information

Use [runs info](cmd:runs-info) to show information about a run.

By default, Guild shows information about the latest run:

``` command
guild runs info
```

You can select a specific run by providing a run ID or index.

Run indexes are displayed in run lists (see [List runs](#list-runs)
above).

## Compare runs

Compare runs by running:

``` command
guild compare
```

Guild Compare is spreadsheet-like application that displays runs,
their status, and metrics such as validation accuracy and training
loss.

To display compare results as a table, use:

``` command
guild compare --table
```

To display compare results in CSV format (e.g. for use in Excel), use:

``` command
guild compare --csv
```

For more help, see the [](cmd:compare) command.

## Label runs

Runs can have *labels*, which provide additional information about the
run. A label can used for filtering in the [runs list](cmd:runs-list)
command.

Use [runs label](cmd:runs-label) to set or clear a label for a run.

Use ``guild runs list LABEL`` to list runs with the specified label.

## Delete runs

Delete runs using ``guild runs delete`` or ``guild runs rm``. See
[runs delete](cmd:runs-delete) for command details.

Guild will display the list of runs to be deleted and ask you to
confirm the operation. You must type ``y`` and then press `ENTER` to
confirm.

Deleted runs can be restored using the [runs
restore](cmd:runs-restore) command. Refer to [Restoring deleted
runs](#restore-deleted-runs) below for details.

### Frequently used delete commands

To delete all failed runs, use:

``` command
guild runs rm -E
```

To permanently delete all failed runs, use:

``` command
guild runs rm -Ep
```

!!! important
    Permanently deleted runs cannot be recovered!

To delete all failed and terminated runs, use:

``` command
guild runs -ET
```

## Restore deleted runs

Deleted runs can be recovered by running:

``` command
guild runs restore [RUN...]
```

For more help, see the [runs restore](cmd:runs-restore) command.

## Purge deleted runs

The disk space used by deleted runs can be recovered by permanently
deleting them using [runs purge](cmd:runs-purge).

!!! tip
    You can show the list deleted runs using ``guild runs --deleted``.

For example, to permanently delete all deleted runs, use:

``` command
guild runs purge
```

Guild will prompt you before proceeding.

!!! important
    Purging deleted runs will permanently delete them! Be certain that
    you don't need a run before permanently deleting it.

For more help, see the [runs purge](cmd:runs-purge) command.
