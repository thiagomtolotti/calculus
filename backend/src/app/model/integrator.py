from enum import Enum
from typing import Callable


class IntegratorMethod(Enum):
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
        method: IntegratorMethod = IntegratorMethod.LEFT,
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

        if not isinstance(method, IntegratorMethod):  # type: ignore
            raise TypeError("Direction must be an instance of RiemannSumDirection")

        self.func = func
        self.start = start
        self.end = end
        self.steps = steps
        self.dx = (end - start) / steps
        self.direction = method

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

    def _get_effective_x(self, step: int) -> float:
        start, finish = self._get_steps_coordinates(step)

        if self.direction == IntegratorMethod.LEFT:
            return start
        elif self.direction == IntegratorMethod.RIGHT:
            return finish

        return (start + finish) / 2

    def _get_slice(self, step: int) -> float:
        if self.direction == IntegratorMethod.TRAPEZOIDAL:
            start, finish = self._get_steps_coordinates(step)

            start_height = self._get_height(start)
            end_height = self._get_height(finish)
            triangle_height = end_height - start_height

            return (self.dx * start_height) + (self.dx * triangle_height) / 2

        effective_x = self._get_effective_x(step)
        triangle_height = self._get_height(effective_x)

        return self.dx * triangle_height
