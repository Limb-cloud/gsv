from dataclasses import field
from typing import Callable

import flet as ft

from controllers.game_controller_interface import GameControllerInterface
from controllers.preset_settings_controller_interface import PresetSettingsControllerInterface
from models.game import Game
from models.preset import Preset
from views.components.game_details_components.game_details_header import (
    GameDetailsHeader,
)
from views.components.game_details_components.game_details_settings import GameDetailsSettings
from views.components.game_details_components.game_info import GameInfo
from views.components.game_details_components.notes_section import NotesSection
from views.components.preset_components.preset_dialog import PresetDialog
from views.components.preset_components.preset_panel import PresetPanel


@ft.control
class GameDetailsView(ft.Column):

    game_controller: GameControllerInterface = field(
        kw_only=True,
        metadata={"skip": True}
    )

    game: Game = field(
        kw_only=True,
        metadata={"skip": True}
    )

    preset_settings_controller: PresetSettingsControllerInterface = field(
        kw_only=True,
        metadata={"skip": True}
    )

    on_back: Callable | None = None

    def init(self):
        self.expand = True
        self.spacing = 24
        self.scroll = ft.ScrollMode.AUTO

        self.presets: list[Preset] = []
        self.selected_preset: Preset | None = None

        self._load_presets()
        self._build_view()

    def _load_presets(self):
        result = self.preset_settings_controller.load_presets(
            self.game.id
        )

        if result.data is None:
            self.presets = []
            self.selected_preset = None
            return

        self.presets = result.data

        if self.presets:
            self.selected_preset = self.presets[0]
        else:
            self.selected_preset = None

    def _build_view(self):
        self.preset_panel = PresetPanel(
            presets=self.presets,
            selected_preset_id=(
                self.selected_preset.id
                if self.selected_preset is not None
                else None
            ),
            on_add=self._add_preset,
            on_edit=self._edit_preset,
            on_delete=self._delete_preset,
            on_change=self._change_preset,
        )

        self.controls = [
            GameDetailsHeader(
                game_name=self.game.name,
                is_favorite=self.game.favorite,
                on_back=self.on_back,
                on_favorite=self._toggle_favorite
            ),

            GameInfo(
                game_name=self.game.name,
                description=self.game.description,
                preset_count=len(self.presets),
                resolution=(
                    self.selected_preset.display.resolution
                    if self.selected_preset is not None
                    else "—"
                ),
                fps=(
                    self.selected_preset.performance.average_fps
                    if self.selected_preset is not None
                    else 0
                ),
            ),

            self.preset_panel,

            GameDetailsSettings(
                preset=self.selected_preset
            ),

            NotesSection(
                notes=(
                    self.selected_preset.notes
                    if self.selected_preset is not None
                    else None
                ),
            ),
        ]

    def _change_preset(self, e):
        selected = self.preset_panel.selector.selected

        if not selected:
            return

        preset_id = selected[0]

        result = self.preset_settings_controller.get_preset(
            int(preset_id)
        )

        if result.notification is not None:
            self.page.show_dialog(
                result.notification
            )

        if result.data is None:
            return

        self.selected_preset = result.data

        self._build_view()
        self.update()

    def _add_preset(self, e):
        self.preset_dialog = PresetDialog(
            on_save=self._save_preset,
            on_cancel=self._close_preset_dialog,
        )

        self.page.show_dialog(
            self.preset_dialog
        )

    def _edit_preset(self, e):
        if self.selected_preset is None:
            return

        print(
            "Редактировать пресет:",
            self.selected_preset.name
        )

    def _delete_preset(self, e):
        if self.selected_preset is None:
            return

        result = self.preset_settings_controller.on_delete_preset(
            self.selected_preset
        )

        if result.data is None:
            if result.notification is not None:
                self.page.show_dialog(
                    result.notification
                )

            return

        self._load_presets()
        self._build_view()
        self.update()

        if result.notification is not None:
            self.page.show_dialog(
                result.notification
            )

    def _close_preset_dialog(self, e):
        self.page.pop_dialog()

    def _save_preset(self, e):
        if not self.preset_dialog.form.validate():
            return

        result = self.preset_settings_controller.on_add_preset(
            game_id=self.game.id,
            name=self.preset_dialog.form.name_field.value,
            resolution=self.preset_dialog.form.display_form.resolution_field.value,
            display_mode=self.preset_dialog.form.display_form.display_mode_field.value,
            refresh_rate=self.preset_dialog.form.display_form.refresh_rate_field.value,
            fps_limit=self.preset_dialog.form.display_form.fps_limit_field.value,
            graphics_preset=self.preset_dialog.form.graphics_form.preset_field.value,
            textures=self.preset_dialog.form.graphics_form.textures_field.value,
            shadows=self.preset_dialog.form.graphics_form.shadows_field.value,
            ray_tracing=self.preset_dialog.form.graphics_form.ray_tracing_field.value,
            upscaler=self.preset_dialog.form.graphics_form.upscaler_field.value,
            dpi=self.preset_dialog.form.control_form.dpi_field.value,
            sensitivity=self.preset_dialog.form.control_form.sensitivity_field.value,
            fov=self.preset_dialog.form.control_form.fov_field.value,
            average_fps=self.preset_dialog.form.performance_form.average_fps_field.value,
            gpu_temperature=self.preset_dialog.form.performance_form.gpu_temperature_field.value,
            cpu_temperature=self.preset_dialog.form.performance_form.cpu_temperature_field.value,
            notes=self.preset_dialog.form.notes_field.value,
        )

        if result.data is None:
            if result.notification is not None:
                self.page.show_dialog(
                    result.notification
                )

            return

        self.page.pop_dialog()

        created_preset_id = result.data.id

        self._load_presets()

        self.selected_preset = next(
            (
                preset
                for preset in self.presets
                if preset.id == created_preset_id
            ),
            result.data
        )

        self._build_view()
        self.update()

        if result.notification is not None:
            self.page.show_dialog(
                result.notification
            )

    def _toggle_favorite(self, e):
        result = self.game_controller.on_toggle_favorite(
            self.game
        )

        if result.notification is not None:
            self.page.show_dialog(
                result.notification
            )

        if result.data is None:
            return

        self.game = result.data

        self._build_view()
        self.update()
