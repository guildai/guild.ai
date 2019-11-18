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

### Guild Runs vs Scripts

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
directories are stored under the *Guild home* for an environment. See
[Environments](cmd:environments.md) for information about Guild home
and the location of runs.

All run metadata and generated files are located in a run directory.

A run directory can be deleted to remove the run. Note however, that
deleted run directories for in-process runs will result in an orphaned
run process that Guild cannot manage. To safely delete a run, either
use [runs delete](cmd:runs-delete) or stop the run first, either using
[stop](cmd:stop) or by terminating the run operating system process.

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

### Run in the Background

By default, Guild executes runs in the foreground. To run an operation
in the background, specify either the `--background` or `--pidfile`
option.

You can watch the progress of a background run using
[](cmd:watch). Note that watching a run does not attach to the process
--- it merely tails the operation log. Therefore pressing `Ctrl-C`
when watching a run will not terminate the run. To stop a background
run, use [](cmd:stop).

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

To list files associated with a run, use [ls](cmd:ls). The command is
named after the shell command for listing files for a directory.

By default, Guild shows all non-private files in the [run directory](ref:rundir)

### View Run File Contents

TODO

## List Runs

TODO

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
