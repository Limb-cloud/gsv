from enum import Enum
from pathlib import Path


class Paths(Enum):
    BASE_DIR = Path(__file__).resolve().parent.parent

    ASSETS = BASE_DIR / "assets"

    GAME_CARD_PICTURE_NONE = str(ASSETS / "game_card_picture_none.png")

    APPLICATION_ICON = str(ASSETS / "icon.ico")