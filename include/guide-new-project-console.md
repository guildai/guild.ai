- Open a new command console or a new window/pane if using
  [](alias:tmux).

- Change to the project directory and activate the environment:

``` command
cd $PROJECT
source guild-env
```

!!! note
    If you forget to activate the environment, you won't see
    project runs or Python packages installed for the project. When in
    doubt, check the console prompt and look for the environment name
    in form `(<env name>) <default prompt>`. You can also run `guild
    check` and confirm that `guild_home` is located in the project
    directory.
