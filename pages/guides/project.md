# End-to-End Project

[TOC]

## Overview

This guide describes how to use Guild AI for a sample problem:
*predict survival on the titanic given information about a passenger*.

The problem and associated data set are from the Kaggle competition
[Titanic: Machine Learning from
Disaster](https://www.kaggle.com/c/titanic).

The source code, applicable licenses, and attributions are provided in
the [Guild AI `titanic` example source
code](https://github.com/guildai/guildai/tree/master/examples/titanic)

The guide covers:

- Approach to experiment tracking
- Reproducibility
- Work with Jupyter Notebooks and scripts
- Factoring project operations
- Pipelines
- Hyperparameter tuning

## Requirements

- [Guild AI](/install.md)
- [virtualenv ->](https://virtualenv.pypa.io/en/stable/installation/)

## Approach

### Experiment Tracking

An experiment is simple: *try something and measure the result.*

This begs the question: *what are we trying to achieve and how do we
measure progress?*

Guild helps you measure results as you work. When you track
experiments early on, you can focus your efforts to complete your work
faster and with higher quality.

The approach you take in this guide follows these steps:

1. Use a [Guild file](term:guild-file) to define operation stubs that
   simulate your real work
2. Run mock experiments to establish baselines for your work
3. Fill in stubs with real work
4. Re-run experiments to measure progress
5. Improve your work as needed

You repeat this process --- in particular steps 4 and 5 --- until
you're satisfied with the work.

This approach follows the pattern used in [test-driven development
->](https://en.wikipedia.org/wiki/Test-driven_development).

### Reproducibility

The value of reproducibility is first and foremost to you --- the data
scientist, developer, or researcher who writes the code. By
consistently and reliably reproducing results, you know when you're
improving or regressing. Without reliable measurement, you can't be
sure of your progress.

The value of reproducibility extends to others. When your results can
be reproduced by colleagues, reviewers, or your software release team,
your work has higher value.

When using Guild to automate and record experiments, your work is
reproducible. [^reproducible]

[^reproducible]: *Reproducible* does not necessarily mean bit-level
    equivalence. In many cases, results are a function of stochastic
    processes, which may include random seeds, but also may be
    inherently stochastic. A *reproducible result* is one that falls
    within the expected range for a given process.

## Create a Project

In this guide you create a new project from scratch, rather than use a
template or code-generator. This helps you learn each step as you
build the project incrementally.

For reference, you may consult the [completed project source code on
GitHub
->](https://github.com/guildai/guildai/tree/master/examples/titanic).

!!! important
    If you are running on Windows, your user account must be
    able to create symbolic links. You can either open a command
    prompt as Administrator, or [setup the require permissions
    ->](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)
    for your user account.


Create a new project directory:

``` command
mkdir guild-titanic
```

Change to the project directory:

``` command
cd guild-titanic
```

Initialize a new virtual environment within the project directory:

``` command
guild init
```

Guild prompts you with details about the environment.

Press `Enter` to confirm.

Guild uses `virtualenv` to create a new virtual environment.

Activate the environment:

``` command
source guild-env
```

This guide assumes that the commands below are run *from the
`guild-titanic` project directory*. If you open a new

## Create a Guild File

A [Guild file](term:guild-file) defines project operations. In keeping
with process [described above](experiment-tracking) our first task is
to answer the question: *what are we trying to achieve and how do we
measure progress?*

Your task in this guide is to predict the survival of a passenger on
the titanic given information about a passenger.
