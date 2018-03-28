# Images

## Recording screen

- Initialize the env as needed for the demo
- Set tty to 36 x 12
- Run `ttyrec -e sh`
- Perform steps
- Press `CTRL-D` to exit
- Run `ttygif ttyrecord -s 1.2`
- View `tty.gif` and adjust speed as needed by re-running previous
  step
- Crop scrollbar and and optimize the gif:

    gifsicle --crop 0,0+402x254 -O9 tty.gif > tty2.gif

- View `tty2.gif` to verify the recording
- Copy `tty2.gif` to the project file
