# Upgrade Guild

[TOC]

## From 0.6.x

!!! important
    There are breaking changes from `0.6.x`. Read the list
    below carefully before upgrading production systems.

### Guild no longer imports flags by default

Prior to `0.7`, Guild automatically imported all detected flags for
operations defined in a Gulid file. Guild no longer imports flags by
default. You must either use `flags-import` or define the complete set
of flags.

Required Guild file configuration for upgrade:

``` yaml
train:
  flags-import: all
```


^ Guild no longer imports flags by default. Use `flags-import` to
specify `all` or a list of flag names.

For more information, see [Flags](/flags.md).

### Some command line options have changes

The following command line short-form options have changed from
`0.6.x`:

| Command          | Short-Form Option in `0.6.x` | Changed To | Description                |
|------------------|------------------------------|------------|----------------------------|
| multiple         | `-st`                        | `-S`       | Filter by start time       |
| multiple         | `-u`                         | `-U`       | Filter by unlabeled status |
| multiple         | `-U`                         | `-N`       | Filter by unmarked status  |
| [diff](cmd:diff) | `-g`                         | `-f`       | Diff run flags             |
