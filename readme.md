# Arch Linux - QTILE
![Qtile](/qtile/screenshot1.png)
![Qtile](/qtile/screenshot.png)
## Guide to install everything :)

1. Install arch linux using installation guide:
https://wiki.archlinux.org/title/Installation_guide

Change mirrors:
```
sudo reflector --latest 20 --protocol https --sort rate --save /etc/pacman.d/mirrorlist
```
Install essential packages:
```
pacman -S vi vim sudo nano networkmanager
```
Enable NetworkManager
```
systemctl enable NetworkManager
```
Allow wheel group to use sudo commands:
```EDITOR=nano visudo```
```
/etc/sudoers
## Uncomment to allow members of group wheel to execute any command
%wheel ALL=(ALL:ALL) ALL
```
Add user, create root and user password:
###### Replace 'User' with desired user ###### 
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
sudo pacman -S adobe-source-sans-fonts adobe-source-serif-fonts alacritty alsa-utils base-devel blueberry brightnessctl cheese cmatrix code d-feet discord dolphin dolphin-emu fbida feh ffmpeg filezilla firefox flameshot gimp gnome-boxes gnome-calculator gnome-calendar gnome-clocks gparted grub-customizer gtop htop libreoffice-fresh lightdm lightdm-gtk-greeter lightdm-webkit2-greeter lxapperance neofetch nmtui ntfs-3g obs-studio pamixer papirus-icon-theme picom pulseaudio qtile reflector rofi samba speedtest-cli steam thunar tor transmission-gtk ttf-caladea ttf-carlito ttf-dejavu ttf-liberation ttf-linux-libertine-g unzip vlc xorg zim zip
```
Reboot the system:
```
reboot
```
Install AUR Helper (yay)
```
git clone https://aur.archlinux.org/yay.git \
cd yay \
makepkg -si \
```
Install AUR Packages: 
```
yay -S catppuccin-gtk-theme-frappe catppuccin-gtk-theme-latte catppuccin-gtk-theme-macchiato catppuccin-gtk-theme-mocha downgrade firefox-profile-switcher-connector lightdm-webkit-theme-osmos nerd-fonts-ubuntu-mono parsec-bin teamviewer upnp-router-control wii-u-gc-adapter
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
git clone https://github.com/cgiacoman/archdots ~/archdots
cd ~/archdots
sudo cp -r qtile/ ~/.config/qtile
sudo cp -r wallpapers/ /wallpapers
sudo chmod +x ~/.config/qtile/autostart.sh
```
Add picture to LightDM:
###### Replace 'username' with account user
```
cd wallpapers/
sudo mv username.png /var/lib/AccountsService/icons/username.png
sudo rm /var/lib/AccountsService/users/username
sudo touch /var/lib/AccountsService/users/username
udo echo "[User]
Icon=/var/lib/AccountsService/icons/username.png" | sudo tee /var/lib/AccountsService/users/username
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
Install qtile bluetooth dependency:
```
pip install dbus-next
```
