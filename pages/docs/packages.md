tags: concepts

# Packages

[TOC]

A Guild AI _package_ is a container for [models](term:model) and
[resources](term:resource). Packages let developers easily publish
their work for users to discover. They let users easily find, install,
and use models. Packages are a central feature of Guild's support for
model collaboration, sharing and reuse.

## Create a package

To createa a package, add a `package` top-level object to a project
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

## Find packages

Guild packages are standard Python packages that can be searched using
`pip search`.

Guild provides a [](cmd:search) command that searches for packages
created using [guild package](cmd:package).

For example, to search for Guild packages containing ``resnet-50`` in
their description or keywords, run:

``` command
guild search resnet-50
```

## Install packages

Packages can be installed using pip or Guild.

To use Guild to install a package, use the [](cmd:install) command:

``` command
guild install PACKAGE
```

You can find package names using [](cmd:search) (see [Find
packages](#find-packages) above).

You can also browse [](alias:packages).

## List installed packages

To list installed Guild AI packages, run:

``` command
guild packages
```

You can list specific packages using [packages
list](cmd:packages-list):

``` command
guild packages list FILTER
```

For example, to list installed packages containing `magenta`, run:

``` command
guild packages list magenta
```

## Uninstall packages

Uninstall a package by running:

``` command
guild uninstall PACKAGE
```

Guild will prompt you before deleting package files.

If you'd prefer to skip the prompt, use the `-y` option:

``` command
guild uninstall PACKAGE -y
```

## Create package

Creating packages is an advanced topic that is not currently covered
in this documentation.

You may however review the package definitions at
[https://github.com/guildai/packages
->](https://github.com/guildai/packages) for examples of packages.

If you need help creating a package, drop us a line at
[niceperson@guild.ai](mailto:niceperson@guild.ai) and we'll be happy
to help!
