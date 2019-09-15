# Guild File

[TOC]

## Overview

## Operations

## Models

## Packages

A Guild file may contain at most one top-level package object. A
package object is identified by the use of the `package` attribute.

Guild uses package configuration when [package](cmd:package) is
run. If a package object is not defined for a Guild file, Guild uses
default values, which are described below.

Define a package when you want to:

- Distribute your project as a Python distribution (e.g. on PyPI,
  etc.)
- Include additional data files for remote runs
- Control the package name and version associated with remote
  operations

As a convention, we recommend that you define the package as the last
object in a Guild file. Package information is generally less
important than the models and operations defined in a Guild
file. Positioning the package at the bottom of the file makes it
easier to locate this information when available.

### Attributes

`package`
: Package name (string)
  <p>
  Defaults to name of default model.

`version`
: Package version (string)
  <p>
  Defaults to `0.0.0`.

`description`
: Package description (string)
  <p>
  This can be a multi-line description.

`url`
: URL to package website (string)

`author`
: Name of individual or organization author (string)

`author-email`
: Email of package author (string)

`license`
: Name of package license (string)

`tags`
: List of package tags (list of strings)

`python-tag`
: Python tag used in the distribution name (string)

`data-files`
: List of additional data files to include in the distribution (list
  of strings)
  <p>
  Guild always includes `guild.yml`, `LICENSE.*`, and `README.*`. The
  list of files specified by this attribute is added to this list.
  <p>
  This is another paragraph yop.

`python-requires`
: Version of Python required by the package (string)

`requires`
: Requirements that must be satisfied when the package is installed
  (list of string)

`packages`
: Project Python packages to be included in the distribution (list of
  strings)
  <p>
  Default is the list of packages returned by
  `setuptools.find_packages()`.

### Examples

``` yaml
- model: hello
  operations:
    say:
      main: say

- package: hello
  description: Simple hello workd package
  version: 1.0
  url: https://github.com/guildai/packages/tree/master/gpkg/hello
  author: Guild AI
  author-email: packages@guild.ai
  license: Apache 2.0
  data-files:
    - msg.txt
```

## Config
