tags: popular, models

# Create an image classifier

In this guide we create an image classifier by extending model
configuration from [gpkg.slim](pkg:slim), which is a [Guild
package](term:package) that provides support for image classifiers
implemented with [TF-Slim
->](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/slim).

TF-Slim provides state of the art image classification networks,
including networks pretrained on ImageNet. TF-Slim is the basis for
both the TensorFlow [Object Detection API
->](https://github.com/tensorflow/models/tree/master/research/object_detection)
and [TensorFlow Hub ->](https://www.tensorflow.org/hub/) image
classification modules.

!!! note
    TF-Slim is deprecated and no [longer supported by the
    TensorFlow
    team](https://groups.google.com/a/tensorflow.org/forum/?#!msg/developers/XOMDDeFxgmU/SZP6sNkKCAAJ).
    Nonetheless, it's an important library that provides state of the
    art pretrained networks used by teams and engineers from Google
    and other organizations.

## Requirements

- [Install Guild AI](alias:install-guild)

## Create a project

## Initialize a project environment

{!guide-init-project-env.md!}

## Install `gpkg.slim`

##
