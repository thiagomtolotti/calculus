import math
from typing import Callable

from .integrator import Integrator


def get_volume_shell_method(
    start: int, end: int, steps: int, func: Callable[[float], float]
):
    def volume_func(x: float) -> float:
        return 2 * math.pi * abs(x) * func(x)

    return Integrator(start, end, volume_func, steps).calculate()
