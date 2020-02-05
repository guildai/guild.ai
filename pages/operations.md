tags: concept

# Operations

[TOC]

## Overview

Operations are used to start [runs](term:run). Operations are
specified when calling [run](cmd:run) in the format:

``` command
guild run OPERATION
```

Operations are defind in [Guild files](term:guildfile).

## Python Based Operations

Python based operations are defined in `*.py` files and must be
specified using their *module name* as the `main` operation attribute
in a Guild file.

``` yaml
train:
  main: train_logreg
```

^ Guild file (`guild.yml`) defining operation `train`, implemented in
Python module `train_logreg`.

!!! note
    Do not include the `.py` suffix when specifying `main`. The
    value refers to the module name, not the file name.

Guild loads such modules as `__main__` in the same way that Python
itself loads them when run using ``python -m <module name>`` from the
command line.

You may perform operation tasks directly in the module like this:

``` python
from models import logreg

logreg.train("data.csv")
```

^ Sample Python module --- always executes task when loaded

Alternatively, check the module name and only perform operation tasks
if it `__main__`.

``` python
from models import logref

def main():
    logreg.train("data.csv")

if __name__ == "__main__":
    main()
```

^ Sample Python module --- execute task only when module is loaded as
  `__main__`

## Other Language Operations
