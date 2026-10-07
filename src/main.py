import getpass
from pathlib import Path

import flet as ft

from controllers.game_controller_interface import GameControllerInterface
from controllers.impl.game_controller import GameController
from controllers.impl.preset_settings_controller import PresetSettingsController
from controllers.preset_settings_controller_interface import PresetSettingsControllerInterface
from database.database import Database
from database.initializer import DatabaseInitializer
from enums.colors import Colors
from enums.paths import Paths
from reports.abstract_application_report import AbstractReport
from reports.application_report import ApplicationReport
from repositories.game_repository import GameRepository
from repositories.preset_repository import PresetRepository
from views.main_view import MainView


def main(page: ft.Page):
    report: AbstractReport = ApplicationReport(
        login=getpass.getuser(),
        report_path=(
            Path(Paths.BASE_DIR.value)
            / "data"
            / "application_report.txt"
        )
    )

    async def window_event(e: ft.WindowEvent):
        if e.type == ft.WindowEventType.CLOSE:
            report.save()

            await page.window.destroy()

    page.window.prevent_close = True
    page.window.on_event = window_event

    page.title = "Game Settings Vault"
    page.padding = 0
    page.spacing = 0
    page.bgcolor = Colors.BACKGROUND.value
    page.theme_mode = ft.ThemeMode.DARK
    page.window.icon = Paths.APPLICATION_ICON.value

    database = Database()

    database_initializer = DatabaseInitializer(
        database
    )

    database_initializer.initialize()

    game_repository = GameRepository(database)
    preset_repository = PresetRepository(database)

    game_controller: GameControllerInterface = GameController(
        game_repository=game_repository
    )

    preset_settings_controller: PresetSettingsControllerInterface = PresetSettingsController(
        preset_repository=preset_repository
    )

    page.add(
        MainView(
            game_controller=game_controller,
            preset_settings_controller=preset_settings_controller,
        )
    )

if __name__ == "__main__":
    ft.run(main)