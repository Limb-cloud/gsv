from typing import Callable

import flet as ft

from enums.colors import Colors
from views.components.game_card_components.game_card_popup_menu_item import CardPopupMenuItem


@ft.control
class CardPopupMenu(ft.PopupMenuButton):

    on_edit: Callable | None = None
    on_delete: Callable | None = None

    def init(self):
        self.icon = ft.Icons.MORE_VERT_ROUNDED
        self.icon_color = Colors.TEXT_SECONDARY.value
        self.menu_position = ft.PopupMenuPosition.UNDER

        self.items = [
            CardPopupMenuItem(
                title="Редактировать",
                item_icon=ft.Icons.EDIT_ROUNDED,
                item_color=Colors.TEXT_PRIMARY.value,
                on_click=self.on_edit,
            ),

            CardPopupMenuItem(
                title="Удалить",
                item_icon=ft.Icons.DELETE_OUTLINE_ROUNDED,
                item_color=Colors.RED.value,
                on_click=self.on_delete,
            )
        ]