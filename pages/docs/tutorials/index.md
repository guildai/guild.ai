sidenav_title: Overview
tags: guide

# Tutorials

[TOC]

- [Introductory](category:/docs/tutorials/#intro)
- [Advanced](category:/docs/tutorials/#advanced)
- [Tools](category:/docs/tutorials/#tools)

## Tutorial virtual environments

Each tutorial is structured to work with or without a virtual
environment. However, there are some advantages to using a virtual
environment for each tutorial:

- You can focus on the packages, models, and operations specific to
  that tutorial.

- Your work on a tutorial work won't interfere with other projects.

- When you've completed a tutorial, you can archive or delete the
  virtual environment directory if you no longer need it.

Follow these steps to setup a virtual environment for a tutorial:

- Ensure that you have Virtualenv installed --- see [Virtualenv
  Installation ->](https://virtualenv.pypa.io/en/stable/installation/)
- Create a virtual environment: ``virtualenv DIR``
- Active the environment: ``source DIR/bin/activate``
- Install Guild AI: ``pip install guildai``
- Install TensorFlow: ``pip install tensorflow`` or ``pip install
  tensorflow-gpu``
- Verify your setup: ``guild check``

Once you've activated your environment, Guild operations will apply to
that environment, including package installation and model runs.

Below are scripts that you can copy-and-paste to setup your
environments.

### Setup a virtual environment on Linux or Mac OS

``` command
echo -n "Virtualenv directory name: " && read DIR \
&& echo -n "Use GPU enabled TensorFlow: (y/n) " && read TF_GPU \
&& virtualenv $DIR \
&& cd $DIR && source bin/activate \
&& pip install guildai tensorflow${TF_GPU/y/-gpu} \
&& guild check
```
