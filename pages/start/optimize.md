# Hyperparameter Optimization

In [Quick Start](/start.md) you perform a *random search* for optimal
hyperparameters. In this section, you use two other methods: *grid
search* and *Bayesian optimiation*.

For review, this is the loss function used in the mock training script
`train.py`:

``` python
loss = (np.sin(5 * x) * (1 - np.tanh(x ** 2))
        + np.random.randn() * 0.1)
```

The relationship between `x` and `loss` is plotted below. While the
function includes random noise, we can expect that optimal values for
`x` will be close to -0.3.

![](/assets/img/bayesian-optimization.png)

^ Plot of `x` (horizontal axis) to `loss` (vertical axis) [^hparam-plot]

[^hparam-plot]: Image credit: [Bayesian optimization with skopt
    ->](https://scikit-optimize.github.io/notebooks/bayesian-optimization.html)

In a real training scenario, we don't know the optimal hyperparameter
values.
