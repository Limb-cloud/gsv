from typing import Callable

import flet as ft

from enums.colors import Colors
from views.components.game_card_components.game_card_popup_menu import CardPopupMenu
from views.components.game_card_components.game_card_stat import GameCardStat


@ft.control
class GameCardInfo(ft.Container):

    game_name: str = ""
    preset_name: str = ""
    resolution: str = ""
    fps: int = 0

    on_edit: Callable | None = None
    on_delete: Callable | None = None

    def init(self):
        self.padding = 16

        self.content = ft.Column(
            spacing=8,
            controls=[
                ft.Text(
                    self.game_name,
                    size=17,
                    weight=ft.FontWeight.W_600,
                    color=Colors.TEXT_PRIMARY.value,
                    max_lines=1,
                    overflow=ft.TextOverflow.ELLIPSIS,
                ),

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column(
                            spacing=8,
                            controls=[
                                ft.Row(
                                    spacing=6,
                                    controls=[
                                        ft.Icon(
                                            ft.Icons.TUNE,
                                            size=16,
                                            color=Colors.PURPLE.value,
                                        ),

                                        ft.Text(
                                            self.preset_name,
                                            size=13,
                                            color=Colors.TEXT_SECONDARY.value,
                                        ),
                                    ],
                                ),

                                ft.Row(
                                    spacing=14,
                                    controls=[
                                        GameCardStat(
                                            stat_icon=ft.Icons.MONITOR,
                                            value=self.resolution,
                                        ),

                                        GameCardStat(
                                            stat_icon=ft.Icons.SPEED,
                                            value=f"{self.fps} FPS",
                                        ),
                                    ],
                                ),
                            ],
                        ),

                        CardPopupMenu(
                            on_edit=self.on_edit,
                            on_delete=self.on_delete,
                        ),
                    ],
                ),
            ],
        )