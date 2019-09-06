# Hyperparameter Optimization

In [Quick Start](../start.md) you perform a *random search* for optimal
hyperparameters. In this section, you use two other methods: *grid
search* and *Bayesian optimiation*.

For review, here's the loss function used in `train.py`:

``` python
loss = (np.sin(5 * x) * (1 - np.tanh(x ** 2)) + np.random.randn() * 0.1)
```

The relationship between `x` and `loss` is plotted below. While the
function includes random noise, we can expect that optimal values for
`x` will be close to -0.3. In a real training scenario, we don't know
the optimal hyperparameter values and have to search for them.

![](/assets/img/bayesian-optimization.png)

^ Plot of `x` (horizontal axis) to `loss` (vertical axis) [^hparam-plot]

[^hparam-plot]: Image credit: [Bayesian optimization with skopt
    ->](https://scikit-optimize.github.io/notebooks/bayesian-optimization.html)

## Grid Search

*Grid search* --- also known as a *parameter sweep* --- tries manually
specified values.

For a grid search, you can run separate commands for each value of
`x`, but as you saw in [Quick Start](/start.md), Guild lets you run
multiple trials with a single command.

Run a grid search on thee values for `x`:

``` command
guild run train.py x=[-2,0,2]
```

Press `Enter` to confirm the operation.

From the plot above, you can expect the `loss` for these runs to all
be near 0.

## Bayesian Optimization

Large or continuous search spaces present an intractable problem for
exhaustive grid search.

*Bayesian optimization* methods use light weight probabilistic models
that consider results from previous runs in the search for optimal
hyperparameter values.

Run another ten trials, this time using a Bayesian optimizer:

``` command
guild run train.py -m 10 --optimizer bayesian
```

Press `Enter`
