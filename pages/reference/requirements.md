# Requirements

[TOC]

## Supported Operating Systems

Guild provides precompiled packages that can be installed using
[pip](ref:pip). Below is a table listing the supported platforms.

*Operating System*
: *Python Runtime*

Linux
: Python 2.7, 3.5, 3.6, 3.7, 3.8

maxOS 10.14, 10.15
: Python 2.7, 2.6, 3.7, 3.8

Windows 10
: Python 3.5, 3.6, 3.7

If your operating system configuration is not suppored by one of
Guild's precompiled packages, you can try to compile Guild from source
by following the steps in [*Install Guild AI - From Source
Code*](/install/#from-source-code).

If you need help getting Guild running on your system, please contact
us through [](ref:slack) or by [opening an issue on
GitHub](ref:open-an-issue).

## Required Software Libraries

Guild requires various software libraries. Each dependency is
carefully considered in light of its value to users. If a library does
not provide core functionality, Guild is designed to run without it,
making it optional.

*Pillow*
: Converting images to raw format for TensorBoard summaries

*PyYAML*
: YAML file decoding

*Werkzeug*
: HTTP server used by [Guild View](ref:guild-view) and other Guild web
  applications

*daemonize*
: Background runs and other Guild background tools

*filelock*
: Coordination across Guild processes (e.g. queues)

*jinja2*
: Template support

*pkginfo* and *setuptools*
: Python package support

*scikit-optimize*
: Built-in Bayesian optimization

*tabview*
: Curses based application support used by [Guild Compare](ref:guild-compare]

*tensorboard*
: Embedded TensorBoard support

## Optional Software Libraries

*Pandas*
: Required by `guild.ipy`, Guild's Python Notebook interface

*HiPlot*
: Required when using `--tool hiplot` with [guild compare](cmd:compare)

*TensorFlow*
: If enabled via plugins, Guild logs system metrics for each scalar
  step logged by TensorFlow

*Keras*
: Guild detects Keras scripts and applies the [applicable default
  settings](/reference/defaults.md#keras-scripts) for output scalars
