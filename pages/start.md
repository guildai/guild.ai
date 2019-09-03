navbar_item: yes

# Quick Start

<div class="row" style="margin-top:-20px"></div>

<div class="col col-lg-10" markdown="1">
## 1. Install Guild AI

In an activated virtual environment (`virtualenv` or `conda`) run:

``` command
pip install guildai
```

Alternatively, from outside an activated environment:

``` command
pip install guildai --user
```

When Guild is installed, check the environment:

``` command
guild check
```

If everything checks out, you're ready to run experiments! Otherwise
refer to [Install Guild AI](install.md) for more information or [ask
for help](alias:slack).

</div>

<div class="row"></div>

<div class="col col-lg-10" markdown="1">
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
</div>

<div class="row"></div>

<div class="col col-lg-10" markdown="1">
## 3. Compare Results

To compare run performance:

``` command
guild compare --min loss
```

The best results (i.e. the lowest loss) appear at the top of the
list. Use your arrow keys to navigate. Press `1` to sort by the
current column (ascending) or `2` (descending).

Exit by pressing `q`.

View results in TensorBoard:

``` command
guild tensorboard
```

</div>

<div class="row"></div>

<div class="col col-lg-10" markdown="1">
## 4. Learn More

</div>
