When working with projects, we recommend using a [Guild
environment](term:environment) to isolate project runs and installed
Python packages.  This ensures that work in one project does not
conflict with work in other projects.

At a command prompt, ensure that you're in the project directory:

``` command
cd $PROJECT
```

Use the [init](cmd:init) command to initialize a Guild environment:

``` command
guild init
```

Guild prompts you before initialzing the environment in the project
`env` directory with the default Python runtime and TensorFlow version
for your system.

Press `Enter` to confirm.

Guild creates a new Python virtual environment in the project
directory under `env`, which contains the Python runtime, installed
Python packages, and project [Guild home](term:guild-home).

A project environment must be activated using the operation system
`source` command.

Activate the project environment:

``` command
source guild-env
```

When an environment is activated in a command console, the command
prompt shows the environment name in the format `(<env name>) <default
prompt>`. The environment name is the project directory name by
default but can be set using the `--name` when running [guild
init](cmd:init).

!!! note
    You must activate the project environment using ``source
    guild‑env`` each time you open a new command console for project
    work.

Verify that the environment is activated using the [check](cmd:check)
command:

``` command
guild check
```

Guild shows environment details, including the location of [Guild
home](term:guild-home), which is identified by `guild_home` in the
output.

Confirm that the path for `guild_home` is in the project directory
under `env/.guild`. If it is in a different location, verify the steps
above to ensure that your project environment is initialized and
activated.
