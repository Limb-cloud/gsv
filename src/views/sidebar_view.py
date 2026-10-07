from typing import Callable

import flet as ft
from flet import Container

from enums.colors import Colors
from views.components.side_bar_components.logo import Logo
from views.components.side_bar_components.side_bar_footer import SidebarFooter
from views.components.side_bar_components.sidebar_menu import SidebarMenu


@ft.control
class SidebarView(Container):

    on_navigation: Callable[[int], None] | None = None

    def init(self):
        self.width = 220
        self.bgcolor = Colors.SIDEBAR.value
        self.padding = ft.Padding.all(16)

        self.content = ft.Column(
            expand=True,
            controls=[
                Logo(),
                ft.Container(height=24),
                SidebarMenu(on_navigation=self.on_navigation),
                ft.Container(expand=True),
                SidebarFooter()
            ]
        )