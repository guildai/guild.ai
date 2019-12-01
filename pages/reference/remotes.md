sidenav_title: Remotes

# Remotes Reference

[TOC]

## Overview

This reference guide lists each remote type, its supported attributes,
and provides examples.

For information on using remotes, see [Remote Training](/remote.md).

## SSH

<a id="ssh-attributes"></a>

### Attributes

{! remote-core-attrs.md !}

`host`
: Host name to use when connecting to the remote (required string)

{! remote-ssh-core-attrs.md !}

### Status

On [remote status](cmd:remote-status), Guild attempts to connect to
the remote host over SSH using the specified connect information. If
the connect succeeds, Guild considers the remote to be available.

<a id="ssh-start-stop"></a>

### Start and Stop

SSH remotes cannot be started or stopped. Guild assumes that the
specified host is available using the specified connect information.

SSH remotes can, however, be initialized using the `--reinit` option
to [remote start](cmd:remote-start). When `--reinit` is specified,
Guild runs the shell command defined in the remote's `init` attribute.

Consider the following remote configuration:

``` yaml
remotes:
  my-remote:
    type: ssh
    host: remote-hostname
    init: |
      sudo apt update -y
      sudo apt upgrade -y
```

The command ``guild remote start my-remote --reinit`` will run the
`init` command on the `remote-hostname` host. Use this facility to
ensure that the remote is configured correctly before running Guild
commands.

### Remote Commands

The commands below can be used with SSH remotes.

{! remote-cmds-all.md !}

### Security

Security is managed by the SSH protocol between the local system
(client) and the remote (server). Connection settings are defined as
attributes (see above) and by the SSH environment. Refer to the SSH
documentation for your system for additional security details.

### Examples

For additional examples, see [Remote Cheatsheet -
SSH](/cheatsheets/remotes.md#SSH).

The following is a minimal SSH remote configuration. It used all of
the default values. Runs will be located in `~/.guild` on the remote
server where `~` is the home directory for the default user associated
wit `remote-hostname`.

``` yaml
remotes:
  ssh-remote:
    type: ssh
    description: Remote runs
    host: remote-hostname
```

Note that `ssh` defaults are specified according to the SSH
implementation on the local (client) system. Refer to the
documentation for your SSH client for details on configuring defaults.

The next example defines additional SSH settings as well as a Guild
environment.

``` yaml
remotes:
  production:
    type: ssh
    description: Production runs
    host: remote-hostname
    user: ubuntu
    port: 2222
    guild-env: ~/Envs/production
    init: test -e ~/Envs/production || guild init -y ~/Envs/production
```

Note that `init` defines a command that creates a Guild environment if
one doesn't exist. Use ``guild remote start production --reinit`` to
ensure that the environment is setup correctly before running Guild
commands.

## EC2

EC2 provide the same features as SSH remotes. In addition, EC2 remotes
can be started and stopped on EC2 by configuring EC2 instance
attributes. Refer to [Attributes](#ec2-attributes) below for details.

### Attributes

{! remote-core-attrs.md !}

`ami`
: The AMI used to create the EC2 instance (required string)

`instance-type`
: The type of EC2 instance to create (required string)

`region`
: The AWS region to create the EC2 instance in (string)

    If this value isn't specified, Guild uses the value defined by the
    `AWS_DEFAULT_REGION` environment variable.

`root-device-size`
: The size of the root volume created for the server (integer)

    If this value is omitted, the default volume size for the AMI is
    used.

`public-key`
: Local path to the public key associated with `private-key` (string)

    The contents of the local file referenced by this path is included
    in the remote server's authorized keys for the SSH user.

{! remote-ssh-core-attrs.md !}

`init-timeout`
: Number of seconds to allow the `init` command to finish before
  timing out (integer)

    By default, the `init` command does not have a timeout.

### Status

On [remote status](cmd:remote-status), Guild attempts to connect to
the remote host over SSH using the specified connect information. If
the connect succeeds, Guild considers the remote to be available.

### Start and Stop

On [remote start](cmd:remote-start), Guild uses [](ref:terraform) to
start an EC2 instance using the EC2 remote settings. On [remote
stop](cmd:remote-stop), Guild similarly terminates the EC2 instance
using Terraform.

### Remote Commands

The commands below can be used with EC2 remotes.

{! remote-cmds-all.md !}

### Security

The following environment variables must be defined when starting or
stopping an EC2 remote.

`AWS_ACCESS_KEY_ID`
: The AWS access key ID that has the requisite permissions for
  starting or terminating the applicable EC2 instance.

`AWS_SECRET_ACCESS_KEY`
: The AWS secret access key associated with the access key ID.

The following environment variables may be optionally defined:

`AWS_DEFAULT_REGION`
: The AWS region the remote instance is creatd in. This value may
  alternatively be defined in the EC2 remote configuration.

Once an EC2 remote is created, security is managed by the SSH protocol
between the local system (client) and the remote (server).

### Examples

For additional examples, see [Remote Cheatsheet -
EC2](/cheatsheets/remotes.md#EC2).

The following is a minimal example of an EC2 remote:

``` yaml
remotes:
  ec2-v100:
    type: ec2
    description: NVIDIA V100 on EC2
    region: us-east-2
    ami: ami-0a47106e391391252
    instance-type: p3.2xlarge
    public-key: ~/.ssh/id_rsa.pub
    user: ubuntu
```

## S3

Use S3 remotes to store runs remotely. S3 buckets support the full set
of remote management commands. See [Remote
Commands](#s3-remote-commands) below for details.

### Attributes

{! remote-core-attrs.md !}

`bucket`
: S3 bucket to store runs in (required string)

`root`
: Path in the S3 bucket to store runs in (string)

`region`
: AWS region where the bucket was created (string)

    The region may alternatively be specified using the
    `AWS_DEFAULT_REGION` environment variable when running a remote
    command for the S3 remote.

### Status

On [remote status](cmd:remote-status), Guild checks that the bucket
exists and that Guild can read from it. This check does not perform a
write test.

### Start and Stop

S3 remotes can be started and stopped. When started, Guild creates the
remote bucket as needed. When stopped, Guild deletes the remote bucket
if it exists.

!!! important
    Stopping an S3 remote will delete all contents of the
    remote bucket, including Guild runs any objects that were copied
    to the bucket independently of Guild. This operation cannot be
    undone.

<a id="s3-remote-commands"></a>

### Remote Commands

The following commands can be used with S3 remotes.

{! remote-cmds-run-mgmt.md !}

### Security

The following environment variables must be defined when running any
command on an S3 remote.

`AWS_ACCESS_KEY_ID`
: The AWS access key ID that has the requisite permissions on the
  remote S3 bucket.

`AWS_SECRET_ACCESS_KEY`
: The AWS secret access key associated with the access key ID.

The following environment variables may be optionally defined:

`AWS_DEFAULT_REGION`
: The AWS region associated with the bucket. This value may
  alternatively be defined in the S3 remote configuration.

### Examples

The following example stores runs directly in `my-s3-production-runs`
bucket.

``` yaml
remotes:
  s3-production:
    type: s3
    description: Production runs
    bucket: my-s3-production-runs
```

You can use `root` to store runs under a bucket path.

``` yaml
remotes:
  s3-test:
    type: s3
    description: Test runs
    bucket: my-s3-runs
    root: test

  s3-production:
    type: s3
    description: Production runs
    bucket: my-s3-runs
    root: production
```
