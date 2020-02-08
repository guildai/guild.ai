# Plugins

[TOC]

## Overview

Guild supports a *plugin* API that is used to modify and extend Guild
behavior.

Guild plugins can be used for the following functions:

- Extend or modify Guild file configuration
- Perform tasks during a run
- Provide built-in operations

## Enable Plugins for an Operation

By default, plugins are not enabled for operations. You can enable one
or more plugins for an operation using the `plugins` operation
attribute.

For example, to enable all summary-related plugins for operation
`train`, use:

``` yaml
train:
  plugins: summary
```

For more information, see [`plugins` operation
attribute](/reference/guildfile.md#operation-plugins).

{! summary-plugin-support-notice.md !}

## Built-In Plugins

Guild provides the following built-in plugins:

`cpu`
: Logs CPU usage per step

`disk`
: Logs disk usage per step

`exec_script`
: Support for running executable scripts

`gpu`
: Logs GPU usage per step

`keras`
: Support for running Keras scripts

`memory`
: Logs memory usage per step

`perf`
: Logs last step performance per step

`python_script`
: Support for running Python scripts

`queue`
: Support for queue operations

`skopt`
: Support for scikit-optimize based operations (e.g. Bayesian
  optimizers)

## Custom Plugins

To provide a custom plugin, create a class that extends
`guild.plugins.Plugin` and register it as a [Python entry point
->](https://packaging.python.org/specifications/entry-points/).

Refer to [Guild AI plugins source code
->](https://github.com/guildai/guildai/tree/master/guild/plugins) for
examples.

Below are specific examples for various uses.

*Example*
: *Use*

[cpu.py ->](https://github.com/guildai/guildai/blob/master/guild/plugins/cpu.py)
: Log additional scalar values for a given step.

[python_script.py ->](https://github.com/guildai/guildai/blob/master/guild/plugins/python_script.py)
: Support new operation types --- e.g. handling operation specs such
  as a path to an R script, a Java JAR file, a URL, etc.

[keras_script.py ->](https://github.com/guildai/guildai/blob/master/guild/plugins/keras_script.py)
: Support new Python based frameworks.

[skopt.py ->](https://github.com/guildai/guildai/blob/master/guild/plugins/skopt.py)
: Add built-in operations including optimizers.
