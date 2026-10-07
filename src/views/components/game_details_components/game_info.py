import flet as ft

from enums.colors import Colors
from enums.paths import Paths
from views.components.game_details_components.game_info_item import GameInfoItem


@ft.control
class GameInfo(ft.Container):

    game_name: str = ""
    description: str = ""
    preset_count: int = 0
    resolution: str = ""
    fps: int = 0
    cover_path: str = ""

    def init(self):
        self.padding = 20
        self.border_radius = 16
        self.bgcolor = Colors.SURFACE.value

        self.border = ft.Border.all(
            width=1,
            color=Colors.BORDER.value,
        )

        self.content = ft.Row(
            spacing=24,
            controls=[
                ft.Container(
                    width=240,
                    height=135,
                    border_radius=12,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    content=ft.Image(
                        src=(
                            self.cover_path
                            or Paths.GAME_CARD_PICTURE_NONE.value
                        ),
                        width=240,
                        height=135,
                        fit=ft.BoxFit.COVER,
                    ),
                ),

                ft.Column(
                    spacing=10,
                    controls=[
                        ft.Text(
                            self.game_name,
                            size=22,
                            weight=ft.FontWeight.W_600,
                            color=Colors.TEXT_PRIMARY.value,
                        ),

                        ft.Text(
                            self.description,
                            size=14,
                            color=Colors.TEXT_SECONDARY.value,
                        ),

                        ft.Row(
                            spacing=20,
                            controls=[
                                GameInfoItem(
                                    item_icon=ft.Icons.TUNE_ROUNDED,
                                    text=f"{self.preset_count} пресета",
                                    item_color=Colors.PURPLE.value,
                                ),

                                GameInfoItem(
                                    item_icon=ft.Icons.MONITOR_ROUNDED,
                                    text=self.resolution,
                                    item_color=Colors.CYAN.value,
                                ),

                                GameInfoItem(
                                    item_icon=ft.Icons.SPEED_ROUNDED,
                                    text=f"{self.fps} FPS",
                                    item_color=Colors.GREEN.value,
                                )
                            ]
                        )
                    ]
                )
            ]
        )