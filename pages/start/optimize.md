tags: start

# Optimize a Model

In [the previous section](/start.md) you ran a *random search* to
find optimal values for `x`. In this section, you use two other
methods: *grid search* and *Bayesian optimiation*.

For review, here's the loss function used in `train.py`:

``` python
loss = (np.sin(5 * x) * (1 - np.tanh(x ** 2)) + np.random.randn() * 0.1)
```

The relationship between `x` and `loss` is plotted below. We know that
optimal values for `x` will be around -0.3. In a real scenario, we
don't know the optimal hyperparameter values. We have to search for
them.

![](/assets/img/bayesian-optimization.png)

^ Plot of `x` (horizontal axis) to `loss` (vertical axis) [^hparam-plot]

[^hparam-plot]: Image credit: [Bayesian optimization with skopt
    ->](https://scikit-optimize.github.io/notebooks/bayesian-optimization.html)

## Grid Search

[Grid search](term:grid-search) --- also called a *parameter sweep*
--- tries specific values.

To perform a grid search, you could run separate commands for each
value of `x`. However, as you saw in [the previous
section](/start.md), Guild lets you run multiple trials with a
single command.

Run a search over three values of `x`:

``` command
guild run train.py x=[-2,0,2]
```

``` output
You are about to run train.py in a batch
  x: [-2, 0, 2]
Continue? (Y/n)
```

Press `Enter` to confirm.

Guild generates three runs, one for each specified value of `x`.

From the plot above, we expect the `loss` for these runs to be
approximately 0, which is not very close to the minimum.

## Bayesian Optimization

*Bayesian optimization* methods use light weight probabilistic models
that use results from previous runs to suggest promising
hyperparameter values.

Run ten trials using a Bayesian optimizer with gaussian processes:

``` command
guild run train.py --max-trials 10 --optimizer gp x=[-2.0:2.0]
```

``` output
You are about to run train.py with 'gp' optimizer (max 10 trials)
  x: [-2.0:2.0]
Continue? (Y/n)
```

Press `Enter` to confirm.

Guild generates ten trials. The optimizer uses past experience to
explore areas of the search space that have a higher probability of
minimizing `loss`.

With some luck (results are non-deterministic due to random effects),
the search will spend more time exploring values of `x` close to the
optimal value -0.3.

!!! highlight
    Guild uses a standard interface to run scripts using
    variety of methods: *single runs*, *grid search*, *random search*,
    and *Bayesian optimization*.

## Show the Best Runs

Show the five runs with the lowest values for `loss`:

``` command
guild compare --top 5 --min loss --table
```

The `--table` option tells Guild to print the results to standard
output rather than run interactively.

You can also save the comparison data as a CSV file.

``` command
guild compare --csv results.csv
```

## Next Steps

In this section, you ran a grid search and performed Bayesian
optimization to find optimal values of `x`.

In the next section, you learn about more about runs.
