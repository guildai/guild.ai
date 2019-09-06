navbar_item: yes

# Quick Start

## Install Guild AI

In an activated virtual environment (e.g. [virtualenv
->](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
or [conda
->](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html))
run:

``` command
pip install guildai
```

When Guild is installed, check the environment:

``` command
guild check
```

Refer to [Install Guild AI](install.md) for detailed install
instructions or [ask for help](alias:slack).

## Create a Mock Training Script

Create a file named `train.py` that contains this Python code:

``` python
import numpy as np

x = 0.1

loss = (np.sin(5 * x) * (1 - np.tanh(x ** 2)) + np.random.randn() * 0.1)

print("loss: %f" % loss)
```

This script simulates a loss function. It accepts a hyperparameter `x`
and prints the resulting `loss`.

## Run Some Experiments

Run 10 experiments to calculate loss for randomly generated values of
`x` between -2.0 and 2.0:

``` command
guild run train.py -m 10 x=[-2.0:2.0]
```

Press `Enter` to confirm the operation.

!!! tip
    Guild *magic* to set values of `x`. This is convenient for
    simple scripts like `train.py`. Guild also supports non-magic
    interfaces such as command line arguments. For more information,
    see [Magic](kb/magic.md).

## Compare Runs

View the experiment results:

``` command
guild compare --min loss
```

Runs with lower `loss` appear at the top of the list. Use your arrow
keys to navigate. Press `1` to sort by the current column (ascending)
or `2` (descending).

Exit the Compare application by pressing `q`.

## View Runs in TensorBoard

To visualize the relationship between the hyperparameter `x` and
`loss`, use TensorBoard's [HParam plugin
->](https://www.tensorflow.org/tensorboard/r2/hyperparameter_tuning_with_hparams).

First, ensure that the plugin is supported by TensorBoard by
installing TensorFlow:

!!! note
    This step is only required if you have TensorBoard 1.14 or
    lower installed. If you have TensorBoard 1.15 or higher, you can
    skip this step. Use `tensorboard --version` to show the installed
    version.

``` command
pip install tensorflow
```

View the runs in TensorBoard:

``` command
guild tensorboard
```

Guild opens TensorBoard in your browser. Click the **HParams** tab to
compare run performance. You can visualize the runs using parallel
coordinates and scatter plot matrix views by clicking the applicable
tab.

![](/assets/img/tb-hparams.png)

^ Compare runs using parallel coordinates

## Summary

With one Guild command, you generated serveral experiments for a mock
training script. Each run used a randomly chosen value for the
hyperparameter `x` to generate `loss`. This process is know as a
*random search*. Guild also supports *grid search* and *Bayesian
optimization* as well as individual runs.

You compared the runs in using two of Guild's built-in analytics
tools:

- Guild Compare
- TensorBoard

These steps highlight two of Guild's core features:

- Run and capture machine learning experiments
- Support analysis of results
