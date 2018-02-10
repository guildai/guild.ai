tags: support

# FAQ

[TOC]

## Manage runs

### How do I quickly delete failed runs?

Guild saves every run whether it succeeds or not. This lets you
troubleshoot issues But over time failed runs can accumulate and
you'll want to delete them.

Use this command to delete failed runs:

``` command
guild runs delete --error
```

Use this command to delete terminated runs (i.e. runs that were
stopped by the user by typing `CTRL-c`):

``` command
guild runs delete --terminated
```

You can delete both failed and terminated runs by using both
``--error`` and ``--terminated`` options at the same time, or using
this short form:

``` command
guild runs delete -ET
```

Guild will let you confirm the list of runs before deleting them.

You can later restore a deleted run using (cmd:runs-restpre)[runs
restore].

## Troubleshooting

### How do I know which library version I'm using?

The [](cmd:check) command shows software library versions:

- Guild AI
- Python
- TensorFlow
- CUDA and cuDNN

To show this information, run:

``` command
guild check
```

To show more information, use the ``--verbose`` option:

``` command
guild check --verbose
```
