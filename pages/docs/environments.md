tags: concepts

# Environments

A Guild environment is a Python virtual environment used to isolate
models and runs. Each environment is a separate file system directory
that contains its own set of runs and Python packages.

Environments generally correspond to a project workflow. We recommend
using them for your work with Guild as they provide a number of
benefits:

- Restrict models to those you're interested in working with
- Isolate runs associated with a particular project or worflow
- Minimize software package version conflicts and broken dependencies

## Create a Guild environment

Use [guild init](cmd:init) to create a new Guild environment:

``` command
guild init
```

By default, Guild create an environment in a directory named `env` in
the current working directory. You can optionally specify a different
environment:

``` command
guild init ENVIRONMENT-DIR
```

## Activate a Guild environment

Once created, a Guild environment must be *activated* to be
used. Activating a Guild environment changes you shell environment to
ensure the following are environment specific:

- Python runtime used for commands
- Available Python packages

To activate an environment `env` in the current directory, run:

``` command
source guild-env
```

To activate an environment located somewhere else, run:

``` command
source guild-env ENVIRONMENT-DIR
```

## Environment packages

Guild environments start with a minimal number of installed Python
packages. They do not use system or user site packages.

Initial packages include:

`pip`, `setuptools`, `wheel`
: Core Python packages needed to install additional packages.

`guildai`
: Guild AI is always installed in new environments.

`tensorflow` or `tensorflow-gpu`
: TensorFlow is installed by default unless `--no-tensorflow` is
  specified for the `init` command. See [TensorFlow and
  environments](#tensorflow-and-environments) for more information.

Guild installs additional packages if any of the following are true:

- You include `-r, --requirement` options with `init`. In this case,
  Guild installs the package requirements listed in each requirement
  file.

- The environment parent directory contains `requirements.txt`. In
  this case, `requirements.txt` is implicitly included in the list of
  requirement files Guild uses for installing packages.

- The environment parent directory contains `guild.yml` and that file
  contains a `package` with a list of required packages. In this case,
  Guild installs each of the required packages defined in `guild.yml.`
  It also recursively installs required packages defined in inherited
  Guild files---i.e. Guild files containing model or config
  definitions that are extended in the initial Guild file.

You can prevent Guild from installing required packages by specifying
`--no-reqs`.

## TensorFlow and environments

By default, TensorFlow is installed in new environments. Guild detects
whether the system supports GPU acceleration and installs the
corresponding Python package.

The following options can be used to change this behavior:

`--no-tensorflow`
: Do not install TensorFlow in the environment. Note that you will
  need to install TensorFlow yourself before running TensorFlow
  operations.

`--gpu`
: Install the `tensorflow-gpu` package even if the system does not
  support GPU acceleration.

`--no-gpu`
: Install the `tensorflow` package even if the system supports GPU
  acceleration.

## Additional Python paths

If you are working with source based Python packages, you can include
the path to each project using `-p, --path` option when running
`init`.

For example, let's suppose you are using an environment to develop a
model in a project located in `~/my-project` and that model requires
Python modules or Guild config defined in another project
`~/required-project`. You can use `-p` to add the path to the required
project this way:

``` command
guild init ~/my-project -p ~/required-project
```

## Environment labels

When activated, an environment changes the command prompt to display
an environment *label*. By default, Guild uses the name of the
environment parent directory. In most cases this is sufficient to
identify the environment when active.

If you want to specify a different level, use the `-l, --label` option
when running `init`.

## Resource caches

By default, Guild environments share the user-level resource cache
`~/.guild/cache/resources`. This ensures that resources downloaded
within the activated environment are available outside the
environment.

You can use a local resource cache by specifying
`--local-resource-cache` when running `init`. This ensures that
resources downloaded within the activated environment are local to
that environment.

!!! note
    Local resource caches can be used to completely isolate an
    environment within a system at the cost of both potentially
    re-downloading resource files as well as duplicating local file
    storage.

For details on resource cache directories, see [Guild home
reference](/docs/reference/guild-home/).

## Environments and project workflow

We recommend using Guild environments whenever running operations,
apart from temporary experimentation. Environments isolate both
installed packages and runs, ensuring that work in one project doesn't
interfere with other projects.

We recommend the following project workflow conventions:

- Create a default environment in each Guild project directory:

``` command
cd $PROJECT_DIR
guild init
```

- When working with a project, change to the directory and activate
  the environment:

``` command
cd $PROJECT_DIR
source guild-env
```

- Include `env` or `/env` in your project `.gitignore` file, if
  applicable.

- If you are certain you no longer need runs associated with a project
  (e.g. the runs were used for development only) you can delete the
  environment by deleting the project `env` directory:

``` command
rm -rf $PROJECT_DIR/env
```

!!! important
    Deleting an environment will delete all runs generated
    while that environment was activated. Take care when deleting
    Guild environments.
