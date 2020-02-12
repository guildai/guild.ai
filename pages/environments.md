tags: concept

# Environments

[TOC]

## Overview

A *Guild environment* is a system runtime used to manage runs. All
Guild commands are executed in the context of a Guild environment.

You can view information about the current environment using
[](cmd:check).

``` command
guild check
```

The `guild_home` attribute in the `check` output identifies the
location of the Guild environment. By default, the Guild environment
is `~/.guild` where `~` is the active user home directory.

Guild stores the following under `guild_home`:

- Runs
- Cached downloaded resources
- Cached run output scalars
- Remote state

## Guild Environments vs Virtual Environments

By default, Guild environments correspond to activated virtual
environments. Use virtual environments created using [](ref:conda) or
[](ref:virtualenv) to isolate your work, including Guild runs.

You can change this behavior by setting Guild home, which is described
below.

!!! important
    When using a virtual environment, bear in mind that runs
    are saved *within the environment*. Take care when deleting
    virtual environments as they may contain Guild runs. Look for
    `.guild/runs` within the virtual environment directory to verify
    that you're not deleting runs.

## Set Guild Home

By default, Guild resolves Guild home by first looking in the
activated virtual environment. If an environment isn't activated,
Guild uses `.guild` in the active user home directory.

You can specify a different location for Guild home using one of two
methods:

- Set `GUILD_HOME`
- Use `-H` when running a Guild command

To set `GUILD_HOME` for all Guild commands in a command shell, run:

```
export GUILD_HOME=<path>
```

To set Guild home for one command, use one of these methods:

```
GUILD_HOME=<path> guild COMMAND ...
```

or:

```
guild -H <path> COMMAND ...
```

Note that when using `-H`, the option must be specified *before*
`COMMAND`.

## Create a Guild Environment

New environments may be created using various techniques.

- Create an environment using [guild init](cmd:init)
- Create a virtual environment using [](ref:virtualenv) or
  [](ref:conda)
- Create a new directory and [set it as Guild home](#set-guild-home)

Guild's [](cmd:init) command uses `virtualenv` to create a new virtual
environment. When running `init`, Guild performs additional steps to
streamline the process of creating a virtualized Guild environment for
a project:

- Uses a [Python version
  requirement](/commands/init.md#required-python-version) to select an
  appropriate Python version when creating the virtual environment
- Runs `pip install -r requirements.txt` if `requirements.txt` is
  defined for a project
