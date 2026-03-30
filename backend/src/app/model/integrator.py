from enum import Enum
from typing import Callable


class IntegrationMethod(Enum):
    LEFT = 0
    RIGHT = 1
    MIDPOINT = 2
    TRAPEZOIDAL = 3


class Integrator:
    def __init__(
        self,
        start: float,
        end: float,
        func: Callable[[float], float],
        steps: int,
        method: IntegrationMethod = IntegrationMethod.LEFT,
    ):
        """
        Calculates the Riemann Sum of a given function over an interval.

        :param start: The start of the interval
        :param end: The end of the interval
        :param func: The function to integrate
        :param steps: The number of rectangles to use
        :param direction: Whether to sample from the left, right, or midpoint of each step
        """

        if steps <= 0:
            raise ValueError("Steps must be greater than zero")

        if not isinstance(start, (float, int)) or not isinstance(end, (float, int)):  # type: ignore
            raise TypeError("Start and end must be floats")

        if start >= end:
            raise ValueError("Start must be less than end")

        if not callable(func):
            raise TypeError("Function must be callable")

        if not isinstance(method, IntegrationMethod):  # type: ignore
            raise TypeError("Direction must be an instance of RiemannSumDirection")

        self.func = func
        self.start = start
        self.end = end
        self.steps = steps
        self.dx = (end - start) / steps
        self.method = method

    def calculate(self) -> float:
        acc: float = 0

        for step in range(self.steps):
            acc += self._get_slice(step)

        return acc

    def _get_steps_coordinates(self, step: int) -> tuple[float, float]:
        start = self.start + step * self.dx
        finish = start + self.dx

        return start, finish

    def _get_height(self, x: float) -> float:
        return self.func(x)

    def _get_slice(self, step: int) -> float:
        x_i = self.start + step * self.dx
        x_next = x_i + self.dx

        if self.method == IntegrationMethod.TRAPEZOIDAL:
            return self.dx * (self.func(x_i) + self.func(x_next)) / 2

        sample_point = {
            IntegrationMethod.LEFT: x_i,
            IntegrationMethod.RIGHT: x_next,
            IntegrationMethod.MIDPOINT: (x_i + x_next) / 2,
        }[self.method]

        return self.dx * self.func(sample_point)
