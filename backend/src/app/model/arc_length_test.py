import math
from typing import Callable
import pytest

from .arc_length import get_arc_length


@pytest.mark.parametrize(
    "func, start, end, expected",
    [
        (lambda _: 10, 0, 1, 1),  # type: ignore
        (lambda x: x, 0, 1, math.sqrt(2)),  # type: ignore[arg-type]
        (lambda x: math.sqrt(1 - x**2), 0, 1, math.pi / 2),  # type: ignore
    ],
)
def test_arc_length(
    func: Callable[[float], float], start: int, end: int, expected: float
):
    length = get_arc_length(start, end, func, 10000)

    assert math.isclose(length, expected, rel_tol=1e-2)
