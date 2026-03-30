import math
from typing import Callable

from .integrator import IntegrationMethod, Integrator


def get_arc_length(
    start: float, end: float, func: Callable[[float], float], steps: int
) -> float:
    def arc_func(x: float) -> float:
        h = 1e-8
        df_dx = (func(x + h) - func(x - h)) / (2 * h)

        return math.sqrt(1 + df_dx**2)

    return Integrator(start, end, arc_func, steps, IntegrationMethod.LEFT).calculate()
