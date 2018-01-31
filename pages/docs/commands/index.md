sidenav_title: Overview
tags: reference

# Commands

[TOC]

- [General](category:/docs/commands/#general)
- [Model support](category:/docs/commands/#models)
- [Run support](category:/docs/commands/#runs)
- [Package support](category:/docs/commands/#packaging)
- [Visualization](category:/docs/commands/#visual)
- [Utilities](category:/docs/commands/#util)

## Running commands

Guild commands must be executed on a command line. If you're
unfamiliar with running commands on your system, refer to [Getting to
Know the Command Line
->](https://www.davidbaumgold.com/tutorials/command-line/) for a quick
primer.

All Guild commands run in the foreground and terminate when the
command succeeds or an error occurs. You can stop a command at any
time by typing `CTRL-C` (i.e. hold down the [control
key](term:control-key) for your system and press `C`).

### Running commands in a separate console

There are some commands that will not terminate until you explicitly
stop them by typing `CTRL-C`:

- [](cmd:view)
- [](cmd:tensorboard)

To run other Guild commands while these are running, run them in a
separate console. There are various strategies for managing separate
consoles:

- Simply open another console/terminal
- Use a console/terminal application that supports multiple tabs
- Use a multiplexer like [tmux ->](https://github.com/tmux/tmux/wiki)
