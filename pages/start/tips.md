# Tips

[TOC]

Below is a list of tips that you may find useful when using Guild.

### Skip confirmation prompts

Any Guild commands that prompts for confirmation can be run with the
`-y` or `--yes` option to skip the prompt. This speeds up an operation
when you don't need to manually verify it first. It's also useful when
running Guild in unattended scripts.

### Quick access to run files via shell (Linux and macOS)

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
