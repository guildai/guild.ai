tags: remote

# Backup to S3

[TOC]

This guide describes how to use S3 to backup runs.

## Requirements

- [Install Guild AI](alias:install-guild)
- [Install AWS CLI ->](https://docs.aws.amazon.com/cli/latest/userguide/installing.html)
- [Create S3 bucket ->](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-configure-bucket.html)
- Obtain AWS access key for [IAM Users
  ->](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)
  or for [AWS account root user
  ->](https://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html)
- [Verify IAM user S3 permissions
  ->](https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-managing-access-s3-resources.html)
  (if using IAM user access key)

## Define a remote

Guild remotes are defined in `~/.guild/config.yml`. You must edit this
file to add and modify remote definitions.

In this guide we add a remote named `s3-backup` that will serve as a
backup location in S3 for runs.

Modify `~/.guild/config.yml` and add the following at the end of the
file:

``` yaml
remotes:
  s3-backup:
    type: s3
    description: Backups on S3
    bucket: <your S3 bucket>
    root: guild-backups
```

!!! note
    If you already have a `remotes` section, add `s3-backup` within
    that section---don't add a second `remotes` section.

Save your changes to `~/.guild/config.yml`.

In a command console, list available remotes:

``` command
guild remotes
```

Guild should show:

``` output
s3-backup        Backups on S3
```

If you don't see the remote or Guild exits with an error, verify the
step above and try again.

## Check remote status

Use [remote status](cmd:remote-status) to check status for
`s3-backup`:

``` command
guild remote status s3-backup
```

Guild should exit with this error message:

``` error
guild: missing required AWS_ACCESS_KEY_ID environment variable
```

Guild requires AWS access keys to check server status in S3. You must
define the following two environment variables to use EC2 remotes in
Guild:

`AWS_ACCESS_KEY_ID`
: Access key ID for your AWS security credentials.

`AWS_SECRET_ACCESS_KEY`
: Secret access key for your AWS security credentials.

!!! note
    If you don't have these values, refer to
    [Requirements](#requirements) above for help.

Define the required environment variables, replacing `<...>` with your
access key values:

``` command
AWS_ACCESS_KEY_ID=<your access key id>
AWS_SECRET_ACCESS_KEY=<your secret access key>
```

Check status again:

``` command
guild remote status s3-backup
```

Guild should show:

``` output
s3-backup (S3 bucket guild-dev-backup) is available
```

If Guild exits with an error, verify that the
[requirements](#requirements) above are met. If you cannot resolve the
issue, [](alias:open-an-issue).

!!! important
    Do not post AWS security credentials to GitHub issues or
    otherwise make them available in plain text to others.

## Install sample package and run operations

To illustrate backing up runs to S3, we need to first generate some
runs. We use the `gpkg.mnist` package in this guide, but any Guild
project or package will work.

Install `gpkg.mnist`:

``` command
guild install gpkg.mnist
```

To verify installation, list available operations for `mnist`:

``` command
guild operations mnist
```

Verify that you see the following:

``` output
gpkg.mnist/cnn:evaluate     Evaluate a trained CNN
gpkg.mnist/cnn:train        Train the CNN
gpkg.mnist/logreg:evaluate  Evaluate a trained logistic regression
gpkg.mnist/logreg:train     Train the logistic regression
gpkg.mnist/samples:prepare  Generate a set of sample MNIST images
```

Run `train` for the `logreg` model:

``` command
guild run logreg:train
```

Press `Enter` to confirm.

Guild trains the model for ten epochs. When the run is finished, list
available runs:

``` command
guild runs
```

You should see the following run (ID and dates will differ):

``` output
[1:d6e12108]  gpkg.mnist/logreg:train  2018-10-26 04:23:46  completed
```

If you see other runs that's okay. We just backup this run in this
guide.

## Push run to S3

With our S3 remote and a training run, we're ready to backup.

Use the [](cmd:push) command to backup the latest run to `s3-backup`:

``` command
guild push --operation gpkg.mnist/logreg:train 1 s3-backup
```

The use of `--operation` limits the command to operations matching the
specified value. The value `1` indicates that only the latest run
should be copied. The command can be read to mean "copy the latest
MNIST logreg training run to the S3 backup".

Verify that the `gpkg.mnist/logreg:train` run will be copied and press
`Enter`.

Guild copies the run to the configured S3 bucket under the
`guild-backups` root path. You may use the AWS console or other S3
bucket browser to verify.

!!! note
    You can copy all available runs by omitting run selection
    options---e.g. by using ``guild push s3-backup``. Refer to
    the [](cmd:push) command for details.

Next, list the runs in the S3 remote:

``` command
guild runs -r s3-backup
```

Guild shows the run, but in this case its from S3.

## Restore run from S3

In this section we delete our local run and restore it from S3.

Delete the local `gpkg.mnist/logreg:train` run:

``` command
guild runs rm --operation gpkg.mnist/logreg:train 1
```

Confirm that our sample run is displayed in the confirmation prompt
and press `Enter` to confirm.

We use `--operation` and the value `1` to ensure that only the latest
`gpkg.mnist/logreg:train` run is deleted.

Next, we use the S3 remote to restore the run.

!!! note
    You can recover a deleted run in Guild using the [runs
    restore](cmd:runs-restore) command, provided it's not been
    permanently deleted. In this case we will restore

Use the [](cmd:pull) command to copy runs from `s3-backup`:

``` command
guild pull --operation gpkg.mnist/logreg:train 1 s3-backup
```

Verify the run to be copied and press 'Enter'.

Guild copies the run from S3 to the local system.

Verify that the run is restored:

``` command
guild runs
```

## Delete run from S3

In this section we demonstrate Guild's run management support for S3
by deleting the backup run.

Delete the latest `gpkg.mnist/logreg:train` run in S3:

``` command
guild runs rm --operation gpkg.mnist/logreg:train 1 -r s3-backup
```

Verify the run to be deleted and press `Enter`.

Guild deletes the run in S3. You can verify using the AWS console or
an S3 browser.

List the runs in S3:

``` command
guild runs -r s3-backup
```

## Manage runs in S3

Guild supports the following run management commands for S3
remotes. This includs:

[runs delete](cmd:runs-delete)
: Delete a run in S3 (can be undeleted using `restore`).

[runs info](cmd:runs-info)
: Show run information for a run in S3.

[runs label](cmd:runs-label)
: Label a run in S3.

[runs list](cmd:runs-list)
: List runs in S3.

[runs purge](cmd:runs-purge)
: Permanently delete runs in S3.

[runs restore](cmd:runs-restore)
: Restore a (non-permanently) deleted run in S3.

You may have noted that in the previous section, when we deleted the
run in S3, Guild did not actually delete the run in S3 but moved it to
a `trash` path under the bucket root. Guild does this to support
restoring deleted runs.

You can list deleted runs using the `--deleted` option:

``` command
guild runs --deleted -r s3-backup
```

You can restore deleted runs on S3 using:

``` command
guild runs restore -r s3-backup
```

!!! note
    This command restores all deleted runs. If you want to
    restore a subset of runs, use the run filter options available
    with the [](cmd:runs-restore) command.

Finally, if you want to permanently delete the run, use the
`--permanent` option:

``` command
guild runs rm \
  --permanent \
  --operation gpkg.mnist/logreg:train 1 \
  -r s3-backup
```
