navbar_item: yes

# Quick Start

## 1. Install Guild AI

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

## 2. Run Some Experiments

Create a file named `train.py` that contains this Python code:

``` python
import numpy as np

x = 0.1

loss = (np.sin(5 * x) * (1 - np.tanh(x ** 2))
        + np.random.randn() * 0.1)

print("loss: %f" % loss)
```

This script simulates a loss function. It accepts a hyperparameter `x`
and prints the resulting `loss`.

Run 10 experiments to search for values of `x` that minimize `loss`.

``` command
guild run train.py -m 10 x=[-2.0:2.0]
```

## 3. Compare Results

Compare run performance:

``` command
guild compare --min loss
```

Runs with lower loss appear at the top of the list. Use your arrow
keys to navigate. Press `1` to sort by the current column (ascending)
or `2` (descending).

Exit the Compare application by pressing `q`.

## 4. View in TensorBoard

[TensorBoard
->](https://www.tensorflow.org/guide/summaries_and_tensorboard) is an
open source analytics tool developed by Google that lets you visualize
run results. TensorBoard was originally designed to work with
TensorFlow but has become generalized to work with any machine
learning framework.

Guild AI provides built-in support for TensorBoard. For example, Guild
generates [HParam experiment data
->](https://www.tensorflow.org/tensorboard/r2/hyperparameter_tuning_with_hparams)
for your runs so you can compare results using [parallel coordinates
->](https://en.wikipedia.org/wiki/Parallel_coordinates) and [scatter
plot matrices
->](https://en.wikipedia.org/wiki/Scatter_plot#Scatter_plot_matrices).

To ensure that the **HParams** tab (shown below) is supported by
TensorBoard, install TensorFlow:

!!! note
    If TensorBoard 1.15 or greater is installed, you can skip
    this step. Use `tensorboard --version` to show the installed
    version.

``` command
pip install tensorflow
```

View the runs in TensorBoard:

``` command
guild tensorboard
```

Guild opens TensorBoard in your browser, which shows you the list of
runs. Click the **HParams** tab to compare run performance. You can
visualize the runs using parallel coordinates and scatter plot matrix
views by clicking the applicable tab.

![](/assets/img/tb-hparams.png)

^ Compare runs using parallel coordinates


## 4. Learn More
