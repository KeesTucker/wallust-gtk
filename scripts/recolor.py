from typing import Type
from .utils import replacetext, replaceAllText
from .var import (src_dir, work_dir)
from .wallust import WallustBase, WallustDark, WallustLight


def recolor_accent():
    """
    Recolors the accent color in a file.
    """
    print(f"Recoloring all accents")
    replaceAllText(  # Recolor as per base for dark theme. (the color code we are replacing is a blue because the default colloid theme's accent is blue)
        work_dir, "5b9bf8", WallustDark.accent)
    replaceAllText(  # Recolor as per accent for light.
        work_dir, "3c84f7", WallustLight.accent)

def recolor(theme: Type[WallustBase]):
    print("Recoloring to suit soggy wallust theme")
    print("Recoloring accents")

    # Wee hack to fix up a missing sass function in the colloid theme
    replaceAllText(
        f"{work_dir}",
        "gtkmix",
        "mix"
    )

    recolor_accent()

    print("MOD: Gtkrc.sh")
    replacetext(f"{work_dir}/gtkrc.sh", "background_light='#FFFFFF'",
                f"background_light='#{WallustLight.base}'")
    replacetext(f"{work_dir}/gtkrc.sh", "titlebar_light='#F2F2F2'",
                f"titlebar_light='#{WallustLight.base}'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "titlebar_light='#F2F2F2'", f"titlebar_light='#{WallustLight.base}'")

    replacetext(f"{work_dir}/gtkrc.sh", "background_dark='#0F0F0F'",
                f"background_dark='#{theme.base}'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_darker='#121212'",
                f"background_darker='#{theme.mantle}'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "background_alt='#212121'", f"background_alt='#{theme.crust}'")
    replacetext(f"{work_dir}/gtkrc.sh", "titlebar_dark='#030303'",
                f"titlebar_dark='#{theme.crust}'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_dark='#2C2C2C'",
                f"background_dark='#{theme.base}'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_darker='#3C3C3C'",
                f"background_darker='#{theme.mantle}'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "background_alt='#464646'", f"background_alt='#{theme.crust}'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "titlebar_dark='#242424'", f"titlebar_dark='#{theme.crust}'")

    print("Mod SASS Color_Palette_default")

    # Greys
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-050: #FAFAFA", f"grey-050: #{theme.overlay2}")
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-100: #F2F2F2", f"grey-100: #{theme.overlay1}")
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-150: #EEEEEE", f"grey-150: #{theme.overlay0}")
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-200: #DDDDDD", f"grey-200: #{theme.surface2}")  # Surface 0 Late
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-250: #CCCCCC", f"grey-250: #{theme.surface1}")  # D = Surface 1 Late
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-650: #3C3C3C", f"grey-650: #{theme.surface0}")  # H $surface $tooltip
    replacetext(f"{src_dir}/sass/_color-palette-default.scss", "grey-700: #2C2C2C",
                f"grey-700: #{theme.base}")  # G $background; $base; titlebar-backdrop; $popover
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-750: #242424", f"grey-750: #{theme.crust}")  # F $base-alt
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-800: #212121", f"grey-800: #{theme.crust}")  # E $panel-solid;p
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-850: #121212", f"grey-850: #020202")  # H Darknes
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-900: #0F0F0F", f"grey-900: #010101")  # G Darknes
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "grey-950: #030303", f"grey-950: #000000")  # F Darknes

    # Make the hover black
    replacetext(f"{src_dir}/sass/gtk/_common-3.0.scss",
                r"if\(\$colorscheme != 'dracula', white, rgba\(black, 0\.5\)\)", "rgba(black, 0.5)")
    replacetext(f"{src_dir}/sass/gtk/_common-4.0.scss",
                r"if\(\$colorscheme != 'dracula', white, rgba\(black, 0\.5\)\)", "rgba(black, 0.5)")

    # Buttons
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "button-close: #fd5f51", f"button-close: #{theme.red}")
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "button-max: #38c76a", f"button-max: #{theme.green}")
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "button-min: #fdbe04", f"button-min: #{theme.yellow}")
