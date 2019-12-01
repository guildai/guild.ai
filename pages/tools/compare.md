sidenav_title: Compare

# Guild Compare

TODO

Guild Compare is a [curses based application
->](https://en.wikipedia.org/wiki/Curses_(programming_library)) that
you run from the command line. It's convenient both for local and
remote comparisons as it works equally well over ssh.

Use Guild Compare to view runs in a spreadsheet format including flags
and scalar values.

![](/assets/img/compare-feature-2.png)

^ Guild Compare shows runs in a spreadsheet format

### Start Guild Compare

To start Guild Compare, run:

``` command
guild compare
```

This shows all available runs. You can limit the runs using filters
like operation, status, and start time. For a list of filters, see
[](cmd:compare).

### Use the Application

Sort runs by a column
: Use the arrow keys to navigate to the column you want to sort by.
  Press `1` to sort in ascending order or `2` for descending.

Refresh the display with the latest information
: Press `r` (for refresh) at any point to show the latest
  information. Guild does not automatically update the display.

List key bindings
: Press `?` to show the list of key bindings. To exit the list, press
  `q`.

Exit
: Press `q` to exit Guild Compare.

### Export Data

You can use Guild Compare to generate JSON and CSV files with run
details.
