# Guild Compare

[TOC]

## Overview

Guild Compare is a [curses based application
->](https://en.wikipedia.org/wiki/Curses_(programming_library)) that
you run from the command line. It's convenient both for local and
remote comparisons as it works equally well over ssh.

Use Guild Compare to view runs in a spreadsheet format including flags
and scalar values.

![](/assets/img/compare-feature-2.png)

^ Guild Compare shows runs in a spreadsheet format

!!! tip
    Guild Compare runs in terminals across SSH connections. It's
    convenient for viewing results on remote servers without having to
    run servers or copy files.

## Start Guild Compare

To start Guild Compare, run:

``` command
guild compare
```

This shows all available runs. You can limit the runs using filters
like operation, status, and start time. For a list of filters, see
[](cmd:compare).

## Interactive Mode

By default, Guild Compare runs in *interactive mode*. It runs as an
application that lets you explore runs using key commands.

For a list of supported key commands, press `?` when running in
interactive mode.

Below are some common actions you perform in interactive mode.

Navigate
: Use the arrow keys to move the active cell to different rows and
  columns.

Sort runs by a column
: Use the arrow keys to navigate to the column you want to sort by.
  Press `1` to sort in ascending order or `2` for descending.

Refresh the display with the latest information
: Press `r` (for refresh) at any point to show the latest
  information. Guild does not automatically update the display.

View run details
: Press `Enter` to view details for a selected run. Press `q` to exit
  the detail window.

List key bindings
: Press `?` to show the list of key bindings. To exit the list, press
  `q`.

Exit
: Press `q` to exit Guild Compare.

## Export Data

You can use Guild Compare to generate a CSV file with run data.

To export data to a CSV file, use the `--csv` option.

``` command
guild compare --csv runs.csv
```

^ Writes runs compare data to `runs.csv`

To print the CSV contents to the console, use ``-`` for the file name:

``` command
guild compare --csv -
```

^ Prints runs compare data to the console

## Compare Tools

Guild supports *tool extensions* that let you compare runs using
different tools.

To compare runs using a tool extension, use the `--tool` option with
the tool name.

For example, to compare runs using HiPlot, run:

``` command
guild compare --tool hiplot
```

Supported tools:

`hiplot`
: Use [HiPlot ->](https://facebookresearch.github.io/hiplot/) to
  compare runs.

Refer to the sections below for detail on each tool.

### HiPlot

HiPlot is a visualization tool developed by Facebook used to discover
correlations and patterns in high-dimensional data. It has a high
performance parallel plots graphing engine that can be used as an
alternative to TensorBoard's HParams plugin.

![](/assets/img/hiplot.png)

^ Compare runs using Facebook's HiPlot visualization tool

To use HiPlot with Guild Compare, first install the HiPlot Python
library:

``` command
pip install hiplot
```

Verify that the `hiplot-render` program is installed:

``` command
hiplot-render --help
```

If you get an error, confirm that HiPlot is installed correctly. Refer
to [Installing
HiPlot](https://facebookresearch.github.io/hiplot/getting_started.html#installing)
for help.

To use HiPlot with Guild Compare, run:

``` command
guild compare --tool hiplot
```

#### Alternate location of `hiplot-render`

Use the `HIPLOT_RENDER` environment variable to specify an alternative
location to the `hiplot-render` program. This is useful when running
HiPlot from a location that isn't on your system path.
