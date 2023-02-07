###
### ---------------------------------
###            __
###           (  ) NERO's CONFIG :)
###            ||
###            ||
###        ___|""|__.._
###       /____________\
###       \____________/~~~.
### ---------------------------------
###

### Libraries
import os
from os import path
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
redbg = '#820910'
whitebg = '#858585'
white = '#a39e9f'
black = '#000000'
violet = '#9400D3'
terminal = 'alacritty' # Default terminal
mod = "mod4" #"Windows" key


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

# Keys
keys = [
    ### Movement
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    ### Main
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    ### Size of windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    ### ETC
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Rofi spawn apps"),
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),
    Key([mod], "f", lazy.spawn("firefox"), desc="Open Firefox"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Open Dolphin (explorer)"),
    Key([mod], "p", lazy.spawn("pavucontrol"), desc="Open Pavucontrol (GUI for pavucontrol)"),
    Key([mod], "c", lazy.spawn("code"), desc="Open Visual Studio Code"),
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Open Flameshot (lightshot alternative)"),
    Key(["shift"], "Print", lazy.spawn("flameshot full"), desc="Flameshot fullscreen"),
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
    # F keys
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    ### ------------------------------------------------------------------------------------------
]
groups = [Group(i) for i in ["爵 ",""," "," " ," ﭮ", " ", " "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
# Mouse configs
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
# Layouts
layout_conf = {
    'border_focus': 'red',
    'border_width': 3,
    'margin': 8
}
layouts = [
    layout.Max(),
     layout.MonadTall(**layout_conf)
]
### -----------------------------------------------------------------------------
### WIDGETS
widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
      #  wallpaper='/wallpapers/dark.png',
      #  wallpaper_mode='stretch',
        bottom=bar.Bar(
            [
                widget.GroupBox(   ### Workspaces Widget
                    foreground='#858585',
                    background='#820910',
                    font='UbuntuMono Nerd Font',
                    fontsize=19,
                    margin_y=4,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active="#f1ffff", ## TASKBAR, ACTIVE WINDOWS
                    inactive=black,
                    highlight_method='block',
                    this_current_screen_border=["#F07178", "#F07178"], ## TASKBAR, LIGHT RED
                    this_screen_border=["#5c5c5c", "#5c5c5c"],
                    other_current_screen_border=["#0f10la", "#0f10la"],
                    other_screen_border=["#0f101a", "#0f101a"]
                ),
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'White-Red.png')
                ),
                widget.WindowName( ## Selected window name
                background=whitebg,
                foreground=black
                ),
                widget.TextBox(  ## Separator
                fmt='|',
                background=whitebg,
                foreground=black
                ),
                widget.CurrentLayout( ## Current layout name
                    background=whitebg,
                    foreground=black,
                ),
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'Red-White.png')
                ),
                widget.WindowCount( ## Window Count on workspace + icon
                    fmt='{} ﱚ',
                    background=redbg,
                    foreground=white,
                    show_zero=True
                ),
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'White-Red.png')
                ),
                widget.Bluetooth( ## Bluetooth
                    ## Set up bluetooth, with d-feet running as root get the hci and paste it here.
                    hci='/dev_20_1B_88_75_0E_DE', 
                    background=whitebg,
                    foreground=black,
                    max_chars=4
                ),
                  widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'Red-White.png')
                ),
               widget.Wlan( ## SSID
                    interface='wlp4s0',
                    max_chars=4,
                    background=redbg,
                    foreground=white
                ),
                widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'White-Red.png')
                ),
               widget.PulseVolume(
                background=whitebg,
                foreground=black,
                update_interval=0.1,
                fmt='Vol:{}',
                max_chars=7
               ),
               widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'Red-White.png')
                ),
               widget.KeyboardLayout( ### KBLayout switcher
                    background=redbg,
                    foreground=white,
                    configured_keyboards=['us', 'es'],
                    display_map={'us': 'US', 'es': 'ES'} ,
                    max_chars=2             
                ),
               widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'White-Red.png')
                ),
               widget.Battery(  ### Battery 0
                    foreground=black,
                    background=whitebg,  
                    low_foreground="#f07178", # Low Battery
                    battery=0,
                    format="{percent:2.0%}{char}",
                    charge_char='+', # Charging indicator
                    discharge_char='-', # Discharging indicator
                    max_chars=7,
                    unknown_char='',
                    update_interval=30
                ),
               widget.Battery(  ### Battery 1
                    foreground=black,
                    background=whitebg,  
                    low_foreground="#f07178", # Low Battery
                    battery=1,
                    format="| {percent:2.0%}{char}",
                    charge_char='+', # Charging indicator
                    discharge_char='-', # Discharging indicator
                    unknown_char='',
                    max_chars=7,
                    update_interval=30
                ),
               widget.Image(
                    filename=path.join(path.expanduser('~'), '.config', 'qtile', 'img', 'Red-White.png')
                ),
               widget.Clock(
                    background=redbg,
                    foreground=white,
                    format="%a,%d/%m/%Y | %I:%M%p",
                    max_chars=24
                ), 
            ],
            24,
        ),
    ),
]
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ], border_focus='#a151d3')
### -----------------------------------------------------------------------------


# ADDITIONAL CONFIG
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
