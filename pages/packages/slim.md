overview_title: gpkg.slim :: TF Slim core support
tags: cv

# gpkg.slim

`gpkg.slim` is an image classification toolkit for [TensorFlow Slim
->](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/slim). It
is used by model developers who want to implement image classifiers
using state of the art models from TF-Slim.

To use `gpkg.slim` you must extend package configuration in your
project [Guild file](term:guild-file). Refer to the documentation
below for details.

This package does not contain any models. If you want to use TF-Slim
models directly, install [gpkg.slim.models](pkg:slim-models).

!!! note

    While the underlying TensorFlow Slim library is
    [deprecated](https://github.com/tensorflow/tensorflow/issues/16182#issuecomment-372397483),
    TensorFlow continues to support state of the art models and pretrained
    networks using TF-Slim. TF-Slim also serves as the basis for
    [TensorFlow Hub computer vision models
    ->](https://tfhub.dev/s?module-type=image-classification). Guild
    maintains up-to-date support for these model architectures through
    this package and through [gpkg.slim.models](pkg:slim-models).

[PKG-HELP gpkg/slim]

[TOC]

## Create TF-Slim based classifier

TODO
