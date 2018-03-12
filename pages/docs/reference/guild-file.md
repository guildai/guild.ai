sidenav_title: Guild file
tags: reference

# Guild file reference

[TOC]

Guild files are files named `guild.yml` that contain information that
Guild needs to perform an operation.

Guild files are authored in [YAML ->](http://yaml.org/).

## Top level objects

Guild files may contain a single top-level object or a list of
top-level objects.

A top-level object may one of:

- `package`
- `model`
- `config`

Top-level objects are identified by the presence of an identifying
attribute: `package`, `model`, or `config`. A Guild file may contain
top-level objects that do not have one of these identifying
attributes, but these objects are ignored by Guild.

The value of identifying attributes are used as object identifiers.

A top-level object must only contain one and only one identifying
attribute.

### Examples

Top-level package:

```yaml
package: my-package
description: My package
```

Top-level model:

```yaml
model: my-model
description: My model
```

Top-level config:

```yaml
config: my-config
description: My config
```

List of top-level objects:

``` yaml
- package: my-package
  description: My package

- model: model-a
  description: Model A

- model: model-b
  description: Model B

- config: shared
  description: Share config
```

Illegal top-level object (multiple identifiers):

``` yaml
model: my-model
package: my-package
```

## Inheritance

Top-level objects may extend other top-level objects by specifying an
`extends` attribute. The value of `extends` may be a string, which
identifies a single object to extend, or a list of strings, which
identifies multiple objects to extend.

When an object extends another object, it inherits its
attributes. Extending objects may redefine attributes of the objects
they extend.

When more than one object is extended, attributes of objects later in
the list take precedence of those higher in the list.

Config objects are used exclusively for inheritance and are not
otherwise used by Guild.

### Examples

In the following example, two models extend a base config. The first
model redefines its description while the second does not.

``` yaml
- config: base
  description: A base config

- model: model-a
  extends: base
  description: My model

- model: model-b
  extends: base
```

## Packages

A Guild file must contain at most one `package` object.

Packages contain information used by Guild to generate Guild packages.

### Attributes

`package`
: Package name (required string)

`description`
: Project description (string)
  <p>
  This may be a multi-line description.

`version`
: Project version (required string)<p>

`url`
: URL to package website (URL)

`maintainer`
: Name of individual or organization package maintainer (string)

`maintainer-email`
: Email of package maintainer (email address)

`license`
: Name of package license (string)

`tags`
: List of packages tags (list of strings)

`python-tag`
: Value used as the Python tag when generating the package (string)

`data_files`
: List of additional files to include in the package (list of strings)

`resources`
: List of package resources (list of [resources](#resources))

`python-requires`
: Version of Python required by the package (string)

`requires`
: List of other packages required by the package (list of strings)

### Examples

Package definition for `slim.resnet`:

``` yaml
package: slim.resnet
version: 0.3.0
description:
  TF-Slim ResNet models (50, 101, 152, and 200 layer models for ResNet v1 and v2)
url: https://github.com/guildai/index/tree/master/slim/resnet
maintainer: Guild AI
maintainer-email: packages@guild.ai
requires:
  - slim>=0.3.0.dev11
  - slim.datasets>=0.3.0.dev3
license: Apache 2.0
tags: [resnet, images, model]
```

## Models

Models may may be defined as top-level Guild file objects using the
`model` identifying attribute.

Here's a Guild file that defines two models:

``` yaml
- model: model-a
- model: model-b
```

Models define operations, which can be run using the [](cmd:run)
command.

Models may also define resources that operations require.

### Attributes

`model`
: Model name (required string)

`description`
: Model description (string)
  <p>
  This may be a multi-line description.

`operations`
: Model operations (list of [operations](#operations))

`resources`
: Model resources (list of [resources](#resources))

`references`
: Model references (list of URLs)
  <p>
  References are displayed in help text.

`extra`
: Additional information used by Guild and Guild plugins

### Examples

Complete example of `mnist-layers` (from
[`tensorflow.mnist`](https://github.com/guildai/packages/tree/master/tensorflow/mnist)):

``` yaml
- model: mnist-layers
  description: CNN estimator for MNIST using tf.layers
  operations:
    train:
      description: Train the CNN
      cmd: mnist/mnist --data_dir mnist-idx-data --model_dir . --export_dir .
      requires:
        - mnist-lib
        - mnist/dataset
      flags:
        batch-size:
          description: Number of images to process in a batch
          default: 100
        epochs:
          description: Number of epochs to train
          default: 40
          arg-name: train_epochs
  resources:
    mnist-lib:
      description: Python library for tensorflow.mnist
      private: yes
      sources:
        - url: https://github.com/tensorflow/models/archive/v.1.6.0.zip
          sha256: ed8fd7066bb014feccaed2cd2a46e516468ef24c40be8ef21a96a09849db7ff5
          select: models-v.1.6.0/official/mnist
  references:
    - https://github.com/tensorflow/models/tree/v.1.6.0/official/mnist
```

## Operations

Operations define commands that are run for a model. Operations are
defined as named objects under the `operations` model attribute.

Here's model with two operations, `train` and `test`:

``` yaml
model: my-model
operations:
  train:
    cmd: train --epochs 1
  test:
    cmd: test --data .
```

### Attributes

`description`
: Operation description (string)
  <p>
  This may be a multi-line description.

`cmd`
: Operation command (required string)
  <p>
  Operation commands must be in the form `[MODULE] [ARG...]`. `MODULE`
  may reference a Python module defined in the model Guild file
  directory or any Python available on the system. `ARG` values are
  passed through as arguments to the Python module.
  <p>
  `MODULE` must not end in `.py`.
  <p>
  `ARG` values may contain references to [#flags](#flags) in the
  format `${FLAG_NAME}`. Such references are resolved to the current
  flag value when the command is executed.

`flags`
: Operation flags (list of [flags](#flags))
  <p>
  Flags define the arguments that are passed to `cmd` when the command
  is executed. For more information, see [Flags](#flags).

`plugin-op`
: The name of a plugin operation to used instead of `cmd` (string)
  <p>
  `cmd` and `plugin-op` cannot both be used.

`required`
: One or more required resources (string or list of strings)
  <p>
  Values must be in the form `[PACKAGE_OR_MODEL/]RESOURCE`.

`remote`
: Flag indicating whether or not the operation is remote (boolean)

## Flags

Flags are defined for [operations](#operations) under the `flags`
attribute as named objects.

### Attributes

`description`
: Flag description (string)
  <p>
  This may be a multi-line description.

`default`
: Default value if not specified by the user (string or number)

`required`
: Flag indicating whether or not the flag is required (boolean)

`arg-name`
: Name of the command argument used for flag values (string)
  <p>
  Defaults to the flag name.

`arg-skip`
: Boolean indicating whether not to include the flag as a command
  argument (boolean)

`choices`
: Allowed choices for the flag (list of [choices](#flag-choices))

## Flag choices

Flag choices may be simple values (string or number) or objects.

### Attributes

`value`
: Flag value when choice is specified (string or number)

`description`
: Flag choice description (string)

`args`
: Map of argument names to values (object)
  <p>
  This attribute can be used to define sets of command arguments that
  are applied when the choice is selected.

### Examples

Operation that can train one of two model versions (default is `1`):

``` yaml
model: my-model
operations:
  train:
    cmd: train
    flags:
      version:
        default: 1
        choices: [1, 2]
```

Snippet from the [shared
configuration](https://github.com/guildai/packages/blob/master/slim/shared.yml)
in the `slim` package.

``` yaml
- config: slim-image-classifier
  operations:
    predict:
      cmd: label_image --graph graph.pb --labels data/labels.txt
      flags:
        ...
        dataset:
          description: Dataset name to use for labels and image transformation
          required: yes
          arg-skip: yes
          choices:
            - cifar10
            - mnist
            - flowers
            - value: imagenet
              args:
                input-mean: 0.0
                input-std: 255
            - custom
```

## Resources

Resources may be included in packages and models under the `resources`
object attribute. Resources are identified by their object key.

Resources may be required by operations. Required resources are known
as *operation dependencies*.

A resource must contain at least one source. Sources may be files,
URLs, operation output, or Python modules.

All required resource sources are resolved before an operation is run
to ensure the operation has what it needs to run. Guild creates
symbolic links to resource sources in the run directory. For more
information, see [Resource sources](#resource-sources) below.

Here's a model with two resources, each with a single source file.

``` yaml
model: my-model
resources:
  resource-a:
    sources: [file-a]
  resource-b:
    sources: [file-b]
```

### Attributes

`description`
: Resource description (string)

`path`
: Relative path within the run directory where resolved sources are
  saved (string)

`sources`
: List of resource sources (list of [resource sources](#resource-sources))

`post-process`
: Shell command that is executed after all sources have been resolved (string)

`private`
: Flag indicating whether or not the resource is private (boolean)
  <p>
  Private resources don't appear in resource lists.

`references`
: List of reference URLs associated with the resource (list of URLs)
  <p>
  References are displayed in help text.

## Resource sources

A resource source defines what is resolved and therefore available to
an operation that requires the resource.

Source files are provided to runs within the run directory as symbolic
links.

### Source type

Sources have a *type*, which is identified by the use of one and only
one of the following type attribute:

`file`
: Source is a file relative to the defining Guild file

`url`
: Source is a URL (`http` and `https` protocols are supported)

`operation`
: Source is generated from an operation
  <p>
  Value is an operation spec consisting of
  `[PACKAGE/[MODEL:]]OPERATION`.  Multiple operation specs may be
  specified separated with a comma. By default Guild will use the
  latest completed or terminated run matching any of the operation
  specs. Users may alternatively specify a run ID for the resource
  when running the requiring operation.

`module`
: Source is a Python module

If source is a string, the value is treated as a `file` source type.

### Attributes

`sha256`
: SHA 256 hash used to verify the source (string)

`unpack`
: A flag indicating whether or not the source should be unpacked (boolean)
  <p>
  By default Guild attempts to unpack files with common archive
  extensions (`.zip`, `.tar`, `.tar.gz`, `.tgz`).

`select`
: One or more regular expressions used to select sources from a
  directory or unpacked archive (string or list of strings)

`resolution-help`
: Help text displayed when a source cannot be resolved (string)
  <p>
  This can be used to help a user install a missing Python module, run
  a required operation, etc.

### Examples

File `data-train.csv` and `data-test.csv` provided as a part of `data`
resource:

``` yaml
package: my-package
resources:
  data:
    description: Data files
    sources:
    - data-train.csv
    - data-test.csv
```

MNIST IDX sources as a `dataset` resource, stored under
`mnist-idx-data` in the run directory:

``` yaml
package: mnist
resources:
  dataset:
    description: "Yann Lecun's MNIST dataset in compressed IDX format"
    path: mnist-idx-data
    sources:
      - url: http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
        sha256: 440fcabf73cc546fa21475e81ea370265605f56be210a4024d2ca8f203523609
      - url: http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
        sha256: 3552534a0a558bbed6aed32b30c495cca23d567ec52cac8be1a0730e8010255c
      - url: http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
        sha256: 8d422c7b0a1c1c79245a5bcf07fe86e33eeafee792b84584aec276f5a2dbc4e6
      - url: http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
        sha256: f7ae60f92e00ec6debd23a6088c31dbd2371eca3ffa0defaefb259924204aec6
```

Operation `finetune` depends on the output of `train`, which is stored
under `model` in the run directory:

``` yaml
model: my-model
operations:
  train:
    cmd: train
  finetune:
    cmd: finetune
    requires: trained-model
resources:
  trained-model:
    path: model
    sources:
      - operation: train
        select: checkpoint|model\.ckpt.*
```
