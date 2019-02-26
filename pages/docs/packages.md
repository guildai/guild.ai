tags: advanced-concept

# Packages

[TOC]

A Guild AI _package_ is a container for [models](term:model) and
[resources](term:resource). Packages let developers easily publish
their work for users to discover. They let users easily find, install,
and use models. Packages are a central feature of Guild's support for
model collaboration, sharing and reuse.

## Create a package

To create a package, add a `package` top-level object to a project
[Guild file](term:guild-file).

Here's an example of a basic package definition in a file:

``` yaml
- package: my-package
  version: 1.0
```

To create a package distribution, use the [](cmd:package) command from
the project directory:

``` command
guild package
```

This generates a file `dist/NAME-VERSION-py2.py3-none-any.whl` that
can be shared with colleagues or [published to
PyPI](/docs/guides/publish-to-pypi/).

For a list of

For a list of package attributes, refer to [Packages
reference](/docs/reference/guild-file/#packages).

### Package name and version

Guild package names may be any valid Python package name. If you plan
to publish your package (e.g. by uploading to PyPI), pick a name that
is not already used by another package.

You may use a Python namespace in package names. For example, Guild AI
packages are in the `gpkg` namespace (i.e. they start with `gpkg.`).

Refer to [PEP 423 - Naming conventions and recipes related to
packaging ->](https://www.python.org/dev/peps/pep-0423/).

The package version is used to determine which version of a package is
more recent. Versions may also contain a *pre-release* designation to
indicate that it must be installed using the `--pre` option with `pip
install` or [guild install](cmd:install).

Refer to [PEP 440 - Version Identification and Dependency
Specification ->](https://www.python.org/dev/peps/pep-0440/) for
details on package versions.

### Other metadata

You can additional metadata for a package that helps users find and
use your package.

`description`
: The package description is a multi-line text value that provides a
single line summary with an optional detailed package
description. Here's an example:

<div class="dl">
<div class="row">
<div class="dt col col-sm-4 col-lg-3"></div>
<div class="dd col col-sm-8 col-lg-9">
<pre class="language-yaml" style="margin:0">
<code class="language-yaml">
package: my-package
description: >
  A sample package

  This package demonstrates a multi-line description. The
  first line, appearing above, is used as the package summary,
  or short description. The description as a whole is used as
  the package long description.
</code>
</pre>
</div>
</div>
</div>

`url`
: Link to more information about the package.

`author`
: Name of the package author or maintainer.

`author-email`
: Email address of the package author or maintainer.

`license`
: The license under which the packaged software and models is
  available. For help selecting an open source license for your
  project, see [Choose an open source license
  ->](https://choosealicense.com/). This value should correspond to
  the `LICENSE` file in your project.

`tags`
: A list of tags associated with the project. These are used to
  construct the package *keywords*. A tag should only contain
  alpha-numeric or underscore characters.

!!! note
    Guild always adds the `gpkg` keyword to packages it
    generated. This keyword must be present in order to designate the
    Python package as a Guild package.

### Data files

Guild automatically packages the following project files:

- Guild file - `guild.yml`
- License file - `LICENSE`, `LICENSE.*`
- README file - `README`, `README.*`
- Python source files - `*.py`

If your project requires additional files, you must specify them using
`data-files`, which is a list of paths or glob patterns relative to
the project root directory.

For example, if your project requires the file `labels.txt` and the
contents of the `sample-data` directory, both located in the project
root directory, you must specify it this way:

``` yaml
name: my-project
data-files:
  - labels.txt
  - sample-data/*
```

### Required packages

If your package requires other packages, you can specify those in the
package `requires` attribute. This value must be a list of valid
Python package names that may contain [requirement specifiers
->](https://pip.pypa.io/en/stable/reference/pip_install/#requirement-specifiers).

The following package definition illustrates the use of `requires`:

``` yaml
- package: my-package
  version: 1.0
  requires:
    - matplotlib
    - Pillow
    - keras==2.2.4
    - scipy>=1.1.0
```

### Using `setuptools` to create a package

As an alternative to Guild's packaging facility, you may use Python's
standard method of creating packages, which uses typically uses
`setup.py` and the `setuptools` module.

For more information, see [Packaging Python Projects
->](https://packaging.python.org/tutorials/packaging-projects/).

If you use `setuptools` to generate a Python package rather than
[guild package](cmd:package), you must make two changes to your
`setup.py` file to support Guild.

First, you must include ``gpkg`` as a package keyword. This is
specified using the setup `keywords` argument:

``` python
import setuptools

setuptools.setup(
    name="example_pkg",
    version="0.0.1",
    keywords="example gpkg"
    ...
)
```

Guild uses the ``gpkg`` keyword to identify Guild packages for the
[](cmd:search) and [packages list](cmd:packages-list) commands.

Second, you must add a `guild.model:PackageModel` entry to the
`guild.models` entry point for each model the package contains.

For example, if your package contains the models ``resnet-50`` and
``resnet-101``, you would include those models using the setup
`entry_points` argument as follows:

``` python
import setuptools

setuptools.setup(
    name="example_pkg",
    version="0.0.1",
    entry_points={
        "guild.models": [
            "resnet-50 = guild.model:PackageModel",
            "resnet-101 = guild.model:PackageModel",
        ]
    }
```

Guild uses the `guild.models` entry point to discover installed
models.

For more information on entry points, see [Entry points specification
->](https://packaging.python.org/specifications/entry-points/).

## Publish a package

You can upload a package to [PyPI ->](https://pypi.org/) when running
the [](cmd:package) command by specifying the `--upload` option. You
may alternatively upload to [TestPyPI ->](https://test.pypi.org/)
using `--upload-test`.

Guild supports the following additional upload parameters:

- Repository URL
- PyPI user name
- PyPI user password
- GPG identity used to sign the published package

For more information, see [](cmd:package) command.

In order to publish to PyPI or TestPyPI, you must first create an
account on the respective site.

- [Create an account on PyPI for official packages
  ->](https://pypi.org/account/register/)
- [Create an account on TestPyPI for testing
  ->](https://test.pypi.org/account/register/)

Once you have an account, specify the applicable user name and
password when uploading your Guild package.

## Find packages

You can find Guild packages several ways:

- Use [guild search](cmd:search)
- Use [pip search ->](https://pip.pypa.io/en/stable/reference/pip_search/)
- Search using [PyPI ->](https://pypi.org/)
- Browse [Guild AI packages](alias:packages)

`guild search` limits search results to Guild packages (i.e. packages
that have the ``gpkg`` keyword), while `pip search` does not.

The following command, for example, searches for Guild packages that
contain ``resnet-50`` in their description or tags/keywords:

``` command
guild search resnet-50
```

## Install packages

Install packages using either [guild install](cmd:install) or [pip
->](https://pip.pypa.io/en/stable/reference/pip_install/).

Guild's `install` command uses a slightly different set of options
than pip's `install` command. Refer to [](cmd:install) for details.

Packages may be specified as PyPI project names, including
[requirement specifiers
->](https://pip.pypa.io/en/stable/reference/pip_install/#requirement-specifiers),
or as paths to package distributions (e.g. wheels generated by [guild
package](cmd:package)).

You can find package names using [](cmd:search) (see [Find
packages](#find-packages) above) or alternatively browse
[](alias:packages).

## List installed packages

List all installed Guild AI packages using [](cmd:packages).

You can list packages matching one or more terms using [packages
list](cmd:packages-list):

For example, to list installed packages containing `magenta`, run:

``` command
guild packages list magenta
```

## Uninstall packages

Uninstall packages using [guild uninstall](cmd:uninstall) or [pip
->](https://pip.pypa.io/en/stable/reference/pip_uninstall/).

Uninstalling a package will not remove dependencies that were
installed when the package was installed. You must uninstall these
packages separately.
