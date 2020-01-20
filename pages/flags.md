tags: concept

# Flags

[TOC]

## Overview

Flags are parameter values used as inputs to an operation. Flags are
used to specify a variety of values such as hyperparameters, file and
directory paths, and data set names.

## Flags Interface

XXX

## Automatic Flag Detection

Unless otherwise configured in a Guild file, Guild attempts to detect
script flags by inspecting the script Python module.

Guild first attempts to determine if the Python script uses command
line arguments or if it used global variables.

- If the main module imports the [`argparse` module
  ->](https://docs.python.org/library/argparse.html), Guild assumes
  that flags are set using command line arguments.

- If the main module does not import `argparse`, Guild assumes that
  flags are defined in global variables.

## Explicit Flag Configuration

## Command Line Arguments

## Batch Files

## Special Flag Values

### Value Lists

### Sequence Functions

`range[START:END:STEP=1]`
: Generates a list of values starting with `STEP` and ending with
  `END` in increments of `STEP`. `STEP` may be omitted, in which case
  the value `1` is used.

      Examples:

      ```
      range[1:4] -> [1, 2, 3, 4]
      range[1:4:2] -> [1, 3]
      range[0:0.3:0.1] -> [0.0, 0.1, 0.2, 0.3]
      ```

### Search Space Functions

### List Concatenation

Guild supports Python's syntax for generating a list of repeating
elements using the syntax `[VAL1,VAL2,...,VALN]*M` where `M` is the
number of times to repeat the list sequence.

For example, Guild expands the value `[1]*5` to the sequence
`[1,1,1,1,1]`.

Use this pattern to repeat
