sidenav_title: Remotes

# Remote Cheatsheet

[TOC]

The examples below apply to Guild [user
configuration](ref:user-config). For a complete reference of remote
configuration, see [Remotes Reference](../reference/remotes.md).

!!! note
    Each example includes the top-level `remotes` attribute. This
    attribute may only appear once in a configuration file. If your
    configuration file already has a `remotes` top-level attribute,
    ensure that you don't include it again when pasting content from
    the examples.

## s3 Examples

s3 remotes must use the `s3` type. Refer to [Remotes Reference -
S3](../reference/remotes.md#s3) for full configuration details.

### Minimal Definition

At a minimum, specify a description and a bucket.

``` yaml
remotes:
  s3:
    type: s3
    description: Published results on S3
    bucket: my-s3-bucket
```

### Store Under a Path

To store runs under a path, use a `root` attribute.

``` yaml
remotes:
  s3:
    type: s3
    description: Published results on S3
    bucket: my-s3-bucket
    root: some_path
```
