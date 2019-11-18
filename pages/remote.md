tags: concept

# Remote Training

[TOC]

## Overview

Guild supports training on remote system by way of a *remote*
facility.

- Define a remote in [user configuration](ref:user-config)
- Specify the remote name using the `--remote` option when running an
  operation

For a complete reference on remote configuration, see [Remotes
Reference](reference/remotes.md).

## Define a Remote

Remotes are defined in [user configuration](ref:user-config). Below is
an example of an SSH remote named `remote-gpu`:

``` yaml
remotes:
  remote-gpu:
    type: ssh
    host: gpu001.mydomain.com
    user: ubuntu
    private-key: ~/.ssh/gpu001.pem
```

Guild supports a variety of remote types:

[`ssh`](reference/remotes.md#ssh)
: Connect to a remote server over [SSH](term:ssh). Use this type to
  train on remote servers on-premises or on any cloud vendor. Guild
  does not support support starting of `ssh` remote types.

[`ec2`](reference/remotes.md#ec2)
: Connect to a remote EC2 host over [SSH](term:ssh). This remote type
  supports [start](cmd:remote-start) and [stop](cmd:remote-stop) given
  EC2 specific configuration for the remote.

[`s3`](reference/remotes.md#s3)
: Copy runs to and from S3. This remote type does not support runs but
  can be used for backup and restore.

For a complete list of remote types, including examples, see
[Remotes](ref:remote).




## Run a Remote Operation

TODO

## Manage Remotes

Remotes can be listed, checked for status, and, if supported by the
remote type, started and stopped.

Remote management commands are:

[remotes](cmd:remotes)
: List available remotes.

[remote status](cmd:remote-status)
: Show status for a remote.

[remote start](cmd:remote-start)
: Start a remote. Not all remote types can be startd.

[remote stop](cmd:remote-start)
: Stop a remote. Not all remote types can be stopped.

A remote must be available before it can be used in a remote
command. Check a remote using [remote status](cmd:remote-status). If a
remote is not available and can be started, use [remote
start](cmd:remote-start) to start it first. Note that some remote
types cannot be started or stopped. Refer to [Remotes](ref:remote)
for detail on each remote type.

## Remote Commands

To run apply a command to a remote, use the `--remote` option. For
example, to run [check](cmd:check) on a remote named `remote-gpu` (see
example above), run:

``` command
guild --remote remote-gpu check
```

Not all remote types support every command. For example, the `s3`
remote type does not support the `run` command. Refer to
[Remotes](ref:remote) for details on which remote commands are
support for a particular remote type.

Remote commands include:

[run](cmd:run)
: Run an operation on a remote. Not all remote types support running
  an operation.

[runs stop](cmd:runs-stop)
: Stop runs in progress on a remote.

[watch](cmd:watch)
: Connect to a remote run in progress and watch its output.

[runs list](cmd:runs-list)
: List runs on a remote.

[runs info](cmd:runs-info)
: Show information about a remote run.

[label](cmd:label)
: Apply a label to one or more remote runs.

[runs delete](cmd:runs-delete)
: Delete runs on a remote.

[runs restore](cmd:runs-restire)
: Restore deleted runs on a remote.

[runs purge](cmd:runs-purge)
: Purge deleted runs on a remote.

[pull](cmd:pull)
: Copy remote runs to the local system.

[push](cmd:push)
: Copy local runs to the remote.

## Compare Remote Operations

TODO
