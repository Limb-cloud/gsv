import flet as ft

from enums.colors import Colors
from views.components.settings_section import (
    SettingsSection,
)
from views.components.settings_components.settings_switch_item import (
    SettingsSwitchItem,
)
from views.components.settings_components.settings_item import (
    SettingsItem,
)


@ft.control
class SettingsView(ft.Container):

    def init(self):
        self.expand = True

        self.confirm_game_delete = SettingsSwitchItem(
            title="Подтверждать удаление игры",
            subtitle="Показывать предупреждение перед удалением игры",
            value=True,
            on_change=self._change_confirm_game_delete,
        )

        self.confirm_preset_delete = SettingsSwitchItem(
            title="Подтверждать удаление пресета",
            subtitle="Показывать предупреждение перед удалением пресета",
            value=True,
            on_change=self._change_confirm_preset_delete,
        )

        self.content = ft.Column(
            spacing=24,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                self._build_header(),

                SettingsSection(
                    title="Интерфейс",
                    section_icon=ft.Icons.TUNE_ROUNDED,
                    section_controls=[
                        self.confirm_game_delete,
                        self.confirm_preset_delete,
                    ],
                ),

                SettingsSection(
                    title="Данные",
                    section_icon=ft.Icons.FOLDER_ROUNDED,
                    section_controls=[
                        SettingsItem(
                            title="Хранилище данных",
                            value="game_settings.db",
                        ),
                    ],
                ),

                SettingsSection(
                    title="О приложении",
                    section_icon=ft.Icons.INFO_OUTLINE_ROUNDED,
                    section_controls=[
                        SettingsItem(
                            title="Приложение",
                            value="Game Settings Vault",
                        ),
                        SettingsItem(
                            title="Версия",
                            value="1.0.0",
                        ),
                    ],
                ),
            ],
        )

    def _build_header(self):
        return ft.Column(
            spacing=2,
            controls=[
                ft.Text(
                    "Настройки",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=Colors.TEXT_PRIMARY.value,
                ),
                ft.Text(
                    "Настройки приложения",
                    size=13,
                    color=Colors.TEXT_SECONDARY.value,
                ),
            ],
        )

    def _change_confirm_game_delete(self, e):
        print(
            "Подтверждение удаления игры:",
            self.confirm_game_delete.value,
        )

    def _change_confirm_preset_delete(self, e):
        print(
            "Подтверждение удаления пресета:",
            self.confirm_preset_delete.value,
        )