# Model scripts

Model scripts are standard Python modules that can be run from the
command line. They implement model [operations](term:operation).

Scripts are run as follows:

``` command
python SCRIPT [ARGUMENTS]
```

Guild operations wrap these scripts and associated arguments. Here's
an example of a model with a `train` operation that executed a Python
module named `train_model`:

``` yaml
name: my-model
operations:
  train:
    cmd: train_model --rundir .
```

Here's what `train_model.py` might look like:

``` python
import datasets
import models
import util

def train(rundir):
    imagenet = datasets.ImageNet()
    model = models.ResNet()
    model.train(imagenet, rundir)

if __name__ == "__main__":
    train(util.parse_args())
```

This simple example illustrates how model scripts typically work:

- Runnable from the command line
- Implement `train` and other operations as Python functions
- Parse command line arguments and use to parameterize operations