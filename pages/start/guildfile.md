# Create a Guild File

In the previous sections, you ran a script `train.py` directly with
Guild. In this section, you run the same script as an
[operation](term:operation) defined in a [Guild file](ref:guildfile).

Guild files provide information about your scripts so Guild can run
them without modifications.

In the `guild-start` directory from [Get Started](../start.md), create
a file named `guild.yml` that contains this YAML configuration:

``` yaml
- model: sample
  description: A sample (mock) model
  operations:
    train:
      description: Generate a sample loss
```

^ Guild file `guild.yml`

Your directory should look like this:

<div class="file-tree">
<ul>
<li class="is-folder open">guild-start
 <ul>
 <li class="is-file">guild.yml</li>
 <li class="is-file">train.yml</li>
 </ul>
</li>
</ul>
</div>

## Show Project Info

From the `guild-start` directory, run:

``` command
guild help
```

``` output
OVERVIEW

    You are viewing help for models defined in the current directory.

    To run a model operation use 'guild run MODEL:OPERATION' where MODEL
    is one of the model names listed below and OPERATION is an associated
    operation.

    You may set operation flags using 'FLAG=VALUE' arguments to the run
    command. Refer to the operations below for a list of supported flags.
    Model flags apply to all operations.

    For more help, try 'guild run --help' or 'guild --help'.

MODELS

    sample

      A sample (mock) model

      Operations:

        train
          Generate a sample loss

          Flags:
            x  (default is 0.1)

```

Guild displays help for the current project, which is generated from
the Guild file.

Press `q` to exit help.

List models defined for the project:

``` command
guild models
```

``` output
sample  A sample (mock) model
```

List operations defined for the project:

``` command
guild ops
```

``` output
sample:train  Generate a sample loss
```

## Delete Runs (optional)

In preparation for the operations below, we recommend that you delete
your existing runs. Recall from [Manage Run](runs.md) that you can
restore deleted runs later.

``` command
guild runs rm
```

Press `Enter` to confirm.

## Run an Operation

Run the `train` operation for the `sample` model:

``` command
guild run sample:train
```

``` output
You are about to run sample:train
  x: 0.1
Continue? (Y/n)
```

Press `Enter` to confirm.

Guild runs the module defined in `train.py`. It uses the operation
name to infer the main module. Later you control the module that Guild
runs.

Guild imports the flag `x` and its default value 0.1 from
`train.py`. Later you control the flags that are imported and how they
are applied to a script.

View available runs:

``` command
guild runs
```

``` output
[1:19be34a8]  sample:train  2019-09-23 14:44:13  completed
```

When running an operation, use `--help-op` to show help without
running anything.

``` command
guild run train --help-op
```

``` output
Usage: guild run [OPTIONS] sample:train [FLAG]...

Generate a sample loss

Use 'guild run --help' for a list of options.

Flags:
  x  (default is 0.1)
```

!!! tip
    The `--help-op` option is useful when you're typing a command
    and forget the names of available flags.

## Next Steps

In this section, you created a Guild file that defines a `train`
operation. The operation is an abstraction for the script
`train.py`. It provides additional help text that users can view by
running various Guild commands.

In the next section, you create a real classifier using [scikit-learn
support vector machines
-](https://scikit-learn.org/stable/modules/svm.html).
