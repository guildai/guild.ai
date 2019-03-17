tags: get-started

# Manage Runs

This guide provides a quick tour of run management functions.

[TOC]

## Requirements

{!start-requirements-2.md!}

## A script to test runs

In the `sample-project` directory, create a file named `echo.py`:

``` python
msg = "Hello Guild!"

print(msg)
with open("message.txt", "w") as out:
    out.write(msg + "\n")
```

^ sample-project/echo.py

Verify that your project structure is:

<div class="file-tree">
<ul>
<li class="is-folder open">sample-project
 <ul>
 <li class="is-file">echo.py</li>
 <li class="is-file">train.py</li>
 </ul>
</li>
</ul>
</div>

## Common tasks

### Start runs

To start a run, use the [](cmd:run) command.

Run `echo.py`:

``` command
guild run
```

Press `Enter` to accept the default message and run the operation. The
script prints the greeting:

``` output
Hello Guild!
```

By default, Guild prompts you before starting the operation. You can
bypass this prompt by including `-y, --yes` as a command line option:

``` command
guild run echo.py -y
```

`echo.py` supports a single [](term:flag) *msg*, which it prints to
the console. You can set that value when you run the script with
Guild:

``` command
guild run echo.py msg='Yo Guild!' -y
```

``` output
Yo Guild!
```

### Stop runs

By default, Guild lets a script run to completion, regardless of how
long it takes to complete.

You can stop an operation early by typing `Ctrl-C` in the command run
console.

You can alternatively stop a run from a different console by running:

``` command
guild stop
```

This stops all running operations. For more information, see
[](cmd:stop).

### List runs

List the latest 20 runs:

``` command
guild runs
```

List all runs by providing the `-a, --all` command line option:

``` command
guild runs --all
```

You can filter runs using a variety of options. For example, to show
all runs with a status of `completed`, use the `-C, --completed`
command line option:

``` command
guild runs --completed
```

Guild shows runs with a 1-based index to simplify operations that
accept runs as arguments.

For a list of filter options, see [](cmd:runs).

### Show run info

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

### List run files

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

### Open run files

Use the [](cmd:open) command to open a run directory in your system
file browser:

``` command
guild open
```

By default, Guild opens the latest run directory.

You can also open specific files using the `-p, --path` command line
option:

``` command
guild open -p message.txt
```

You can browse the source code associated with a run by specifying the
`--source` command line option:

``` command
guild open --source
```

### Delete runs

Delete runs using [runs delete](cmd:runs-delete) or the alias `runs rm`.

By default, Guild deletes all runs. You can specify one or more of:

- run index
- run index range
- run ID

to limit the runs to delete. You can additionally specify status
filters such as `--terminated`, `--error`, `--completed`, etc.

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
promt by specifying the `-y, --yes` command line option.

!!! note
    Deleted runs can be restored later using [runs
    restore](cmd:runs-restore). See below for details.

### Restore deleted runs

Deleted runs can be restored using [runs
restore](cmd:runs-restore). For example, to restore the last deleted
run, use:

``` command
guild runs restore 1
```

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
