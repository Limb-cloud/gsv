import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from enums.paths import Paths


class Database:
    def __init__(self):
        self._data_dir = self._get_data_directory()
        self._db_path = self._data_dir / "game_settings.db"

        self._engine = create_engine(
            f"sqlite+pysqlite:///{self._db_path.as_posix()}",
            echo=False,
        )

        self._session_factory = sessionmaker(
            bind=self._engine,
            autoflush=False,
            expire_on_commit=False,
        )

    def _get_data_directory(self) -> Path:
        flet_data_dir = os.getenv("FLET_APP_STORAGE_DATA")

        if flet_data_dir:
            data_dir = Path(flet_data_dir)
        else:
            data_dir = (
                Path(Paths.BASE_DIR.value)
                / "data"
            )

        data_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        return data_dir

    @property
    def engine(self):
        return self._engine

    @property
    def session_factory(self):
        return self._session_factory

    @property
    def db_path(self) -> Path:
        return self._db_path

    def create_session(self):
        return self._session_factory()