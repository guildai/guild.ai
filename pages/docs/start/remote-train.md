tags: get-started

# Remote Training

This guide highlights Guild's support for running training operations
on GPU accelerated servers running on AWS EC2.

!!! important
    This guide starts a `p2.xlarge` GPU enabled instance on
    EC2, which costs $0.9 per hour to run. If left running, this
    server will cost $650 per month! **Be certain to run the steps in
    [Cleanup](#cleanup) or otherwise stop the instance after
    completing this guide.**

## Requirements

{!start-requirements-4.md!}

In addition, you must complete the following steps for Amazon S3
bucket support:

- [Sign up for Amazon EC2 ->](https://aws.amazon.com/ec2/)
- [Create access keys for a user who can start and stop EC2 servers ->](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)
- [Install AWS CLI ->](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

Note the AWS access key ID and secret access key of the IAM user who
can start and stop EC2 servers.

Verify that your `guild-start` project has `fashion_mnist_mlp.py` and
`guild.yml`:

<div class="file-tree">
<ul>
<li class="is-folder open">guild-start
 <ul>
 <li class="is-file">fashion_mnist_mlp.py</li>
 <li class="is-file">guild.yml</li>
 </ul>
</li>
</ul>
</div>

## Create a `remote` entry in Guild config

Using your text editor, open `~/.guild/config.yml`.

Add the following to the bottom of the file:

``` yaml
remotes:
  ec2:
    type: ec2
    region: us-east-2
    instance-type: p2.xlarge
    ami: ami-0174e69c12bae5410
    root-device-size: 100
    public-key: ~/.ssh/id_rsa.pub
    user: ubuntu
    init: |
      set -ex
      pip install --upgrade pip
      pip install guildai
      pip install tensorflow-gpu==1.12.0
      guild check --verbose
```

!!! note
    If a `remotes` section already exists in `config.yml`, omit
    that line from the snippet above and only copy the lines after
    `remotes`.

You can change the region from `us-east-2` to a different region
(e.g. your IAM user doesn't have rights to start instances in that
region). If you change the region, you must also change the `ami` to
the [Deep Learning -
Ubuntu](https://aws.amazon.com/marketplace/pp/B077GCH38C) AMI
available for that region.

Save you changes.

## Set AWS environment variables

In the same command console you'll use throughout this guide, set the
following environment variables:

``` command
export AWS_ACCESS_KEY_ID=<access key ID>
export AWS_SECRET_ACCESS_KEY=<secret access key>
```

Replace `<access key ID>` and `<secret access key>` with the
respective values associated with the IAM user who can start and stop
EC2 instances.

## Start the remote

Start the `ec2` remote by running:

``` command
guild remote start ec2
```

``` output
You are about to start ec2
Continue? (Y/n)
```

Press `Enter` to start the server.

Guild starts a new `p2.xlarge` instance. This process may take a
few minutes to complete.

When the command finishes, very that the remote is available by
running:

``` command
guild remote status ec2
```

If the remote is availble, Guild will print:

``` output
Getting remote status
ec2 (<public DNS>) is available
```

where `<public DNS>` is the server public hostname.

## Train Fashion-MNIST on EC2

Verify that your Guild file is configured correctly by running:

``` command
guild operations
```

You should see:

``` output
fashion:dropout-experiment  An experiment that explores the impact of dropout
fashion:train               Train classifier
```

If you don't see `fashion:train` in the list, confirm the steps in
[Reproducibility](/docs/start/reproducibility/) --- the project
requires a Guild file to run the `fashion_mnist_mlp.py` script
remotely.

Run `fashion:train` on `ec2` by running:

``` command
guild run fashion:train --remote ec2
```

``` output
You are about to run fashion:train on ec2
  batch_size: 128
  dropout: 0.2
  epochs: 5
  lr: 0.001
Continue? (Y/n)
```

Press `Enter` to continue.

Guild packages the project and uploads it to the remote server and
runs the operation.

When the operation is finished, list the runs on the remote:

``` command
guild runs --remote ec2
```

``` output
[1:c099fd42]  fashion/fashion:train  2019-03-22 23:03:57  completed
```

## Copy remote run

Copy the run from `ec2` to your local system:

``` command
guild pull ec2
```

Press `Enter` to synchronize the runs on `ec2` to the local system.

When the runs have been copied, list local runs using:

``` command
guild runs
```

## Cleanup

To stop the remote, run:

``` command
guild remote stop ec2
```

``` output
WARNING: You are about to STOP ec2
This action may result in permanent loss of data.
Continue? (y/N)
```

Type `y` and `Enter` to confirm the command.

!!! important
    The [remote stop](cmd:remote-stop) command terminates
    the EC2 sever --- any runs on the remote will be deleted. If you
    want to keep any of the runs on the remote, use the [](cmd:pull)
    command to copy the remote servers before stopping the remote.

!!! important
    We recommend verifying that all EC2 instances have
    stopped by using the [AWS Management Console
    ->](https://aws.amazon.com/console/).

## Summary

In this guide, we started a GPU accelerated server on EC2 to run a
training operation.

- Guild remotes are defined in [user configuration](term:user-config)
- Start and stop remotes using [remote start](cmd:remote-start) and
  [remote stop](cmd:remote-stop) respectively
- Run project operations (e.g. `train`) on a remote by specifying an
  extra command line option: ``--remote NAME``
- Copy runs from a remote to the local system using [](cmd:pull)

This is a simple scheme but it's powerful! EC2 has a host of powerful
GPU accelerated servers that you can use to train your models --- all
without changing your workflow in Guild.

## Next steps

{!start-docs.md!}
