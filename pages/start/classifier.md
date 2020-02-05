tags: start

# Create a Classifier

In the previous sections, you create a [Guild file](ref:guildfile) in
the `guild-start` project directory. In this section, you enhance the
project by adding a classifier.

## Download Classifier Script

Download the file
[`plot_iris_exercise.py`](ext:https://raw.githubusercontent.com/guildai/examples/master/iris-svm/plot_iris_exercise.py)
and save it to the `guild-start` directory.

The script trains a model on the Iris benchmark data set. [^iris-script]

[^iris-script]: Adapted from [scikit-learn SVM Exercise
->](https://scikit-learn.org/stable/auto_examples/exercises/plot_iris_exercise.html)

The `guild-start` directory should look like this:

<div class="file-tree">
<ul>
<li class="is-folder open">guild-start
 <ul>
 <li class="is-file">guild.yml</li>
 <li class="is-file">plot_iris_exercise.py</li>
 <li class="is-file">train.yml</li>
 </ul>
</li>
</ul>
</div>

## Add `iris-svm` Model to guild.yml

In the `guild-start` directory, modify `guild.yml` by adding the
`iris-svn` model below.

The final modified `guild.yml` should be:

``` yaml
- model: sample
  description: A sample model
  operations:
    train:
      description: Generate a sample loss

- model: iris-svm
  description: Iris classifier using a SVM
  operations:
    fit:
      description: Fit SVM model
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

```

^ `guild.yml` after adding `iris-svm` model

The `iris-svm` model defines a single `fit` operation, which
introduces three new attributes:

`main`
: Python [main module](term:main-mod) to run for the operation

`flags`
: [Operation flags](term:flags), which provide additional information
  about flag imported from `plot_iris_exercise`

    Guild gives you total control over how flags are imported
    including the ability to disable flag imports altogether. See
    [Flags](ref:flags) for more information.

`output-scalars`
: Two [output scalars](term:output-scalars), which tell Guild to log
  values that match specified patterns in the run output

Verify that the `fit` operation is available:

``` command
guild ops
```

``` output
iris-svm:fit  Fit SVM model
sample:train  Generate a sample loss
```

If you don't see `iris-svm:fit` in the list above, check that your
`guild.yml` is the same as above and that you're running the command
from `guild-start`.

## Install Required Libraries

The script `plot_iris_exercise.py` requires two additional libraries:

- scikit-learn (already installed)
- Matplotlib

Install Matplotlib:

``` command
pip install matplotlib
```

Refer to [Installing Matplotlib
->](https://matplotlib.org/3.1.1/users/installing.html) for additional
help.

## Fit the Classifier

Run the `fit` operation on the `iris-svm` model:

``` command
guild run iris-svm:fit kernel=[linear,poly,rbf] random_seed=[1,2]
```

``` output
You are about to run iris-svm:fit
  degree: 3
  gamma: 10
  kernel: [linear, poly, rbf]
  random_seed: [1,2]
  test_split: 0.2
Continue? (Y/n)
```

Press `Enter` to confirm.

Guild runs the script `plot_iris_exercise.py` six times, once for each
unique combination of flag values.

## Compare Runs

Use [compare](cmd:compare) to list results, ordered by `test_accuracy`:

``` command
guild compare --max test_accuracy
```

Use the arrow keys to scroll to the right and view the values for
`test_accuracy`. Runs with higher accuracies are listed first.

## Next Steps

In this section you added a new model `iris-svm` to your project. The
model defines a single `fit` operation, which runs the script
`plot_iris_exercise.py` to fit a support vector machine to the Iris
data set. You ran a preliminary grid search

In the next section, you add a new operation to `iris-svm` that
automates a more complete search.
