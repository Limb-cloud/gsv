from dataclasses import dataclass


@dataclass
class GraphicsSettings:
    preset: str | None = None
    textures: str | None = None
    shadows: str | None = None
    ray_tracing: str | None = None
    upscaler: str | None = None