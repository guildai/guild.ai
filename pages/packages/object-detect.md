overview_title: gpkg.object-detect :: TensorFlow object detection core support
tags: cv

# gpkg.object-detect

`gpkg.object-detect` provides support for [TensorFlow Object Detection
->](https://github.com/tensorflow/models/tree/master/research/object_detection). It
is used by model developers who want to implement object detectors
using state of the art models from TF-Slim.

To use `gpkg.object-detect`, extend model configuration in your
project [Guild file](term:guild-file). Refer to the documentation
below for details.

This package does not contain any model definitions---it only provides
model configuration that you can extend in your projects. If you want
to use object detection models directly, install
[gpkg.object-detect.models](pkg:object-detect-models).

[PKG-HELP gpkg/object_detect]

[TOC]

## Step-by-step example

See the guide [Create an object
detector](/docs/guides/create-object-detector/) for an example of how
to use the model configuration in this package.

## Extending model configuration

You can extend any of the following model configurations from a model
definition:

[PKG-CONFIG-LIST gpkg/object_detect model-config]

The following model extends `faster‑rcnn‑resnet‑50`:

``` yaml
model: detector
extends:
  - gpkg.object-detect/faster-rcnn-resnet-50
```

When a model extends a model configuration, it inherits its operation
and resource definitions.

If you extend a base configuration (e.g. `model-base`, `ssd-base`,
etc.) you must provide additional configuration using model
parameters. See [Configuration](#configuration) below for more
information.

## Configuration

The TensorFlow object detection API uses a complex protobuf based
configuration schema. For schema details, refer to the API
[configuration protobuf
files](https://github.com/tensorflow/models/tree/master/research/object_detection/protos).

This package supports configuration in three formats:

- A complete protobuf configuration file
- Section specific YAML formatted configuration files
- Selected flags

These three formats are used to generate a single `generated.config`
protobuf file that serves as the configuration for an operation
run. Each operation run generates a different configuration according
to the configuration in effect for that run.

To view `generated.config` for a run, use the [](cmd:cat) command:

``` command
guild cat generated.config [-o OPERATION] [RUN]
```

`OPERATION` and `RUN` are both optional. By default, Guild shows the
contents of `generated.config` for the latest run. If that's not the
run you want to view, use `OPERATION` to specify the operation
name. By default Guild selects the latest run matching that name.

For example, to view `generated.config` for the latest
`transfer-learn` run, use:

``` command
guild cat generated -o transfer-learn
```

`RUN` may be specified as a run ID or as a one-based index.

### Configuration flags

Operation modules (see [below](#operation-main-modules)) support
configuration settings that are frequently set using
[flags](term:flag) for a given run. These may be set as default flag
values in the model configuration as well as set by users when
executing the [](cmd:run) command.

The following configuration flags are supported:

`train-steps`
: Number of steps to train. Supported by `train.py`.

`eval-examples`
: Number of examples to evaluate. Supported by `train.py` and
  `eval.py`.

`batch-size`
: Batch size used in training. Supported by `train.py`.

`quantize`
: Whether or not to quantize model outputs. Supported by `train.py`.

`quantize-delay`
: Number of steps after which to start quantization. Supported by
  `train.py`.

### Section specific YAML configuration

To facilitate reuse of configuration shared across model
architectures, this package supports section specific YAML
configuration. Each section specific configuration is used to generate
a part of the final generated protobuf config (see details on
`generated.config` above).

The following configuration sections are supported:

*model*
: Configuration for the `model` section in `generated.config`. See
  [config/models](https://github.com/guildai/packages/tree/master/gpkg/object_detect/config/models)
  for examples.

*train*
: Configuration for the `train_config` section in
  `generated.config`. See [config/train
  ->](https://github.com/guildai/packages/tree/master/gpkg/object_detect/config/train)
  for examples.

*evaluate*
: Configuration applied to evaluation operations. This configuration
  is typically defined in the *train* configuration, but may
  optionally be specified as additional or modified configuration as
  needed.

*dataset*
: Configuration that is dataset specific. Dataset related
  configuration applies across multiple sections in
  `generated.config`. Dataset configuration may be specified as a YAML
  file directly by a project, or it, as in the case of
  [voc_images_prepare.py](https://github.com/guildai/packages/blob/master/gpkg/object_detect/voc_images_prepare.py),
  it may be generated programmatically.

*extra*
: Extra configuration that applies anywhere in
  `generated.config`. This can be used to add or modify default
  configuration provided by model configuration.

Section specific YAML is provided to various package operation modules
through command line options. See [Operation main
modules](#operation-main-modules) below for details.

Section specific YAML can be defined for a model using model
parameters. See [Model parameters](#model-parameters) below for
details.

### Model parameters

`train-pipeline-config-proto`
: Full protobuf configuration for the `train` operation. When
  specified, section specific YAML configuration is ignored as it is
  assumed that this configuration is complete. Use this parameter when
  you want to use existing object detection pipeline configuration or
  otherwise want to bypass the YAML based configuration scheme.
  <p>
  Refer to [object detection sample config
  ->](https://github.com/tensorflow/models/tree/master/research/object_detection/samples/configs)
  for example of complete protobuf configuration.

`transfer-learn-pipeline-config-proto`
: Full protobuf configuration for the `transfer-learn` operation. As
  with `train-pipeline-config-proto`, this configuration is assumed to
  be complete and YAML configurations are ignored.

`eval-pipeline-config-proto`
: Full protobuf configuration for the `evaluate` operation. As with
  `train-pipeline-config-proto` and
  `transfer-learn-pipeline-config-proto`, this configuration is
  assumed to be complete and YAML configurations are ignored.

`dataset-config`
: YAML based configuration that defines dataset specific config. This
  configuration is applied across multiple sections in
  `generated.config`.

`model-config`
: YAML based configuration that defines the model. This configuration
  is applied only to the `model` section in `generated.config`.

`train-config`
: YAML based configuration that defines the training method and
parameters for the `train` operation. This configuration is applied
only to the `train_config` section in `generated.config`.

`transfer-learn-config`
: YAML based configuration that defines the training method and
parameters for the `transfer-learn` operation. This configuration is
applied only to the `train_config` section in `generated.config`.

`extra-config`
: Additional YAML based configuration that is applied across all
  sections in `generated.config`. This is used to add or modify
  configuration provided by other YAML configurations.

### Examples

Model configuration that uses the same protobuf configuration across
all operations. This replicates the way that you would use the object
detection API normally.

``` yaml
model: detector
extends:
  - gpkg.object-detect/model-base
params:
  train-pipeline-config-proto: ssd_inception_v2_coco.config
  transfer-learn-pipeline-config-proto: ssd_inception_v2_coco.config
  eval-pipeline-config-proto: ssd_inception_v2_coco.config
```

See [sample ssd_inception_v2_coco.config
->](https://github.com/tensorflow/models/blob/master/research/object_detection/samples/configs/ssd_inception_v2_coco.config)
for a full configuration.

Model that uses package-defined configuration for *model* and *train*
but modifies some configuration using *extra*:

``` yaml
model: detector
extends:
  - gpkg.object-detect/model-base
params:
  model-config: ssd-mobilenet-v2.yml
  train-config: ssd-train-default.yml
  transfer-learn-config: ssd-transfer-learn-default.yml
  extra-config: extra.yml
```

In this case, `extra.yml` might be:

``` yaml
optimizer:
  rms_prop_optimizer:
    learning_rate:
      exponential_decay_learning_rate:
        initial_learning_rate: 0.0001
        decay_steps: 10000
```

## Operation main modules

This package provides a number of main modules that can be used to
implement operations.

[detect.py](https://github.com/guildai/packages/blob/master/gpkg/object_detect/detect.py)
: Applies a frozen inference graph to detect objects in a set of
  provided images.

[train.py](https://github.com/guildai/packages/blob/master/gpkg/object_detect/train.py)
: Trains an object detector. This is used for both training from
  scratch as well as transfer learning, the difference being
  determined by configuration.

[eval.py](https://github.com/guildai/packages/blob/master/gpkg/object_detect/eval.py)
: Evaluates a trained object detector.

[export_and_freeze.py](https://github.com/guildai/packages/blob/master/gpkg/object_detect/export_and_freeze.py)
: Generates a frozen inference graph for a trained model.
