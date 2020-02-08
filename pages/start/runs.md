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

If you want to restore a deleted run, use [runs
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

!!! tip
    When deleting runs, avoid the temptation to use `--permanent`
    flag so that you have the option of restoring them later.

## Label a Run

Labels are string values that help identify a run. Guild shows run
labels when listing and comparing runs.

By default, Guild generates a default label for each run containing
the flag values. You can specify a different label using the `--label`
or `--tag` options.

After a run is started, you can set the label using the
[label](cmd:label) command.

First, find the run with the lowest `loss` using [compare](cmd:compare):

``` command
guild select -o train.py --min loss
```

Guild shows the run ID with the lowest loss. You can confirm this by
running ``guild compare -o train.py --min loss`` -- the run with the
lowest loss appears at the top of the list.

Use the `--tag` option with the [label](cmd:label) command to prepend
"best" to the run label:

``` command
guild label --tag best <run ID from previous command>
```

Guild prompts you with the proposed change. Press `Enter` to modify
the run label.

!!! tip
    If you are running on Linux, macOS, or another POSIX
    compatible operating system, you can use [command substitution
    ->](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html)
    and the [select](cmd:select) command to specify a run ID. For
    example, ``guild run --tag best $(guild select -o train --min
    loss)`` can be used to tag the "best" run (i.e. with the lowest
    `loss`) of `train.py`.

Show runs with "best" in their label:

``` command
guild runs -l best
```

``` output
[1:c4a48fb8]  train.py  2020-01-20 18:39:03  completed  best noise=0.1 x=-0.28771
```

Due to random effects, the selected run in your case may have a
different value for `x`. The optimal value of `x` is be near `-0.3`.

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

For example, to show runs that were started within the last 15
minutes, run:

``` command
guild runs --started 'last 15 minutes'
```

For availble filter options, refer to command help, either
[online](/commands) or using `--help` with the command.

## Export Runs

You can export runs to a directory for backup or to clear runs from
your list.

Export all runs to a local `archived-runs` directory:

``` command
guild export --move archived-runs
```

Press `Enter` to confirm.

Guild moves your runs into a local `archived-runs` directory. Your
`guild-start` project directory should look like this:

<div class="file-tree">
<ul>
<li class="is-folder open">guild-start
 <ul>
 <li class="is-folder">archived-runs</li>
 <li class="is-file">guild.yml</li>
 <li class="is-file">train.yml</li>
 </ul>
</li>
</ul>
</div>

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

In this section you use various commands to manage your runs:

- Delete runs
- Restore deleted runs
- Label a run
- Export (archive) runs to a local directory

!!! highlight
    Use Guild to label, archive, and delete runs as needed
    to help you focus on the most promising results without losing
    information from other experiments.

In the next section, you use a [Guild file](ref:guildfiles) to define
operations your project.
