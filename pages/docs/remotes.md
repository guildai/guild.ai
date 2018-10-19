tags: concepts

# Remotes

A *remote* is an non-local environment that can be used for various
Guild commands. Remotes are defined in [user
configuration](term:user-config).

Guild supports three types of remotes:

*SSH*
: Use to run operations on a remote server over SSH.

*AWS EC2*
: Use to create AWS EC2 instances and use them to run operation over
  SSH.

*AWS S3*
: Use to store and manage runs in an AWS S3 bucket.

Remotes

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

### Supported commands

SSH remotes support the following Guild commands:

- [remote status](cmd:remote-status)
- [](cmd:run)
- [runs list](cmd:runs-list)

SSH remotes cannot be started or stopped using Guild.

## EC2

## S3
