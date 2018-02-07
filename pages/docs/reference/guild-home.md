pagenav_title: Guild home reference
tags: reference

# Guild home

[TOC]

Guild home is a directory that Guild AI uses to store various files.

Every Guild command is associated with a Guild home. If Guild home
does not exist, Guild will automatically create it.

By default Guild home is ``$HOME/.guild`` where `$HOME` resolves to
the user's home directory.

However, if a Guild command is run within a virtual environment,
[^virtual-env] the default Guild home is ``$VIRTUAL_ENV/.guild`` where
`$VIRTUAL_ENV` is the virtual environment directory.

[^virtual-env]:
    If the environment variable `VIRTUAL_ENV` is defined, Guild
    assumes it's running within a virtual environment. This variable
    is set when you run ``source DIR/bin/activate`` to activate a
    virtual environment in `DIR`.

## Runs

## Resource cache

## Runs index
