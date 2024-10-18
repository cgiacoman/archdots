# Arch Linux - QTILE
with multiple themes! :)\
WIP!
<br>
![Qtile](/qtile/screenshot-red2.png)
![Qtile](/qtile/screenshot-red1.png)
![Qtile](/qtile/screenshot-black2.png)
![Qtile](/qtile/screenshot-black1.png)
Use table of contents for better navigation 

## Guide to setup post-installation 

1. Install arch linux using installation guide:
https://wiki.archlinux.org/title/Installation_guide

Inside chroot:

Change mirrors:
```
sudo reflector --latest 20 --protocol https --sort rate --save /etc/pacman.d/mirrorlist
```
Install essential packages:
```
pacman -S reflector vi vim  sudo nano networkmanager base-devel picom git qtile lightdm-webkit2-greeter lightdm-webkit-theme-osmos xorg-server feh firefox code pulseaudio pulseaudio-equalizer pulseaudio-alsa pamixer pavucontrol python-iwlib python-dbus-next d-feet blueberry brightnessctl dolphin adobe-source-sans-fonts adobe-source-serif-fonts ttf-ubuntu-mono-nerd fbida feh thunar flameshot gimp gnome-boxes gparted grub-customizer htop libreoffice-fresh ntfs-3g obs-studio rofi tor ttf-caladea ttf-carlito ttf-dejavu ttf-liberation ttf-linux-libertine-g unzip vlc zip
```
Install non essential packages: (optional)
```
sudo pacman -S discord dolphin-emu steam zim gnome-calculator gnome-calendar gnome-clocks filezilla papirus-icon-theme lxapperance neofetch speedtest-cli samba transmission-gtk
```
Add wallpapers from repo, and qtile configs:
```
git clone https://github.com/cgiacoman/archdots
cp -r archdots/images ~/Pictures/wallpapers
sudo cp -r archdots/qtile/ ~/.config
sudo chmod +x ~/.config/qtile/autostart.sh
```
Change alacritty theme, add transparency:
```
git clone https://github.com/catpuccin/alacritty.git ~/.config/alacritty/catpuccin
---
~/.config/alacritty/alacritty.yml
import:
  ~/.config/alacritty/catpuccin/catpuccin-frappe.yml
window:
  opacity:0.9
```




Install essential AUR packages
```
paru -S downgrade firefox-profile-switcher-connector qtile-extras-git
```
Install not essential AUR packages (optional)
```
paru -S catppuccin-gtk-theme-frappe catppuccin-gtk-theme-latte catppuccin-gtk-theme-macchiato catppuccin-gtk-theme-mocha parsec-bin teamviewer upnp-router-control wii-u-gc-adapter
```
Install windows fonts on /usr/local/share/fonts/ (Get from a Windows system)

Add profile picture to user in LightDM:
> Replace 'User' with account user
```
cd wallpapers/
sudo mv User.png /var/lib/AccountsService/icons/User.png
sudo rm /var/lib/AccountsService/users/User
sudo touch /var/lib/AccountsService/users/User
udo echo "[User]
Icon=/var/lib/AccountsService/icons/User.png" | sudo tee /var/lib/AccountsService/users/User
```
Enable and start bluetooth service:
```
sudo systemctl enable bluetooth.service
sudo systemctl start bluetooth.service
sudo systemctl status bluetooth.service
```

## Color scheme info
The colors are easily modified by changing the hex values on the variables at the start of the config.py file. The setup is made so that it works with two colors, but it can be adapted to use only one. It uses the qtile-extra powerbar feature so that when the colors are changed, the powerbar is modified too. 
<br><br>There are some example themes inside, just uncomment the one that you're going to use.
<br>Variables work like this:
```
bar_bg: Background of the bar
bar_inactive: Color of the groups that don't have any windows.
bar_active: Color of the groups that have a window inside.
bar_focus: Color of the group that you have curently open.

colorx_bg: Foreground of the widget that has color x
colorx_fg: Background of the widget that has color x
```
