# Remotes

[TOC]

## Overview

This reference guide lists each remote type, its supported attributes,
and provides examples.

For information on using remotes, see [Remote Training and
Backup](../guides/remote.md).

## SSH

### Attributes

`host`
: Host name to use when connecting to the remote.

### Status

Guild attempts to connect to the remote host over SSH using the
specified connect information. If the connect succeeds, Guild
considers the remote to be *available*.

### Start and Stop

SSH remotes cannot be started or stopped. Guild assumes that the
specified host is available using the specified connect information.

### Remote Commands

SSH remotes support all [remote
commands](../guides/remote.md#remote-commands).

## S3

### Attributes


## EC2
