title: Install
layout: default
navbar: yes

# Get started with Guild AI

## Requirements

Before installing Guild, review the requirements below.

- Windows, Max OS, Linux
- Python 2.7, Python 3
- pip

Guild is installed from PyPI using the `pip` command. Refer to
[Installing pip ->](https://pip.pypa.io/en/stable/installing/) to
ensure you have pip installed.

## Installation

In a console, run the following:

``` shell
pip install guildai
```

!!! note
    You may need to run `pip` as a privileged user, in which case
    run the above command as `sudo pip install guildai`. If you
    would prefer to install Guild as an unpriviledged user, we
    recommend using a Python virtual environment. Refer to
    [Install using Virtualenv](#install-using-virtualenv) below.

### Install using Virtualenv

You may alternatively install Guild within a Python virtual
environment. This has the advantage of isolating Guild and its
requirements in a single directory.

``` shell
virtualenv guild
source guild/bin/activate
pip install guildai
```

!!! note
    If you install Guild in a virtual environment, you must activate the
    environment before using Guild using the command `source
    VIRTUAL_ENV_DIR/bin/activate`.

For more information refer to the [Virtualenv documentation
->](https://virtualenv.pypa.io/en/stable/).

## Verify your installation

Verify that Guild is installed propery by running the
[`check`](docs/commands/check) command:

``` shell
guild check
```
