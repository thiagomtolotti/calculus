import math
import pytest

from typing import Any, Callable, cast
from .riemann_sum import RiemannSum, RiemannSumDirection


class TestRiemannSum:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.start = 0
        self.end = 1
        self.steps = 1000

        self.function: Callable[[float], float] = lambda x: x**2

    def test_left(self):
        area = RiemannSum(
            self.start,
            self.end,
            self.function,
            self.steps,
            direction=RiemannSumDirection.LEFT,
        ).area

        assert math.isclose(area, 1 / 3, rel_tol=1e-2)

    def test_middle(self):
        area = RiemannSum(
            self.start,
            self.end,
            self.function,
            self.steps,
            direction=RiemannSumDirection.MIDDLE,
        ).area

        assert math.isclose(area, 1 / 3, rel_tol=1e-3)

    def test_right(self):
        area = RiemannSum(
            self.start,
            self.end,
            self.function,
            self.steps,
            direction=RiemannSumDirection.RIGHT,
        ).area

        assert math.isclose(area, 1 / 3, rel_tol=1e-2)

    def test_default_direction(self):
        area = RiemannSum(self.start, self.end, self.function, self.steps).area

        assert math.isclose(area, 1 / 3, rel_tol=1e-2)

    def test_zero_steps(self):
        with pytest.raises(ValueError):
            RiemannSum(self.start, self.end, self.function, steps=0).area

    def test_negative_steps(self):
        with pytest.raises(ValueError):
            RiemannSum(self.start, self.end, self.function, steps=-1).area

    def test_non_callable_function(self):
        with pytest.raises(TypeError):
            RiemannSum(
                self.start,
                self.end,
                func=cast(Any, "not a function"),
                steps=self.steps,
            ).area

    def test_non_numeric_start_end(self):
        with pytest.raises(TypeError):
            RiemannSum(
                start=cast(Any, "not a number"),
                end=cast(Any, "not a number"),
                func=self.function,
                steps=self.steps,
            ).area

    def test_non_numeric_steps(self):
        with pytest.raises(TypeError):
            RiemannSum(
                self.start,
                self.end,
                self.function,
                steps=cast(Any, "not a number"),
            ).area

    def test_non_numeric_direction(self):
        with pytest.raises(TypeError):
            RiemannSum(
                self.start,
                self.end,
                self.function,
                self.steps,
                direction=cast(
                    Any, "Direction must be an instance of RiemannSumDirection"
                ),
            ).area

    def test_large_steps(self):
        area = RiemannSum(
            self.start,
            self.end,
            self.function,
            steps=1000000,
            direction=RiemannSumDirection.MIDDLE,
        ).area

        assert math.isclose(area, 1 / 3, rel_tol=1e-4)

    def test_small_steps(self):
        area = RiemannSum(
            self.start,
            self.end,
            self.function,
            steps=10,
            direction=RiemannSumDirection.MIDDLE,
        ).area

        assert math.isclose(area, 1 / 3, rel_tol=1e-1)

    def test_start_greater_than_end(self):
        with pytest.raises(ValueError):
            RiemannSum(
                start=1,
                end=0,
                func=self.function,
                steps=self.steps,
            ).area

    def test_rectangle(self):
        area = RiemannSum(
            self.start,
            self.end,
            lambda x: 1,
            self.steps,
            direction=RiemannSumDirection.LEFT,
        ).area

        assert math.isclose(area, 1, rel_tol=1e-7)

    def test_zero_area(self):
        area = RiemannSum(
            self.start,
            self.end,
            lambda x: 0,
            self.steps,
            direction=RiemannSumDirection.LEFT,
        ).area

        assert math.isclose(area, 0, rel_tol=1e-7)
