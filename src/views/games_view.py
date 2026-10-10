from dataclasses import field

import flet as ft

from controllers.game_controller_interface import GameControllerInterface
from controllers.preset_settings_controller_interface import PresetSettingsControllerInterface
from models.data_classes.controller_result import ControllerResult
from models.game import Game
from views.components.game_card_components.game_dialog import GameDialog
from views.components.games_components.games_header import GamesHeader
from views.game_details_view import GameDetailsView

@ft.control
class GamesView(ft.Container):

    game_controller: GameControllerInterface = field(
        kw_only=True,
        metadata={"skip": True}
    )

    preset_settings_controller: PresetSettingsControllerInterface = field(
        kw_only=True,
        metadata={"skip": True}
    )

    favorites_only: bool = False

    def init(self):
        self.expand = True

        self.games_grid = ft.GridView(
            expand=True,
            max_extent=280,
            child_aspect_ratio=0.78,
            spacing=16,
            run_spacing=16,
        )

        self.header = GamesHeader(
            title=(
                "Избранное"
                if self.favorites_only
                else "Мои игры"
            ),
            subtitle=(
                "Избранные игровые настройки"
                if self.favorites_only
                else "Сохранённые игровые настройки"
            ),
            on_add_game=self._open_add_game_dialog,
            on_search=self._search_games,
        )

        self._load_games()

        self.content = self._build_games_view()

    def _build_games_view(self):
        return ft.Column(
            expand=True,
            spacing=24,
            controls=[
                self.header,
                self.games_grid,
            ],
        )

    def _show_games(self):
        self._load_games()

        self.content = self._build_games_view()
        self.update()

    def _open_add_game_dialog(self, e):
        self.game_dialog = GameDialog(
            on_save=self._add_game,
            on_cancel=self._close_game_dialog,
        )

        self.page.show_dialog(
            self.game_dialog
        )

    def _close_game_dialog(self, e):
        self.page.pop_dialog()

    def _load_games(self):
        self.games_grid.controls.clear()

        if self.favorites_only:
            cards = self.game_controller.load_favorites(
                self._open_game,
                self._toggle_favorite,
                self._on_delete_game
            ).data
        else:
            cards = self.game_controller.load_games(
                self._open_game,
                self._toggle_favorite,
                self._on_delete_game
            ).data

        self.games_grid.controls.extend(cards)

    def _open_game(self, e):
        self.content = GameDetailsView(
            on_back=self._show_games,
            preset_settings_controller=self.preset_settings_controller,
            game_controller=self.game_controller
        )

        self.update()

    def _load_games(self):
        self.games_grid.controls.clear()

        if self.favorites_only:
            result = self.game_controller.load_favorites(
                self._open_game,
                self._toggle_favorite,
                self._on_delete_game
            )
        else:
            result = self.game_controller.load_games(
                self._open_game,
                self._toggle_favorite,
                self._on_delete_game
            )

        if result.notification is not None:
            self.page.show_dialog(
                result.notification
            )

        if result.data is None:
            return

        self.games_grid.controls.extend(
            result.data
        )

    def _open_game(self, game: Game):
        self.content = GameDetailsView(
            game=game,
            on_back=self._show_games,
            preset_settings_controller=self.preset_settings_controller,
            game_controller=self.game_controller
        )

        self.update()

    def _result_handler(self, result: ControllerResult[Game]):

        if result.data is None:
            if result.notification is not None:
                self.page.show_dialog(
                    result.notification
                )
            return

        self.page.pop_dialog()

        self._load_games()
        self.update()

        if result.notification is not None:
            self.page.show_dialog(
                result.notification
            )

    def _toggle_favorite(self, game: Game):
        result = self.game_controller.on_toggle_favorite(game)

        if result.notification is not None:
            self.page.show_dialog(
                result.notification
            )

        if result.data is None:
            return

        self._load_games()
        self.update()

    def _search_games(self):
        result = self.game_controller.on_search(
            query=self.header.search_field.value,
            on_open=self._open_game,
            on_favorite=self._toggle_favorite,
            on_delete=self._on_delete_game
        )

        if result.notification is not None:
            self.page.show_dialog(
                result.notification
            )

        if result.data is None:
            return

        self.games_grid.controls.clear()
        self.games_grid.controls.extend(
            result.data
        )

        self.update()

    def _add_game(self):
        if not self.game_dialog.form.validate():
            return

        result = self.game_controller.on_add_game(
            name=self.game_dialog.form.name_field.value,
            description=self.game_dialog.form.description_field.value,
            favorite=bool(
                self.game_dialog.form.favorite_checkbox.value
            ),
            cover_path=self.game_dialog.form.cover_picker.cover_value,
        )

        self._result_handler(result)

    def _on_delete_game(self, game: Game):
        result = self.game_controller.on_delete_game(game)
        self._result_handler(result)