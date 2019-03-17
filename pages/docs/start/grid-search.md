tags: get-started

# Grid Search

## Requirements

{!start-requirements-2.md!}

## Grid Search

Grid search --- also referred to as a *parameter sweep* --- is a form
of hyperparameter tuning that uses exhaustive search over a manually
defined set of hyperparameter values.

Grid search in Guild is easy --- simply provide a list of values to
use for any given flag. If you specify lists for multiple flags, Guild
runs trials for each possible flag value combination.

To illustrate, change to the `simple-project` directory (if you
haven't created `simple-project` yet, follow the steps in
[](alias:quick-start) first):

``` command
cd simple-project
```

Run a grid search over five values for *x*:

``` command
guild run train.py x=[-0.5,-0.4,-0.3,-0.2,-0.1]
```

Press `Enter` to confirm the operation.

Guild runs `train.py` for each of the specified values.

Compare the last five runs:

``` command
guild compare 1:5 --table --min loss
```

This command tells Guild to show runs from index `1` to index `5` (the
last five runs) sorted in ascending order by `loss`. Note that the
loss is lowest where `x=-0.3`. (For background on the function
generating *loss*, see [](alias:quick-start).)

Next, run a search that includes two values for *x* and two values for
*noise*:

``` command
guild run x=[-0.3,-0.35] noise=[0.0,0.1]
```

Press

## Summary

## Next Steps

{!start-random-search.md!}

{!start-manage-runs.md!}

{!start-image-classifier.md!}
