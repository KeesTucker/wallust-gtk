class WallustBase:
    crust: str
    mantle: str
    base: str
    surface0: str
    surface1: str
    surface2: str
    text: str
    subtext1: str
    subtext0: str
    overlay2: str
    overlay1: str
    overlay0: str
    accent: str
    red: str
    green: str
    yellow: str



class WallustDark(WallustBase):
    crust      = "080000"
    mantle     = "0B0000"
    base       = "0E0000"
    surface0   = "3E3333"
    surface1   = "6E6666"
    surface2   = "938C8C"

    text       = "BDF7BC"
    subtext1   = "A1D2A0"
    subtext0   = "84AD84"
    overlay2   = "556F55"
    overlay1   = "2F3E2F"
    overlay0   = "1C251C"

    accent     = "487F82"
    accent1     = "7580A6"

    red        = "fd5f51"
    green      = "38c76a"
    yellow     = "fdbe04"



class WallustLight(WallustBase):
    crust      = "719471"
    mantle     = "97C696"
    base       = "BDF7BC"
    surface0   = "CAF9C9"
    surface1   = "D7FAD7"
    surface2   = "E1FBE1"

    text       = "0E0000"
    subtext1   = "0C0000"
    subtext0   = "0A0000"
    overlay2   = "060000"
    overlay1   = "030000"
    overlay0   = "020000"

    accent     = "446D70"
    accent1     = "70778F"

    red        = "fd5f51"
    green      = "38c76a"
    yellow     = "fdbe04"
