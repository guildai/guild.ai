tags: concepts

# Packages

[TOC]

A Guild AI _package_ is a container for [models](term:model) and
[resources](term:resource). Packages let developers easily publish
their work for users to discover. They let users easily find, install,
and use models. Packages are the central feature of Guild's support
for model collaboration, sharing and reuse.

## Find packages

You can find Guild packages in various ways:

- Visit Guild's [model repository](/models/)
- Search for a model using the [](cmd:search) command

For example, to find models that support the ImageNet dataset, simply run:

``` command
guild search imagenet
```

New models are being published all the time so if you don't find what
you're looking for, let the community know by [submitting a request on
Guild's issue tracker](alias:guild-issues).

It's also easy to create and publish your own models.

## Install packages

Install a package by running:

``` command
guild install PACKAGE
```

You can find package names using [](cmd:search) (see [Find
packages](#find-packages) above).

You can also browse [](alias:guild-models).

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
