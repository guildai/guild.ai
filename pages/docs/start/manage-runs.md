tags: get-started

# Manage Runs

This guide provides a quick tour of run management functions.

[TOC]

## Requirements

{!start-requirements-2.md!}

## A script to test runs

In the `guild-start` directory, create a file named `echo.py`:

``` python
msg = "Hello Guild!"

print(msg)
with open("message.txt", "w") as out:
    out.write(msg + "\n")
```

^ guild-start/echo.py

Verify that your project structure is:

<div class="file-tree">
<ul>
<li class="is-folder open">guild-start
 <ul>
 <li class="is-file">echo.py</li>
 <li class="is-file disabled">train.py <small>(created
 in <a href="/docs/start/">Quick Start</a> - not used in this guide)</small></li>
 </ul>
</li>
</ul>
</div>

## Start runs

To start a run, use the [](cmd:run) command.

Run `echo.py`:

``` command
guild run echo.py
```

Press `Enter` to accept the default message and run the operation. The
script prints the greeting:

``` output
Hello Guild!
```

By default, Guild prompts you before starting the operation. You can
bypass this prompt by including `-y` or `--yes` as a command line
option:

``` command
guild run echo.py -y
```

`echo.py` supports a single [](term:flag) *msg*, which it prints to
the console. You can list supported flags for a script by specifying
the `--help-op` option to the `run` command:

``` command
guild run echo.py --help-op
```

``` output
Usage: guild run [OPTIONS] echo.py [FLAG]...

Use 'guild run --help' for a list of options.

Flags:
  msg  (default is Hello Guild!)
```

We can run the script with a different value for `msg`:

``` command
guild run echo.py msg='Yo Guild!'
```

``` output
You are about to run echo.py
  msg: Yo Guild!
Continue? (Y/n)
```

Press `Enter` to continue. The script prints the alternate greeting:

``` output
Yo Guild!
```

## Stop runs

By default, Guild lets a script run to completion, regardless of how
long it takes to complete.

You can stop an operation early by typing `Ctrl-C` in the command run
console.

You can alternatively stop a run from a different console by running:

``` command
guild stop
```

^ Alternative to typing `Ctrl-C` --- run in a different command
console

This stops all running operations. You can alternatively specify
specific runs to stop. For more information, see the [](cmd:stop)
command.

## List runs

List the latest 20 runs:

``` command
guild runs
```

List all runs by providing the `-a` or `--all` command line option:

``` command
guild runs --all
```

You can filter runs using a variety of options. For example, to show
all runs with a status of `completed`, use the `-C` or `--completed`
command line option:

``` command
guild runs --completed
```

Guild shows runs with a 1-based index, which may be in commands that
accept runs as arguments.

For a list of filter options, see the [](cmd:runs) command.

## Show run info

If you want information about a run, use [runs info](cmd:runs-info):

``` command
guild runs info
```

``` output
id: be12ef24483d11e98c3ec85b764bbf34
operation: echo.py
status: completed
started: 2019-03-16 17:49:23
stopped: 2019-03-16 17:49:23
marked: no
label:
run_dir: ~/.guild/runs/be12ef24483d11e98c3ec85b764bbf34
command: /usr/bin/python -um guild.op_main echo --msg "Yo Guild!"
exit_status: 0
pid:
flags:
  msg: Yo Guild!
```

By default, Guild shows information for the latest run. You can
specify a different run as either an index or a run ID. For example,
to show information for the second to last run:

``` command
guild runs info 2
```

You can request additional information by specidying various command
line options:

- Files associated with the run (`--files`)
- Run output (`--output`)
- Process environment (`--env`)
- Scalars (`--scalars`)
- Dependencies (`--deps`)
- Source code (`--source`)

For more information, see the [runs info](cmd:runs-info) command.

## List run files

Show files associated with a run using the [](cmd:ls) command:

``` command
guild ls
```

``` output
~/.guild/runs/be12ef24483d11e98c3ec85b764bbf34:
  message.txt
```

By default, Guild shows files associated with the latest run. You can
specify a different run using a run index or run ID.

The `echo.py` writes the value of the *msg* flag to a file named
`message.txt`.

You can display the contents of a file using [](cmd:cat):

``` command
guild cat message.txt
```

``` output
Yo Guild!
```

To show the contents of `message.txt` for the previous run:

``` command
guild cat message.txt 2
```

``` output
Hello Guild!
```

## Open run files

Use the [](cmd:open) command to open a run directory in your system
file browser:

``` command
guild open
```

By default, Guild opens the latest run directory.

You can also open specific files using the `-p` or `--path` command
line option:

``` command
guild open -p message.txt
```

You can browse the source code associated with a run by specifying the
`--source` command line option:

``` command
guild open --source
```

## Delete runs

Delete runs using [runs delete](cmd:runs-delete) or the alias `runs rm`.

By default, Guild deletes all runs. You can specify one or more runs
to delete using these forms:

- run index
- run index range
- run ID

Run index ranges are in the form `START:STOP` and will select all runs
starts with index `START` up to and including the run with index
`STOP`.

You can additionally specify status filters such as `--terminated`,
`--error`, `--completed`, etc.

For example, to delete the last run, use:

``` command
guild runs rm 1
```

``` output
You are about to delete the following runs:
  [c654363a]  echo.py  2019-03-16 18:18:14  completed
  Delete 1 run(s)? (Y/n)
```

By default, Guild prompt before deleting runs. You can bypass this
promt by specifying the `-y` or `--yes` command line option.

!!! note
    Deleted runs can be restored later using [runs
    restore](cmd:runs-restore). See below for details.

!!! tip
    To delete all failed runs --- i.e. runs with status `error`
    --- use ``guild runs rm --error`` or the short version ``guild
    runs rm -E``.

## Restore deleted runs

Deleted runs can be restored using [runs
restore](cmd:runs-restore). By default, Guild restores all deleted
runs. You can specify specific runs using indexes or run IDs. For
example, to restore the last deleted run, use:

``` command
guild runs restore 1
```

!!! tip
    To show deleted runs --- i.e. runs that can be restored ---
    use ``guild runs --deleted`` or the short version ``guild runs
    -d``.

## Summary

In this guide you learned about basic run management, including how
to:

- Start and stop runs
- List runs
- Show run info
- List and view run files
- Delete and restore runs

## Next steps

{!start-image-classifier.md!}
