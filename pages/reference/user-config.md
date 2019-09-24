# User Configuration

[TOC]

## Overview

Guild user configuration is defined in `~/.guild/config.yml`. User
configuration applies across all projects and packages.

## Diff

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

Remotes are defined in user configuration under a top-level `remotes`
mapping.

``` yaml
remotes:
  remote-1:
    ...
  remote-2:
    ...
```

A remote is applied to a command using the `-r, --remote` option. For example:

``` command
guild run --remote remote-1 train
```

Not all commands support remotes. For a list of remote-enabled
commands, see [Remote Commands](../guides/remote.md#remote-commands).

Refer to [Remotes](remotes.md) for details on configuring remote
types.
