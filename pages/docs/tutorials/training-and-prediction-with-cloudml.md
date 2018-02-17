tags: tutorial, popular, intro

# Training and prediction with Cloud ML

[TOC]

In this tutorial, we'll train a model with Google's Cloud Machine
Learning Engine (Cloud ML) and use the trained model to make
prediction.

This tutorial is based on [Cloud ML Engine - Getting Started
->](https://cloud.google.com/ml-engine/docs/getting-started-training-prediction)
and follows similar steps.

!!! important
    This tutorial uses Cloud ML to train models, which will incur
    changes to your Google Cloud account. While these charges will be
    nominal (under $5) if you're concerned about the cost of training
    in Cloud ML, you may skip any of the `cloudml` operations below.

## Requirements

This tutorial assumes the following:

- Guild AI is [installed and verified](/install)
- [Google Cloud SDK ->](https://cloud.google.com/sdk/docs/) is installed
- Your [virtual environment is activated](alias:virtualenv-activate)
  (if applicable)
- You have a working Internet connection

While not required, we recommend using a dedicated virtual environment
for this tutorial. To setup your environment, see
[](alias:tut-env-setup).

## Install the census package

We'll be training a model in the `cloudml.census` package. From a
command line, run:

``` command
guild install cloudml.census
```

You can list the model operations available from the package by
running:

``` command
guild ops cloudml.census
```

``` output
cloudml.census/census-dnn:cloudml-train  Train the classifier on Cloud ML
cloudml.census/census-dnn:train          Train the model locally
```

## Train the model locally

Let's first train the model locally. This will confirm that we can get
a reasonable result locally before training in Cloud ML.

Train the model using 1000 steps by running:

``` command
guild train census train-steps=1000
```

Guild lets you review the flags used in the run before
proceeding. Press `ENTER` to confirm the operation and start training.

With only 1,000 training steps, the model should be trained on most
systems in under a minute.

After the run has finished, list it by running:

``` command
guild runs
```

The [](cmd:runs) command is shorthand for [runs list](cmd:runs-list),
which shows your runs. If you trained other models you'll see those
runs in the list as well. If you'd like to limit your listing to runs
associated with the `cloudml-census` model, use:

``` command
guild runs -o census
```

This command shows run that have an operation containing the string
"census". Feel free to experiment with other filters to show only the
runs you're interested in. Try ``guild runs --help`` for a
list of filter options.

## View training results

The training run generates a number of files. Let's view them by
running:

``` command
guild runs info --files
```

[runs info](cmd:runs-info) is used to view information for a run. By
default the command shows information for the latest run. The
``--files`` option tells Guild to include file information in the
output.

Here's a breakdown of the files associated with our training run:

`census-data/*`
: Census data used for training and test

`checkpoint`
: Latest TensorFlow checkpoint marker

`eval_census-eval/events.out.tfevents.*`
: TensorFlow event log generated during evaluation

`events.out.tfevents.*`
: TensorFlow event log generated during training

`export/census/*/saved_model.pb`
: TensorFlow SavedModel

`export/census/*/variables/`
: TensorFlow variables

`graph.pbtxt`
: TensorFlow GraphDef

`model.ckpt-1.*`
: TensorFlow checkpoint at training step 1

`model.ckpt-1000.*`
: TensorFlow checkpoint at training step 1000

`trainer/`
: Link to training scripts

Run files are stored locally on your system. To view the full path to
run files, use the ``--full-path`` option:

``` command
guild runs info --files --full-path
```

This can be useful if you want to refer to a file from the command
line (e.g. to copy it, open it, etc.)

Next we'll use Guild View to view our training results. In a
[](alias:separate-console), run:

``` command
guild view
```

This opens a browser window showing you the list of runs for the
census classifier. You can see the list of files for a run by clicking
the **FILES** tab.

If you have runs from other models, you can filter the runs that Guild
View displays using the ``-o`` option (short for ``--operation``). To
limit runs for operations containing ``census``, use:

``` command
guild view -o census
```

!!! note
    The [](cmd:view) command will not terminate until you stop it by
    typing `CTRL-c`. To continue running Guild commands, run Guild
    View from a separate console.

From Guild View, you can open TensorBoard by clicking ![View in
TensorBoard](/assets/img/view-in-tensorboard.png) in the upper left of
the window.

In TensorBoard, note the model **accuracy**, which can be viewed under
the **SCALARS** tab. The value for our first run should be
approximately 80%.

You may keep the Guild View and TensorBoard windows open for the
remainder of this tutorial --- they'll automatically refresh as you
generate runs. When you no longer need them, close the browser windows
and stop Guild View by typing `CTRL-c`.

## Label your run

Over time you'll generate a lot of runs and it's helpful to label them
for easy identification. Guild provides [runs label](cmd:runs-label),
which associates a run with a simple string.

Let's label our run to indicate that it was local and used 1,000
training steps:

``` command
guild runs label local-1000
```

Guild will confirm that you want to label the latest run --- press
`ENTER` to apply the label.

You can view the new label when you list runs:

``` command
guild runs
```

!!! tip
    You can filter runs using their label by running ``guild runs -l
    LABEL`` where `LABEL` is a label or part of a label to filter
    on. For example, assuming we consistenly label our local runs
    using the convention ``local-NNNN``, we could filter them using
    ``guild runs -l local``.

## Train the model in Cloud ML

Now that we've trained the model locally, let's train it in Cloud ML!

When training in Cloud ML, we need a Cloud Storage bucket that you
have write access to. The bucket is used to store the Cloud ML jobs.

For instructions on creating and configuring a bucket, see [Set up
your Cloud Storage bucket
->](https://cloud.google.com/ml-engine/docs/getting-started-training-prediction#set_up_your_cloud_storage_bucket)
in the Cloud ML Getting Started guide.

We'll use the name of your Cloud Storage bucket throughout this
tutorial so let's create a variable for it. Run this command to set
the name of your bucket:

``` command
echo -n "Google Cloud Storage bucket name: " && read BUCKET
```

Verify that you can use `gsutil` to write to the bucket by running:

``` command
echo 'It works!' | gsutil cp - gs://$BUCKET/guild_test \
 && gsutil cat gs://$BUCKET/guild_test
```

If you have write access to `$BUCKET` you should see:

``` output
It works!
```

When you've confirmed that you can write to the Cloud Storage bucket,
train the census classifier in Cloud ML by running:

``` command
guild run census:cloudml-train \
  bucket-name=$BUCKET \
  train-steps=1000 \
  --label cloud-1000
```

The `cloudml-train` operation is otherwise identical to the `train`
operation, but it's run remotely on Cloud ML rather than locally. The
command needs `bucket-name` to know where to create the Cloud ML job.

Note that we included a label for our run using the ``--label``
option. We'll use this convention throughout the tutorial so we can
easily idenfity our runs. In this case, we're indicating that the run
is cloud based and uses 1,000 steps.

!!! note
    Earlier we used ``guild train census`` to train our model. The
    [](cmd:train) command is an [alias](term:operation-alias) for the
    `train` operation, so our previous command was equivalent to running
    ``guild run census:train``. The `cloudml-train` operation doesn't
    have an alias, so we have to use the [](cmd:run) command in this
    case.

The remote operation will take longer to run because Cloud ML first
provisions a job and waits for TensorFlow to start. This can take up
to several minutes. You can view the run status as it progresses in
the console.

You can also view the run status from Guild View and TensorBoard,
which will both reflect the latest information.

As the Cloud ML job progresses, Guild automatically synchronizes with
it. This includes downloading generated files such as TensorFlow event
logs and saved models as well as updating run status.

!!! note
    If Guild becomes disconnected from a remote job --- for example,
    you terminate the command by typing `CTRL-c` or lose network
    connectivity --- the job will continue to run in Cloud ML. You can
    synchornize with the job by running ``guild sync``. If you'd like
    to reconnect to a running job, run ``guild sync --watch``. For
    more information, see the [](cmd:sync) command.

When the run has finished, view the list of runs:

``` command
guild runs
```

You should see that the run ``cloud-1000`` has completed.

## Compare runs

Each time you train a new model, you'll want to compare the results to
those of previous runs. Guild's [](cmd:compare) command can be used to
quickly sort and compare training accuracies and loss.

Compare your runs by running:

``` command
guild compare
```

This command starts Guild Compare, which is a spreadsheet-like
application that displays run details. You can view run status,
duration (time), accuracy, loss, and hyperparameters. We'll learn more
about hyperparameters later in this tutorial.

In Guild Compare, note the accuracy for the two runs --- they should
be similar. We'd expect this because we trained the same model with
the same flags and data. The only difference between the runs is where
the training occurred!

To exit Guild Compare, press ``q`` (quit).

!!! note
    As with the [](cmd:view) command, [](cmd:compare) will not exit
    until you explicitly stop it.  If you want to keep it running,
    start the command in a [](alias:separate-console) and press ``r``
    (refresh) when you want to update the display with the latest run
    status.

    For a complete list of commands supported by Guild Compare, press
    ``?`` while it's running.

If you'd like to export the comparison data in [CSV format
->](https://en.wikipedia.org/wiki/Comma-separated_values) run:

``` command
guild compare --csv
```

To save the comparison to a file, use your shell's output redirection:

``` command
guild compare --csv > census-runs.csv
```

### Use TensorBoard to compare runs

Let's now compare run results in TensorBoard. If you have TensorBoard
open from the previous run, it will automatically refresh to display
the current training results. If you need to restart Guild View, run:

``` command
guild view
```

In Guild View, click **VIEW IN TENSORBOARD** to open TensorBoard.

You may alternatively open TensorBoard directly using the
[](cmd:tensorboard) command:

``` command
guild tensorboard
```

!!! tip
    In TensorBoard, it helps to make two changes when viewing results
    for census training in this tutorial:

    1. In the left sidebar, uncheck **Ignore outliers in chart scaling**
    2. In the left sidebar, use the slider to set **Smoothing** to ``0``

    You can also maximize the **accuracy** scalar by clicking
    ![Maximize button](/assets/img/tb-maximize.png) under the chart.

The values for **accuracy** in TensorBoard correspond to the values
displayed in Guid Compare. TensorBoard however shows all available
scalars for selected runs, including their values at various stages of
training.

For a quick high-level summary of run results, use Guild Compare. To
view run details, use TensorBoard.

## Improve model accuracy

Let's try to improve the accuracy of the model with more training.

To increase the training steps, set the `train-steps` flag to a higher
level. We'll use 10,000 steps time:

``` command
guild run cloudml-train \
  bucket-name=$BUCKET \
  train-steps=10000 \
  --label cloud-10000
```

While this is a 10x increase, the training time Cloud ML should not be
much longer than our previous cloud run.

!!! note
    The census model trains quickly even with 10,000 steps. The time
    spent in Cloud ML for fast training models like `census` is
    primarily the setup and teardown of the Cloud ML job.

You can monitor the training progress using Guild View, Guild Compare
or TensorBoard.

As the training proceeds, the model accuracy should surpass that of
the previous two runs.

Let's use Guild Compare to confirm. If Guild Compare is already
running, press ``r`` to refresh the display. If it's not running,
start it:

``` command
guild compare
```

When you're done comparing the runs, press ``q`` to exit Guild
Compare.

## Scale up

Let's take advantage of Cloud ML's ability to scale! We can train our
model using distributed TensorFlow and multiple workers by setting the
`scale-tier` flag to a multi-worker tier.

See [Scale Tier
->](https://cloud.google.com/ml-engine/reference/rest/v1/projects.jobs#scaletier)
for more information on Cloud ML's supported environments.

By default, Cloud ML operations in Guild AI use the `BASIC` scale
tier, which is suitable for small models and experimentation. Let's
train again with the `STANDARD_1` scale tier. We'll use the same
number of training steps as our previous run (10,000) so we can
compare the performance of the two runs.

Train with the `STANDARD_1` scale tier and 10,000 steps by running:

``` command
guild run cloudml-train \
  bucket-name=$BUCKET \
  scale-tier=STANDARD_1 \
  train-steps=10000 \
  --label scaled-10000
```

This operation should take less time than our previous run of 10,000
steps, though it may in some cases take longer (see note below). You
can check the result using Guild Compare:

``` command
guild compare
```

The accuracies of `cloud-10000` and `scaled-10000` should be very
close since the model was trained with the same number of steps, flag
values, and data.

!!! note
    In some cases you won't see much difference in training time
    between `cloud-10000` and `scaled-10000` or the scaled run may
    even be longer! This is due to job setup and teardown overhead,
    which can add several minutes to a run. For longer training runs,
    the use of distributed TensorFlow in multi-worker scale tiers
    can take considerably less time than single worker training.

## Hyperparameter tuning

Cloud ML provides a feature called *hyperparameter tuning*, which can
optimize training results by automatically modifying model
hyperparameters. A hyperparameter is a model setting that can be
configured with flags. The census model we're training has three
tunable hyperparameters:

`first-layer-size`
: Number of nodes in the first layer of the DNN (default is 100)

`layers`
: Number of layers in the DNN (default is 4)

`scale-factor`
: How quickly the size of the layers in the DNN decay (default is 0.7)

Up to this point we've training using the default values for each
flag. But what if we could improve our model's predictive accuracy by
using different values?

Cloud ML hyperparameter tuning tries different values for us using an
algorithm that attempts to optimize the training result. In this case
we want to maximize predictive accuracy.

For more information see [Overview of Hyperparameter Tuning
->](https://cloud.google.com/ml-engine/docs/hyperparameter-tuning-overview)
in the Cloud ML Engine documentation.

Let's see if we can improve model accuracy accuracy using Cloud ML
hyperparameter tuning. We can use our model's `cloudml-hptune`
operation for this.

!!! important
    The command below trains the census model 6 times, each time using
    10,000 steps. While this is still a relatively low cost training
    run, if you're concerned about the cost of this operation, you may
    skip this command.

Start a hyperparameter tuning run with 6 trials of 10,000 training
steps each by running:

``` command
guild run census:cloudml-hptune \
  bucket-name=$BUCKET \
  max-trials=6 \
  train-steps=10000 \
  --label tune-6x-10000
```

This uses the [default tuning configuration
->](https://raw.githubusercontent.com/guildai/packages/master/cloudml/census/hptuning_config.yaml)
provided by the `cloudml.census` package and changes the default
`max-trials` count to 6 from 4. The `max-trials` flag determines how
many trials are run during the hyperparameter tuning operation.

Each trial run generated in Cloud ML is synchronized as a new Guild
run, which you can treat like any other run.

As the hyperparameter tuning operation progresses, use Guild Compare
to view the trial results. As each trial is completed, it will appear
as a new run with its own accuracy and loss. Guild automatically
labels trial runs so you can identify the tuning run that generated
them.

To view trial run results while the tuning operation is running, start
Guild Compare in a [](alias:separate-console) by running:

``` command
guild compare
```

As the trials are completed, press ``r`` in Guild Compare to refresh
the display and view the trial results. You can compare the
differences in accuracy and loss and see what hyperparamter values
were used for each result.

!!! note
    The `cloudml-hptune` itself will not have accuracy or loss. It's
    job is limited to starting other training runs (trials), which do
    have accuracy and loss.

!!! tip
    In Guild Compare, you can sort any column in numeric descending
    order by moving the cursor to the column and pressing ``1``. This
    is useful for sorting runs by accuracy --- the most accuracy model
    will appear at the top of the list. You can sort in ascending
    order by pressing ``!``. This is useful for sorting runs by loss,

    Note that you must re-order a column after you refresh the display.

## Cleanup

Over the course of this tutorial you generated a number of runs and
Cloud ML jobs. If you no longer need these, you can delete them to
free up resources.

### Delete unneeded Cloud ML jobs

Use the `gsutil` command to delete any jobs from your Cloud Storage
bucket that you don't need. To delete all Guild related files, run:

```
gsutil rm -r gs://$BUCKET/guild_*
```

### Delete Guild runs

If you ran the tutorials from a virtual environment, you can simply
delete the virtual environment directory, which will free up all disk
space used by steps from this tutorial.

!!! important
    Only delete virtual environments when you're certain you
    no longer need them.

If you want to only delete runs associated with the `cloudml-census`
model, which was used in this tutorial, run:

``` command
guild runs delete -o cloudml-census -p
```

The ``-p`` option indicates that the delete should be
*permanent*. This ensures that the runs no longer consume disk space.

## Summary

In this tutorial we worked with Google's Cloud Machine Leaning Engine
(Cloud ML) to train and deploy a classifier.
