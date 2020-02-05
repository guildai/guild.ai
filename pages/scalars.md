tags: concept

# Scalars

[TOC]

## Overview

Scalars are numeric values that are logged during a run. Scalars are
used to log metrics like accuracy and loss.

A scalar value is associated with a *key* and a *step*. A scalar step
denotes the training step or epoch associated with a value. In cases
where a step does not apply, the step is `0`.

## Logging Scalars

Scalars may be logged using one of two methods:

- Writing values to script output
- Explicit logging of TensorBoard summaries

A scalar that is written to script output is known as an *output
scalar*. For more information, see [Output Scalars](#output-scalars)
below.

TensorBoard summaries are written to files supported by
[TensorBoard](ref:tensorboard) and other machine learning tools. For
more information, see [TensorBoard Summaries](#tensorboard-summaries)
below.

### Output Scalars

By default, Guild logs for scalars in script output in the format
``key: value`` where each value is written on a single line without
leading whitespace. Guild sets the current scalar step when the `step`
key is used. Subsequently logged values are associated with the latest
step.

The following output generates a series of 3 scalar values for `loss`:

``` output
step: 1
loss: 0.1
step: 2
loss: 0.05
step: 3
loss: 0.01
```

^ Sample output --- compatible with Guild's default output scalar logging

In this case, the logged scalar values are:

| key    | value | step |
|--------|-------|------|
| `loss` | 0.1   | 1    |
| `loss` | 0.05  | 2    |
| `loss` | 0.01  | 3    |

You can modify the way Guild logs output scalars using the
`output-scalars` operation attribute in a [Guild
file](ref:guildfile).

Consider the following output:

``` output
Epoch 1/3
- loss: 0.5 - accuracy: 0.8
Epoch 2/3
- loss: 0.1 - accuracy: 0.9
Epoch 3/3
- loss: 0.05 - accuracy: 0.95
```

^ Alternative sample output --- requires custom configuration

The default format ``key: value`` will not work in this case. To
capture scalars for this output, the operation needs a custom
`output-scalars` attribute.

``` yaml
train:
  output-scalars:
    - step: 'Epoch (\step)'
    - '- (\key): (\value)'
```

^ Custom `output-scalars` attribute to support alternative output

Output patterns are [regular expressions](term:regex). Guild supports
a variety of pattern formats for logging output scalars. Refer to
[Output Scalar Specs - Guild File
Reference](/reference/guildfile.md#output-scalar-specs) for a complete
specification of the `output-scalars` attribute.

Refer to [Output Scalars - Guild File
Cheatsheet](/cheatsheets/guildfile.md#output-scalars) for examples of
`output-scalars`.

### TensorBoard Summaries

TODO Include ways to write summaries:

- https://www.tensorflow.org/api_docs/python/tf/summary
- https://pytorch.org/docs/stable/tensorboard.html
- https://github.com/lanpa/tensorboardX

## Viewing Run Scalars
