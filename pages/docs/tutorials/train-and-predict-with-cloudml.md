tags: tutorial, popular, intro

# Train and predict with Cloud ML

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
    in Cloud ML, feel free to skip any of the `cloudml` operations
    below.

## Requirements

This tutorial assumes the following:

- Guild AI is [installed and verified](/install)
- [Google Cloud SDK ->](https://cloud.google.com/sdk/docs/) is
  installed (see verification step below)
- Your [virtual environment is activated](alias:virtualenv-activate)
  (if applicable)
- You have a working Internet connection

While not required, we recommend using a dedicated virtual environment
for this tutorial. To setup your environment, see
[](alias:tut-env-setup).

To verify you have the Google Cloud SDK `gcloud` program installed and
configured, run the following:

``` command
gcloud ml-engine jobs list
```

If the command reports an error, resolve the issue before proceeding.

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

We'll run each of these operations over the course of this tutorial.

## Train the model locally

Before we jump into training in Cloud ML, let's train our model
locally. This will confirm that we can get a reasonable result with
the data we're using.

Train the model locally using 1,000 steps:

``` command
guild train census train-steps=1000
```

Guild lets you review the flag values for the operation before
started. Press `Enter` to accept the values.

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
    typing ``Ctrl-C``. To continue running Guild commands, run Guild
    View from a separate console.

From Guild View, you can open TensorBoard by clicking ![View in
TensorBoard](/assets/img/view-in-tensorboard.png) in the upper left of
the window.

In TensorBoard, note the model **accuracy**, which can be viewed under
the **SCALARS** tab. The value for our first run should be
approximately 80%.

You may keep the Guild View and TensorBoard windows open for the
remainder of this tutorial---they'll automatically refresh as you
generate runs. When you no longer need them, close the browser windows
and stop Guild View by typing ``Ctrl-C``.

## Label your run

Over time you'll generate a lot of runs and it's helpful to label them
for easy identification. Guild provides [runs label](cmd:runs-label),
which associates a run with a simple string.

Let's label our run to indicate that it was local and used 1,000
training steps:

``` command
guild runs label local-1000
```

Guild will confirm that you want to label the latest run---press
`Enter` to apply the label.

You can view the new label when you list runs:

``` command
guild runs
```

!!! tip
    You can filter runs using their label by running ``guild runs -l
    LABEL`` where `LABEL` is a label or part of a label to filter
    on. For example, assuming we consistently label our local runs
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
  bucket=$BUCKET \
  train-steps=1000 \
  --label cloud-1000
```

Review the operation flag values and press `Enter` to begin training.

The `cloudml-train` operation is otherwise identical to the `train`
operation, but it's run remotely on Cloud ML rather than locally. The
command needs `bucket` to know where to create the Cloud ML job.

Note that we included a label for our run using the ``--label``
option. We'll use this convention throughout the tutorial so we can
easily identity our runs. In this case, we're indicating that the run
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
    If Guild becomes disconnected from a remote job---for example,
    you terminate the command by typing ``Ctrl-C`` or lose network
    connectivity---the job will continue to run in Cloud ML. You can
    synchronize with the job by running ``guild sync``. If you'd like
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
application that displays run details. You can view run status, time,
accuracy, loss, and hyperparameters. We'll learn more about
hyperparameters later in this tutorial.

You can use the arrow keys to navigate to cells that you can't see.

In Guild Compare, note the accuracy for the two runs---they should
be similar. We'd expect this because we trained the same model with
the same flags and data. The only difference between the runs is where
the training occurred!

To exit Guild Compare, press ``q`` (quit).

!!! note
    As with the [](cmd:view) command, [](cmd:compare) will not exit
    until you explicitly stop it.  If you want to keep it running,
    start the command in a [](alias:separate-console). Press ``r``
    (refresh) whenever you want to update the display with the latest
    run status.

    For a complete list of commands supported by Guild Compare, press
    ``?`` while running Guild Compare.

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
displayed in Guild Compare. TensorBoard shows all available scalars for
selected runs, including their values at various stages of training.

## Improve model accuracy

Let's try to improve the accuracy of the model with more training.

To increase the training steps, set the `train-steps` flag to a higher
level. We'll use 10,000 steps this time:

``` command
guild run census:cloudml-train \
  bucket=$BUCKET \
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

Note the accuracy of the newly trained model---it should be a few
percentage points higher than the other two! When you're done
comparing, press ``q`` to exit Guild Compare.

## Scale up

Let's take advantage of Cloud ML's ability to scale! We can train our
model using distributed TensorFlow and multiple workers by setting the
`scale-tier` flag to a multi-worker tier.

See [Scale Tier
->](https://cloud.google.com/ml-engine/reference/rest/v1/projects.jobs#scaletier)
for more information on Cloud ML's supported environments.

By default, Cloud ML operations in Guild AI use the `BASIC` scale
tier, which is suitable for small models and experimentation. We can
alternatively use the `STANDARD_1` scale tier, which uses multiple
workers to train the model in parallel.

Train the model again using 10,000 steps, but this time on the
`STANDARD_1` scale tier:

``` command
guild run census:cloudml-train \
  bucket=$BUCKET \
  scale-tier=STANDARD_1 \
  train-steps=10000 \
  --label scaled-10000
```

This operation will take a similar amount of time as the previous
operation, despite being run on a higher scale tier. This is because
the job setup and teardown overhead dominates the overall operation
time.

We can use TensorBoard to view the time spent in training. If
TensorBoard isn't already running, you can start it directly by
running the following in a [](alias:separate-console):

``` command
guild tensorboard
```

In TensorBoard, in the left sidebar under **Horizontal Axis**, click
**RELATIVE**. This will plot scalars using their relative times along
the horizontal axis. This is useful for viewing time spent actually
training as it does not include job setup and teardown time.

Note the relative times between the last two runs. Our latest run,
which used a higher scale tier, should be noticeably faster for the
same number of steps.

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
    The command below trains the census model 6 times, each
    time using 10,000 steps. While this is still a relatively low cost
    training run, if you're concerned about the cost of this
    operation, feel free to skip this command.

Start a hyperparameter tuning run with 6 trials of 10,000 training
steps each by running:

``` command
guild run census:cloudml-hptune \
  bucket=$BUCKET \
  max-trials=6 \
  train-steps=10000 \
  --label tune-6x-10000
```

This uses the [default tuning configuration
->](https://raw.githubusercontent.com/guildai/packages/master/cloudml/census/hptuning_config.yaml)
provided by the `cloudml.census` package and changes the default
`max-trials` count to 6 from 4. The `max-trials` flag determines how many
trials are run during the hyperparameter tuning operation.

Each trial in Cloud ML is synchronized as a new Guild run, which you
can treat like any other run.

As hyperparameter tuning progresses, use Guild Compare to view the
trial results. As each trial is completed, it will appear as a new run
with its own accuracy and loss. Guild automatically labels trial runs
so you can identify the tuning run that generated them.

To view trial run results while the tuning operation is running, start
Guild Compare in a [](alias:separate-console) by running:

``` command
guild compare
```

As the trials are completed, press ``r`` in Guild Compare to refresh
the display and view the trial results. You can compare the
differences in accuracy and loss to see what hyperparameter values
provide the best result.

!!! note
    The `cloudml-hptune` itself will not have accuracy or loss. It's
    job is limited to starting training run trials, which do have
    accuracy and loss.

!!! tip
    In Guild Compare, you can sort any column in numeric descending
    order by moving the cursor to the column and pressing ``1``. This
    is useful for sorting runs by accuracy---the most accuracy model
    will appear at the top of the list. You can sort in ascending
    order by pressing ``!``. This is useful for sorting runs by loss.

    Note that you must re-order a column after you refresh the display.

Wait for the hyperparameter tuning operation to finish. In the next
section we'll deploy the trial that has the highest accuracy.

## Deploy a model

Now that we've tuned our hyperparameters to find an optimal model (at
least within the six trials that we ran) it's time to deploy a model!

Using Guild Compare, select the run with the highest accuracy. You may
sort runs by accuracy by moving the cursor to the **accuracy** column
and pressing ``1``. This will reorder the runs, displaying the most
accurate run first. Note its run ID (from the **run** column on the
far left) -- we'll use this ID for deployment.

Exit Guild Compare by pressing ``q``.

Define a variable `DEPLOY_RUN` with the run ID you selected:

``` command
echo -n "Run ID to deploy: " && read DEPLOY_RUN
```

When prompted, enter the run ID you'd like to deploy (e.g. the run
with the highest accuracy).

!!! note
    When specifying run IDs in Guild, you don't have to provide
    the entire run ID---you may use a run ID prefix as long as it's
    unique. Usually the first few characters is enough to identify a
    run.

Verify that the specified run is the one you'd like to deploy. You can
confirm the accuracy for `DEPLOY_RUN` by running:

``` command
guild compare $DEPLOY_RUN --table
```

The table should contain a single run. If it contains a run other than
the one you want to deploy, re-enter the run ID using the step above.

When you're ready, deploy the model for your selected run using the
`cloudml-deploy` operation:

``` command
guild run census:cloudml-deploy run=$DEPLOY_RUN bucket=$BUCKET
```

This will create a model in Cloud ML named ``census_dnn`` if one
doesn't already exist. This name is generated using the deployed model
name ``census-dnn``. Cloud ML doesn't allow certain characters in
model names (e.g. ``-``) and Guild replaces these with an underscore
(``_``). If you want to specify a different model name, use the
`model` flag when running the `cloudml-deploy` operation.

After ensuring that a Cloud ML model exists, Guild creates a model
*version*. This deploys the trained model to Cloud ML. By default,
Guild uses a version containing the deployment run ID. If you want to
specify a different version, use the `version` flag when running the
`cloudml-deploy` operation.

For more information on model deployment in Cloud ML, see:

- [Prediction Basics - Model deployment
  ->](https://cloud.google.com/ml-engine/docs/prediction-overview#model_deployment)
  Cloud ML concepts
- [Deploying Models
  ->](https://cloud.google.com/ml-engine/docs/deploying-models) Cloud
  ML how-to guide

Verify the deployed model and its version by running:

``` command
gcloud ml-engine versions list --model census_dnn
```

You should see the newly deployed `census_dnn` model version.

!!! note
    Guild does not provide a complete interface for managing deployed
    Cloud ML models and versions. For a details on Cloud ML models and
    versions, see [gcloud ml-engine
    ->](https://cloud.google.com/sdk/gcloud/reference/ml-engine/)
    command line reference.

List your current runs:

``` command
guild runs
```

Note the latest run---it will be for the `cloudml-deploy` operation
and have a label that contains the deployed model run ID. Deployments
are like any other operation in Guild.

Let's examine the `cloudml-deploy` run:

``` command
guild runs info
```

Note the following attributes in the output:

`cloudml_model_name`
: Name of the deployed Cloud ML model

`cloudml_model_version`
: Version of the deployed Cloud ML model

`cloudml_model_binaries`
: Google Cloud Storage location of the deployed model binaries

`trained_model_run`
: Run ID of the deployed trained model

This information can be used to verify a deployment and is retained as
an artifact of the deploy operation. In the next section, we'll see
how this information is used to run predictions.

## Use a deployed model to make predictions

In our final tutorial segment, we'll use our recently deployed model
to make predictions!

Cloud ML makes predictions by running the inference operation of
deployed model with new data. Data are provided as one or more
*instances*, each corresponding to a prediction that will be made
using the trained model. You may provide instances as JSON or plain
text format.

For details on how Cloud ML makes predictions, see [Prediction Basics
->](https://cloud.google.com/ml-engine/docs/prediction-overview) in
Cloud ML concepts.

Cloud ML can make predictions in two ways: *online* and
*batch*. Online predictions are made immediately and returned in the
operation result. Batch predictions are submitted to Cloud ML as a job
that runs in the background, similar to training. When a batched
prediction job is completed, predictions are written to a file in the
job directory.

In general, online prediction is faster if you have a small number of
predictions to make while batch processing is faster when you need to
make a large number of predictions. The specific performance
characteristics will vary across models. Refer to [Online prediction
versus batch prediction
->](https://cloud.google.com/ml-engine/docs/prediction-overview#online_prediction_versus_batch_prediction)
in Cloud ML Prediction Basics for more information.

We'll use both techniques to see how each works.

### Online prediction

First, let's run an online prediction:

``` command
guild run census:cloudml-predict
```

Guild will prompt you before running the operation. Press `Enter` to
run the operation.

The prediction is made using the latest deployed version of the
`census-dnn` model (`census_dnn` in Cloud ML). The model package
provides sample inputs to make the prediction. You can specify your
own using the `instances` flags.

To experiment with your own inputs, download the [census prediction
samples
->](https://raw.githubusercontent.com/guildai/packages/master/cloudml/census/prediction-samples.json)
and make changes accordingly. Assuming your samples is named
`census-inputs.json` and is located in the current directory, you can
run a `cloudml-predict` operation using:

```
guild run census:cloudml-predict instances=census-inputs.json
```

For online prediction, the results are printed to the
console. However, they are also saved as a file in the run
directory. Let's take a look!

If Guild View isn't already running, start it in a
[](alias:separate-console) by running:

``` command
guild view
```

In Guild View, select the latest run---it should be a
`cloudml-predict` operation---and click the **FILES** tab. The run
will have two files:

`prediction.inputs`
: The inputs used in the prediction

`prediction.results`
: The prediction results

Click on **`prediction.results`** to see how the instances were
classified by the deployed model. The values correspond to the inputs
provided in `prediction.inputs`. Click the **NEXT** button to view the
contents of `prediction.inputs`.

!!! tip
    Guild View can be used to view the contents of some files:
    text files, images, and audio. Look for a grey button background
    on the file name, which can be clicked to open the file.

As you can see, the `cloudml-predict` operation generates a run like
other operations. In this case the run contains information about the
model version used to make the prediction along with the prediction
inputs and outputs.

### Batch prediction

In the previous section we performed an *online* prediction that
returned the result immediately. In this section we'll use *batch*
prediction. Batch prediction runs on Cloud ML as a job.

We use the `cloudml-batch-predict` operation to start a prediction
job. Start a batch prediction job by running:

``` command
guild run census:cloudml-batch-predict bucket=$BUCKET
```

This will use the sample prediction inputs as before. We need to
specify `bucket` to tell Guild where to create the job.

The job will take some time to complete. When finished, it will save
generated a file named `prediction.results-00000-of-00001`, which you
can view in Guild View, or inspect from the command line.

When the operation has finished, view the generated files by running:

``` command
guild runs info --files --full-path
```

The ``--full-path`` option is used to show the full path to
`prediction.results-00000-of-00001`, which you can use to copy or view
the file.

You may use online or batch predictions as needed to use your deployed
models in Cloud ML!

## Summary

In this tutorial we worked with Google's Cloud Machine Leaning Engine
(Cloud ML) to train and deploy a classifier.

We covered a number of topics:

- Train a model locally to sanity-check our results and then train in
  Cloud ML to scale up

- Use hyperparameter tuning in Cloud ML to optimize our predictive
  accuracy with a set of hyperparameter values

- Evaluate runs using Guild View, Guild Compare, and TensorBoard

- Select an optimized model and deploy it to Cloud ML

- Use a model deployed in Cloud ML to make predictions using new data

Guild AI models and their operations encapsulate the complexities of
this process, letting you focus on the high level workflow and get
your work done faster!

## Cleanup

Over the course of this tutorial we generated a number of runs and
Cloud ML jobs. If you no longer need these, you may delete them to
free up resources.

### Delete unneeded Cloud ML jobs

Use the `gsutil` program to delete any jobs from your Cloud Storage
bucket that you don't need. To delete all Guild related files, run:

``` command
gsutil rm -r gs://$BUCKET/guild_*
```

### Delete unneeded Cloud ML model versions

Use the `gcloud` program to delete any model versions you don't need.

First, list the model versions:

``` command
gcloud ml-engine versions list --model census_dnn
```

For each version that you want to delete, run:

``` command
gcloud ml-engine versions delete --model census_dnn VERSION
```

where `VERSION` is the model version you want to delete.

If you no longer need the model, you may delete it provided there are
no versions associated with it:

``` command
gcloud ml-engine models delete census_dnn
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
*permanent*. This ensures that the runs no longer consume disk
space. Omit this option if you want to retain the ability to restore
them at a later time. Note that disk space will not be freed up for
these jobs until you permanently delete them (see the [](cmd:purge)
command).

Finally, if you deleted any runs without using the ``-p`` option and
you want to free up disk space consumed by them, you can can
permanently delete them by running:

``` command
guild runs purge
```

!!! important
    Review the list of runs carefully before permanently deleting
    them!

## Next steps

- Read [Cloud ML Engine - Getting Started
  ->](https://cloud.google.com/ml-engine/docs/getting-started-training-prediction)
  to view the same workflow using lower-level Cloud ML commands
