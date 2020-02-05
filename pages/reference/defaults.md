# Default Behavior

[TOC]

## Overview

This document describes the assumptions that Guild makes in the
absence of explicit configuration.

The topics cover a number of topics:

- [Flags interface](ref:flags-interface)
- [Output scalars](ref:output-scalars)

## Python Scripts

Unless otherwise configured in a [Guild file](ref:guildfile), Guild
makes a number of assumptions when running Python scripts. This
includes cases when a script is run directly and when a script is
defined using the `main` operation attribute.

#### Flags Interface

If the `flags-dest` attribute, which specifies the [flags
interface](ref:flags-interface), is not defined for an operation,
Guild attempts to detect the interface by inspecting the operation
Python module.

- If the module imports the [`argparse` module
  ->](https://docs.python.org/library/argparse.html), Guild assumes
  that flags are set using command line arguments.

- If the main module does not import `argparse`, Guild assumes that
  flags are defined in global variables.



Guild inspects the script to determine if it uses `argparse` to parse
command line arguments

## Keras Scripts
