We recommend using a [Guild environment](term:environment) to isolate
project runs and installed Python packages. In this section we use
[guild init](cmd:init) to create an envronment for our sample project.

At a command prompt, ensure that you're in the project directory:

``` command
cd $PROJECT
```

Initialize an environment:

``` command
guild init
```

Guild prompts you before initialzing the environment. It prepares to
initialize an environment in the project `env` directory using the
default Python runtime and TensorFlow version for your system.

Press `Enter` to confirm.

Guild initializes the environment, installing required Python
packages. When it finishes, it prompts you to activate the
environment.

An environment must be activated using the operation system `source`
command.

Activate the project environment:

``` command
source guild-env
```

When an environment is activated in a command console, the command
prompt shows the environment name in the format `(NAME)`.

Verify that the environment is activated using the [check](cmd:check)
command:

``` command
guild check
```

Guild shows environment details, including the location of [Guild
home](term:guild-home), which is identified by `guild_home` in the
output.

Confirm that the value for `guild_home` is `$PROJECT/env/.guild`. If
it is not, verify the steps above.
