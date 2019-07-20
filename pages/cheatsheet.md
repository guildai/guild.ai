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

For general documentation on Guild files see, [Guild
Files](/guildfiles.md).

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
#

# Read the annotations below and modify this file as needed. We
# recommend that you remove any annotations that you don't need so
# that your final Guild file remains small and easily readable.

# For help with Guild files, see https://guild.ai/guildfiles/

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

  # By default, Guild snapshots your project source code for each
  # operation. You can view and diff your source code files later
  # using commands such as:
  #
  #  $ guild ls --sourcecode
  #  $ guild open --sourcecode
  #  $ guild diff --sourcecode

  # Note that you can only include one 'sourcecode' section. If you
  # uncomment any of the sections below, ensure that it is the only
  # section you uncomment.
  #
  # If you want to disable source code snapshots, uncomment the
  # following line:

  #sourcecode: no

  # By default, Guild considers any text file that is less than 1M in
  # size to be "source code". Additionally, Guild only copies at most
  # 1000 source code files. These measures ensure that Guild does not
  # mistakenly copy large files (e.g. such as data sets stored as
  # text) or copy too many file.
  #
  # You can specify explicitly which files in your project should be
  # copied as source code.
  #
  # The line below tells Guild to copy only Python source files. Note
  # that you must include the wild card character '*' in quotes to
  # comply with YAML synaxt rules.

  #sourcecode: '*.py'

  # To specify multiple patterns, use a list of patterns. The block
  # below indicates that Guild copy only Python source files and files
  # ending in '.txt'.

  #sourcecode:
  #  - '*.py'
  #  - '*.txt'

  # You can also indicate that Guild should exclude certain files. For
  # example, if you have a csv file that should not be treated as
  # source code, you can exclude it using:

  #sourcecode:
  #  - exclude: my_dataset.csv

  # To include specific files that would not otherwise be treated as
  # source code by Guild (e.g. they are binary files such as images or
  # they are larger than 1M), explicitly include them as the block
  # below illustrates. Note that these includes are applied in
  # addition to the default rules - files that match the patterns are
  # added to the default list of copied source files.

  #sourcecode:
  #  - include: my_image.png
  #  - include: my_very_large_file.csv

  # Include and exclude directives can be used together for more
  # advanced specifications. Directives are applied in the order
  # specified.

  #sourcecode:
  #  - exclude: '*'
  #  - include: '*.py'
  #  - exclude: 'dont_include.py'

  # If your source code is not located in the same directory as the
  # Guild file - e.g. it's in the parent directory or in a
  # subdirectory - you can specify an alternative root directory to
  # copy from. Uncomment the block below to use this feature. Note
  # that the value for 'select' below in this case is used as the file
  # selection specification - any of the examples above can be used
  # for the 'select' value below. To apply the default copy rules, you
  # can omit 'select'.

  #sourcecode:
  #  root: ..
  #  select: '*.py'

  # -----------------------------------------------------------------
  # Required files
  # -----------------------------------------------------------------

  # When Guild runs an operation, it first creates an empty directory
  # for the run. This is referred as the 'run directory'. Running each
  # operation in a unique directory ensures that each experiment is
  # kept separate. The directory is initially empty to control the
  # files used during the run.
  #
  # The run directory is configured as the current working directory
  # for each operation. This means that project files that you expect
  # to be available to the script will not be available - at least by
  # default.
  #
  # To access a file from the run directory, you must define the file
  # in the operation 'requires' section. Guild supports several ways
  # to define required files. Each method tells Guild how to resolve
  # any files needed by the operation.
  #
  # Note that Guild does not copy required files to the run
  # directory. It creates symbolic links to them. For this reason,
  # Guild requires permission to create symolic links (on Windows,
  # this permission is not granted to unpriviledged users by default).
  #
  # In some cases, Guild uses a resource cache to save files
  # (e.g. when downloading files and when unpacking archives). The
  # resource cache is located under Guild home (use 'guild check' to
  # see where Guild home is) in the directory 'cache/resources'. If
  # you want to clear this cache, simply delete that directory.
  #
  # Once you have defined a required file (e.g. using one of the
  # samples below) you can test the run directory layout without
  # actually running the operation by using the '--stage' option of
  # the run command. When using the '--stage' option, specify a
  # directory to serve as the run directory. You can then study the
  # run directory to config that it's layed out as you expect.
  #
  #  $ guild run train --stage /tmp/train-stage
  #
  # Note that only one 'requires' section may be defined. If you
  # uncomment any of the sections below, ensure that it is the only
  # section that you uncomment. If you want to combine examples, copy
  # the applicable items to your one 'requires' section.
  #
  # The sample block below defines a single file 'my_config.yml'. When
  # the operation is run, Guild creates a symbolic link to this file
  # in the run directory. If this file doesn't exit, Guild exits with
  # an error indicating that a required resource cannot be resolved.

  #requires:
  #  - file: my_config.yml

  # In some cases, your script may require files in a directory
  # located in your project. You can include the directory as a file
  # as well. The block below creates a link to the directory
  # 'my_config_subdir' in the run directory.

  #requires:
  #  - file: my_config_subdir

  # If you specify an archive (e.g. zip, tar, compressed tar) Guild
  # will automatically unpack the archive in its resource cache
  # directory and create links to each top-level archive file. The
  # block below indicates that files contained in 'samples.zip'
  # are available in the run directory.

  #requires:
  #  - file: samples.zip

  # You can indicate that an archive should not be unpacked using the
  # 'unpack' attribute.

  #requires:
  #  - file: samples.zip
  #    unpack: yes

  # URLs may also be specified. Guild automatically downloads files to
  # its resource cache. If the downloaded file is an archive, Guild
  # unpacks it according to the rules above. This block tells Guild to
  # download a file and unpack it in preparation for a run.

  #requires:
  #  - url: https://my.co/datasets/mnist.zip

  # The block below combines several file requirements.

  #requires:
  #  - file: samples.zip
  #  - file: config_files
  #  - url: https://my.co/datasets/cifar.zip

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
