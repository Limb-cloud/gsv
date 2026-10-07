from dataclasses import dataclass


@dataclass
class ControlSettings:
    dpi: int | None = None
    sensitivity: float | None = None
    fov: int | None = None