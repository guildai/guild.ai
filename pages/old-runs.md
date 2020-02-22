tags: concept

<!-- TODO

- Section on Run Filters - refer to this wherever filters are
  referenced

- Section on staging

-->

# Runs

[TOC]

## Overview

A Guild *run* generally corresponds to single ML experiment. However,
a run may be any type of operation, including data preparation, model
optimization, model compression, deployment --- or any other action
you want to perform as a part of your ML pipeline.

The term "run" may refer to one of two things:

- The *operating system process* associated with the operation
- The *run directory* containing metadata associated with the
  operation and all files associated with the run

The meaning of *run* can typically be inferred from the usage
context. For example, to "stop a run" means to terminate the operating
system process associated with a run. To "delete a run" means to
delete the run directory.

### Guild Runs vs Script Execution

A Guild run is similar to traditional script execution:

- Run a program as an operating system process
- Determine run status by process exit code (0 for success, non-zero
  for failure)

A Guild run is different from traditional script execution:

- A run process is associated with a unique *run directory* rather
  than the current directory
- Guild saves run metadata along with run-generated files in the run
  directory

Guild alters the run program by setting the process *current working
directory* to the run directory. Files written with relative paths are
written to the run directory.

Guild additionally writes run metadata to a `.guild` subdirectory
within the run directory. Run metadata includes:

- Operation name
- Flag values
- Process information such as command, environment, pid and exit code
- Source code at the time the script is executed
- Start and stop time
- Platform information
- Output written to standard output and error streams
- Metrics parsed from run output

With this simple scheme, Guild isolates runs to capture unique
experiments without relying on containers or virtual machines for
isolation.

### Run Directory

A *run directory* is a unique directory created for a run process. Run
directories are stored under [Guild home](term:guild-home) for an
environment. See [Environments](/environments.md) for information
about Guild home and the location of runs.

All metadata and generated files associated with a run are located in
the run directory.

You may move or delete a run directory, however, keep in mind the
following:

- Avoid moving or deleting a run directory while the run is in a
  `running` status. Stop the run first using [stop](cmd:stop) or by
  terminating the run process (use [runs info](cmd:runs-info) to show
  the run `pid`).

- You can relocated a run using [export](cmd:export) rather than
  moving the directory.

- You can delete a run using [runs delete](cmd:runs-delete). This
  command provides a safe-guard for deleting running runs. It also
  lets you restore deleted runs, provided you don't specify the
  command `--permanent` option.

### Run Status

If a run process is alive, the run is said to be *running*. Otherwise
the run is *not running* and has one of the following status based on
the process state:

completed
: Run completed successfully --- i.e. exited with a 0 status.

error
: Run completed unsuccessfully --- i.e. exited with a non-0 status.

terminated
: Run was stopped prior to completion by the user or a system signal.

pending
: Guild started the run but the operating system process has not yet
  started.

staged
: Guild staged the run to be started later.

Run status is displayed for various Guild commands including
[runs](cmd:runs), which lists runs, and [runs info](cmd:runs-info),
which shows information about a run.

## Start a Run

Start a run using [](cmd:run). You can run a script directly or run an
operation defined in a [Guild file](term:guildfile).

To run a script, specify the path to the script:

``` command
guild run train.py
```

When running a script directly, Guild inspects the script and attempts
to identify its input parameters, or [flags](term:flags). If the flags
that Guild detects are incorrect, you can explicitly define them in a
[Guild file](ref:guildfile).

If a project provides a Guild file (i.e. a file named `guild.yml`),
you can list available operations by running:

``` command
guild operations
```

Guild lists the operations defined in the Guild file.

You can run any of the operations:

``` command
guild run OPERATION
```

By default, Guild shows a preview of the operation, including the
script or operation name and flag values used. Review the information
and press `Enter` to start the run. If you need to change anything,
press `n` and `Enter`.

If you want to bypass the confirmation --- or you are running the
command in a script or other unattended mode --- specify the `--yes`
option.

### Specify Run Flags

*Flags* are run settings that can be specified as arguments to the
`run` command. Flags are specified using the format
``NAME=VALUE``. Each flag assignment must be provided as a single
`run` command argument.

For example, the following

### Run in the Background

By default, Guild executes runs in the foreground. To run an operation
in the background, specify either the `--background` or `--pidfile`
option.

You can watch the progress of a background run using
[](cmd:watch). Note that watching a run does not attach to the process
--- it merely tails the operation log. Therefore typing `Ctrl-C` in a
command terminal when watching a run will not terminate the run. To
stop a background run, use [](cmd:stop).

## List Runs

Use [runs](cmd:runs) to list available runs.

``` command
guild runs
```

![](assets/img/runs.png)

^ Sample runs list

Guild shows the following run information:

Runs list index and run ID
: The first column contains the runs list index and run ID, which are
  separated by a colon. The runs list index starts with 1 and is
  incremented by 1 for each subsequent run. The index value may be
  used reference a run by its position in the list. The run ID is the
  first eight characters of the unique full run ID. Use the run ID to
  reference a run independent of its order in a list.

    Note that the runs list index changes based on the number of runs
    and the filter used in the `runs` command.

    Either the index or run ID can be used whenever a ``RUN`` argument
    is supported for a Guild command. For example, to show information
    for the second run in the list (index `2`), use ``guild runs info
    2``.

Operation
: The second column of the runs list shows the run operation. The
  operation name is used in the [run](cmd:run) command. You can filter
  the runs list by operation name using the `-o` or `--operation`
  option. For example, to show only runs containing "train" in their
  operation, use ``guild runs -o train``.

Start date and time
: The third column shows the start date and time of the run. You can
  filter runs by start time using the `-s` or `--started`
  option. Guild supports a flexible filter specification for start
  time. Refer to [Filter Runs by Start
  Time](/commands/runs-list.md#filter-by-run-start-time) for more
  information on limiting runs by start time.

Run status
: The fourth column shows the run status. Refer to [Run Status](#run-stats)
  for a list of possible values for this column.

Label

: The fifth column shows the run label. Run labels are arbitrary
  strings used to identify a run. By default, Guild assigns a run
  label based on user provided flag values. You can set the label for
  a run using the `-l` or `--label` option of the `run` command. See
  [Label Runs](#label-runs) for more information.

<!-- TODO

- Elaborate on start time filter in user docs here

-->

The `runs` command supports a number of options for filtering
runs. For example, to show only *terminated* runs, use the `-T` or
`--terminated` option.

To filter runs by operation, use `-o` or `--operation`. Guild shows
all runs whose operations contain the specified value.

For a complete list of filters, see [runs](cmd:runs).

By default, Guild shows only the latest 20 runs. To view more runs,
use the `-m` or `--more` option, which shows an additional 20 runs for
each occurrence.

To show all runs, use `-a` or `--all`.

## Get Information About a Run

To show information about a run, use [runs info](cmd:runs-info).

``` command
guild runs info [RUN]
```

By default, Guild shows information for the latest run. Specify a
value for `RUN` to show information for a specific run. You can use a
run index, where `1` is the most recent run for the given set of
filters.

For example, to show the latest successful run for an operation
matching the string `train`, use:

``` command
guild runs info 1 --completed --operation train
```

To can alternatively use a run ID for `RUN` to reference a run
explicitly.

You can show information for any run, even those still running. Guild
shows the latest information at the time [runs info](cmd:runs-info) is
executed.

### List Run Files

To list files associated with a run, use [ls](cmd:ls). By default,
Guild shows files associated with the latest run. You can specify an
alternative run, using an index or a run ID.

``` command
guild ls [RUN]
```

Run files are stored in the [run directory](ref:run-dir).

Commonly used [ls](cmd:ls) options include:

`-f, --full-path`
: Show the full path for each run file. This is useful when you want
  to access a run file using its full path.

`-a, --all`
: Show all run files, including Guild-managed files, which are located
  in the `.guild` subdirectory.

`-L, --follow-links`
: Show files under symbolic link directories. By default, Guild does
  not follow linked directories.

`-p, --path`
: List contents of a subpath with the run directory.

For a complete list of options, see the [``ls``
command](/commands/ls).

### View Run File Contents

To view the contents of a run file, use [cat](cmd:cat) with the ``-p,
--path`` option. By default, the ``cat`` command applies to the latest
run. To view a file for a different run, specify the run index or run
ID.

``` command
guild cat [RUN] -p PATH
```

!!! note
    [cat](cmd:cat) prints file contents to standard output and is
    therefore typically used to view text files. You can use `cat` to
    copy a file using [IO redirection
    ->](https://www.tldp.org/LDP/abs/html/io-redirection.html). For
    example, to write a file `model.ckpt` to `/tmp/model.ckpt`, use
    ``guild cat -p model.ckpt > /tmp/model.ckpt``.

### View Run Output

To view run output, use [cat](cmd:cat) with the `--output` option:

``` command
guild cat --output [RUN]
```

Use the `--page` option to use a pager when viewing long files or
output.

``` command
guild cat --output --page
```

## Compare Runs

Guild provides several ways to compare runs. Refer to the
documentation for each of these tools for more information.

[Guild Compare](ref:guild-compare)
: Curses based application (terminal friendly) for comparing runs and
  exporting comparison data to CSV.

[Guild View](ref:guild-view)
: Visual application to compare runs and explore run results.

[Guild Diff](ref:guild-diff)
: Integration with diffing tools to compare run files.

[TensorBoard](ref:guild-tensorboard)
: Visual application developed by the TensorFlow team for comparing
  run scalars, images, hyperparameters, and other run summaries.

## Delete Runs

Use [runs delete](cmd:runs-delete) or its alias [runs rm](cmd:runs-rm)
to delete runs.

By default Guild prompts you with the full list of runs it will delete
before deleting them. This gives you an opportunity to review the list
before deleting runs. If you want to bypass this prompt and have Guild
delete the runs directly, use the `--yes` or `-y` option.

By default, you can restore deleted runs using [runs
restore(cmd:runs-restore) (see below). If you want to permanently
delete runs, use the `--permanent` or `-p` option.

!!! important
    Permanently deleted runs cannot be restored.

!!! tip
    Avoid using `--permanent` when deleting runs. Deleted runs can
    be purged later (see below), after time has passed and you're more
    certain that you won't need them.

You can list deleted runs by specifying the `--deleted` option to
[runs](cmd:runs).

### Restore Deleted Runs

If you make a mistake and need to restore a deleted run, use [runs
restore](cmd:runs-restore).

As with other run management operations, Guild prompts you with the
list of runs it will restore. To bypass this prompt, use the `--yes`
or `-y` option.

!!! tip
    If you find yourself restoring runs frequently, consider using
    [export](cmd:export) with the `--move` option to archive runs you
    no longer need. Archives runs are stored in a directory that you
    control and cannot be deleted using [runs purge](cmd:runs-purge).

### Purge Deleted Runs

Deleted runs, provided they weren't deleted with the `--permanent` or
`-p` option, still reside on disk. To permanently delete these runs,
use [runs purge](cmd:runs-purge).

!!! tip
    Use [check](cmd:check) with the `--space` option to show disk
    space consumed by delete runs.

Guild prompts you with the list of runs to purge before proceeding.

!!! important
    Permanently deleted runs cannot be restored.

## Export and Import Runs

Runs can be exported from the Guild environment using
[export](cmd:export). By default, runs are *copied* from the
environment to the specified directory. You can alternatively *move*
runs using the `--move` option.

By default, Guild exports all runs. You can select specific runs or
use filter options to limit the exported runs. Refer to [`export`
command help](/commands/export.md) for details on supported filter
options.

For example, to export runs to a local directory ``exported-runs`` by
moving them, run:

``` command
guild export --move exported-runs
```

Exported runs reside in a directory of your choosing. You can move the
directory as needed and still be able to import its runs later, either
on the same system or a different system.

List runs in an archive directory using [runs](cmd:runs) with the
`--archive` or `-A` option.

``` command
guild runs --archive exported-runs
```

!!! tip
    Use [export](cmd:export) with `--move` to keep your working
    environment clean without risk of accidentally deleting useful
    runs. Use different archive directories to organize runs that
    you're not currently working with.

To import runs from a directory, use [import](cmd:import). By default,
Guild *copies* runs from a directory into the environment when
importing. Use the `--move` option to move them instead.

By default, Guild imports all runs from an archive directory. You can
alternatively select specific runs or use filter options to limit the
imported runs. See [`import` command help](/commands/import.md) for a
list of filter options.

## Label Runs

TODO

<!-- TODO

## Sync Runs with Remote Systems

-->

## Batches

A *batch run* is a run that generates other runs, or *trials*.

Guild supports different ways to run a batch:

- Specify a [flag value list](ref:flag-value-list)
- Specify a flag value that uses a [search space
  function](ref:search-space-function)
- Run using `--optimize` or `--optimizer` option with [run](cmd:run)
- Run with [batch file](#batch-files) arguments

Batch runs are distinct from trial runs and appear in run lists
separately. Batch runs use a distinct naming convention:

```
OPERATION+[OPTIMIZER]
```

Batches generate trials. Limit the number of trials using
`--max-trials` or `-m`. If this option is omitted, a batch is limited
to a default number of trials based on the batch type.

### Standard Batch

A *standard batch* is run by specifying [value
lists](ref:flag-value-list) for one or more flag values.

The following command starts a batch of three trials --- one for each
item in the value list:

``` command
guild run x=[1,2,3]
```

When more than one flag value is a list, Guild runs trials for all
possible flag value combinations.

For example, the following command starts a batch of four trials:

``` command
guild run x=[1,2] y=[3,4]
```

Generated trials:

- `x=1` `y=3`
- `x=1` `y=4`
- `x=2` `y=3`
- `x=2` `y=4`

Standard batches are named as ``OPERATION+`` where `OPERATION` is the
trial operation.

Use [sequence functions](ref:flag-sequence-function) to generate value
lists. For example, the following commands are equivalent:

``` command
guild run x=range[1:5]
```

^ Use [sequence functions](ref:flag-sequence-function) to generate
  value lists

``` command
guild run x=[1,2,3,4,5]
```

^ The flag function ``range[1:5]`` generates the list value
  ``[1,2,3,4,5]``

By default, Guild runs all possible flag value combination (i.e. the
Cartesian product of the flag value lists). Use `--max-trials` or `-m`
to limit the trials. When limited, Guild selects trials at random from
the original set.xs

!!! important
    When running grid searches, the number of trials grows
    combinatorially with each flag value list. Use `--max-trials` to
    limit the number of trials based on budgeted time and resources.

### Random Search Batch

Guild runs a *random search batch* under the following conditions:

- At least one flag value is a [search space
function](ref:flag-search-space-function)
- The run command does not include `--optimize` or `--optimizer`

In this case, Guild implicitly uses
[`random`](/reference/optimizers.md#random) as the optimizer. See
[Optimizer Batch](#optimizer-batch) below for more information on
optimizers.

For example, the following commands starts a random search batch:

``` command
guild run x=uniform[0:1000]
```

^ Use of [`uniform`](/flags.md#uniform) function implies a random
  search

By default, the maximum trials for a random search is 20. Change this
limit using the `--max-trials` or `-m` option.

### Optimizer Batch

Guild runs a batch when `--optimizer` or `--optimize` options are
specified. Optimizers are standard Guild operations that specialize in
generating and running trials.

For a list of supported optimizers, see [Optimizer
Reference](/reference/optimizers.md).

Each optimizer may have its own default max trials setting. However,
most optimizers limit trials to 20. Change this limit using the
`--max-trials` or `-m` option.

#### Default Optimizer

Operations support a default optimizer, which can be used by
specifying the `--optimize` or `-O` option.

``` command
guild run train --optimize
```

^ Start an optimizer batch using the default optimizer for `train`

See [*Guild File Reference - Operation
Optimizers*](/reference/guildfile.md#operation-optimizers) for
information on configuring a default optimizer.

#### Optimizer Flags

Optimizers support their own set of flags. Use `--help-op` with the
optimizer name for help with optimizer flags.

For example, to show operation help for the [`gp`
optimizer](/reference/optimizers.md#gp), run:

``` command
guild run gp --help-op
```

Specify an optimizer flag values using the `--opt-flag` or `-Fo`
option. Use these options multiple times as needed to set more than
one optimizer flag.

For example, to use the `gp` optimizer with different values for
`random-starts` and `xi`:

``` command
guild run --optimizer gp -Fo random-starts=10 -Fo xi=0.1
```


## Batch Files

A batch file is a data file that contains one or more sets of flag
values for use in an operation. Batch files may be defined using
various formats:

- CSV format -- first line defines flag names and each subsequent line
  contains associated flag values for a run
- JSON format -- encoded list of objects representing flag values for a run
- YAML format -- encoded list of mappings representing flag values for
  a run

Batch files are specified using an argument in the format ``@PATH`` to
the [run](cmd:run) command. Guild starts a run for each set of flags
defined in each specified batch files.

Consider this CSV file:

``` csv
learing-rate,batch-size
0.1,100
0.1,1000
0.01,100
0.01,1000
```

^ `batch.csv`

The following command would generate four runs, one for each set of
flag values defined in `batch.csv`:

``` command
guild run train @batch.csv
```

Here's is an equivalent batch file using the JSON format:

``` json
[
  {"learning-rate": 0.1, "batch-size": 100 },
  {"learning-rate": 0.1, "batch-size": 1000 },
  {"learning-rate": 0.01, "batch-size": 100 },
  {"learning-rate": 0.01, "batch-size": 1000 }
]
```

^ `batch.json`

And in YAML format:

``` yaml
- learning-rate: 0.1
  batch-size: 100
- learning-rate: 0.1
  batch-size: 1000
- learning-rate: 0.01
  batch-size: 100
- learning-rate: 0.01
  batch-size: 1000
```

^ `batch.yml`

<!-- TODO

- Section about saving trials

-->
