tags: concept

# Runs

[TOC]

## Overview

A *run* in Guild AI is one of two things:

run process
: Operating system process started with [run](cmd:run)

run directory
: Directory containing metadata and files associated with a run
  process

      A run cannot exist apart from a run directory.

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

Run directories are stored in either a Guild environment or in an
archive directory. To view the location of runs in the current
environment, use [check](cmd:check) to show environment details. Runs
are stored in the `runs` subdirectory of the path shown by the
`guild_home` environment attribute.

Use [runs](cmd:runs) to show the current list of runs.

Use [runs info](cmd:runs-info) to show information about a
specific run, including the location of its run directory, which is
shown by the `run_dir` attribute.

Run directories contain all information associated with a run and may
be freely moved to different locations.
