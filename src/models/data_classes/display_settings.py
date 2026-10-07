from dataclasses import dataclass


@dataclass
class DisplaySettings:
    resolution: str | None = None
    display_mode: str | None = None
    refresh_rate: int | None = None
    fps_limit: int | None = None