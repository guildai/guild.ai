tags: tutorial, tools

# Working with Virtualenv

[TOC]

[Virtualenv->](https://virtualenv.pypa.io) is a tool that creates
isolated environments for running Python applications. A virtual
environment is contained in a single file system directory and does
not rely on Python packages installed at the system level.

You are free to create as many virtual environments as you need. Each
environment is independent of the others and may use different
software versions, including different versions of Python.

Guild AI is designed to work with or without a virtual environment ---
the choice is yours.

## When to use a virtual environment

There are a number of reasons to use virtual environments:

- Isolate Guild AI and is library dependencies
- Manage different versions of Guild AI
- Manage versions of Python and TensorFlow used by Guild
- Maintain separate model and run repositories

There are some downsides to using virtual environments:

- Each environment requires its own set of installed packages, which
  may be excessively time consuming for short-lived environments
- You must remember to activate the environment to use it
- You may accidentally use the wrong environment

If you don't need to isolate Guild and its dependencies or to manage
different software versions, the added complexity of Virtualenv may be
more hindrance than help.

## Installing Virtualenv

Refer to [https://virtualenv.pypa.io/installation/
->](https://virtualenv.pypa.io/en/stable/installation/) for details on
installing Virtualenv.

Generally speaking though, you simply run:

``` shell
pip install virtualenv
```

If you need to install as a privileged user, run:

``` shell
sudo pip install virtualenv
```

## Creating a virtual environment

Once Virtualenv is installed, it's easy to create new
environments. Simply run:

``` shell
virtualenv DIRECTORY
```

where `DIRECTORY` is the file system directory that will contain the
environment.

You can specify the Python version to use in environment using the
``-p`` option. For example, to indicate that Python 2 should be used,
run:

``` shell
virtualenv -p python2 DIRECTORY
```

Users who make extensive use of virtual environments typically create
them in a common parent directory. Here's a theoretical directory
structure that could be used to manage different configurations of
Guild:

<div class="file-tree">
<ul>
<li class="is-folder open">Environments <i>Directory containing the virtual environments</i>
 <ul>
 <li class="is-folder">guild-python2<i>Guild installed with Python 2</i></li>
 <li class="is-folder">guild-python3<i>Guild installed with Python 3</i></li>
 <li class="is-folder">guild-tensorflow-gpu<i>Guild with the GPU version of TensorFlow</i></li>
 <li class="is-folder">gans<i>Environment for work on GAN models</i></li>
</ul>
</li>
</ul>
</div>

## Virtual environments and `GUILD_HOME`

Guild manages [packages](term:package), [runs](term:run), and
[indexes](term:index) under a single directory named
`GUILD_HOME`. The default value of `GUILD_HOME` depends how Guild is
run:

- If Guild is run within a virtual environment, the value is
  ``$VIRTUAL_ENV/.guild``

- If Guild is not run within a virtual environment, the value is
  ``$HOME/.guild``

This behavior is designed to completely isolate Guild within a virtual
environment. However, you may want to share packages and runs across
environments. You can do this by explicitly setting the `GUILD_HOME`
environment variable to the shared location. This should be done in
the `activate` script of the environment.

To share a common `GUILD_HOME` across environments, modify
``$VIRTUAL_ENV/bin/active`` for each environment and add the following
line at the end of the file:

```
export GUILD_HOME=~/.guild
```

If you want to use a different location, change ``~/.guild``
accordingly.

## Using a virtual environment

You must activate a virtual environment to use it. This is done by
*sourcing* the script as follows:

``` shell
source $VIRTUAL_ENV/bin/activate
```

This will configure your shell environment to use the Python runtime
and associated packages contained in the environment. It will also set
`GUILD_HOME` if you modified `activate` as per the instructions above.

For more information, refer to [Virtualenv User Guide: activate
script](https://virtualenv.pypa.io/en/stable/userguide/#activate-script).

Once activated, run Guild commands as you normally would.

You can verify Guild details by running ``guild check``, which will
display `guild_home` and `guild_install_location` settings, letting
you confirm that Guild is isolated as expected.

## Summary

In this tutorial we reviewed Virtualenv and how it can be used to
isolate Guild on a system. We described how `GUILD_HOME` can be shared
across virtual environments by explicitly setting an environment
variable in the `activate` script.
