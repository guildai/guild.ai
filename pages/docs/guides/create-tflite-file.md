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
    - gpkg.object-detect/faster-rcnn-resnet-50
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
    - gpkg.object-detect/faster-rcnn-resnet-50
    - gpkg.tflite/tflite-support
```

This adds `tflite-support` to the list of model extensions. By
including `tflite-support` we inerit a new operation, `tflite`, which
is used to generate a TensorFlow Lite file from a frozen inference
graph.

Save you changes to `guild.yml`.

Verify that
