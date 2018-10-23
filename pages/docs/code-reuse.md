tags: concepts

# Code reuse

[TOC]

Guild supports code reuse through various features:

Model definition inheritance
: Guild models can extend the definition of other models, which lets
  you assemble models and model workflows using a few lines of
  configuration.

Packaged operation modules
: You can implement a model operation by specifying a main module from
  any Python package, including those in any Python package as well as
  a project.

Packaged models
: In some cases you might not need to customize a model, in which case
  you can install a model and use it without custom code.

## Model definition inheritance

Here's an example of a model that extends another model:

``` yaml
model: my-model
extends: gpkg.slim.models/resnet-50
```

With the addition of ``extends: gpkg.slim.models/resnet-50`` to the
model definition, the model inherits the operations and resources for
the `resnet-50` TF-Slim model.

Running ``guild operations`` in the `my-model` project directory shows:

``` output
./my-model:evaluate           Evaluate a trained model
./my-model:export-and-freeze  Export an inference graph with checkpoint weights
./my-model:finetune           Finetune a trained model
./my-model:label              Classify an image using a trained model
./my-model:tflite             Generate a TFLite file from a frozen graph
./my-model:train              Train model from scratch
./my-model:transfer-learn     Train model using transfer learning
```

### Redefine inherited operations

A model can redefine model operations, including default flag values,
and resources.

Here's an example of extending `resnet-50` and redefining the default
learning rate for the `train` operation:

``` yaml
model: my-model
extends: gpkg.slim.models/resnet-50
operations:
  train:
    flags:
      learning-rate: 0.002
```

### Add new operations

Models can add new operations.

Here's an example of extending `resnet-50` and adding an application
specific `deploy` operation:

``` yaml
model: my-model
extends: gpkg.slim.models/resnet-50
operations:
  deploy:
    description: Deploy trained model to our production server.
    main: deploy --host prod-serving.myorg.net
```

### Config and parameters

In addition to extending models, you can extend *config*
objects. Config objects are top-level Guild file objects that are
designed with the `config` attribute. They provide configuration for
models and other config.

Here's an example of a base model config:

``` yaml
- config: model-base
  operations:
    train:
      description: Train the model
      main: '{{train-main}}'
      flags:
        batch-size:
          description: Number of images to include in a training batch
          default: 100
        epochs:
          description: Number of epochs to train
          default: 10
```

The config provides a model definition that can be extended by
models. It uses a *parameter* named `train-main` that extending models
must define to specify the main module for the `train` operation.

Here are two models that each extend `model-base`:

``` yaml
- model: cnn
  extends: model-base
  params:
    train-main: train_cnn

- model: logistic-regression
  extends: model-base
  params:
    train-main: train_logistic_regression
```

In this example, both `cnn` and `logistic-regression` inherit the
`train` operation from `model-base`. Using pararameters, each
extending model defines values used by the extended configuration.

## Packaged operation modules

Another form of code reuse in Guild is a *packaged operation module*,
which is a module that is available from an installed Python
packaged. These modules are available when the package is installed.

Here's an example of implementing a `serve` operation by using a
module from the `gpkg.tfserve` package:

``` yaml
model: my-model
extends: gpkg.slim.models/resnet-50
operations:
  serve:
    main: gpkg.tfserve/serve
```

## Packaged models
