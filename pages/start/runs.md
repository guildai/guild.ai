tags: start

# Manage Runs

[TOC]

In [the previous section](optimize.md) you generate several runs in
search of optimal hyperparameters for the `train.py` script. When
developing models, it's not uncommon to run dozens or hundreds of
experiments as you try different approaches, data sets, and
hyperparameters.

In this section, you learn about Guild commands for managing runs.

## Show Runs

Use [runs](cmd:runs) or [runs list](cmd:runs-list) to show current
runs. By default, Guild only shows the latest 20.

``` command
guild runs
```

You can show 20 additional runs using `--more` or `-m` option.

``` command
guild runs -m
```

Specify `m` multiple times as needed in increase the number ---
e.g. `-mm` shows 40 additional runs.

To show all runs, use `--all` or `-a`.

``` command
guild runs -a
```

## Delete Runs

Use [runs rm](cmd:runs-rm) or [runs delete](cmd:runs-delete) to delete
one or more runs. You can restore deleted runs if make a mistake.

Delete all of the runs (you restore them later):

``` command
guild runs rm
```

Guild shows the list of runs to delete. Press `Enter` to confirm.

Guild moves deleted runs to *trash* [^trash] where they can be viewed,
restored, or purged if you want to permanently delete them.

[^trash]: Deleted runs are moved to `$GUILD_HOME/trash/runs`. Use
    [check](cmd:check) to show the location of `GUILD_HOME` for the
    current environment.

Show deleted runs by using the `--deleted` option with
[runs](cmd:runs):

``` command
guild runs --deleted
```

## Restore Runs

If you want restore a delete run, use [runs
restore](cmd:runs-restore).

Restore all of the deleted runs:

``` command
guild runs restore
```

Guild shows the runs to restore. Press `Enter` to confirm.

Verify that the runs appear in the runs list:

``` command
guild runs
```

## Label a Run



## Mark a Run

## Filter Runs for a Command

Run-related commands support a common interface for filtering runs
effected by the command.

Runs can be filtered by:

- Operation name
- Label
- Run status
- Marked status
- When the run was started
- Source code digest

For availble filter options, refer to command help, either
[online](/commands) or using `--help` with the command.

For example, to show runs that were started within the last 15
minutes, run:

``` command
guild runs --started 'last 15 minutes'
```

## Export Runs

You can export runs to a directory for backup or to clear runs from
your list.

Export all runs to a local `archived-runs` directory:

``` command
guild export --move archived-runs
```

Press `Enter` to confirm.

Guild moves all of your runs into `archived-runs`.

Verify that your runs list is empty:

``` command
guild runs
```

List runs in an archive directory by specifying the `--archive`
option:

``` command
guild runs --archive archived-runs
```

Guild shows the list of runs in the directory.

If you want to import any runs back into your list, use
[import](cmd:import). For this guide, keep the runs list empty for the
next section.

!!! tip
    Use [export](cmd:export) to keep your list clear of runs
    you're no longer working with. Use different export directories to
    categorize your runs as needed. If you want to move runs to a
    remote location, use [push](cmd:push) with a [remote
    configuration](ref:remote).

## Next Steps

In this section, you deleted and restored runs. You exported runs to
an archive.

In the next section, you use a [Guild file](ref:guildfiles) to define
operations your project.
