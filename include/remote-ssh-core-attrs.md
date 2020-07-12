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

`venv-path`
: Path to a virtual environment on the remote host (string)

    Guild activates the environment for each remote command.

    Paths are relative to the remote user home directory.

    Virtual environments are standard Python virtual environments that
    are created with `virtualenv`, `guild init`, or the Python `venv`
    module.

    To strictly control the environment activation, use
    `venv-activate` instead.

`guild-env`
: Alias for `venv-path` (see above for details)

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
