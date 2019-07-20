title: Quick Ref
navbar_item: yes
hide_sidenav: yes

# Quick Reference

[TOC]

<div class="row"></div>

<div class="col col-lg-6" markdown="1">

## Install Guild AI

Use the [pip command ->](https://pip.pypa.io/en/stable/installing/)
to install Guild AI:

``` command
pip install guildai
```

Install without admin privileges:

``` command
pip install guildai --user
```

Install with elevated priviledges (Linux and macOS):

``` command
sudo pip install guildai
```

More information:

- [Detailed installation steps](/install/)

</div>

<div class="col col-lg-6" markdown="1">

## Check Environment

Verify that Guild is installed:

``` command
guild check
```

To get more details about your environment use the `--verbose` option:

``` command
guild check --verbose
```

More information:

- [Guild environments](/environments/)
- [`check` command](/commands/check/)

</div>

<div class="row"></div>

<div class="col col-lg-6" markdown="1">

## Run a Script

Run a script directly to generate an experiment:

``` command
guild run train.py
```

`train.py` in this case is a training script located in the current
directory.

#### Flags

If the script accepts flags, you can specify a values when running it:

``` command
guild run train.py learning_rate=0.01
```

#### Grid Search

To run a script over multiple flag values, specify a list of values
for each flag:

``` command
guild run train.py \
  learning_rate=[0.01,0.001] \
  batch_size=[50,100]
```

This command will run `train.py` four times --- one run for each
possible combination of flag values.

#### Random Search

To run a script using randomly selected values, specify a
*distribution* search space for a flag:

``` command
guild run train.py \
  --max-trials 10 \
  learning_rate=loguniform[1e-5:1e-2] \
  batch_size=50
```

This runs 10 trials using randomly selected values for `learning_rate`
using a loguniform distribution and the fixed value 50 for
`batch_size`.

To specify a uniform distribution, replace `loguniform` with `uniform`:

``` command
guild run train.py dropout=uniform[0.1:0.8]
```

Alternatively, in the case of `uniform`, you can omit the name
altogether. This command is equivalent to the previous command:

``` command
guild run train.py dropout=[0.1:0.8]
```

#### Hyperparameter Optimization

To optimize hyperparameters (i.e. find flag values that minimize loss)
use the `--optimizer` option:

``` command
guild run train.py \
  --max-trials 10 \
  --optimizer bayesian \
  learning_rate=loguniform[1e-5:1e-2] \
  batch_size=50
```

</div>

<div class="col col-lg-6" markdown="1">

## View Results

List your experiments, which are also called *runs*:

``` command
guild runs
```

View information for a run:

``` command
guild runs info [RUN]
```

`RUN` is either a run index (a number displayed in the runs list) or a
run ID. If you omit `RUN`, the latest run is used.

#### List Run Files

List files associated with a run:

``` command
guild ls [RUN]
```

#### Open Run Files

Open the directory containing run files:

``` command
guild open [RUN]
```

This command works only when running from a desktop environment.

#### Open TensorBoard

View run results in TensorBoard:

``` command
guild tensorboard [RUN]
```

If `RUN` is not specified, Guild opens all runs in TensorBoard.

By default, Guild runs TensorBoard on a randomly assigned port. To run
TensorBoard on an explicit port, use the `--port` option:

``` command
guild tensorboard --port 8080
```

</div>

<div class="row"></div>

<div class="col col-lg-6" markdown="1">
</div>

<div class="row"></div>

<div class="col col-lg-6" markdown="1">
</div>

<div class="row"></div>

<div class="col col-lg-6" markdown="1">
</div>

<div class="row"></div>

<div class="col col-lg-6" markdown="1">
</div>

<div class="row"></div>

<div class="col col-lg-6 qref" markdown="1">
## Operations

### Scripts

Run a script directly:

``` command
guild run SCRIPT_FILENAME
```

### Guild File Operations

If the current directory contains a [Guild file](term:guildfile) you
can run operations defined in that file.

List operations defined in the current directory Guild file:

``` command
guild operations
```

To run an operation:

``` command
guild run OPERATION_NAME
```

Specify flag values for an operation:

``` command
guild run OPERATION FLAG_NAME=VALUE
```

### Operation Help

To view help for an operation, use the [run](cmd:run) command with the
`--help-op` option:

``` command
guild run OPERATION --help-op
```

</div>

<div class="col col-lg-6" markdown="1">
## Do Something Else
</div>

<div class="row"></div>
