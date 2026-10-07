from dataclasses import field

import flet as ft

from models.preset import Preset
from views.components.settings_components.settings_item import SettingsItem
from views.components.settings_section import SettingsSection


@ft.control
class GameDetailsSettings(ft.Column):

    preset: Preset | None = field(
        default=None,
        kw_only=True,
        metadata={"skip": True}
    )

    def init(self):
        self.spacing = 16

        self.controls = [
            ft.Row(
                spacing=16,
                height=225,
                controls=[
                    SettingsSection(
                        title="Экран",
                        section_icon=ft.Icons.MONITOR_ROUNDED,
                        expand=True,
                        section_controls=[
                            SettingsItem(
                                title="Разрешение",
                                value=self._value(
                                    self.preset.display.resolution
                                    if self.preset is not None
                                    else None
                                ),
                            ),
                            SettingsItem(
                                title="Режим",
                                value=self._value(
                                    self.preset.display.display_mode
                                    if self.preset is not None
                                    else None
                                ),
                            ),
                            SettingsItem(
                                title="Частота",
                                value=self._value(
                                    self.preset.display.refresh_rate
                                    if self.preset is not None
                                    else None,
                                    " Hz"
                                ),
                            ),
                            SettingsItem(
                                title="Ограничение FPS",
                                value=self._value(
                                    self.preset.display.fps_limit
                                    if self.preset is not None
                                    else None
                                ),
                            ),
                        ],
                    ),

                    SettingsSection(
                        title="Графика",
                        section_icon=ft.Icons.AUTO_AWESOME_ROUNDED,
                        expand=True,
                        section_controls=[
                            SettingsItem(
                                title="Пресет",
                                value=self._value(
                                    self.preset.graphics.preset
                                    if self.preset is not None
                                    else None
                                ),
                            ),
                            SettingsItem(
                                title="Текстуры",
                                value=self._value(
                                    self.preset.graphics.textures
                                    if self.preset is not None
                                    else None
                                ),
                            ),
                            SettingsItem(
                                title="Тени",
                                value=self._value(
                                    self.preset.graphics.shadows
                                    if self.preset is not None
                                    else None
                                ),
                            ),
                            SettingsItem(
                                title="Ray Tracing",
                                value=self._value(
                                    self.preset.graphics.ray_tracing
                                    if self.preset is not None
                                    else None
                                ),
                            ),
                            SettingsItem(
                                title="Upscaler",
                                value=self._value(
                                    self.preset.graphics.upscaler
                                    if self.preset is not None
                                    else None
                                ),
                            ),
                        ],
                    ),
                ],
            ),

            ft.Row(
                spacing=16,
                height=175,
                controls=[
                    SettingsSection(
                        title="Управление",
                        section_icon=ft.Icons.MOUSE_ROUNDED,
                        expand=True,
                        section_controls=[
                            SettingsItem(
                                title="DPI",
                                value=self._value(
                                    self.preset.control.dpi
                                    if self.preset is not None
                                    else None
                                ),
                            ),
                            SettingsItem(
                                title="Чувствительность",
                                value=self._value(
                                    self.preset.control.sensitivity
                                    if self.preset is not None
                                    else None
                                ),
                            ),
                            SettingsItem(
                                title="FOV",
                                value=self._value(
                                    self.preset.control.fov
                                    if self.preset is not None
                                    else None
                                ),
                            ),
                        ],
                    ),

                    SettingsSection(
                        title="Производительность",
                        section_icon=ft.Icons.SPEED_ROUNDED,
                        expand=True,
                        section_controls=[
                            SettingsItem(
                                title="Средний FPS",
                                value=self._value(
                                    self.preset.performance.average_fps
                                    if self.preset is not None
                                    else None
                                ),
                            ),
                            SettingsItem(
                                title="Температура GPU",
                                value=self._value(
                                    self.preset.performance.gpu_temperature
                                    if self.preset is not None
                                    else None,
                                    " °C"
                                ),
                            ),
                            SettingsItem(
                                title="Температура CPU",
                                value=self._value(
                                    self.preset.performance.cpu_temperature
                                    if self.preset is not None
                                    else None,
                                    " °C"
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        ]

    @staticmethod
    def _value(value, suffix: str = "") -> str:
        if value is None:
            return "—"

        return f"{value}{suffix}"
