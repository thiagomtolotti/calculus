import math
from typing import Callable

import pytest

from .shell_method import get_volume_shell_method


@pytest.mark.parametrize(
    "func, start, end, expected",
    [
        (lambda x: x, 0, 1, 2 * math.pi / 3),  # type: ignore[arg-type]
        (lambda x: 1 - x**2, 0, 1, math.pi / 2),  # type: ignore
    ],
)
def test_disk_method(
    func: Callable[[float], float], start: int, end: int, expected: float
):
    volume = get_volume_shell_method(start, end, 1000, func)

    assert math.isclose(volume, expected, rel_tol=1e-2)
