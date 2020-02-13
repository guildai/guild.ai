tags: guide

# Workflow

[TOC]

## Overview

This guide relies on steps you complete in [Get
Started](/start/classifier.md).

In the [Get Started](/start/classifier.md), you add the classifier
`iris-svm` to your project. In this section, you add a new operation
to `iris-svm` to automate search steps.

## Add `search` Operation to `guild.yml`

In the `guild-start` directory, modify `guild.yml` by adding the
`search` operation below to the `iris-svn` model.

The final modified `guild.yml` should be:

``` yaml
- model: sample
  description: A sample model
  operations:
    train:
      description: Sample training script
      main: train
      flags-dest: globals
      flags-import:
        - noise
        - x
      output-scalars: '(\key): (\value)'

- model: iris-svm
  description: Iris classifier using a support vector machine (SVM)
  operations:
    train:
      description: Train SVM model on Iris data set
      main: plot_iris_exercise
      flags:
        kernel:
          description: SVM kernel type
          default: rbf
          choices: [linear, poly, rbf]
        test_split:
          description: Percentage of examples held out for test
          default: 0.2
        random_seed:
          description: Seed used for shuffling data
          default: 0
        degree:
          description: Degree of the poly kernel function
          default: 3
        gamma:
          description: Kernel coefficient for rbf and poly
          default: 10
      output-scalars:
        train_accuracy: 'Train accuracy: (\value)'
        test_accuracy: 'Test accuracy: (\value)'
    search:
      description: Generate runs to find optimal hyperparameters
      steps:
        - run: train
          flags:
            kernel: [linear, poly, rbf]
            gamma: [0.1, 0.5, 1, 5, 10, 25]
        - run: train
          flags:
            kernel: poly
            degree: [2, 3, 4]
```

^ `guild.yml` after adding `iris-svm:search` operation

The `search` operation defines two [steps](term:step). Each step runs
`iris-svm:train` with the specified flags. Guild executes these in
order when you run `search`.

!!! highlight
    Use `steps` to define higher-order operations, or
    [workflows](term:workflow).

Verify that the `search` operation is available:

``` command
guild ops
```

``` output
iris-svm:search  Generate runs to find optimal hyperparameters
iris-svm:train   Train SVM model on Iris data set
sample:train     Sample training script
```

If you don't see `iris-svm:search`, verify that `guild.yml` is the
same as above and that you're running the command from `guild-start`.

## Run Search

Run `iris-svm:search`:

``` command
guild run iris-svm:search
```

Press `Enter` to confirm.

Guild runs a series of trials as defined by the flags in `search`.

- 18 trials for the first step: six trials for each of the three
  `kernel` values (`linear`, `poly`, `rbf`), each with a different
  value for `gamma` (`0.1`, `0.5`, `1`, `5`, `10`, `25`)

- 3 trials for the second step: one for each of the specified `degree`
  values (`2`, `3`, `4`).

These values are manually selected to provide a first-pass coverage of
the hyperparameter search space. See

## View Results in TensorBoard

The trials take a few minutes to complete. As they run, you can open a
separate console and run the command below. Otherwise, wait for the
trials to finish.

!!! note
    If you open a new console, be sure to activate your
    environment before running Guild commands.

View the trial results in TensorBoard:

``` command
guild tensorboard --tab hparams
```

Guild starts TensorBoard and opens the **HPARAMS** tab, shown below.

![](/assets/img/workflow-hparams-grid.png)

^ Hyperparameter table view

Click **PARALLEL COORDINATES VIEW**. TensorBoard shows the results for
the `iris-svm:fit` runs, including **train_accuracy** and
**test_accuracy**.

![](/assets/img/tb-hparams2.png)

^ Parallel coordinates view

- Each run is represented by a line that crosses a vertical axis at
  the associated run scalar value.

- You can control what is displayed in the view using the forms on the
  left and top of the view.

- When you click a line, TensorBoard shows the associated run details
  below the coordinates plot.

- You can highlight runs associated with specific ranges along each
  axis. Click-and-drag your cursor on each vertical axis for the range
  you want to highlight.

Note the values along the **test_accuracy** vertical axis. Click the
run with the highest value for **test_accuracy** and note the
corresponding value in **train_accuracy**. The run is highly
overfit.

Click-and-drag along the **test_accuracy** axis to select a range
between 0.76 and 0.72 (see *Parallel coordinates view* above). This
range is where the model appears to perform the best without
overfitting.

The hyperparameters that appear to contribute most clearly to these
results:

- `degree` is 3
- `gamma` is 1.0 or less
- `random_seed` is 0

Random seed appears to be a factor in the results. This is a problem
that requires further investigation.

Each of the three `kernel` types produce optimal results. This
suggests that you might favor simpler kernels over more complex
kernels. Use the **time** axis to view optimal runs that train faster.

## Summary

In this section, you created a higher order operation called `search`
that automates a grid search. You studied the results using
TensorBoard's parallel coordinates view to draw tentative conclusions
about a model.

In the next section, you modify the model implementation to improve
results.
