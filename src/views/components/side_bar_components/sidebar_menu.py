from typing import Callable

import flet as ft

from views.components.side_bar_components.menu_item import MenuItem


@ft.control
class SidebarMenu(ft.Column):

    on_navigation: Callable[[int], None] | None = None

    def init(self):
        self.spacing = 8

        self.selected_index = 0

        self.items = [
            ("Игры", ft.Icons.SPORTS_ESPORTS_ROUNDED),
            ("Избранное", ft.Icons.FAVORITE_BORDER_ROUNDED),
            ("Настройки", ft.Icons.SETTINGS_ROUNDED),
        ]

        self._build_menu()

    def _build_menu(self):
        self.controls.clear()

        for index, (title, icon) in enumerate(self.items):
            self.controls.append(
                MenuItem(
                    title=title,
                    icon=icon,
                    selected_index=(
                        index == self.selected_index
                    ),
                    on_click=lambda e, i=index: self._select(i),
                )
            )

    def _select(self, index: int):
        self.selected_index = index

        self._build_menu()
        self.update()

        if self.on_navigation:
            self.on_navigation(index)