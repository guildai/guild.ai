sidenav_title: TensorBoard

<!-- TODO

Sections for:

- Using TB to compare images - esp plots. Include some examples.

-->

# Guild TensorBoard

Guild provides integrated support for [TensorBoard](ref:tensorboard).

To use TensorBoard to view Guild runs, use the
[tensorboard](cmd:tensorboard) command:

``` command
guild run tensorboard
```

Guild manages the TensorBoard log directory by synchronizing with the
current set of runs and their summaries. You can leave TensorBoard
running while you generate more runs or while runs are logging
summaries. TensorBoard will update automatically.

## Differences in Guild TensorBoard

Guild runs the installed version of TensorBoard without
customization. This lets you use the current features of TensorBoard
from Guild.

A number of things are different when you run TensorBoard with Guild:

- Guild dynamically adds images saved to the run directory as
  TensorBoard summaries. This lets you view run-generated images
  without having to write them as summaries.

- Guild dynamically adds summaries so that flags and scalars can be
  compared in the **HParams** tab. This lets you use TensorBoard to
  compare hyperparameter results without having to write summaries
  yourself.

- Guild filters runs shown in TensorBoard according to the run filter
  options used with the [tensorboard](cmd:tensorboard) command. This
  lets you quickly compare runs matching various criteria without
  having to manually create a TensorBoard log directory.

## Running TensorBoard Manually

To run TensorBoard manually to view Guild runs, use [check](cmd:check)
to find [Guild home](term:guild-home):

``` command
guild check
```

Find the path listed for ``guild_home:`` in the output. Use the
following command to run TensorBoard manually:
