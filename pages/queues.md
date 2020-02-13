tags: concept

# Queues

<!-- TODO

This page needs to be filled out. There's a conceptual problem with
queues and parallel runs, escp with batches.

-->

!!! important
    Queues are currently experimental in Guild.

A *queue* is a long-running runs implemented by the built-in `queue`
operation. A queue is used to start staged runs.

Queues can be used to:

- Schedule runs
- Run operations in parallel
- Assign runs to GPUs

To start a queue, run:

``` command
guild run queue
```

Once running, queues look for staged runs and start them under the
following conditions:

- The queue is not waiting for a run to complete
- The staged run is compatible with the queue GPU affinity

A queue waits for a run to complete when:

- The queue starts the run
- The queue is started with the `ignore-running` flag equal to `no`
  (default)

A run matches a queue GPU affinity when:

- The queue is started with an undefined `gpu` flag (default) *and*
  the staged run does specify a GPU affinity
- The queue `gpu` flag value matches the staged run GPU affinity

Queues coordinate amoung themselves when starting runs so you can
start multiple queues as needed.

## Schedule Staged Runs

Use a queue to start staged runs in the order staged. This is useful
when you want to run several operations back-to-back without attending
them.

To use a queue to stage runs, first start a queue in the background:

``` command
guild run queue --background
```

Check status of the operation as needed using ``guild runs``.

To list running runs, use:

``` command
guild runs --running
```

You can stop runs using [stop](cmd:stop).

Stage a run by specifying the `--stage` option. For example, to stage
an run for `train`, run:

```
guild run train --stage
```

Guild initializes the run but does not start it. Instead, the queue,
running in the background, starts the queue and waits for it to
finish. You can continue staging runs as needed.

Staged runs have a status of ``staged``, which you can filter by
running:

``` command
guild runs --staged
```
