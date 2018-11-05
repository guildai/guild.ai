tags: mobile, tflite

# Create a TensorFlow Lite file

[TensorFlow Lite ->](https://www.tensorflow.org/lite/) is a runtime
platform used to run TensorFlow models on mobile and embedded devices.

In this guide, we use a Guild project to implement a simple workflow
for generating an object detector that can be deployed on iPhone and
Android devices.

## Requirements

- [Install Guild AI](alias:install-guild)
- Sample object detector project from [](alias:create-object-detector)

## Verify sample object detector project

Follow the steps in [](alias:create-object-detector) to create a Guild
AI project containing an object detector.

Verify each of the steps below.

### `PROJECT` environment variable

Confirm that the `PROJECT` environment variable is set to the sample
project directory:

``` command
echo $PROJECT
```

If `PROJECT` is not defined, set it to the sample project location:

``` command
set PROJECT=<location of sample object detector project>
```

Replace `<location of sample object detector project>` with the full
path to the sample project from [](alias:create-object-detector).

### Activate and verify project environment

Change to the project directory:

``` command
cd $PROJECT
```

Activate the environment:

``` command
source guild-env
```

If you see the message ``Guild environment ./env does not exist``,
revisit the steps in [Initialize a project
environment](/docs/guides/create-object-detector/#initialize-a-project-environment).

Use [guild check](cmd:check) to verify the environment:

``` command
guild check
```

Confirm that the value for `guild_home` is in the project directory
under `env/.guild`.

### List available project operations

From the project directory, list operations by running:

``` command
guild ops
```

Guild should display the available operations for the object detector:

``` output
./detector:detect             Detect images using a trained detector
./detector:evaluate           Evaluate a trained detector
./detector:export-and-freeze  Export a detection graph with checkpoint weights
./detector:prepare            Prepare images annotated using Pascal VOC format
./detector:train              Train detector from scratch
./detector:transfer-learn     Train detector using transfer learning
```

If you see a different list of operations, verify the project Guild
file (`guild.yml` in the project directory) is:

``` yaml
- model: detector
  description: Sample object detector
  extends:
    - gpkg.object-detect/voc-annotated-images-directory-support
    - gpkg.object-detect/ssd-mobilenet-v2
```

If you receive an error message, verify that the project environment
is active (see above) and that `gpkg.object-detect` is installed. To
view the list of installed Guild packages, run:

``` command
guild packages
```

If `gpkg.object-detect` is not shown in the list, install it by
running:

``` command
guild install gpkg.object-detect
```

## Install `gpkg.tflite`

The modifications we make below require a new Guild package,
`gpkg.tflite`, which provides support for TensorFlow Lite.

Verify that the project is environment is activated (see above) and
install `gpkg.tflite` by running:

``` command
guild install gpkg.tflite
```

## Add TensorFlow Lite support

In this section, we add support to our object detector for generating
a `tflite` file.

Modify `guild.yml` to be:

``` yaml
- model: detector
  description: Sample object detector
  extends:
    - gpkg.object-detect/voc-annotated-images-directory-support
    - gpkg.object-detect/ssd-mobilenet-v2
    - gpkg.tflite/tflite-support
```

This adds `tflite-support` to the list of model extensions. By
including `tflite-support` we inerit a new operation, `tflite`, which
is used to generate a TensorFlow Lite file from a frozen inference
graph.

Save you changes to `guild.yml`.

Verify that the detector now has the `tflite` operation by running:

``` command
guild ops tflite
```

Guild should show the new operation:

``` output
./detector:tflite  Generate a TFLite file from a frozen graph
```

## Modify `export-and-freeze` to support tflite

To generated a tflite file, we need to make a change to the
`export-and-freeze` operation. The exported graph needs additional
operations to support TensorFlow Lite.

The export support in `gpkg.object-detect` supports this by way of a
`tflite` flags, which, when set to `yes`, causes the exported graph to
include the required operations.

Let's modify our model definition so that this behavior is enabled by
default.

Modify `guild.yml` to be:

``` yaml
- model: detector
  description: Sample object detector
  extends:
    - gpkg.object-detect/voc-annotated-images-directory-support
    - gpkg.object-detect/ssd-mobilenet-v2
    - gpkg.tflite/tflite-support
  operations:
    export-and-freeze:
      flags:
        tflite: yes
```

This change modifies the default value of the `tflite` flag to
`yes`. The rest of the configuration for the `export-and-freeze`
operation remains unmodified.

Save you changes to `guild.yml`.

You can verify the new default value by running:

``` command
guild run export-and-freeze --help-op
```


The `--help-op` option tells Guild to show operation help without
running the operation. You can use this option whenever you have a
question about an operation's use and its supported flags.

Note the definition of the `tflite` flag:

``` output
tflite  Whether or not to export graph with support for TensorFlow Lite (yes)
```

The default value is listed in parentheses as ``yes``.

## Verify a trained model

To generate a tflite file, you must first train a detector. If you
have not already run the `transfer-learn` operation, revisit [Train a
detector using transfer
learning](docs/guides/create-object-detector/#train-a-detector-using-transfer-learning)
before continuing.

Verify that you have a trained model by running:

``` command
guild ls -o transfer-learn
```

If you see ``No matching runs``, train a detector before continuing.

## Generate a tflite compatible graph

Use `export-and-freeze` to generate a frozen inference graph that
supports TensorFlow Lite:

``` command
guild run export-and-freeze
```

Note that `tflite` is `yes` (the new default value) and press `Enter`
to confirm.

Guild generates a frozen inference graph. You can verify the graph
files generated by running:

``` command
guild ls -p graph
```

Guild shows:

``` output
graph/
graph/frozen_inference_graph.pb
graph/tflite_graph.pb
graph/tflite_graph.pbtxt
```

## Generate a tflite file

Now that we have a frozen inference graph that supports tflite, we can
run the tflite operation:

``` command
guild run tflite
```

Press `Enter` to confirm.

Guild generates a tflite file.

View the run files:

``` command
guild ls
```

Guild shows the files:

``` output
frozen_inference_graph.pb
model.tflite
```

You can deploy the tflite file by copying it from the run
directory. To get the full path of the tflite file, use:

``` command
guild ls -f -p model.tflite
```

The use of `-f` tells Guild to show the full path to the file.

## Summary

In this guide, we modified the object detector project that we created
in the [](alias:create-object-detector) to support TensorFlow
Lite. Specifically, we made the following changes:

- Extend `gpkg.tflite/tflite-support` to inherit the `tflite`
  operation, which is run to generate a tflite file.

- Redefine `tflite` flag of `export-and-freeze` operation.

With these changes, we can generate a tflite file for our object
detector using this sequence of operations:

`prepare`
: Prepare the dataset for training.

`transfer-learn`
: Train the detector using transfer learning.

`export-and-freeze`
: Generate a frozen inference graph that is compatible with TensorFlow
  Lite.

`tflite`
: Generate a tflite file from the frozen inference graph.
