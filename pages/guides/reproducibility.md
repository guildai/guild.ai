<!-- TODO

Needs lot more work

-->

# Reproducibility

[TOC]

## Overview

Reproducibility is an important topic in machine learning. Guild
supports reproducibility by automating the steps for setting up and
training models. Guild captures details about each run so results can
be compared over time.

Reproducibility involves control across various levels:

- Model implementation
- Data set
- Runtime environment
- Random seed

Guild supports reproducibility across any combination of levels and
does not impose limits or enforce a particular definition of
reproducibility. Organizations should define the level of
reproducibility required for their applications and implement support
accordingly.

This guide discusses the various elements of reproducibility.

## Model Implementation

TODO

## Data Set

TODO

## Runtime Environment

A runtime environment plays an important role in reproducing
results. Guild captures platform attributes such as Python version,
operating system details, and installed library versions. Use this
information to compare results.

Guild provides support for initializing Python environments to
facilitate consistency across runs. Developers are responsible for
configuring their projects as needed.

### Python Version

TODO: This content has been moved to the `init` command
help. Reference that link from here.

You can specify a Python requirement in either a project Guild file or
within a `requirements.txt` file.

When you run [](cmd:init), Guild first checks the Guild file for a
Python requirement in a `package` definition and then checks
`requirements.txt` for a requirement comment.

Requirements must comply with the [](ref:pip-reqs).

Below is a package definition with a `python-requires` spec indicating
that Python 3.5 or greater is required for project operations. Guild
will attempt to find the best suitable Python interpreter when
creating a virtual environment using [](cmd:init) that satisfies this
requirement.

``` yaml
- package: sample
  python-requires: >=3.5
```

You may alternatively add a requirement command to `requirements.txt`.

```
# python>=3.5

pandas
matplotlib
keras
```

^ `requirements.txt` with Python requirements comment --- used by
  Guild `init` when creating a virtual environment

The first line of `requirements.txt` is a comment and therefore
ignored by `pip`. However, Guild uses the comment to find a suitable
Python interpreter when creating a virtual environment via [](cmd:init).

Note that you must use [guild init](cmd:init) when creating a virtual
environment to use Python requirement information. Neither Conda nor
virtualenv will use this information.

## Operations

Operations are central to Guild's support of
reproducibility. Operations define how runs are executed, including:

- Program command
- Program environment
- Run directory layout

Guild measures both inputs and outputs for each run and supports
detailed diffs between runs.

For general information about operations, see
[Operations](ref:operations).

To compare run flags and logged metrics (output scalars), use
[](cmd:compare).

To diff two runs, use [](cmd:diff).

## Compare Runs Across Systems

To compare two runs generated on different systems, you must
consolidate the runs using Guild input/output commands.

- Use [](cmd:export) to export runs to an archive that can be copied
  to a consolidated system and imported using [](cmd:import)
- Use [](cmd:push) to copy runs to a remote location where they can be
  copied to a consolidated system using [](cmd:pull)

It's common for organizations to setup a *runs sink* where important
runs can be pushed for backup, deployment, or additional analysis and
comparison. Once consolidated on a sink, use [](cmd:compare) and
[](cmd:diff) to study differences. There you can apply automated
comparison tests to formally apply reproducibility checks.

## Compare Run Attributes

Guild captures a number of attributes for each run that may be
consulted when comparing runs.

Each of these attributes is automatically included when running
[](cmd:diff). However, it's useful to understand the attributes,
especially when running automated checks.

{! run-attrs.md !}
