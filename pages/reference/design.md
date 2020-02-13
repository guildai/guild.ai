# Guild Design

[TOC]

## Overview

This document describes Guild design decisions. Design decisions stem
from opinions, or precepts, that are helpful to understand when using
Guild.

*Opinion*
: *Design Implication*

Source code should not be changed merely to support experiment tracking.
: Support for experiment tracking is provided by external
  configuration to [avoid source code changes](#source-code-change).

Developers should measure results early in a project life cycle.
: Avoid complicated setup and [minimize external dependencies](#dependencies).

<div id="source-code-change"></div>
## Avoid Changes to Project Source Code

Guild avoids asking you to change your source code to support Guild
features. By keeping your source code free of Guild-specific
changes, you enjoy several benefits:

- Your code continues to work without Guild. This means you can share
  your code with others without requiring that they use Guild.

- Start using Guild immediately.

- Add Guild support to someone else's code. For example, to enable
  experiment tracking for someone else's project, add a Guild file and
  submit a pull request.

<div id="dependencies"></div>
## Minimize Dependencies

Dependencies have both up-front and hidden costs:

- Time to install and configure
- Cost to maintain and upgrade
- Ongoing risk of outages
- Reduced portability and flexibility

Guild minimizes dependencies, both in terms of required software
libraries and required system components.

Guild avoid dependencies on:

- Databases
- Distributed or other exotic file systems
- Network processes or agents
- Cloud services

### Required Software Libraries

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

### Optional Software Libraries

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

<!-- TODO

- Section elaborating on lifecycle of Guild - using it as soon as a
  project is started.

-->
