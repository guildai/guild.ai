tags: remote, popular

# Train on EC2

[TOC]

This guide describes how to run Guild operations on EC2 through
Guild's [remote](term:remote) facility.

## Requirements

- [Install Guild AI](alias:install-guild)
- [Install Terraform ->](https://www.terraform.io/intro/getting-started/install.html)
- [Setup AWS EC2 account ->](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.html)
- [Verify Quota for one GPU](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html)
- [Obtain SSH key pair ->](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)
- Obtain AWS access key for [IAM Users
  ->](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)
  or for [AWS account root user
  ->](https://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html)
- [Verify IAM user EC2 permissions
  ->](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html)
  (if using IAM user access key)

## Define a remote

Guild remotes are defined in `~/.guild/config.yml`. You must edit this
file to add and modify remote definitions.

In this guide we add a remote named `ec2-k80` that uses an EC2
`p2.xlarge` GPU instance (running a Tesla K80 GPU).

In addition to the instance type the EC2 remote requires:

- AWS region to start instance in
- AMI
- Path to your SSH public key

Modify `~/.guild/config.yml` and add the following at the end of the
file:

``` yaml
remotes:
  ec2-k80:
    type: ec2
    description: Tesla K80 running on EC2
    instance-type: p2.xlarge
    region: us-east-2
    ami: ami-4f62582a
    public-key: ~/.ssh/id_rsa.pub
    user: ubuntu
    init: |
      set -ex
      echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64' > ~/.bashrc
      . ~/.bashrc
      sudo pip install --pre --upgrade guildai tensorflow-gpu
      guild check
```

!!! note
    If you already have a `remotes` section, add `ec2-k80` within
    that section---don't add a second `remotes` section.

Save your changes to `~/.guild/config.yml`.

In a command console, list available remotes:

``` command
guild remotes
```

Guild should show:

``` output
ec2-k80        ec2  Tesla K80 running on EC2
```

If you don't see the remote or Guild exits with an error, verify the
step above and try again.

## Check remote status

Use [remote status](cmd:remote-status) to check status for `ec2-k80`:

``` command
guild remote status ec2-k80
```

Guild should exit with this error message:

``` error
guild: missing required AWS_ACCESS_KEY_ID environment variable
```

Guild requires AWS access keys to check server status in EC2. You must
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
guild remote status ec2-k80
```

Guild should show:

``` output
guild: remote ec2-k80 is not available (not started)
```

If Guild exits with an error, verify that the
[requirements](#requirements) above are met. If you cannot resolve the
issue, [](alias:open-an-issue).

!!! important
    Do not post AWS security credentials to GitHub issues or
    otherwise make them available in plain text to others.

## Start remote

Start the `ec2-k80` remote by running:

``` command
guild remote start ec2-k80
```

Press `Enter` to confirm.

Guild uses [Terraform ->](https://www.terraform.io/) to create and
start the various services on AWS used by the remote. This may take
serveral minutes.

Guild uses the script specified in the remote's `init` to initialize
the server when it starts. You can customize this script as needed to
initialize your own servers.

Here's the script that we're using in this guide:

``` bash
set -ex
echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64' > ~/.bashrc
. ~/.bashrc
sudo pip install --pre --upgrade guildai tensorflow-gpu
guild check
```

Init scripts are specific to the remote AMI. In this case, the AMI
we're using requires a few things:

- Minor change to the environment init
- Installation of TensorFlow and Guild AI

We use ``set -ex`` at the start of the script to fail on any error and
to help debug issues.

We run [guild check](cmd:check) at the end of the script to verify
that the environment is working as expected.

If the server fails to start, note the error message and
[](alias:open-an-issue) to get help.

If the command succeeds, Guild shows the host name of the EC2
instance.

Confirm that remote is available by checking status:

``` command
guild remote status ec2-k80
```

Guild updates status for the remote and should display the following
(host name will differ):

``` output
ec2-k80 (ec2-18-222-63-152.us-east-2.compute.amazonaws.com) is available
```

## Guild commands with remote

The `ec2-k80` remote is now available for use. Let's run some basic
Guild commands with the remote. Commands that support remote execution
all support a `-r, --remote` option, which indicates that the command
applies to the specified remote.

Check the Guild environment:

``` command
guild check -r ec2-k80
```

Guild shows information for the remote. You can use this to quickly
check a remote environment.

List remote runs:

``` command
guild runs -r ec2-k80
```

As we haven't run an operations on the remote, the list is empty.

## Train Fashion-MNIST on EC2

In this section we train the [Basic Fashion-MNIST image classifier
->](https://github.com/guildai/examples/tree/master/fashion) example
on the `ec2-k80` server.

First, clone the [Guild Examples
->](https://github.com/guildai/examples) repository:

``` command
git clone https://github.com/guildai/examples.git
```

Change to the `examples/fashion` directory:

``` command
cd examples/fashion
```

Before training, we need to prepare the Fashion-MNIST images.

Run `prepare-data` on the `ec2-k80` remote:

``` command
guild run prepare-data -r ec2-k80
```

Press `Enter` to confirm the operation.

Guild packages the local project and installs it on the remote. It
then runs the operation in EC2.

When the operation finishes, view the remote run:

``` command
guild runs -r ec2-k80
```

Guild shows the runs on the remote (ID and times will differ):

``` output
[1:43e252de]  fashion/fashion:prepare-data  2018-10-25 13:24:21  completed
```

Next, run `train` on the remote:

``` command
guild run train -r ec2-k80
```

Press `Enter` to continue.

Guild similarly packages the local project and runs it on EC2.

When the train operation finishes, list remote runs:

``` command
guild runs -e ec2-k80
```

Guild shows two remote runs (IDs and times will differ):

``` output
[1:b50bea64]  fashion/fashion:train         2018-10-25 13:34:41  completed
[2:43e252de]  fashion/fashion:prepare-data  2018-10-25 13:24:21  completed
```

Both of these runs reside on the remote server in EC2. In the next
section we copy them to the local system.

### Pull remote runs

We use EC2 to perform computation but we ultimately want to capture
the results. We can do that using the [](cmd:pull) command, which
synchronizes runs on a remote to our local environment.

Pull all of the remote runs:

``` command
guild pull ec2-k80
```

Press `Enter` to confirm.

Guild copies the runs on EC2 to the local system.

When the command finishes, view the local runs:

``` command
guild runs
```

Guild shows the two remote runs, which have been copied to the local
system.

Once remote runs are pulled, they are like any other local run.

With the runs safely copied, we can stop the remote server so we don't
pay for unused EC2 resources.

## Stop remote

Use [remote stop](cmd:remote-stop) to terminate the `ec2-k80` instance
and all of its supporting EC2 services:

``` command
guild remote stop ec2-k80
```

Type `y` and press `Enter` to confirm that you want to stop the
remote.

!!! important
    Stopping an EC2 remote will terminate the associated EC2
    instance. You will lose any files stored on non-persistent
    storage. If you want remote runs, copy them locally using
    [pull](cmd:pull) first.

## Summary

In this guide we use a Guild [remote](term:remote) to start a server
in EC2 that is used to train the basic Fashion-MNIST example. Once
trained, we copy the remote runs to the local system and stop the
remote to avoid ongoing AWS costs.
