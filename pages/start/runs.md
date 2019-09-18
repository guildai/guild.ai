# Manage Runs

In [the previous section](optimize.md) you searched for optimal values
of a hypeparameter `x` for a simulated loss function.

In this section, you learn more about runs.

## Show Runs

By default, Guild only shows the last 20 runs. Config this listing the
available runs:

``` command
guild runs
```

Guild shows the message ``Showing the first 20 runs (27 total) - use
--all to show all or -m to show more``.

Use `-m` to show the remaining runs:

``` command
guild runs -m
```

## Delete Runs

Delete all of the runs (don't worry, we restore them in next step):

``` command
guild runs rm
```

Press `Enter` to confirm.

Guild deletes all of the runs. Guild does not permanentaly delete runs
unless you specify the `--permanent` option.

## Restore Runs

Guild lets you restore deleted runs as a safeguard.

Show the deleted runs:

```
guild runs --deleted
```

Restore the last 5 deleted runs:

``` command
guild runs restore 1:5
```

Press `Enter` to continue.

This is an example of selecting a range of runs, start with the first
run in the list and ending with the fifth run in the list.

Restore the remaining deleted runs:

``` command
guild runs restore --yes
```

Guild does not prompt you in this case because you specified the `--yes` option.

Press `Enter` to confirm.

## Select Runs

Guild commands that apply to runs support various selection
options. There two ways to select a run:

- Specify a run ID
- Specify a list index or index range that includes the run

If a run ID or index is not specified, Guild selects certain runs by
default. Refer to the command help for details on how Guild selects
default runs.

For example, [runs info](cmd:runs-info) applies to the latest run by
default.

You can specify an alternative run.

``` command
guild runs info 2
```

This commands tells Guild to show you information for the second run
in the default list.

Such commands also support *filters*, which limit the list of runs
that are selected from.

For example, to show information for the latest *completed* run:

``` command
guild runs info --completed
```

## Export and Import

Export all of the runs to an `archive` directory:

``` command
guild export --move archive
```

Press `Enter` to confirm.

The `--move` option tells Guild to move the runs rather than copy
them. You can verify that the current runs list is empty by running
``guild runs``.
