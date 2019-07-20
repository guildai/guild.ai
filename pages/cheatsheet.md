title: Cheatsheet
navbar_item: yes
hide_sidenav: yes

# Cheatsheet

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

Compare results side-by-side, including flag values (e.g. learning
rate, batch size, etc.) and scalars (e.g. loss, accuracy, etc.):

``` command
guild compare
```

#### Run Info

View information for a run:

``` command
guild runs info [RUN]
```

`RUN` is either a run index (a number displayed in the runs list) or a
run ID. If you omit `RUN`, the latest run is used.

To show scalars:

``` command
guild runs info [RUN] --scalars
```

#### Run Output

Print run output to standard output:

``` command
guild cat --output [RUN]
```

#### List Run Files

List files associated with a run:

``` command
guild ls [RUN]
```

#### View Run Files

Use your local file explorer to open the directory containing run
files:

``` command
guild open [RUN]
```

To open a specific file (e.g. to view an image):

``` command
guild open --path path_to_image.png
```

Note: the `open` command only work when running from a desktop
environment.

#### View Runs in TensorBoard

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

<div class="col col-lg-12" markdown="1">

## Guild File - Basic

Use the template below to get started quickly with a basic Guild file.

For other examples and detailed code snippets, see [Create a Guild
File - Examples](/howto/create-guildfile.md#examples).

For general documentation on Guild files see, [Guild File](/guildfile.md).

``` yaml
# ===================================================================
# Sample Guild file
# ===================================================================
#
# This is a sample Guild file. Save the contents as guild.yml to your
# project directory and modify as needed.
#
# In this basic format, Guild files define operations as mapped
# attributes. Each key is the operation name. In the example below, we
# define a single example 'train'. When defined for a project, run the
# operation using:
#
#  $ guild run train
#
# Get help for the train operation by running:
#
#  $ guild run train --help-op
#
# Get help for the entire project by running:
#
#  $ guild help

train:

  description: Train the model

  # -----------------------------------------------------------------
  # Python main module
  # -----------------------------------------------------------------

  # The 'main' attribute specifies the Python module to run for the
  # operation.
  #
  # The value 'train' below tells Guild to run a Python module defined
  # in the file 'train.py' located in the project directory.
  #
  # If your module is defined in a subdirectory, include the
  # subdirectory in the value as 'subdir/train'. If your module is
  # defined in a Python package (i.e. a subdirectory containing
  # '__init__.py') use the value 'package.train'.

  main: train

  # -----------------------------------------------------------------
  # Flags
  # -----------------------------------------------------------------

  # Flags are user-defined inputs to an operation. All hyperparameters
  # are flags, though flags aren't necessarily hyperparameters.
  #
  # Default flag values are used unless the user redefines them when
  # running the operation like this:
  #
  #  $ guild run train learning_rate=0.001
  #
  # By default, Guild tries to import flags automatically by
  # inspecting the Python main module specified above. To disable this
  # functionality, uncomment the following line:

  #flags-import: no

  # If you want Guild to automatically import flags, but you want to
  # explicitly limit the list of flags imported, uncomment the
  # following block and modify the list of flags to import:

  #flags-import:
  #  - batch_size
  #  - learning_rate

  # If you want to import most of the flags but skip specific imports,
  # uncomment the following block and modify the list of flags to
  # skip:

  #flags-imports-skip:
  #  - num_classes
  #  - another_flag_to_skip

  # To define flags explicitly in this file, define them under the
  # 'flags' section below. Note that flags are still imported from the
  # Python main module according to the rules above. Flag attributes
  # defined below will override imported values (specifically default
  # value and description if provided via argparse).
  #
  # Modify the flags section below as needed to define your flag
  # attributes. If you're happy with the imported flags (based on the
  # import settings above) you can delete this section altogether.

  flags:
    batch_size:
      description: Batch size used for training

      # Flag default values are imported according to the import rules
      # above. If you To redefine a default, uncomment the line
      # below. Similarly, if you have disable flag imports altogether,
      # define flag defaults the same way.

      #default: 100

    learning_rate:
      description: Learning rate used for training
      default: 0.01

  # -----------------------------------------------------------------
  # Scalars
  # -----------------------------------------------------------------

  # Scalars are named values that are generated by an
  # operation. Scalars are used to convey results such as training
  # loss, accuracy, and other metrics. Scalar values are associated
  # with steps, allowing you to record scalar values over multiple
  # training iterations.
  #
  # By default, Guild automatically detects scalars in operation
  # output (both standard output and standard error streams) that
  # match the format:
  #
  #  KEY: VALUE
  #
  # - KEY must not contain any leading white space and may only
  #   contain non-whitespace characters
  #
  # - VALUE must be represented as a valid number (integer or floating
  #   point value)
  #
  # The current scalar step is detected by looking for the 'step: N'
  # pattern. Guild remembers the last detected step and uses it for
  # subsequent logged scalars. The step is changed for scalars when it
  # is logged again.
  #
  # Guild detects scalars in output using Python regular
  # expressions. For details on regular expression syntax, see
  # https://docs.python.org/3/library/re.html.
  #
  # Scalars and keys are captured using regular expression
  # groups. Guild supports different ways of capturing scalars. See
  # the examples below for details.
  #
  # To simplify the use of key and value patterns, Guild supports two
  # regular expression aliases:
  #
  #   \key       matches any repeating non-whitespace characters
  #   \value     matches a string that can be converted to a number
  #
  # These aliases can be used to in regular expression groups to match
  # scalar keys and values respectively.
  #
  # To help debug output scalar patterns, Guild provides a
  # '--test-output-scalars' option with the run command. To debug
  # output in a file, use:
  #
  #  $ guild run train --test-output-scalars SAMPLE_OUTPUT_FILE
  #
  # You can alternatively use '-' as the file to read from standard
  # intput. This reads and evaluates each line as you enter it. To
  # exit, press Enter without providing a value.
  #
  #  $ guild run train --test-output-scalars -
  #
  # Type one of more non-empty lines that you want to test. When
  # you're done entering lines, press Enter (providing a final empty
  # line) and Guild will test the output provided.

  output-scalars:

    # The default pattern is specified below. It matches output in the
    # format:
    #
    #  KEY: VALUE
    #
    # If you're happy with this pattern, you can delete this entry
    # along with the 'output-scalars' section. Otherwise, modify the
    # sections below to match your script output.

    - '^(\key):\s+(\value)'

    # To match scalars with specific patterns, uncomment the block
    # below and modify the keys and regular expressions
    # accordingly. Note that the regular expressions use only one
    # group. When a single regular expression group is specified, that
    # group is used to capture the scalar value. In this case, you
    # must provide a mapping of scalar keys to patterns.
    #
    # Note also that 'step' is explicitly defined. The special
    # attribute 'step' is used by Guild to set the step associated
    # with subsequently logged scalars. While this special attribute
    # name cannot be changed (it must be named 'step'), you can define
    # a custom pattern, as shown below.

    #- step: '^Step (\value) of [0-9]'
    #  loss: '^my_script_loss: (\value)'
    #  accuracy: '^my_script_acc: (\value)'

  # -----------------------------------------------------------------
  # Source code snapshots
  # -----------------------------------------------------------------

  # Guild snapshots your project source code for each operation.

```
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
