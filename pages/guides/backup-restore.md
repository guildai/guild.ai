# Backup and Restore

Guild lets you backup runs to the cloud and restore those runs at a
later time. This is useful for safeguarding runs from accidental
deletion and can be used for collaboration.

This guide demonstrates Guild's backup and restore capabilities on
Amazon S3. Refer to [Requirements](#requirements) below for more
information.

!!! important
    Storing files on S3 will incur ongoing costs. Refer to
    [Cleanup](#cleanup) below for steps to delete all files uploaded
    to S3 from this guide.

## Requirements

{!start-requirements-3.md!}

In addition, you must complete the following steps for Amazon S3
bucket support:

- [Sign up for Amazon S3 ->](https://docs.aws.amazon.com/AmazonS3/latest/gsg/SigningUpforS3.html)
- [Create an S3 bucket ->](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
- [Allow read and write access to S3 bucket ->](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_s3_rw-bucket.html)
- [Install AWS CLI ->](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

Note the name of the S3 bucket created.

Note the AWS access key ID and secret access key of the IAM user who
has write access to the S3 bucket.

## Create a `remote` entry in Guild config

Using your text editor, open `~/.guild/config.yml`.

Add the following to the bottom of the file:

``` yaml
remotes:
  s3:
    type: s3
    bucket: <name of S3 bucket>
```

^ Adding `s3` to the `remotes` section in `~/.guild/config.yml`

Replace `<name of S3 bucket>` with the name of the S3 bucket created
in [Requirements](#requirements) above.

!!! note
    If a `remotes` section already exists in `config.yml`, omit
    that line from the snippet above and only copy the lines after
    `remotes`.

Save you changes to `~/.guild/config.yml`.

## Set AWS environment variables

In a command line console, set the following environment variables:

``` command
export AWS_ACCESS_KEY_ID=<access key ID>
export AWS_SECRET_ACCESS_KEY=<secret access key>
```

Replace `<access key ID>` and `<secret access key>` with the
respective values associated with the IAM user who has write access to
the S3 bucket.

!!! important
    If you open a new command line console, you must re-run
    the export commands above.

Verify that you have access to the S3 bucket:

``` command
guild remote status s3
```

Guild checks the status of the `s3` remote. If you have access, you
will see:

``` output
s3 (S3 bucket <name>) is available
```

If you get a different message, verify the following:

- Configured S3 bucket exists
- Security credentials defined above by `AWS_ACCESS_KEY_ID` and
  `AWS_SECRET_ACCESS_KEY` are associated with an AWS security policy
  that has read/write access the configured S3 bucket

If you're unable to resolve the issue, [ask for help](ref:get-help).

## Run `fashion_mnist_mlp.py`

Train the Fashion-MNIST classifier by running:

``` command
guild run fashion_mnist_mlp.py
```

Press `Enter` to start training.

This creates a run that we backup in the next step.

## Backup latest run to S3

Copy the latest run to the `s3` remote by running:

``` command
guild push 1 s3
```

The `1` in the command tells Guild to only copy the latest run. `s3`
is the name of the remote you configured above.

Guild prompts before copying:

``` output
You are about to copy (push) the following runs to s3:
  [0def3262]  fashion_mnist_mlp.py  2019-03-22 11:53:44  completed
  Continue? (Y/n)
```

Press `Enter` to continue.

Guild copies the latest run to the S3 bucket. You can verify this
using the [AWS Management Console
->](https://aws.amazon.com/console/).

Additionally, you can list runs available on the `s3` remote using:

``` command
guild runs -r s3
```

``` output
Synchronizing runs with s3
[1:0def3262]  fashion_mnist_mlp.py  2019-03-22 11:53:44  completed
```

## Delete the latest local run

Later we restore the `fashion_mnist_mlp.py` run from S3 --- so let's
delete the local run first:

``` command
guild runs rm 1
```

Once again, the number `1` in the command tells Guild to only delete
the latest run.

Press `Enter` to delete the run.

## Restore the deleted run

In this step, we restore the deleted run by copying it from its backup
location on S3.

To copy latest the run, use:

``` command
guild pull s3 1
```

As with the earlier commands, the number `1` indicates that we only
want to copy the latest run from S3. If you omit this argument, Guild
will copy all of the runs from S3.

Press `Enter` to copy the run from S3.

You can verify that the run has been copied with:

``` command
guild runs info
```

Compare that information to the same command applied to the remote:

``` command
guild runs info -r s3
```

## Cleanup

To delete all of the runs from S3, run:

``` command
guild runs rm --permanent -r s3
```

Note that this command deletes *all* of the runs from the `s3` remote
bucket --- not just the latest run. Guild prompts you before deleting.

Verify the list and press `y` followed by `Enter`.

!!! note
    If you don't use the `--permanent` command line option, the
    run is not deleted from S3 as it can be restored using ``guild
    restore -r s3``. If you want to truly delete the run, use the
    `--permanent` option.

Verify that there are no runs on the `s3` remote:

``` command
guild runs -r s3
```

And that there are no restorable runs:

``` command
guild runs -r s3 --deleted
```

## Summary

In this guide we used S3 to backup and restore a run.

This feature is useful for guarding against accidental run deletion,
but it's also useful when collaborating on teams:

1. One or more researchers or engineers train models and push results
   to S3

2. Other users pull runs for various uses including comparison,
   summary, and release processes

## Next steps

{!start-remote-train.md!}

{!start-docs.md!}
