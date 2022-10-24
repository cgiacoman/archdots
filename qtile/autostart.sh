#!/bin/sh
picom &
feh --bg-scale /wallpapers/dark.png &
xrandr --output eDP1 --primary --mode 1366x768 --output HDMI2 --mode 1920x1080 &