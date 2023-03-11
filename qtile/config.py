###
### ---------------------------------
###      NERO's CONFIG :)
###            __
###           (  ) 
###            ||
###            ||
###        ___|""|__.._
###       /____________\
###       \____________/~~~.
### ---------------------------------
###
### Qtile Cheat sheet:
# ------------------------------------------------------------
# QTILE Movement:
# Move focus: Super + h-l/j-k Left and right / Up and down
# Move windows: Super + h-l/j-k Left and right / Up and down
# Toggle layouts: Super + Tab
# ------------------------------------------------------------
# QTILE Main functions:
# Kill focused window: Super + w
# Reload the config: Super + control + r
# Log off: Super + control + q
# ------------------------------------------------------------
# Spawn apps:
# Spawn rofi:  Super + m
# Open firefox: Super + f
# Open Dolphin Explorer: Super + e
# Open code: Super + c
# Open Bluetooth: Super + k
# Open Flameshot: Print Screen
# Open Flameshot Full Screen: Shift + Print Screen
# Change keyboard layout: Super + Space
# Open Terminal: Super + Enter
# ------------------------------------------------------------
#  F Row apps:
# Mute audio: F1
# Change volume (±5): F2-F3 
# Change brightness (±5): F5-F6
# ------------------------------------------------------------




### Libraries
import os
from os import path
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
#
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration


#Themes
# -----------------------------------------------------------------------
# You can change the color scheme of the desktop changing these values!

# bar_bg: Background of the bar
# bar_inactive: Color of the groups that don't have any windows.
# bar_active: Color of the groups that have a window inside.
# bar_focus: Color of the group that you have curently open.

# colorx_bg: Foreground of the widget that has color x
# colorx_fg: Background of the widget that has color x


# -----------------------------------------------------------------------
# #--- Red and Silver color style ---
# bar_bg = '#820910' # Signature red
# bar_active = '#FFFFFF' # Pure white
# bar_inactive = '#000000' # Pure black 
# bar_focus = '#F07178' # Light red
# color1_bg = '#858585' # Silver
# color1_fg = '#000000' # Black
# color2_bg = '#820910' # Red
# color2_fg = '#B3B3B3' # White

# #--- Red and Black color style ---
# bar_bg = '#820910' # Signature red
# bar_active = '#FFFFFF' # Pure white
# bar_inactive = '#000000' # Pure black 
# bar_focus = '#F07178' # Light red
# color1_bg = '#000000' # Pure black
# color1_fg = '#FFFFFF' # Pure white
# color2_bg = '#820910' # Red
# color2_fg = '#B3B3B3' # White

# --- Black and White color style ---
bar_bg = '#000000' # Pure black
bar_active = '#FFFFFF' # Pure white
bar_inactive = '#525252' # Black-ish grey
bar_focus = '#858585' # Grey-ish
color1_bg = '#858585' # Grey-ish
color1_fg = '#000000' # Black
color2_bg = '#000000' # Black
color2_fg = '#858585' # White-ish

# # --- Black and Purple color style ---
# bar_bg = '#000000' # Pure black
# bar_active = '#FFFFFF' # Pure white
# bar_inactive = '#8000C0' # Purple
# bar_focus = '#858585' # Grey-ish
# color1_bg = '#8000C0' # Purple
# color1_fg = '#000000' # Pure black
# color2_bg = '#000000' # Pure black
# color2_fg = '#858585' # Grey-ish

# # --- Catpuccin color style ---
# bar_bg = '#22273b' # Signature red
# bar_active = '#A1A1A1' # Pure white
# bar_inactive = '#000000' # Pure black 
# bar_focus = '#F07178' # Light red
# color1_bg = '#191927' # Pure black
# color1_fg = '#FFFFFF' # Pure white
# color2_bg = '#22273b' # Red
# color2_fg = '#B3B3B3' # White
# -----------------------------------------------------------------------


terminal = 'alacritty' # Default terminal
mod = "mod4" # "Windows" key

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

# Shortcuts
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
    ### Main functions
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    ### Size of windows (WIP)
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    ### Spawn all apps
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Rofi spawn apps"),
    Key([mod], "f", lazy.spawn("firefox"), desc="Open Firefox"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Open Dolphin (explorer)"),
    Key([mod], "c", lazy.spawn("code"), desc="Open Visual Studio Code"),
    Key([mod], "k", lazy.spawn("blueberry"), desc="Opens bluetooth configuration"),
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Open Flameshot (lightshot alternative)"),
    Key(["shift"], "Print", lazy.spawn("flameshot full"), desc="Flameshot fullscreen"),
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    # F keys
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    ### ------------------------------------------------------------------------------------------
]
### Group setup: add new icon to get more groups
### Note: Grab icons from nerd fonts cheat sheet: https://www.nerdfonts.com/cheat-sheet
###                          1.Web 2.Code 3.File 4.Term 5.Book 6.Disc 7.Spotify 8.Etc 
groups = [Group(i) for i in ["爵 ",  "" ," ",  " " ,   " ", " ﭮ",  " ",    " "]]

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

powerline = {
    "decorations": [
        PowerLineDecoration(path="arrow_right",)
    ]
}
screens = [
    Screen(
      # Actual wallpaper setup with feh on autostart.sh script. 
      # If needed, use the following setup for using wallpapers
      # on qtile.
      #  wallpaper='/wallpapers/dark.png',
      #  wallpaper_mode='stretch',
        bottom=bar.Bar(
            [
                widget.GroupBox(   ### Groups Widget
                    font='UbuntuMono Nerd Font',
                    highlight_method='block',
                    fontsize=19,
                    margin_y=4,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    # Colors
                    background=bar_bg, # Color of the background of bar                   
                    active=bar_active, # Color of the groups that have tabs inisde them
                    inactive=bar_inactive, # Color of the groups that don't have tabs inside them
                    this_current_screen_border=bar_focus, ## TASKBAR, LIGHT RED
                    **powerline
                    ),
                widget.WindowName( ## Selected window name
                background=color1_bg,
                foreground=color1_fg,
                ),
                widget.TextBox(  ## Separator
                fmt='|',
                background=color1_bg,
                foreground=color1_fg
                ),
                widget.CurrentLayout( ## Current layout name
                    background=color1_bg,
                    foreground=color1_fg,
                    **powerline
                ),

                widget.WindowCount( ## Window Count on workspace + icon
                    fmt='{} ﱚ',
                    background=color2_bg,
                    foreground=color2_fg,
                    show_zero=True,
                    **powerline
                ),
                widget.Bluetooth( ## Bluetooth
                    # Set up bluetooth, with d-feet running as root get the hci and paste it here.\
                    # NOTE: Please connect to a device first after getting the hci, it won't show up otherwise.
                    hci='/dev_20_1B_88_75_0E_DE', 
                    background=color1_bg,
                    foreground=color1_fg,
                    max_chars=4,
                    **powerline
                ),

               widget.Wlan( ## SSID
                    interface='wlp4s0',
                    max_chars=4,
                    background=color2_bg,
                    foreground=color2_fg,
                    **powerline
                ),

               widget.PulseVolume(
                background=color1_bg,
                foreground=color1_fg,
                update_interval=0.1,
                fmt='Vol:{}',
                max_chars=7,
                **powerline
               ),

               widget.KeyboardLayout( ### KBLayout switcher
                    background=color2_bg,
                    foreground=color2_fg,
                    configured_keyboards=['us', 'es'],
                    display_map={'us': 'US', 'es': 'ES'} ,
                    max_chars=2,
                    **powerline      
                ),

               widget.Battery(  ### Battery 0
                    foreground=color1_fg,
                    background=color1_bg,  
                    low_foreground="#FF0000", # Low Battery
                    battery=0,
                    format="{percent:2.0%}{char}",
                    charge_char='+', # Charging indicator
                    discharge_char='-', # Discharging indicator
                    max_chars=7,
                    unknown_char='?',
                    update_interval=30
                ),
               widget.Battery(  ### Battery 1
                    foreground=color1_fg,
                    background=color1_bg,  
                    low_foreground="#FF0000", # Low Battery
                    battery=1,
                    format="| {percent:2.0%}{char}",
                    charge_char='+', # Charging indicator
                    discharge_char='-', # Discharging indicator
                    unknown_char='?',
                    max_chars=7,
                    update_interval=30,
                    **powerline
                ),
               widget.Clock(
                    background=color2_bg,
                    foreground=color2_fg,
                    format="%a,%d/%m/%Y | %I:%M%p",
                    max_chars=24 # Total number
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

# from qtile_extras import widget
# from qtile_extras.widget.decorations import PowerLineDecoration

# powerline = {
#     "decorations": [
#         PowerLineDecoration()
#     ]
# }

# screens = [
#     Screen(
#         top=Bar(
#             [
#                 widget.CurrentLayoutIcon(background="000000", **powerline),
#                 widget.WindowName(background="222222", **powerline),
#                 widget.Clock(background="444444", **powerline),
#                 widget.QuickExit(background="666666")
#             ],
#             30
#         )
#     )
# ]
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
