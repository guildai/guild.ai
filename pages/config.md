# Project Configuration

[TOC]

## Guild Files

Guild files are named `guild.yml` and are saved in project directories
to support Guild functionality. Guild files define operations and
models. They support a variety of code reuse features.

See [Guild File](reference/guildfile.md) for a complete list of
configuration options.

## Operations

Operations define what Guild runs to generate an experiment. Here's a
simple operation definition in a Guild file:

``` yaml
train:
  main: train
  flags:
    learning-rate: 0.1
    batch-size: 100
```

- The operation is named `train` and can be run using ``guild run train``.

- The main Python module is also named `train` and should be defined
  in a file named `train.py` in the same directory as `guild.yml`.

- The operation defines two flags: `learning-rate` and `batch-size`,
  each with default values.

To run the `train` operation, change to the directory containing
`guild.yml` and run:

``` command
guild run train
```

Guild shows a preview of the flags used for the operation and asks you
to confirm the operation by pressing `Enter`. When you confirm the
operation, Guild executes the `train` module with the specified flag
values.

See [Flags](#flags) below for information about how Guild communicates
flag values to a Python module.

See [Operations](reference/guildfile.md#operations) for a complete
list of configuration options.

## Flags

## Output Scalars

## Required Resources

## Source Code Snapshots

## Models

## Named Resources

## Packages
