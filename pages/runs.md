tags: concept

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
--- it merely tails the operation log. Therefore pressing `Ctrl-C`
when watching a run will not terminate the run. To stop a background
run, use [](cmd:stop).

## List Runs

Use [runs](cmd:runs) to list available runs.

```
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

<!-- TODO Elaborate on start time filter in user docs here -->

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

To view run outout, use [cat](cmd:cat) with the `--output` option:

``` command
guild cat --output [RUN]
```

Use the `--page` option to use a pager when viewing long files or
output.

``` command
guild cat --output --page
```

## Compare Runs

TODO

## Delete Runs

TODO

### Restore Deleted Runs

TODO

### Permanently Delete Runs

TODO

## Export and Import Runs

TODO

## Label Runs

TODO

## Sync Runs with Remote Systems

TODO

## Batches

A *batch run* is a run that generates other runs, or *trials*.

Guild supports different ways to run a batch:

- Specify a flag value containing a [list of values](ref:flag-value-list)
- Specify a flag value that uses a [search space
  function](ref:search-space-function)
- Run using `--optimize` or `--optimizer`
- Run with batch file arguments

Batch runs are separate from trial runs. Batch runs use a distinct
naming convention:

```
OPERATION+[OPTIMIZER]
```

### Implied Batch Runs

TODO:

- Implied by flag value lists
- Implied by flag range functions

### Optimizing Batch Runs

TODO

## Batch Files

TODO: merge into above

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
