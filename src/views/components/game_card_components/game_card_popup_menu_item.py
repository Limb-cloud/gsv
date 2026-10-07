import flet as ft


@ft.control
class CardPopupMenuItem(ft.PopupMenuItem):

    title: str = ""
    item_icon: str | None = None
    item_color: str | None = None

    def init(self):
        self.content = ft.Row(
            spacing=8,
            controls=[
                ft.Icon(
                    self.item_icon,
                    size=18,
                    color=self.item_color,
                ),

                ft.Text(
                    self.title,
                    color=self.item_color,
                )
            ]
        )