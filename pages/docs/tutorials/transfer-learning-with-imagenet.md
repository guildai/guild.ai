tags: tutorial, popular, intro

# Transfer learning with ImageNet

[TOC]

In this tutorial we'll use a state-of-the-art image classifier that's
been pretrained on [ImageNet ->](http://www.image-net.org/) to
accelerate training with our own images.

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
transfer learning via the `finetune` operation.

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
    install a package, use ``guild models PACKAGE`` (replace ``PACKAGE``
    with the name of the package you installed) to list models provided by
    that package. Package models are displayed in the form
    `PACKAGE/MODEL`.

All of the `slim.*` packages are implemented in [TensorFlow-Slim
->](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/slim),
which is a high level interface for defining, training and evaluating
models.

The models in the `slim.resnet` package are implemented by the
[TensorFlow-Slim image classification model library
->](https://github.com/tensorflow/models/tree/master/research/slim).


## Fine tune ResNet -- part 1

We'll be working with the `resnet-50` model, as it's relatively
smaller and faster to train.

When working with models, it's helpful to familiarize yourself with
their operations. Let's list the operations supported by the
`resnet-50` model:

``` command
guild operations resnet-50
```

``` output
slim.resnet/slim-resnet-50:evaluate   Evaluate a trained ResNet-50 model
slim.resnet/slim-resnet-50:export     Generate a ResNet-50 graph def
slim.resnet/slim-resnet-50:fine tune  Fine tune ResNet-50
slim.resnet/slim-resnet-50:freeze     Generate a ResNet-50 graph def with checkpoint weights
slim.resnet/slim-resnet-50:predict    Use TensorFlow label_image and ResNet-50 to classify an image
slim.resnet/slim-resnet-50:train      Train ResNet-50
```

We're interested in the `finetune` operation. Operations are run
using the [](cmd:run) command in this form:

    guild run MODEL:OPERATION [FLAG...] [DEPENDENCY...]

Let's dive in and run the `finetune` operation on `resnet-50`:

``` command
guild run resnet-50:finetune
```

``` output
Operation requires the following missing flags:

  dataset  Dataset to train with (cifar10, mnist, flowers, custom)

Run the command again with these flags specified as NAME=VAL.
```

We got an error! That's okay --- it's an opportunity to learn more
about required flags.

Guild is telling us that we need to specify a value for the `dataset`
flag. This makes sense --- how would the operation know what data to
use for fine-tuning otherwise?

We'll fix that in a moment, but first let's get some information about
the `finetune` operation:

``` command
guild run resnet-50:finetune --help-op
```

``` output
Usage: guild run [OPTIONS] slim-resnet-50:finetune [FLAG]...

Fine tune ResNet-50

Use 'guild run --help' for a list of options.

Dependencies:
  checkpoint  Pretrained ResNet-50 model

Flags:
  batch-size                Number of samples in each batch (default is 32)
  dataset                   Dataset to train with (cifar10, mnist, flowers,
                            custom) (required)
  learning-rate             Initial learning rate (default is 0.01)
  learning-rate-decay-type  How the learning rate is decayed (default is
                            'exponential')
  log-every-n-steps         Steps between status updates (default is 100)
  max-steps                 Maximum number of training steps (default is 1000)
  optimizer                 Training optimizer (adadelta, adagrad, adam, ftrl,
                            momentum, sgd, rmsprop) (default is 'rmsprop')
  save-model-secs           Seconds between model saves (default is 60)
  save-summaries-secs       Seconds between summary saves (default is 60)
  weight-decay              Weight decay on the model weights (default is
                            4e-05)
```

!!! tip
    It's common to start typing a [](cmd:run) command and wonder "what
    flags are available and which are required?" At that point, specify
    the ``--help-op`` option and press `ENTER`. After you've reviewed the
    operation details, use your command history to continue from where you
    left off.

Take a moment to read through the list of flags. Note that `dataset`
is marked as **required**.

In this tutorial, we'll be fine-tuning with a custom dataset. Let's
run the command again, but this time with the required flag:


``` command
guild run resnet-50:finetune dataset=custom
```

Guild will display the flag values that will be used in the operation
and prompt you before starting the operation. This gives you an
opportunity to cancel the operation and make adjustments.

Let's accept the default values --- go ahead press `ENTER` to start
the operation.

If this is the first time you've run a `slim` operation, Guild will
download the TF-Slim models library as a required resource. This is a
300+ MB package and may take several minutes to download depending on
your network connection.

!!! note
    Guild will cache downloaded resources and reuse them for subsequent
    operations when needed.

When the download has completed, Guild will exit with this output:

``` output
Resolving slim/models-lib dependency
...
Resolving slim-datasets:custom dependency
guild: run failed because a dependency was not met: could not resolve 'operation:slim-custom-images:prepare' in custom resource: no suitable run for slim-custom-images:prepare
```

Another error! That's okay --- it's an opportunity about *operation dependencies*.

Guild could not complete the `finetune` operation because it needs
output generated by the `slim-custom-images:prepare` operation. What
is this?

It's common for a model operation to require something generated by
another operation. In this case, `finetune` needs images generated by
a `prepare` operation. Guild won't automatically run these operations,
but it will point you in the right direction.

In the next section, we'll spend some time preparing some images for
training and return to the `finetune` operation later.

## Prepare your images for training

In this section we'll prepare our images for training.

The `slim` image models support a `custom` dataset, which refers to
images generated by `slim-custom-images:prepare`.

Let's get help for that operation:

``` command
guild run custom-images:prepare --help-op
```

``` output
Usage: guild run [OPTIONS] slim-custom-images:prepare [FLAG]...

Prepare a custom images dataset

Use 'guild run --help' for a list of options.

Flags:
  images  Directory containing images (required)
  shards  Number of shards to create
```

!!! tip
    Note that we didn't type the full model name in the last
    command. Guild let's you use abbreviated values as
    long as it can uniquely identify the operation.

From the help, we can see that `images` is a required flag. That makes
sense --- the operation needs something to prepare!

You have a couple options:

- Provide your own images
- Use a sample dataset

The steps below will walk you through the process of preparing the
images. If you don't have images of your own, we provide instructions
for using the [Cats and Dogs dataset
->](https://www.microsoft.com/en-us/download/details.aspx?id=54765)
from Microsoft Research.

!!! note
    The image quantity and quality has a significant impact on the
    accuracy of the final model. If you don't have a dataset of at
    least a few thousand categorized images, consider using a sample
    dataset such as Cats and Dogs. Of course you can always try with a
    smaller dataset and see what happens!

#### Create a directory for your images

The `prepare` commands expects a directory containing images.

The following creates a simple directory structure in your home
directory for Cats and Dogs. If you'd prefer a different directory
structure or name, use something else --- just take note of the path.

``` command
mkdir -p ~/Data/Cats-and-Dogs
```

#### Download or copy the images

If you're using the Cats and Dogs dataset, download it from the
[Microsoft Download Center
->](https://www.microsoft.com/en-us/download/details.aspx?id=54765)


``` command
cd ~/Data/Cats-and-Dogs
wget https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_3367a.zip
```

If you're using a different dataset, ensure that the images are
accessible from the computer you'll be training from.

#### Unpack the images

If you're using Cats and Dogs, unpack the images:

``` command
cd ~/Data/Cats-and-Dogs
unzip kagglecatsanddogs_3367a.zip
```

If you're using another dataset, ensure that the images are
categorized by storing each image of a particular type (e.g *dog*,
*cat*, etc.) in an associated category subdirectory.

Here's the Cats and Dogs directory structure:

<div class="file-tree">
<ul>
<li class="is-folder open">PetImages
 <ul>
 <li class="is-folder">Cat <i>Contains all cat images</i></li>
 <li class="is-folder">Dog <i>Contains all dog images</i></li>
 </ul>
</li>
</ul>
</div>

Use the same convention with your own images. Take note of the
top-level directory (e.g. ``PetImages`` in the example) as we'll use
it in our `prepare` operation below.

#### Run the `prepare` operation

To prepare your images for use in fine-tuning, run:

``` command
guild run custom-images:prepare images=~/Data/Cats-and-Dogs/PetImages
```

If your images are in a different location, modify ``images=...``
accordingly.

!!! important
    The location of `images` must contain the image category
    directories. I.e. if you run ``ls IMAGES_DIR`` you'll see a list
    of directories, each containing images belonging to a category.

The `prepare` operation scans the images directory and processes each
image file it finds. The operation supports JPEG, PNG, and BMP formats
and will automatically detect the file type. If any images cannot be
converted, the operation will display a message and log details to
`errors.log` (located in the run directory).

!!! note
    The Cats and Dogs dataset provided by Microsoft Research
    contains several files that cannot be converted because they have
    an unsupported format (despite the `.jpg` extension, some files
    are not JPEGs). You can safely ignore the errors and use the
    converted images for fine-tuning.

When the images have been processed, list the runs for the `prepare`
operation:

``` command
guild runs list prepare
```

TODO:

- train
- terminate
- resume
