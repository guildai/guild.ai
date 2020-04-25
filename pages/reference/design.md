# Guild Design

[TOC]

## Overview

This document describes Guild design decisions. Design decisions stem
from various *goals*, which are listed below. Each goal implies
various design approaches, which are helpful in understanding why
Guild works the way it does.

*Goal*
: *Design Implication*

Source code should not be changed merely to support experiment tracking.
: Support for experiment tracking is provided by external
  configuration to [avoid source code changes](#source-code-change).

Developers should measure results early in a project life cycle.
: Avoid complicated setup and [minimize external dependencies](#dependencies).

Guild should work as expected.
: Build reliable systems that minimize complexity and are resiliant to
  failure.

Guild should integrate easily with other systems.
: Adopt architectural idioms that enable rich software ecosystems such
  as the [Unix Philosphy](#unix-philosophy).

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

Guild minimizes dependencies, both in terms of required software
libraries and required system components.

Guild avoids dependencies on:

- Databases
- Exotic file systems
- Network processes or agents
- Cloud services

Dependencies have both up-front and hidden costs:

- Time to install and configure
- Cost to maintain and upgrade
- Ongoing risk of outages
- Reduced portability and flexibility

By avoiding these dependencies, Guild lets you start tracking
experiments faster and avoid ongoing system maintenance costs. Guild
additionally avoids outages associated with unavailable or faulty
required systems.

<!-- TODO

- Section elaborating on lifecycle of Guild - using it as soon as a
  project is started.

-->

## Unix Philosophy

Guild maintains the [Unix philosophy
->](https://en.wikipedia.org/wiki/Unix_philosophy) of keeping things
small, modular, and composable. This has a big payoff, not just for
operating systems, but for ML engineering.

- Guild commands do one thing and one thing well
- Guild commands work together
- Guild features layer on top of system facilities such as commands,
  command line arguments, environment variables, standard input and
  output, and the file system interface

This approach allows Guild to evolve gracefully, adding new features
without disrupting core functionality. It lets Guild support a wide
range of ussage scenarios, from getting started to advanced pipeline
management, all using the same design approach.
