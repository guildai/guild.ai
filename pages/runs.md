tags: concept

# Runs

[TOC]

## Overview

A Guild *run* is an operation that generates a result you're
interested in saving. Runs are commonly ML model training
*experiments*. However, runs may implement any task of your
chosing. Runs are used to:

- Train models
- Prepare data sets
- Evaluate training results on different data sets
- Optimize models for size and performance
- Deploy models

Runs are started using the Guild [run](cmd:run) command. You generate
several runs in [Get Started](ref:get-started).

The term *run* refers to one of two things:

- A in-process run, represented by an operating system process
- A file system artifact associated with a run operating system
  process

Runs are central to systematically improving model performance. By
capturing experiment details, you establish a series of baseline
measurements against which to compare future experiments. You maintain
a record for knowing when you're making progress and when you're
regressing.

Runs also serve as a unit of *reproducibility*. By automating
experiment recording for yourself, you provide an easy way for others
to recreate and compare results.

## Run Artifacts

Guild saves runs on standard file systems. Guild is different in this
respect from experiment management systems that save experiment
results in databases or exotic file systems. For background on why
Guild takes this approach, see [*Guild Design - Minimize
Dependencies*](/reference/design/#dependencies).

Runs are stored under a `runs` directory located in [Guild
home](term:guild-home). To show where Guild saves runs, use the
[check](cmd:check) command. Guild saves runs under the path shown by
`guild_home` in a `runs` subdirectory. Each run is saved in a
directory named with a unique identifier. For more information, see
[*Run Directory*](#run-directory) below.

### Run Directory

A *run directory* is a unique directory created for a run process. Run
directories are stored under [Guild home](term:guild-home) for an
environment under a `runs` subdirectory.

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

## Start a Run

- Run a script vs a Guild operation
- `run` command

## List Runs

## Get Run Information

## Compare Runs

## Delete Runs

## Export and Import Runs

## Label Runs

- Default labels
- Set a label when starting a run
- Label templates
- Change run labels
- Tag run labels
- Clear run labels

## Copy Runs to and from Remote Systems

## Batches

- Batch files
