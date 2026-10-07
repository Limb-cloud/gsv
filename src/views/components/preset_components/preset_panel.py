from dataclasses import field
from typing import Callable

import flet as ft

from enums.colors import Colors
from models.preset import Preset


@ft.control
class PresetPanel(ft.Column):

    presets: list[Preset] = field(
        default_factory=list,
        metadata={"skip": True}
    )

    selected_preset_id: int | None = field(
        default=None,
        metadata={"skip": True}
    )

    on_add: Callable | None = None
    on_edit: Callable | None = None
    on_delete: Callable | None = None
    on_change: Callable | None = None

    def init(self):
        self.spacing = 12

        self.selector = None

        if self.presets:
            self.selector = ft.SegmentedButton(
                selected=(
                    [str(self.selected_preset_id)]
                    if self.selected_preset_id is not None
                    else []
                ),
                show_selected_icon=False,
                on_change=self.on_change,
                segments=[
                    ft.Segment(
                        value=str(preset.id),
                        label=ft.Text(preset.name),
                    )
                    for preset in self.presets
                ],
            )

        self.controls = [
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Text(
                        "Пресеты",
                        size=20,
                        weight=ft.FontWeight.W_600,
                        color=Colors.TEXT_PRIMARY.value,
                    ),

                    ft.Row(
                        spacing=8,
                        controls=[
                            ft.Button(
                                content="Добавить",
                                icon=ft.Icons.ADD_ROUNDED,
                                bgcolor=Colors.PURPLE.value,
                                color=Colors.BACKGROUND.value,
                                on_click=self.on_add,
                            ),

                            ft.IconButton(
                                icon=ft.Icons.EDIT_ROUNDED,
                                tooltip="Редактировать пресет",
                                icon_color=Colors.TEXT_PRIMARY.value,
                                disabled=not self.presets,
                                on_click=self.on_edit,
                            ),

                            ft.IconButton(
                                icon=ft.Icons.DELETE_OUTLINE_ROUNDED,
                                tooltip="Удалить пресет",
                                icon_color=Colors.RED.value,
                                disabled=not self.presets,
                                on_click=self.on_delete,
                            ),
                        ],
                    ),
                ],
            ),
        ]

        if self.selector is not None:
            self.controls.append(
                self.selector
            )
        else:
            self.controls.append(
                ft.Text(
                    "Пресеты отсутствуют",
                    color=Colors.TEXT_SECONDARY.value,
                )
            )