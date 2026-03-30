import math
from typing import Callable

from .integrator import Integrator


def get_volume_disk_method(
    start: int, end: int, steps: int, func: Callable[[float], float]
):
    def volume_func(x: float) -> float:
        return math.pi * (func(x) ** 2)

    return Integrator(start, end, volume_func, steps).total
