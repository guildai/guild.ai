tags: start

# Manage Runs

[TOC]

In [the previous section](optimize.md) you generate several runs in
search of optimal hyperparameters for the `train.py` sample
script. When developing models, it's not uncommon to run dozens or
hundreds of experiments as you try different approaches, data sets,
and hyperparameters.

In this section, you learn various Guild commands for managing runs.

## Show Runs

Use [runs](cmd:runs) or [runs list](cmd:runs-list) to show current
runs. By default, Guild only shows the last 20.

``` command
guild runs
```

You can show 20 additional runs using `--more` or `-m` option.

``` command
guild runs -m
```

You can specify `m` multiple times --- e.g. `-mm` shows 40 additional
runs, and so on.

To show all runs, use `--all` or `-a`.

## Delete Runs

Use [runs rm](cmd:runs-rm) or [runs delete](cmd:runs-delete) to delete
one or more runs.

Delete all of the runs. Don't worry, you restore them in next step.

``` command
guild runs rm
```

Press `Enter` to confirm.

Guild deletes all of the runs.

!!! note
    Guild does not permanentaly delete runs unless you specify
    the `--permanent` option.

## Restore Runs

Guild lets you restore deleted runs as a safeguard.

Show deleted runs:

``` command
guild runs --deleted
```

Restore the last 5 deleted runs:

``` command
guild runs restore 1:5
```

Press `Enter` to continue.

The argument `1:5` indicates that runs one through five are restored.

Restore the remaining deleted runs:

``` command
guild runs restore --yes
```

Guild does not prompt you in this case because you specified the
`--yes` option.

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
