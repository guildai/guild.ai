# Create a Guild File

[TOC]

## Overview

Up to this point, you run `train.py` directly without providing
additional information about the script.

When Guild runs an operation, it must determine the following:

- How the script accesses user-provided values ([flags](term:flag))
- How the script communicates numeric results ([scalars](term:scalar))
  such as training *loss* and *accuracy*

Unless configured otherwise, Guild uses [default
rules](/reference/defaults.md) to determine this information.

You can configure this information explicitly using a [Guild
file](term:guild-file). A Guild file is a human-readable text file
named `guild.yml` located in a project directory.

## Create a Guild File

In the `guild-start` project directory, create a file named
`guild.yml` that contains this YAML code:

``` yaml
train:
  description: Sample training script
  main: train
  flags-import: all
  output-scalars: '(\key): (\value)'
```

^ Project Guild file `train.yml`

The project directory should look like this:

<div class="file-tree">
<ul>
<li class="is-folder open">guild-start
 <ul>
 <li class="is-folder">archived-runs</li>
 <li class="is-file">guild.yml</li>
 <li class="is-file">train.py</li>
 </ul>
</li>
</ul>
</div>

The Guild file explicitly defines how Guild runs the `train`
operation.

Below is a description of each setting.

`description`
: This value appears when listing the operation and in project
  help. See [*Get Project Info*](#get-project-info) below.

`main`
: Guild loads the specified Python module when running the
  operation. By default, Guild uses the operation name. For more
  information, see [*Python Based
  Operations*](/operations.md#python-based-operations).

`flags-import`
: To save time and simplify configuration, Guild can inspect the
  Python module and import detected flags. Setting `flags-import` to
  `all` tells Guild to use all of the flags it detects. For more
  information, see [*Flags*](/flags.md).

`output-scalars`
: Guild refers to numeric results like *loss* and *accuracy* as
  [scalars](term:scalar). Guild can detect scalars logged by script
  output (e.g. using `print` in Python). By default, Guild captures
  scalars written to output in the format ``KEY: VALUE``. The
  `output-scalars` operation attribute explicitly defines the patterns
  that Guild uses. For more information, see [*Output
  Scalars*](ref:output-scalars).

Refer to [*Guild File Reference*](/reference/guildfile.md) for details
about the Guild file format and available configuration options.

!!! note
    The values for `flags-import` and `output-scalars` used in
    the Guild file above are equivalent to the defaults used by
    Guild. They can be omitted without changing the behavior of the
    operation. We define them explicitly for illustration purposes.

## Get Project Info

When you have saved `guild.yml` above, from the command prompt, list
the project operations:

``` command
guild operations
```

``` output
train  Sample training script
```

Show help for the project:

``` command
guild help
```

``` output
OVERVIEW

    You are viewing help for operations defined in the current directory.

    To run an operation use 'guild run OPERATION' where OPERATION is one
    of options listed below. If an operation is associated with a model,
    include the model name as MODEL:OPERATION.

    To list available operations, run 'guild operations'.

    Set operation flags using 'FLAG=VALUE' arguments to the run command.
    Refer to the operations below for a list of supported flags.

    For more information on running operations, try 'guild run --help'.
    For general information, try 'guild --help'.

BASE OPERATIONS

    train
      Sample training script

      Flags:
        noise  (default is 0.1)
        x      (default is 0.1)

```

Press `q` to exit help.

!!! highlight
    Guild files define the user interface to your
    project. This encourages reproducibility as operations are easy to
    recall, run, and compare.

## Run the Operation

Run the `train` operation:

``` command
guild run train
```

``` output
You are about to run train
  noise: 0.1
  x: 0.1
Continue? (Y/n)
```

!!! note
    You use ``train`` rather than ``train.py`` above. `train` is
    the *operation* defined in the Guild file. `train.py` refers to
    the Python script directly. Guild supports both methods: running
    operations defined in Guild files and running scripts.

Press `Enter` to start the operation.

Guild runs `train`, which is equivalent to the operations you've run
to this point, but is explicitly defined in `guild.yml`.

!!! tip
    While it's convenient to run scripts directly in Guild, we
    recommend that you use a Guild file to explicitly define
    operations for your day-to-day workflow. Guild file operations are
    configured explicitly and discoverable as show above. They support
    a wide range of features that are not available when running
    scripts directly. For more information, see [*Guild File
    Reference*](/reference/guildfile.md).

## Summary

In this section, you create a Guild file to explicitly define a
`train` operation.

!!! highlights
    - Guild files help you and your colleagues effectively use a
      project.
    - Guild files let you control and customize Guild support without
      modifying your source code. This ensures that your project code
      and your tools remain independent.

In the [next section](/start/classifier.md), you create a real-world
classifier and use Guild to track and compare results.
