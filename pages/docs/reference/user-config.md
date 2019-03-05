tags: reference

# User Configuration

[TOC]

User configuration is defined in `~/.guild/config.yml`. It defines
configuration and settings that Guild uses on a per-user basis.

## Remotes

Remotes are defined under a top-level `remotes` object. Each remote is
named using its `remotes` section key.

``` yaml
remotes:
  remote-1:
    ...
  remote-2:
    ...
  remote-3:
   ...
```

For information on using remotes, see [Remotes](/docs/remotes/).

### Remote type

Remotes are classified by their *type*, which is specified using the
`type` attribute. Each remote must define its type as one of the
following values:

`ssh`
: System that is accessible over SSH (see [ssh remote](#ssh-remote))

`ec2`
: System running in Amazon EC2 (see [ec2 remote](#ec2-remote))

`s3`
: Remote bucket in Amazon S3 (see [s3 remote](#e3-remote))


## ssh remote

### Attributes

`host`
: Server host name or IP address (required string)

`port`
: Server SSH port (number)
  <p>
  By default, port `22` is used for SSH connections.

`user`
: User used when connecting over SSH (string)
  <p>
  By default, the active user name is used for SSH connections.

`guild-home`
: Path to Guild home on the remote server (string)
  <p>
  Specify this value to use an alternative Guild home location on the
  remote server. By default, the `.guild` relative path is
  used. Relative paths are typically considered relative to the user
  home directory, but this may be different depending on the active
  user's SSH configuration. If `guild-env` is specified, relative
  paths are considered relative to the Guild environment location.

`guild-env`
: Path to Guild environment on the remote server (string)
  <p>
  If this value is specified, Guild will active the environment on the
  remote server before running commands.

`use-prerelease`
: Flag indicating whether or not to use the `--pre` flag when
  installing required packages (boolean)
  <p>
  By default, Guild does not install pre-release package versions when
  installing required packages for a run. If you want to install
  pre-release packages, set this value to ``yes``.

### Examples

Remote named `deep-learning` with IP address `192.168.1.101`:

``` yaml
remotes:
  deep-learning:
    type: ssh
    host: 192.168.1.101
```

Remote named `big-server` that's accessed over the Internet over a
non-standard port using a Guild environment:

``` yaml
remotes:
  big-server:
    host: big.my.co
    port: 2202
    user: ubuntu
    guild-env: ~/sample-project/env
```

## ec2 remote

### Attributes

`ec2` remotes share all of the attribute of `ssh` remotes. See above
for `ssh` attributes.

In addition to the `ssh` attributes, `ec2` remotes support the following:

`region`
: AWS region used when creating the EC2 instance (required string)

`ami`
: AWS AMI used when creating the EC2 instance (required string)

`instance-type`
: EC2 instance type used when creating the EC2 instance (required string)

`public-key`
: Local path to SSH public key to install on the EC2 instance (string)
  <p>
  This value must be specified to access the remote server unless the
  server configures a public key some other way (e.g. the key is on
  the AMI, etc.)

`init`
: Script to run when initializing the instance (string)

`init-timeout`
: Timeout in seconds used when initializing the instance (number)

`private-key`
: Path to private SSH key used when connecting to the instance (string)

`password`
: Password associated with `user` (string)
  <p>
  **CAUTION:** Passwords are stored in plain text and should not be
  used for sensitive applications. To avoid revealing passwords, use
  SSH public/private key authentication.

### Examples

Remote named `k80` used to start a `p2.xlarge` instance in
the `us-east-2` region:

``` yaml
remotes:
  k80:
    type: ec2
    region: us-east-2
    ami: ami-4f62582a
    instance-type: p2.xlarge
    public-key: ~/.ssh/id_rsa.pub
    user: ubuntu
    init: |
      set -ex
      cat > ~/.bashrc << EOF
      export LD_LIBRARY_PATH=/usr/local/cuda/lib64
      EOF
      . ~/.bashrc
      sudo pip install --upgrade pip
      sudo pip install --upgrade guildai
      sudo pip install --upgrade tensorflow-gpu
      guild check
```

## s3 remote

### Attributes

`bucket`
: S3 bucket used for the remote environment (required string)

`root`
: Root path in the S3 bucket used for the remote environment (string)
  <p>
  By default the root of the bucket is used.

`region`
: Region associated with the bucket (string)
  <p>
  By default the environment variable `AWS_DEFAULT_REGION` is used for
  the region.

### Examples

Remote named `s3-backup` that uses the S3 bucket
`deep-learning-backups`:

``` yaml
remotes:
  s3-backup:
    bucket: deep-learning-backups
```

Project specific remote named `s3-my-project` that uses a sub-folder
of the S3 bucket `deep-learning-backups`:

``` yaml
remotes:
  s3-my-project:
    bucket: deep-learning-backups
    root: my-project
```

## Diff

The [](cmd:diff) command uses the `diff` program by default. You can
specify an alternative command by creating a `diff` top-level object.

``` yaml
diff:
  ...
```

### Attributes

`command`
: The command to use when diffing runs (string)
  <p>
  The command will be invoked as specified with two additional
  arguments: the first and second run paths to diff.

### Examples

Use [Meld ->](http://meldmerge.org/) to diff runs:

``` yaml
diff:
  command: meld
```

Use [colordiff ->](https://www.colordiff.org/) to diff runs:

``` yaml
diff:
  command: colordiff -ru
```
