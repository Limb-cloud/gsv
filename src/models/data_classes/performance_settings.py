from dataclasses import dataclass


@dataclass
class PerformanceSettings:
    average_fps: int | None = None
    gpu_temperature: int | None = None
    cpu_temperature: int | None = None