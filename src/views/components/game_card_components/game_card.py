from dataclasses import field
from typing import Callable, cast

import flet as ft
from flet import Container

from enums.colors import Colors
from enums.paths import Paths
from models.game import Game
from views.components.game_card_components.game_card_cover import GameCardCover
from views.components.game_card_components.game_card_info import GameCardInfo


@ft.control
class GameCard(Container):
    game: Game = field(
        kw_only=True,
        metadata={"skip": True},
    )

    on_favorite_click: Callable | None = None
    on_edit: Callable | None = None
    on_delete: Callable | None = None

    def init(self):
        self.width = 260
        self.height = 340
        self.bgcolor = Colors.SURFACE.value
        self.border_radius = 14

        self.border = ft.Border.all(
            1,
            Colors.BORDER.value,
        )

        self.clip_behavior = ft.ClipBehavior.ANTI_ALIAS

        preset = (
            self.game.presets[0]
            if self.game.presets
            else None
        )

        game_name = cast(
            str,
            self.game.name,
        )

        cover_path = (
            cast(
                str | None,
                self.game.cover_path,
            )
            or Paths.GAME_CARD_PICTURE_NONE.value
        )

        is_favorite = cast(
            bool,
            self.game.favorite,
        )

        preset_name = (
            cast(
                str,
                preset.name,
            )
            if preset
            else "Нет пресета"
        )

        resolution = (
            preset.display.resolution
            if preset
            and preset.display.resolution
            else "—"
        )

        fps = (
            preset.performance.average_fps
            if preset
            and preset.performance.average_fps
            else 0
        )

        self.content = ft.Column(
            spacing=0,
            controls=[
                GameCardCover(
                    cover_path=cover_path,
                    is_favorite=is_favorite,
                    on_favorite_click=self._favorite_click,
                ),
                GameCardInfo(
                    game_name=game_name,
                    preset_name=preset_name,
                    resolution=resolution,
                    fps=fps,
                    on_edit=self._edit,
                    on_delete=self._delete,
                ),
            ],
        )

    def _favorite_click(self, e):
        if self.on_favorite_click:
            self.on_favorite_click(
                self.game
            )

    def _edit(self, e):
        if self.on_edit:
            self.on_edit(
                self.game
            )

    def _delete(self, e):
        if self.on_delete:
            self.on_delete(
                self.game
            )