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
    crust      = "000100"
    mantle     = "000200"
    base       = "000200"
    surface0   = "333533"
    surface1   = "666766"
    surface2   = "8C8D8C"

    text       = "BEF1B2"
    subtext1   = "A2CD97"
    subtext0   = "85A97D"
    overlay2   = "566C50"
    overlay1   = "303C2D"
    overlay0   = "1C241B"

    accent     = "8EA02C"
    accent1     = "6BB319"

    red        = "fd5f51"
    green      = "38c76a"
    yellow     = "fdbe04"



class WallustLight(WallustBase):
    crust      = "72916B"
    mantle     = "98C18E"
    base       = "BEF1B2"
    surface0   = "CBF4C1"
    surface1   = "D8F7D1"
    surface2   = "E2F9DC"

    text       = "000200"
    subtext1   = "000200"
    subtext0   = "000100"
    overlay2   = "000100"
    overlay1   = "000000"
    overlay0   = "000000"

    accent     = "727F2C"
    accent1     = "508613"

    red        = "fd5f51"
    green      = "38c76a"
    yellow     = "fdbe04"
