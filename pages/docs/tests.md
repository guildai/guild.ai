tags: concepts

# Tests

[TOC]

Guild tests are defined in [Guild files](term:guild-file). They are
used to test the contents of a Guild file, including models and model
operations.

Here's a test definition that runs three operations on a sample model
and checks final accuracy:

``` yaml
- test: sample
  description: Test sample model
  steps:
    - run: sample:prepare-data
    - run: sample:train
    - run: sample:evaluate
      expect:
        - accuracy: >= 0.4
```

For details on test configuration, see [Tests
reference](/docs/reference/guild-file/#tests) in the.

Tests are run using the [](cmd:test) command.

## Specify flags for test runs

You can specify flag values for a test run using the `flags` attribute.

For example, to reduce testing time, it's common practice to specify a
low training step or epoch count for tests. Here's an example of a
test that trains for just one step to ensure that training can start
and stop without errors:

``` yaml
- test: quick
  description: Quick test to verify train start and stop
  steps:
    - run: train
      flags:
        train-steps: 1
```

## Verify run results

You can check the results of a run using the `expect` attribute for
`run` check.

Guild supports the following result checks:

- File exists
- File contents match another file
- File contains text pattern
- Output contains text pattern

### Verify run files

To check that a run creates a file, use a `file` check. A file check
may optionally specify `contains` or `compare-to` attributes that are
used to check file contents.

File paths may contain glob style patterns.

Here's an example of a test that verifies various files created by a
run:

``` yaml
- test: train
  description: Test train operation
  steps:
    - run: train
      expect:
        - file: labels.pbtxt
        - file: train/model.ckpt-*
          compare-to: test/labels.pbtxt
        - file: train/checkpoint
          contains: model_checkpoint_path: "model.ckpt-1"
```

### Verify run output

To check that a run generates particular output (output written both
to standard output and standard error streams by the run process), use
an `output` check.

Output check values must be valid regular expressions. If run output
does not match the expression, the test fails.

Here's an example that verifies that a particular string is generated
during a run:

``` yaml
- test: evaluate
  description: Test evaluate operation
  steps:
    - run: evaluate
      flags:
        images: test/sample-images/*.jpg
      expect:
        - output: Evaluating image 1/2
        - output: Evaluating image 2/2
```

## Test common operations across multiple models

If a project contains several models that share a common set of
operations, you can use the `for-each-model` step to run steps for
each applicable model.

By default, `for-each-model` runs steps for every model defined in the
Guild file. You can specify a list of models to test using the
`models` attribute. If you want to omit models from the list, you can
specify a value for `except`.

Here's an example that runs the `train` operation for every model
defined in the Guild file.

``` yaml
- test: all
  description: Test train on all models
  steps:
    - for-each-model:
        steps:
          - run: train
```

## Test project help

Use the `compare-help` check to compare help generated for a Guild
file to the contents of a file. This check is useful to ensure that a
Guild file interface---i.e. the user interface---doesn't change
unexpectedly.

This test checks Guild file help by comparing it to a project file
`test/help`:

``` yaml
- test: help
  description: Test project help
  steps:
    - compare-help: test/help
```

!!! note
    Project help is displayed using the [](cmd:help)
    command. Once you verify help content, save it to a file for use
    in a `compare-help` check, for example by running``guild help >
    test/help``.
