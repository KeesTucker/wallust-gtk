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
    crust      = "000007"
    mantle     = "000009"
    base       = "00000B"
    surface0   = "33333C"
    surface1   = "66666D"
    surface2   = "8C8C91"

    text       = "E5E4DD"
    subtext1   = "C3C2BC"
    subtext0   = "A0A09B"
    overlay2   = "676763"
    overlay1   = "393937"
    overlay0   = "222221"

    accent     = "547C94"
    accent1     = "9DA2B6"

    red        = "fd5f51"
    green      = "38c76a"
    yellow     = "fdbe04"



class WallustLight(WallustBase):
    crust      = "898985"
    mantle     = "B7B6B1"
    base       = "E5E4DD"
    surface0   = "EAE9E4"
    surface1   = "EFEFEB"
    surface2   = "F3F3F0"

    text       = "00000B"
    subtext1   = "000009"
    subtext0   = "000008"
    overlay2   = "000005"
    overlay1   = "000003"
    overlay0   = "000002"

    accent     = "5A7585"
    accent1     = "767A88"

    red        = "fd5f51"
    green      = "38c76a"
    yellow     = "fdbe04"
