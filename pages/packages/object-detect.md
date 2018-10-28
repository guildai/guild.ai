overview_title: gpkg.object-detect :: TensorFlow object detection core support
tags: cv

# gpkg.object-detect

`gpkg.object-detect` provides support for [TensorFlow Object Detection
->](https://github.com/tensorflow/models/tree/master/research/object_detection). It
is used by model developers who want to implement object detectors
using state of the art models from TF-Slim.

To use `gpkg.object-detect` you must extend package configuration in your
project [Guild file](term:guild-file). Refer to the documentation
below for details.

This package does not contain any models. If you want to use object
detection models directly, install
[gpkg.object-detect.models](pkg:object-detect-models).

[PKG-HELP gpkg/object_detect]

[TOC]

## Create TF-Slim based classifier

See the guide [Create an object
detector](/docs/guides/create-object-detector/) for step-by-step
instructions.
