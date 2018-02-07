tags: tutorial, popular, intro

# Transfer learning with ImageNet

In this tutorial we'll use a state-of-the-art image classifier that's
been pretrained on [ImageNet ->](http://www.image-net.org/) to
acclerate training with our own images.

This process is referred to as *fine tuning* and uses a pattern in
machine learning called *transfer learning*. It's a technique that can
produce accurate models with smaller datasets.

## Requirements

This tutorial assumes the following:

- Guild AI is [installed and verified](/install)
- Your [virtual environment is activated](alias:virtualenv-activate)
  (if applicable)
- You have a working Internet connection

While not required, we recommend using a dedicated virtual environment
for this tutorial. To setup your environment, see
[](alias:tut-env-setup).

## Install `slim.resnet`

We'll use models from the `slim.reset` package, which support
transfer learning via the `fine-tune` operation.

Install `slim.resnet` by running:

``` command
guild install slim.resnet
```

When the package is installed, list the available resnet models:

``` command
guild models resnet
```

Here's the output:

``` output
slim.resnet/slim-resnet-101     ResNet-101 classifier for TF-Slim
slim.resnet/slim-resnet-152     ResNet-1152 classifier for TF-Slim
slim.resnet/slim-resnet-200     ResNet-200 classifier for TF-Slim
slim.resnet/slim-resnet-50      ResNet-50 classifier for TF-Slim
slim.resnet/slim-resnet-v2-101  ResNet-v2-101 classifier for TF-Slim
slim.resnet/slim-resnet-v2-152  ResNet-v2-152 classifier for TF-Slim
slim.resnet/slim-resnet-v2-200  ResNet-v2-200 classifier for TF-Slim
slim.resnet/slim-resnet-v2-50   ResNet-v2-50 classifier for TF-Slim
```

!!! tip
    Guild packages are like shipping containers for models. After you
    install a package, use ``guild models PACKAGE`` to list models
    provided by that package. Packages are included in the model names in
    the form `PACKAGE/MODEL`.

All of the `slim.*` packages are implemented in [TensorFlow-Slim
->](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/slim),
which is a "lightweight library for defining, training and evaluating
complex models in TensorFlow."

The models in the `slim.resnet` package are implemented by the
[TensorFlow-Slim image classification model library
->](https://github.com/tensorflow/models/tree/master/research/slim).



## Train ResNet - part 1

Let's dive right in and train the ResNet model.
