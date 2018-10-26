tags: reference

# Guild file

[TOC]

Guild files are files named `guild.yml` that contain information that
Guild needs to perform an operation.

Guild files are authored in [YAML ->](http://yaml.org/).

## Top level objects

Guild files may contain a single top-level object or a list of
top-level objects.

A top-level object may one of:

- `model`
- `package`
- `config`
- `test`

Top-level objects are identified by the presence of an identifying
attribute: `model`, `package`, `config`, or `test`. A Guild file may
contain top-level objects that do not have one of these identifying
attributes, but these objects are ignored by Guild.

The value of identifying attributes are used as object identifiers.

A top-level object must only contain one and only one identifying
attribute.

### Examples

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

Top-level package:

```yaml
package: my-package
description: My package
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

- test: all
  description: Test all models
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
      main: mnist/mnist --data_dir mnist-idx-data --model_dir . --export_dir .
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
    main: train --epochs 1
  test:
    main: test --data .
```

### Attributes

`description`
: Operation description (string)
  <p>
  This may be a multi-line description.

`handle-keyboard-interrupt`
: Handle keyboard interrupts from the user (boolean)
  <p>
  By default, an operation must explicitly handle keyboard interrupts,
  which are generated when the user types ``Ctrl-C``, by catching
  Python's ``KeyboardInterrupt`` or the process will terminate with an
  error and a Python traceback. Set `handle-keyboard-interrupt` to
  ``yes`` to indicate that Guild should handle ``KeyboardInterrupt``
  and exit without printing an error message.
  <p>
  If the operation is run with ``--debug``, Guild will print the full
  traceback as a log message.
  <p>
  Note that an operation terminated with ``Ctrl-C`` will still have a
  status of ``terminated`` even if the interrupt is handled by
  Guild. To indicate that the operation should be considered
  ``completed``, set the operation's `stoppable` attribute to ``yes``.

`main`
: Main command module (required string unless `plugin-op` is used)
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
  Flags define the arguments that are passed to `main` when the
  command is executed. For more information, see [Flags](#flags).

`plugin-op`
: The name of a plugin operation to used instead of `main` (string)
  <p>
  `main` and `plugin-op` cannot both be used.

`pre-process`
: Pre-processing shell command
  <p>
  The command is executed as a shell script after required resources
  are resolved and before the operation itself is started.
  <p>
  Commands are executed in the run directory and have access to the
  same set of environment variables as the operation itself. See
  [Operations](/docs/operations#environment-variables) for the
  list of supported environment variables.

`required`
: One or more required resources (string or list of strings)
  <p>
  Values must be in the form `[PACKAGE_OR_MODEL/]RESOURCE`.

`remote`
: Flag indicating whether or not the operation is remote (boolean)

`stoppable`
: Flag indicating that a terminated run should be considered completed
  (boolean)
  <p>
  By default, a terminated run (i.e. a run stopped by typing `Ctrl-C`
  or stopped with a `SIGTERM` signal such as that issued by the
  [](cmd:stop) command) has a status of ``terminated``. If `stoppable`
  is true however, the run status will be ``completed``. Set this
  value to ``yes`` when the operation is designed to be terminated
  explicitly by the user.

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

Flag choices limit the available values for a flag. They can also be
used to apply multiple argument to a command when specified.

### Attributes

`value`
: Flag value when choice is specified (string or number)

`description`
: Flag choice description (string)

`args`
: Map of argument names to values (object)
  <p>This attribute is used to define additional arguments that are
  applied when the choice is selected. Arguments are applied in the
  form ``--NAME VALUE`` where `NAME` and `VALUE` correspond to the
  respective object name value pairs. Use `arg-skip` to omit the flag
  argument itself.

### Examples

Operation that can train one of two model versions (default is `1`):

``` yaml
model: my-model
operations:
  train:
    main: train
    flags:
      version:
        default: 1
        choices: [1, 2]
```

Snippet from the [shared
configuration](https://github.com/guildai/packages/blob/master/slim/shared.yml)
in the `slim` package. Note that when ``imagenet`` is specified, the
arguments ``input-mean`` and ``input-std`` are included in the command
argument.

``` yaml
- config: slim-image-classifier
  operations:
    predict:
      main: label_image --graph graph.pb --labels data/labels.txt
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

`post-process`
: Shell command executed after source has been resolved (string)
  <p>
  This applies to `url` sources only.
  <p>
  Commands are executed in the context of the resource cache directory
  containing the downloaded and unpacked URL source. Commands may use
  the `$RESDEF_DIR` environment variable to reference files relative
  to the directory containing the resource declaration (i.e. the
  directory containing the project or package Guild file).

`help`
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
    main: train
  finetune:
    main: finetune
    requires: trained-model
resources:
  trained-model:
    path: model
    sources:
      - operation: train
        select: checkpoint|model\.ckpt.*
```

## Packages

A Guild file may contain at most one `package` object.

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
package: gpkg.slim.models
version: 0.5.0
description:
  TF-Slim models including support for Inception, ResNet, VGG,
  MobileNet, NASNet, and PNASNet
url: https://github.com/guildai/packages/tree/master/slim/models
author: Guild AI
author-email: packages@guild.ai
license: Apache 2.0
requires:
  - gpkg.slim
  - gpkg.tflite
```

## Tests

A Guild file may contain multiple `test` top-level objects. A test
defines steps used by the [](cmd:test) command.

### Attributes

`test`
: Test name (required string)

`description`
: Test description (string)
  <p>
  This may be a multi-line description.

`steps`
: Test steps (list of [test steps](#test-steps))

### Examples

Tests defined in `gpkg.slim.models:

``` yaml
- test: package-help
  description: Check package help
  steps:
    - compare-help: test/help

- test: models
  description: Basic test of package models
  steps:
    - run: images:prepare
      flags:
        images: test/sample-images
        random-seed: 801
      expected:
        - file: data/train-weights.txt
          compare: test/sample-images/train-weights.txt
    - for-each-model:
        except:
          - images
        steps:
          - run: transfer-learn
            flags:
              auto-scale: no
              clone_on_cpu: 'True'
              train-steps: 1
            expect:
              - file: train/checkpoint
              - file: train/graph.pbtxt
          - run: evaluate
            flags:
              eval-batches: 1
              batch-size: 5
            expect:
              - output: eval/Accuracy\[.+\]
              - output: eval/Recall_5\[1\]
          - run: export-and-freeze
            expect:
              - file: graph.pb
              - file: frozen_graph.pb
          - run: tflite
            expect:
              - file: model.tflite
```

## Test steps

A test step is an action performed for a test. When a test is run,
Guild executes each step in the order defined for the test. If a step
fails, the test fails.

Test steps have a *type*, which is identified by the use of one and
only one of the following type attribute:

`compare-help`
: Compares help generated for the Guild file with the contents of a
  text file. The value of the `compare-help` attribute is a path to
  the text file that contains the expected help. The step fails if the
  generated help does not match the contents of the text file.
  <p>
  To generate the text file, use ``guild help > PATH`` where `PATH` is
  a location relative to the Guild file (e.g. ``test/help``).

`run`
: Runs an operation and optionally verifies its output. The value of
  the `run` attribute is the name of the operation to run. If the
  Guild file contains more than one more and the operation applies to
  a non-default model, the model must be included in the value in the
  form `MODEL:OPERATION`.
  <p>
  See [run step attributes](#run-step-attributes) for a list of
  supported attributes.

`for-each-model`
: Performs a list of steps for each model defined in the Guild file.
  <p>
  See [for-each-model step
  attributes](#for-each-model-step-attributes) for a list of supported
  attributes.

### `run` step attributes

`flags`
: Map of flag names to values to use for the run.

`expect`
: List of [checks](#run-checks) to perform if the run succeeds. If a
  check fails, the run step fails.

`disable-plugins`
: List of plugins to disable for the run. See [](cmd:run) for details
  on disabling plugins.

### run checks

A run check is defines in the `run` step `expects` list. A check is
defined by a type attribute. Guild supports the following checks:

`file`
: Check that a file exists and optionally check its contents.

`output`
: Checkout run output.

#### `file` check

Use a `file` check to verify that a run generated expected files. The
value for the `file` attribute is a path or pattern of the expected
file or files. Paths are relative to the run directory.

You may also check the file contents by either comparing it to a file
or by specifying a regular expression to check, if the expected file
is a text file. See below for details.

Additional attributes:

`compare`
: Compare the file or files to a file containing the expected
  content. If the generated file or files differ, the check fails.

`contains`
: Search the file or files for the specified regular expression. If
  the generated file or files do not contain the pattern, the check
  fails.

#### `output` check

Use an `output` check to check the run output for a pattern. The value
of the `output` attribute is a regular expression. If the run output
does not contain the pettern, the check fails.

### `for-each-model` step attributes

A `for-each-model` step runs a list of steps for each model defined in
the Guild file.

Attributes:

`steps`
: A list of [test steps](#test-steps) to run for each model.

`models`
: An optional list of models to run steps for. If not specified, all
  of the models in the Guild file are used.

`except`:
: An optional list of models to omit from the list of models.
