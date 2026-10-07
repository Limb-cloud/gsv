from dataclasses import field

import flet as ft

from controllers.game_controller_interface import GameControllerInterface
from controllers.preset_settings_controller_interface import PresetSettingsControllerInterface
from enums.colors import Colors
from views.games_view import GamesView
from views.settings_view import SettingsView
from views.sidebar_view import SidebarView


@ft.control
class MainView(ft.Container):

    game_controller: GameControllerInterface = field(
        kw_only=True,
        metadata={"skip": True}
    )

    preset_settings_controller: PresetSettingsControllerInterface = field(
        kw_only=True,
        metadata={"skip": True}
    )

    def init(self):
        self.expand = True

        self.view_container = ft.Container(
            expand=True,
            content=GamesView(
                game_controller=self.game_controller,
                preset_settings_controller=self.preset_settings_controller
            )
        )

        self.sidebar = SidebarView(
            on_navigation=self._navigate
        )

        self.content = ft.Row(
            expand=True,
            spacing=0,
            controls=[
                self.sidebar,

                ft.Container(
                    expand=True,
                    bgcolor=Colors.BACKGROUND.value,
                    padding=32,
                    content=self.view_container,
                ),
            ],
        )

    def _navigate(self, index: int):
        match index:
            case 0:
                self._show_games()

            case 1:
                self._show_favorites()

            case 2:
                self._show_settings()

    def _show_games(self):
        self.view_container.content = GamesView(
            favorites_only=False,
            game_controller=self.game_controller,
            preset_settings_controller=self.preset_settings_controller
        )

        self.view_container.update()

    def _show_favorites(self):
        self.view_container.content = GamesView(
            favorites_only=True,
            game_controller=self.game_controller,
            preset_settings_controller=self.preset_settings_controller
        )

        self.view_container.update()

    def _show_settings(self):
        self.view_container.content = SettingsView()
        self.view_container.update()