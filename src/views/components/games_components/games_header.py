import flet as ft
from typing import Callable

from enums.colors import Colors


@ft.control
class GamesHeader(ft.Row):

    title: str = "Мои игры"
    subtitle: str = "Сохранённые игровые настройки"

    on_add_game: Callable | None = None
    on_search: Callable | None = None

    def init(self):
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN

        self.search_field = ft.TextField(
            hint_text="Поиск игр...",
            width=260,
            height=42,
            text_size=14,
            bgcolor=Colors.SURFACE.value,
            color=Colors.TEXT_PRIMARY.value,
            prefix_icon=ft.Icons.SEARCH_ROUNDED,
            on_change=self.on_search,
            border=ft.OutlineInputBorder(
                border_radius=10,
            ),
        )

        self.controls = [
            ft.Column(
                spacing=2,
                controls=[
                    ft.Text(
                        self.title,
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=Colors.TEXT_PRIMARY.value,
                    ),

                    ft.Text(
                        self.subtitle,
                        size=13,
                        color=Colors.TEXT_SECONDARY.value,
                    ),
                ],
            ),

            ft.Row(
                spacing=12,
                controls=[
                    self.search_field,

                    ft.Button(
                        content="Добавить игру",
                        icon=ft.Icons.ADD_ROUNDED,
                        bgcolor=Colors.PURPLE.value,
                        color=Colors.BACKGROUND.value,
                        on_click=self.on_add_game,
                    ),
                ],
            ),
        ]