sidenav_title: init
overview_title: init
tags: common

# init

[TOC]

[CMD-HELP init]

## Project Configuration

### Required Python Version

By default, Guild does not specify the Python version when creating a
virtual environment. It lets `virtualenv` / `venv` select the
version. You can specify the required Python version or location using
`-p` or `--python`.

However, Guild will use project configuration if available to find a
suitable version of Python when creating a virtual environment.

If a project defines a `python-requires` spec in a `package`
definition, Guild will use that spec to find a suitable Python versions
on the system

The spec must comply with the [](ref:pip-reqs).

Below is a package definition with a `python-requires` spec indicating
that Python 3.5 or greater is required for project operations.

``` yaml
- package: sample
  python-requires: >=3.5
```

^ Package definition in `guild.yml` specifying a required Python
  version

Alternatively, if a `requirements.txt` file contains a Python spec
comment in the format ``# python<requirement spec>``, Guild will
attempt to use that spec to select a suitable Python version.

Here's a `requirements.txt` file that indicates that project requires
Python 3.6.

```
# python==3.6

pandas
matplotlib
keras
```

^ Sample `requirements.txt` containing a special comment indicating
  the required Python version

!!! note
    You must use [guild init](cmd:init) when creating a virtual
    environment to use Python requirement information. Neither Conda
    nor virtualenv will use this information.
