# Guild View

[TOC]

## Overview

Guild View is a web based application that lets you view runs and
compare results.

To start Guild Run, use the [view](cmd:view) command from a command
line terminal.

``` command
guild view
```

Guild starts the application and opens it in a web browser.

## Run Guild View Remotely

To access Guild View from a remote server, your local browser must
have network connectivity to the remote server. This typically
requires that specific ports be made available through a firewall or
network router.

To specify a port when running Guild View, use the `--port`
option. For example, if port `8080` is open on the remote server, run:

``` command
guild view --port 8080
```

``` output
Running Guild View at http://hostname:8080 (Type Ctrl-C to quit)
```

!!! important
    Guild will not automatically open Guild View in your
    browser when you run `guild view` remotely. You must open the URL
    show in the console terminal.
