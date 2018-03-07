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

You can later restore a deleted run using (cmd:runs-restore)[runs
restore].

## Resources

### If a source is referenced multiple times, does Guild download each occurrence?

No, Guild will only download the source once. There is no performance
penalty for referencing a resource source multiple times.

## Runtime characterisics

### How much overhead does Guild incur when running an operation?

Guild runs operations in a separate OS process to ensure that the
operation is isolated. As of Guild 0.3.0, the additional overhead
incurred when running an operation is as follows:

- Additional time: typically less than 100 milliseconds but may be
  more on slower systems or loaded systems

- Additional resident RAM: less than 40 MB

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
