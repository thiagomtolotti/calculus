import math
from typing import Callable

from model.riemann_sum import RiemannSum


def get_volume_shell_method(
    start: int, end: int, steps: int, func: Callable[[float], float]
):
    def volume_func(x: float) -> float:
        return 2 * math.pi * abs(x) * func(x)

    return RiemannSum(start, end, volume_func, steps).total
