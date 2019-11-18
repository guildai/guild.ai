`port`
: The port for SSH connections (integer)

`user`
: The user for SSH connections (string)

`private-key`
: Local path to the private key for SSH connections (string)

`proxy`
: Proxy to use for the SSH connection (string)

`connect-time`
: Number of seconds to wait for an SSH connection before quitting (integer)

`guild-env`
: Remote path relative to the remote `user` home directory to a Guild environment (string)

    Guild activates the environment for each remote command.

    Note that Guild environments are standard Python virtual
    environments so this path may be to any directory created with the
    `virtualenv` command on the remote.

    For more control over the environment activation, use
    `venv-activate`.

`conda-env`
: Conda environment name on the remote (string)

    Guild activates the Conda environment for each remote command. If
    `guild-env` is also specified, the Guild environment is activated
    rather than the Conda environment.

`venv-activate`
: The command used to activate an environment on the remote (string)

    Use this to specify the command that Guild uses to activate an
    environment for remote commands. If this attribute is specified,
    Guild ignored `guild-env` and `conda-env`.

`use-prerelease`
: Use pre-release versions for required packages (boolean)

    When Guild starts a remote run, it installs the run code along
    with required Python packages that are specified in the project
    package definition or in `requirements.txt`. Set this flag to
    `yes` to instruct Guild to install pre-release versions of
    required packages.

`init`
: Shell command to run when the remote is reinitialized (string)

    See [Start and Stop](#ssh-start-stop) below for more information
        about initializing an SSH remote.
