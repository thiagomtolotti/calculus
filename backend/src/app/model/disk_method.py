import math
from typing import Callable

from model.riemann_sum import RiemannSum


def get_volume_disk_method(
    start: int, end: int, steps: int, func: Callable[[float], float]
):
    def volume_func(x: float) -> float:
        return math.pi * (func(x) ** 2)

    return RiemannSum(start, end, volume_func, steps).total
