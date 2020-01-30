tags: start

# Configure a Project

Up to this point, you have run `train.py` directly without providing
additional information about the script. When Guild runs an operation,
it must determine a number of things:

- How does the script read user-provided values, or
  [flags](term:flag)?
- How does the script communicate numeric results, or
  [scalars](term:scalar), such as training loss and accuracy?
- Does the script require additional files such as other source code
  files and data sets?

Unless configured otherwise, Guild makes assumptions about the script
to answer these questions. Refer to [Default
Behavior](/reference/defaults.md) for information on how runs scripts
by default.

You can configure this information using a [Guild
file](term:guildfile). A Guild file is a human-readable text file
named `guild.yml` that resides in a project directory.

When you run a script directory without a Guild file, Guild
