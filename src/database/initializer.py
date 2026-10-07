from models.abstract.base import Base
from database.database import Database

from models.data_classes.control_settings import ControlSettings
from models.data_classes.display_settings import DisplaySettings
from models.data_classes.graphics_settings import GraphicsSettings
from models.data_classes.performance_settings import PerformanceSettings
from models.game import Game
from models.preset import Preset


class DatabaseInitializer:
    def __init__(self, database: Database):
        self._database = database

    def initialize(self) -> None:
        first_launch = not self._database.db_path.exists()

        self._create_tables()

        if first_launch:
            self._seed_initial_data()

    def _create_tables(self) -> None:
        Base.metadata.create_all(
            bind=self._database.engine
        )

    def _seed_initial_data(self) -> None:
        with self._database.session_factory.begin() as session:
            game = Game(
                name="Cyberpunk 2077",
                description="Основные игровые настройки Cyberpunk 2077",
                cover_path=None,
                favorite=True,
            )

            session.add(game)
            session.flush()

            if game.id is None:
                raise RuntimeError(
                    "Не удалось получить ID игры"
                )

            preset1 = Preset(
                game_id=game.id,
                name="1440p Ultra",
                display=DisplaySettings(
                    resolution="2560x1440",
                    display_mode="Fullscreen",
                    refresh_rate=240,
                    fps_limit=120,
                ),
                graphics=GraphicsSettings(
                    preset="Ultra",
                    textures="Ultra",
                    shadows="High",
                    ray_tracing="High",
                    upscaler="DLSS Quality",
                ),
                control=ControlSettings(
                    dpi=800,
                    sensitivity=0.75,
                    fov=100,
                ),
                performance=PerformanceSettings(
                    average_fps=115,
                    gpu_temperature=72,
                    cpu_temperature=64,
                ),
                notes="Основной пресет для игры в 1440p",
            )

            preset2 = Preset(
                game_id=game.id,
                name="1080p Ultra",
                display=DisplaySettings(
                    resolution="2560x1440",
                    display_mode="Fullscreen",
                    refresh_rate=240,
                    fps_limit=120,
                ),
                graphics=GraphicsSettings(
                    preset="Ultra",
                    textures="Ultra",
                    shadows="High",
                    ray_tracing="High",
                    upscaler="DLSS Quality",
                ),
                control=ControlSettings(
                    dpi=800,
                    sensitivity=0.75,
                    fov=100,
                ),
                performance=PerformanceSettings(
                    average_fps=115,
                    gpu_temperature=72,
                    cpu_temperature=64,
                ),
                notes="Основной пресет для игры в 1440p",
            )

            game.presets.append(preset1)
            game.presets.append(preset2)