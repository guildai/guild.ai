sidenav_title: User Configuration

# User Configuration Reference

[TOC]

## Overview

Guild user configuration is defined in `~/.guild/config.yml`. User
configuration applies across all projects and packages.

## Check

**Section heading:** `check`

Guild [check](cmd:check) can be configured by defining any of the
attributes below under a top-level `check` mapping.

### Attributes

`offline`
: Flag specifying default offline mode for checks (boolean)

    When offline, Guild will not check for latest versions and will
    instead show ``unchecked (offline)``.

    Default is `no`.

### Examples

Don't check for latest Guild AI version by default:

``` yaml
check:
  offline: yes
```

Note, you can use `--offline` or `--no-offline` when running
[check](cmd:check) to override this setting.

## Diff

**Section heading:** `diff`

Guild [diff](cmd:diff) can be configured by defining any of the
attributes below under a top-level `diff` mapping.

### Attributes

`command`
: The command used when diffing two paths. The two paths are appended
  to this command as separate arguments.

### Examples

Use [Meld](ref:meld) to diff runs:

```
diff:
  command: meld
```

## Remotes

**Section heading:** `remotes`

Remotes provide configuration that Guild uses for remote-related
operations. A remote operation is specified by using the `--remote`
option with the name of remote configured in this section.

For example, the following command starts an operation on a remote
named `my-host`:

```command
guild run train --remote my-host
```

In this case, `my-host` must be defined under `remotes` in user
config:

``` yaml
remotes:
  my-host:
    ...
```


Not all commands support remotes. For a list of remote-enabled
commands, see [Remote Commands](../guides/remote.md#remote-commands).

Refer to [Remotes](remotes.md) for details on configuring remote
types.
