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
