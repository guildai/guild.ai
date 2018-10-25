tags: concepts

# Remotes

[TOC]

A *remote* is an non-local environment that can be used for various
Guild commands. Remotes are defined in [user
configuration](term:user-config).

Guild supports three types of remotes:

SSH
: Use to run operations on a remote server over SSH.

AWS EC2
: Use to create AWS EC2 instances and use them to run operation over
  SSH.

AWS S3
: Use to store and manage runs in an AWS S3 bucket.

## SSH

SSH remotes are used to run operations on remote servers over
SSH. This is useful for taking advantage of powerful GPU servers while
using Guild commands.

Here's an example of an SSH remote named ``v100`` (e.g. it might host
an NVIDIA Tesla V100 GPU):

``` yaml
remotes:
  v100:
    type: ssh
    host: v100.company.net
```

SSH remotes support the following Guild commands:

- [](cmd:pull)
- [](cmd:push)
- [remote status](cmd:remote-status)
- [](cmd:run)
- [runs delete](cmd:runs-delete)
- [runs info](cmd:runs-info)
- [runs label](cmd:runs-label)
- [runs list](cmd:runs-list)
- [runs purge](cmd:runs-purge)
- [runs restore](cmd:runs-restore)
- [runs stop](cmd:runs-stop)
- [](cmd:watch)

SSH remotes cannot be started or stopped using Guild.

Refer to [User configuration for ssh
remote](/docs/reference/user-config/#ssh-remote) for details on
defining an SSH remote.

## EC2

EC2 remotes are SSH remotes with additional support for starting and
stopping.

Guild uses [Terraform ->](https://www.terraform.io/) to setup (for the
start command) and tear down (for the stop command) all AWS
infrastructure associated with an EC2 remote.

EC2 remotes support all of the commands supported by [SSH](#ssh) (see
above).

In addition, EC2 remotes support start and stop:

- [remote start](cmd:remote-start)
- [remote stop](cmd:remote-stop)

Refer to [User configuration for ec2
remote](/docs/reference/user-config/#ec2-remote) for details on
defining an EC2 remote.

## S3

S3 remotes provide an interface for storing and managing runs remotely
in an S3 bucket. S3 remotes are useful for backing up and restoring
runs to the cloud.

S3 remotes support the following Guild commands:

- [](cmd:pull)
- [](cmd:push)
- [remote status](cmd:remote-status)
- [runs delete](cmd:runs-delete)
- [runs info](cmd:runs-info)
- [runs label](cmd:runs-label)
- [runs list](cmd:runs-list)
- [runs purge](cmd:runs-purge)
- [runs restore](cmd:runs-restore)

As S3 does not support compute, S3 remotes cannot be used to run
operation.

Refer to [User configuration for s3
remote](/docs/reference/user-config/#s3-remote) for details on
defining an S2 remote.
