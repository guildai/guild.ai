tags: tool

# TensorBoard

![TensorBoard](/assets/img/tb.png)

^ TensorBoard

TensorBoard is a visualization tool from the TensorFlow team. It's a
web based application that lets you view TensorFlow event logs, which
contain a variety of useful information associated with a run:

- Metrics (scalars)
- Images, audio, and text generated during training
- Model graph
- Model statistics

For more information, see [TensorBoard: Visualizing
Learning](https://www.tensorflow.org/programmers_guide/summaries_and_tensorboard).

## TensorBoard and Guild

Guild integrates TensorBoard to make it easy to visualize TensorFlow
event logs. To visualize events for a set of runs, you can launch
TensorBoard by running:

``` command
guild tensorboard
```

You can also filter runs using Guild's run filtering options. For
example, to view only runs for the `train` operation in TensorBoard,
use:

``` command
guild tensorboard --operation train
```

For more information, see [tensorboard](cmd:tensorboard).

TensorBoard is also integrated with [Guild
View](/docs/visual/guild-view/). You can launch TensorBoard from Guild
View by clicking ![View in
TensorBoard](/assets/img/view-in-tensorboard.png) which is located in
the upper left of the screen.

## Run synchronization

When you run TensorBoard from Guild, by either the `tensorboard`
command or from Guild View, the list of runs is automatically
synchronized with the current [run view](term:run-view).
