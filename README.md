# guild.ai source

## Building

To build the site, run:

    $ make

The generated site is located in the `site` directory.

## Developing

To work on the site, build it (see above) and run:

    $ make serve

The development site can be viewed at http://localhost:8000.

To automatically re-generate site assets when changed, run the
following in a separate process:

    $ make watch-assets

To manually re-generate assets, run:

    $ make refresh-assets
