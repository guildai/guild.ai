# Manage Runs

In [the previous section](optimize.md) you searched for optimal values
of a hypeparameter `x` for a simulated loss function.

In this section, you learn more about runs.

## Show Runs

Use [runs](cmd:runs) or [runs list](cmd:runs-list) to show current
runs. By default, Guild only shows the last 20.

``` command
guild runs
```

You can show additional runs using `--more` or all runs using `--all`.

``` command
guild runs --more
```

## Delete Runs

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

## More Commands

Guild provides various commands that apply to runs. Below are some of
the more common commands.

[diff](cmd:diff)
: Diff two runs. Guild lets you diff entire runs, sections of runs
  (e.g. flags, source code, etc.) or individual files.

[ls](cmd:ls)
: List files associated with a run.

[cat](cmd:cat), [open](cmd:open)
: Show files associated with a run. Use `cat` to show a text file on
  the console or `open` to open a file or directory in your desktop
  file manager.

[export](cmd:export), [import](cmd:import)
: Backup and restore runs or manage the runs visible in your
  environment.

[push](cmd:push), [pull](cmd:pull)
: Copy runs to and from remote locations. Used to backup and restore
  and other run synchronization tasks.

## Next Steps

In this section, you deleted and restored runs. You learned about
other Guild commands that apply to runs.

In the next section, you use a [Guild file](ref:guildfile) to define
operations your project.
