tags: concepts

# Operations

[TOC]

An operation is an action performed on a [](term:model).

## Flags

## Required resources

Operations may require [resources](term:resource). Required resources
are listed in the operation's `requires` attribute.

When Guild starts an operation, it first resolves each required
resource. If a resource cannot be resolved, the operation fails with
an error message.

Resources are resolved by acquiring them (e.g. download a file from
the Internet), verifying them, and finally creating links to resources
files in the run directory. In this way, operations can easily express
"I need these files to run" and ensure that the correct files are
available for each run.
