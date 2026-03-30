import math
import pytest

from typing import Any, Callable, cast
from .integrator import Integrator, IntegrationMethod


class TestRiemannSum:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.start = 0
        self.end = 1
        self.steps = 1000

        self.function: Callable[[float], float] = lambda x: x**2

    def test_left(self):
        area = Integrator(
            self.start,
            self.end,
            self.function,
            self.steps,
            method=IntegrationMethod.LEFT,
        ).calculate()

        assert math.isclose(area, 1 / 3, rel_tol=1e-2)

    def test_middle(self):
        area = Integrator(
            self.start,
            self.end,
            self.function,
            self.steps,
            method=IntegrationMethod.MIDPOINT,
        ).calculate()

        assert math.isclose(area, 1 / 3, rel_tol=1e-3)

    def test_right(self):
        area = Integrator(
            self.start,
            self.end,
            self.function,
            self.steps,
            method=IntegrationMethod.RIGHT,
        ).calculate()

        assert math.isclose(area, 1 / 3, rel_tol=1e-2)

    def test_trapezoid(self):
        area = Integrator(
            self.start,
            self.end,
            self.function,
            self.steps,
            method=IntegrationMethod.TRAPEZOIDAL,
        ).calculate()

        assert math.isclose(area, 1 / 3, rel_tol=1e-2)

    def test_default_direction(self):
        area = Integrator(self.start, self.end, self.function, self.steps).calculate()

        assert math.isclose(area, 1 / 3, rel_tol=1e-2)

    def test_zero_steps(self):
        with pytest.raises(ValueError):
            Integrator(self.start, self.end, self.function, steps=0).calculate()

    def test_negative_steps(self):
        with pytest.raises(ValueError):
            Integrator(self.start, self.end, self.function, steps=-1).calculate()

    def test_non_callable_function(self):
        with pytest.raises(TypeError):
            Integrator(
                self.start,
                self.end,
                func=cast(Any, "not a function"),
                steps=self.steps,
            ).calculate()

    def test_non_numeric_start_end(self):
        with pytest.raises(TypeError):
            Integrator(
                start=cast(Any, "not a number"),
                end=cast(Any, "not a number"),
                func=self.function,
                steps=self.steps,
            ).calculate()

    def test_non_numeric_steps(self):
        with pytest.raises(TypeError):
            Integrator(
                self.start,
                self.end,
                self.function,
                steps=cast(Any, "not a number"),
            ).calculate()

    def test_non_numeric_direction(self):
        with pytest.raises(TypeError):
            Integrator(
                self.start,
                self.end,
                self.function,
                self.steps,
                method=cast(
                    Any, "Direction must be an instance of RiemannSumDirection"
                ),
            ).calculate()

    def test_large_steps(self):
        area = Integrator(
            self.start,
            self.end,
            self.function,
            steps=1000000,
            method=IntegrationMethod.MIDPOINT,
        ).calculate()

        assert math.isclose(area, 1 / 3, rel_tol=1e-4)

    def test_small_steps(self):
        area = Integrator(
            self.start,
            self.end,
            self.function,
            steps=10,
            method=IntegrationMethod.MIDPOINT,
        ).calculate()

        assert math.isclose(area, 1 / 3, rel_tol=1e-1)

    def test_start_greater_than_end(self):
        with pytest.raises(ValueError):
            Integrator(
                start=1,
                end=0,
                func=self.function,
                steps=self.steps,
            ).calculate()

    def test_rectangle(self):
        area = Integrator(
            self.start,
            self.end,
            lambda x: 1,
            self.steps,
            method=IntegrationMethod.LEFT,
        ).calculate()

        assert math.isclose(area, 1, rel_tol=1e-7)

    def test_zero_area(self):
        area = Integrator(
            self.start,
            self.end,
            lambda x: 0,
            self.steps,
            method=IntegrationMethod.LEFT,
        ).calculate()

        assert math.isclose(area, 0, rel_tol=1e-7)

    def test_doubled_func(self):
        area = Integrator(
            self.start, self.end, lambda x: 2, self.steps, IntegrationMethod.LEFT
        ).calculate()

        assert math.isclose(area, 2)

    def test_cone(self):
        def area_func(x: float) -> float:
            return x

        def volume_func(x: float) -> float:
            return math.pi * (area_func(x) ** 2)

        area = Integrator(
            0, 1, volume_func, self.steps, IntegrationMethod.LEFT
        ).calculate()

        assert math.isclose(area, math.pi / 3, rel_tol=1e-2)
