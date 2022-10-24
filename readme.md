# Arch Linux - QTILE
![Qtile](/qtile/screenshot1.png)
![Qtile](/qtile/screenshot.png)
## Guide to install everything :)
Initial config:

Install essential packages:
```pacman -S vi vim sudo nano```

Allow wheel group to use sudo commands:
```EDITOR=nano visudo```

```
/etc/sudoers
%wheel      ALL=(ALL:ALL) ALL
```
Add user, create root and user password:
```
useradd -m --badname User
passwd 
passwd User
```

Enable multilib repository on pacman:
```
/etc/pacman.conf
[multilib]
Include = /etc/pacman.d/mirrorlist
```

Install ALL packages:

```
sudo pacman -S alacritty firefox code lib32-systemd base-devel thunar autoconf automake base bison brightnessctl cmake debugedit efibootmgr fakeroot gcc grub git make xf86-video-intel reflector mypy flex groff hwinfo lightdm lightdm-gtk-greeter lxappearance m4 nano netctl networkmanager nm-connection-editor papirus-icon-theme ntfs-3g patch picom pkgconf python-iwlib python-pip qtile rofi texinfo os-prober xorg gtop htop gimp calc cmatrix code discord dolphin fbida feh filezilla flameshot gnome-calculator gnome-clocks thunar tor transmission-gtk vlc zim libreoffice-fresh neofetch obs-studio pcmanfm-gtk3 speedtest-cli steam adobe-source-sans-fonts nerd-fonts-ubuntu-mono adobe-source-serif-fonts ttf-caladea ttf-carlito ttf-dejavu ttf-liberation ttf-linux-libertine-g pamixer pulseaudio pulseaudio-bluetooth pulseaudio-equalizer alsa-utils bluez bluez-utils d-feet blueberry cheese gnome-calendar
```
Install AUR Helper (yay)
```
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```
Install AUR Packages: 
```
yay -S lightdm-webkit-theme-osmos catpuccin-gtk-theme-mocha catpuccin-gtk-theme-macchiato catpuccin-gtk-theme-frappe catpuccin-gtk-theme-latte downgrade teamviewer parsec-bin
```
Start teamviewer daemon:
```
teamviewer --daemon start
```
Enable LightDM & NetworkManager:
```
systemctl enable lightdm.service
systemctl enable NetworkManager
exit
reboot
```

###### If LightDM doesn't boot, use the downgrade command on the webkit2gtk package to 2.36.7-1.
Install windows fonts on /usr/local/share/fonts/ (Get from a Windows system)

Clone this repository, copy configs:
```
git clone https://cgiacoman/archdots ~/
cd ~/archdots
sudo cp -r qtile/ ~/.config/qtile
sudo cp -r wallpapers/ /wallpapers
```

Open lxapperance, change GTK theme to catpuccin-frappe-red and icon pack to Papirus:
```
lxapperance
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

Enable and start bluetooth service:
```
sudo systemctl enable bluetooth.service
sudo systemctl start bluetooth.service
sudo systemctl status bluetooth.service
```
