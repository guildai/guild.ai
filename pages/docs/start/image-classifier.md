tags: get-started

# Train an Image Classifier

In this guide, we train an image classifier on the Fashion-MNIST data
set.

![Fashion-MNIST](/assets/img/fashion-mnist.png)

[TOC]

## Requirements

{!start-requirements.md!}

## An image classifier trainingscript

In this step, we create a script named `fashion_mnist_mlp.py`, which
is an image classifier training script adapted from the Keras
examples. [^example-src]

[^example-src]: The training script for the image classifier is
    adapted from [keras/examples/mnist_mlp.py on GitHub
    ->](https://github.com/keras-team/keras/blob/master/examples/mnist_mlp.py)

The training script we create in this step doesn't actually train
anything, but instead simulates the training process of accepting
hyperparameters as inputs and generating a *[loss
->](https://en.wikipedia.org/wiki/Loss_function)*.

If you haven't done so already, create a new directory for the
project:

``` command
mkdir guild-start
```

Create a file named `fasion_mnist_mlp.py`, located in the
`guild-start` directory:

``` python

```

^ guild-start/train.py

This mock script simulates a training operation:

- It has two mock hyperparameters: *x* and *noise*
- It calculates a mock *loss* using a "noisy" function [^noisy-credit]

[^noisy-credit]: Credit for "noisy" function: [Gilles Louppe, Manoj
    Kumar
    ->](https://scikit-optimize.github.io/notebooks/bayesian-optimization.html)

Verify that your project structure is:

<div class="file-tree">
<ul>
<li class="is-folder open">guild-start
 <ul>
 <li class="is-file">train.py</li>
 </ul>
</li>
</ul>
</div>


## Summary

## Next Steps

{!start-tensorboard.md!}

{!start-diff.md!}

{!start-reproducibility.md!}

{!start-backup-restore.md!}

{!start-remote-train.md!}
