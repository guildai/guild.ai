tags: concept

# Command Line Interface

[TOC]

## Guild AI Commands

Guild commands must be executed on a command line. If you're
unfamiliar with running commands on your system, refer to [Getting to
Know the Command Line
->](https://www.davidbaumgold.com/tutorials/command-line/) for a
primer.

At a command line, run a Guild command using this convention:

``` command
guild COMMAND
```

where `COMMAND` is one of the commands above. For a list of commands,
refer to this page or run ``guild --help`` on the command line. For
more information on getting see [](ref:command-help) below.

All Guild commands run in the foreground and terminate when the
command succeeds or an error occurs. You can stop a command at any
time by typing `CTRL-c` (i.e. hold down the [control
key](term:control-key) for your system and press `c`).

### Command Options

Commands accept *options*, which may be provided as command line
arguments in the format ``--OPTION [VALUE]`` or ``-OPTION_CHAR
[VALUE]`` where `OPTION` is the full name of the option and
`OPTION_CHAR` is the single character option shortcut. `VALUE` may be
required, optional, or considered invalid depending on the specific
command option.

Options for each command are printed when you run ``guild COMMAND
--help``. They are also listed and described in more details in this
guide.

### Run Commands in Separate Console

There are some commands that will not terminate until you explicitly
stop them:

- [](cmd:compare)
- [](cmd:view)
- [](cmd:tensorboard)

To run another command while one of these is still running, run the
new command in a separate console. There are various strategies for
managing separate consoles:

- Open another console/terminal
- Use a console/terminal application that supports multiple tabs
- Use an integrated developer environment (IDE) that supports running
  commands in different terminals
- Use a multiplexer like [tmux ->](https://github.com/tmux/tmux/wiki)
  (advanced)

## Command help

The Guild CLI provides two levels of help:

- General help
- Command specific help

General help is available by running:

``` command
guild --help
```

This will print Guild's global options as well as available commands.

Global options may be specified for any command but must be specified
before the command.

Command help is available by running:

``` command
guild COMMAND --help
```

This will print details about what the command does and how it can be
configured including details about its options.
