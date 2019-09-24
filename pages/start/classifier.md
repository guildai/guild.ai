# Create a Classifier

In the previous sections, you create a [Guild file](ref:guildfile) in
the `guild-start` project directory. In this section, you extend your
project by adding a classifier.

## Download Classifier Script

Download the file
[`plot_iris_exercise.py`](ext:https://raw.githubusercontent.com/guildai/examples/master/iris-svm/plot_iris_exercise.py)
and save it to the `guild-start` directory.

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

`plot_iris_exercise.py` is adapted from the [scikit-learn SVM Exercise
->](https://scikit-learn.org/stable/auto_examples/exercises/plot_iris_exercise.html).

## Add `iris-svm` Model to guild.yml

In the `guild-start` directory, modify `guild.yml` by adding the
`iris-svn` model, shown below.

The final modified `guild.yml` should be:

``` yaml
- model: sample
  description: A sample (mock) model
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
          choices: [linear, poly, rbf, sigmoid]
        test_split:
          description: Percentage of examples held out for test
          default: 0.2
        random_seed:
          description: Seed used for shuffling data
          default: 0
        degree:
          description: Degree of the polynomial (poly) kernel function
          default: 3
        gamma:
          description: Kernel coefficient for rbf, poly, and sigmoid
          default: 10
      output-scalars:
        train_accuraty: 'Train accuracy: (\value)'
        test_accuracy: 'Test accuracy: (\value)'

```

^ `guild.yml` after adding `iris-svm` model

Verify that the `fit` operation is available:

``` command
guild ops
```

``` output
iris-svm:fit  Fit SVM model
sample:train  Generate a sample loss
```

If you don't see `iris-svm:fit` in the list above, verify that your
`guild.yml` is the same as above and that you're running the command
from `guild-start`.

## Fit the Classifier

Run the `fit` operation on the `iris-svm` model:

``` command
guild run iris-svm:fit kernel=[linear,poly,rbf,sigmoid]
```

``` output
You are about to run iris-svm:fit
  degree: 3
  gamma: 10
  kernel: [linear, poly, rbf, sigmoid]
  random_seed: 0
  test_split: 0.2
Continue? (Y/n)
```

Press `Enter` to confirm.

Guild runs the script `plot_iris_exercise.py`.

The `iris-svm` model introduces
