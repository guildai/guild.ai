tags: concept

# Environments

[TOC]

## Overview

A *Guild environment* is a system runtime used to manage runs. All
Guild commands are executed in the context of a Guild environment.

View information about the current environment using the [](cmd:check)
command.

The `guild_home` attribute in `check` output identifies the location
of the Guild environment. By default the Guild environment is
`~/.guild` where `~` is the active user home directory. For more
information, see [*Guild Home*](#guild-home) below.

## Virtual Environments

By default, Guild environments correspond to activated virtual
environments. Use virtual environments created using [](ref:conda) or
[](ref:virtualenv) to isolate your work, including Guild runs.

Change this behavior by setting Guild home, which is [described
below](#set-guild-home).

!!! important
    When using a virtual environment, runs are saved *within
    the environment*. Take care when deleting virtual environments as
    they may contain Guild runs. Look for `.guild/runs` within the
    virtual environment directory to verify that you're not deleting
    runs.

## Guild Home

*Guild home* is a directory that contains Guild-maintained
files. These include:

- Runs
- Cached downloaded resources
- Cached run output scalars
- Remote state
- Deleted runs
- Interprocess locks

### Guild Home Layout

<div class="file-tree">
<ul>
<li class="is-folder open">Guild Home directory <i>default is <code>~/.guild</code></i>
 <ul>
 <li class="is-folder open">cache <i>Guild-maintained caches</i>
   <ul>
     <li class="is-folder">import-flags <i>cached flags imported from scripts</i></li>
     <li class="is-folder">resources <i>cached resources</i></li>
     <li class="is-folder">runs <i>indexed run scalars</i></li>
   </ul>
 </li>
 <li class="is-folder">locks <i>interprocess resource locks</i></li>
 <li class="is-folder">remotes <i>current remote state</i></li>
 <li class="is-folder">runs <i>runs, each in a unique run directory</i></li>
 <li class="is-folder open">trash <i>deleted objects</i>
   <ul>
     <li class="is-folder">runs <i>deleted runs</i></li>
   </ul>
 </li>
 </ul>
</li>
</ul>
</div>

### Set Guild Home

By default, Guild resolves Guild home by first looking in the
activated virtual environment. If an environment isn't activated,
Guild uses `.guild` in the current user's home directory.

You can specify a different location for Guild home using one of two
methods:

- Set `GUILD_HOME` environment variable
- Use `-H` when running a Guild command

To set `GUILD_HOME` for all Guild commands in a command shell, run:

``` command
export GUILD_HOME=<path>
```

To set Guild home for one command, use one of these methods:

``` command
GUILD_HOME=<path> guild COMMAND ...
```

or:

``` command
guild -H <path> COMMAND ...
```

Note that when using `-H`, the option must be specified *before*
`COMMAND`.

## Create a Guild Environment

New environments may be created using the following methods:

- Use Guild's [init](cmd:init) command
- Use one of the standard Python tools: [](ref:virtualenv),
  [](ref:venv), or [](ref:conda)
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

## Activate Virtual Environments

You must activate a virtual environment before using it. Activate a
virtual environment using the applicable method.

To activate an environment created with [guild init](cmd:init):

``` command
source guild-env [<env path>]
```

^ Activate a virtual environment created using [init](cmd:init)

You may omit `<env path>` if the environment is defined in the current
directory or in a `venv` subdirectory.

!!! note
    Virtual environments created using [init](cmd:init) are
    standard Python virtual environments and can be activated by
    sourcing the `bin/activate` environment. The `guild-env` command
    provides a convenient alternative.

To activate an environment created using `virtualenv` or `venv` use:

``` command
source <env path>/bin/activate
```

^ Activate a virtual environment created using `virtualenv` or `venv`

To activate a Conda environment use:

``` command
conda activate <env name>
```

For more information about Conda environments, see [Conda - Managing
environments
->](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

Once activated, you can verify that Guild home is the expected
environment by running:

``` command
guild check
```

Confirm that the `guild_home` attribute shows the correct directory.
