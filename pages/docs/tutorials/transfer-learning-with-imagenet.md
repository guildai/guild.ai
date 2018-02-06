tags: tutorial, popular, intro

# Transfer learning with ImageNet

In this tutorial we'll use a state-of-the-art image classifier that's
been pretrained on [ImageNet ->](http://www.image-net.org/) to
acclerate training of our own images.

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

## Install `slim.inception`

We'll be using models from the `slim.inception` package, which support
transfer learning via the `fine-tune` operation.

Install `slim.inception` by running:

``` command
guild install slim.inception
```

When the package is installed, list the available models by running:

``` command
guild models
```

You should see this output:

``` output
slim.datasets/slim-cifar10               Support for preparing the CIFAR-10 TF-Slim dataset
slim.datasets/slim-custom-images         Support for preparing a custom images TF-Slim dataset
slim.datasets/slim-flowers               Support for preparing the Flickr flowers TF-Slim dataset
slim.datasets/slim-mnist                 Support for preparing the MNIST TF-Slim dataset
slim.inception/slim-inception-resnet-v2  Inception ResNet v2 classifier in TF-Slim
slim.inception/slim-inception-v1         Inception v1 classifier in TF-Slim
slim.inception/slim-inception-v2         Inception v2 classifier in TF-Slim
slim.inception/slim-inception-v3         Inception v3 classifier in TF-Slim
slim.inception/slim-inception-v4         Inception v4 classifier in TF-Slim
```

The `slim.inception` package provides several version of the Inception
network:


- [Inception v1 ->](http://arxiv.org/pdf/1409.04842)
- [Inception v2 ->](http://arxiv.org/abs/1502.03167)
- [Inception v3 ->](http://arxiv.org/abs/1512.00567)
- [Inception v4 ->](http://arxiv.org/abs/1602.07261)

You also see several models associated with TensorFlow Slim
datasets. These are installed as dependencies via the `slim.datasets`
package.
