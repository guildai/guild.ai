# Tips & Techniques

[TOC]

Below is a list of tips that you may find useful when using Guild.

### Skip confirmation prompts

Any Guild commands that prompts for confirmation can be run with the
`-y` or `--yes` option to skip the prompt. This speeds up an operation
when you don't need to manually verify it first. It's also useful when
running Guild in unattended scripts.

### Quick access to run files via shell (Linux and macOS only)

If you are comfortable using a terminal to view files, the
[open](cmd:open) command supports a `--shell` option that opens a new
shell session in the specified run directory.

For example, to open a new shell in the latest run directory, use:

``` command
guild open --shell
```

Use standard shell commands to view run files.

When you're done, run the `exit` command to return to your previous
shell session.

### Select runs using filters

Commands that apply to runs support a standard set of run
filters. These include the ability to limit runs by:

- Operation
- Status
- Label
- Mark
- Start time

To view filter options for a command use `--help` or refer to the
[online command help](/commands/index.md).

For example, to delete only terminated runs for operations containing
`train`, use:

``` command
guild runs rm --terminated --operation train
```

To export runs with a label containing `best`, use:

``` command
guild export --label best exported-runs
```

To show runs started in the last hour:

``` command
guild runs --started 'last hour'
```

### Evaluate learning rates using `logspace`

The [`logspace`](/flags/#logspace) function is handy for generating a
list of learning rates over a logarithmic scale.

To evaluate learning rates at each order of magnitude from `1.0e-5` to
`0.1`, use a flag value of `logspace[-5:-1:5]`.

For example:

``` command
guild run train learning-rate=logspace[-5:-1:5]
```

### Maintain a clean working environment

Over time you will generate many runs, some of which will fail with an
error message or yield disappointing results. Use one of the following
techniques to move these runs out of your working environment so you
can focus on the runs you're interested in.

#### Delete failed runs

Use `--error` or `-E` with [runs rm](cmd:runs-rm) to delete failed
runs (i.e. runs with the **error** status). Avoid the temptation of
permanently deleting them with the `--permanent` option. Failed runs
are often a souce of useful information. You can purge old runs when
you need to free up disk space (see below).

``` command
guild runs rm -E
```

#### Purge old runs

If you're concerned about disk space consumed by deleted runs, check
disk usage with the [check](cmd:check) command:

``` command
guild check --space
```

View deleted runs with [runs](cmd:runs) and the `--deleted` option:

``` command
guild runs --deleted
```

You can purge deleted runs that were started before a particular time
using [runs purge](cmd:runs-purge) with the `--started` option.

For example, to purge deleted runs that are at least 6 months old,
use:

``` command
guild purge --started 'before 6 months ago'
```

To purge runs started before Jan 1, 2020, use:

``` command
guild purge --started 'before 2020-1-1'
```

#### Archive runs

If you want to move runs out of your environment but save them in a
directory, use [export](cmd:export) with the `--move` option.

For example, to move all runs to a `saved-runs` directory, use:

``` command
guild export --move saved-runs
```

You can list runs in an archive directory using the `--archive` or
`-A` option to [runs](cmd:runs). For example, the following command
list runs that were moved using the `export` command above:

``` command
guild runs -A saved-runs
```

You can import files from an archive directory using
[import](cmd:import). To move them out of the directory, include the
`--move` option.

For example, the following command imports the 10 most recent runs
from `saved-runs`:

``` command
guild import --move 1:10 saved-runs
```

To import the runs from the last 7 days

``` command
guild import --move --started 'last 7 days' saved-runs
```
