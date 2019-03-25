tags: core-concept

# Dependencies

A *dependency* is a set of files required by an operation. Here's a
simple example:

``` yaml
train:
  requires:
    - data.txt
```

^ Sample Guild file (`guild.yml`)

This operation runs the `train` main module (i.e. `train.py`) but
requires the file `data.txt` to do so.

Here's what `train.py` might look like:

``` python
import model

# data.txt assumed to be available in cwd
data = open("data.txt").read()

model.train(data)
```

Here's what the project structure might look like, including the
