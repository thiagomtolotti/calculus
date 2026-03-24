from enum import Enum
from typing import Callable


class RiemannSumDirection(Enum):
    LEFT = 0
    RIGHT = 1
    MIDDLE = 2


class RiemannSum:
    def __init__(
        self,
        start: float,
        end: float,
        func: Callable[[float], float],
        steps: int,
        direction: RiemannSumDirection = RiemannSumDirection.LEFT,
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

        if not isinstance(direction, RiemannSumDirection):  # type: ignore
            raise TypeError("Direction must be an instance of RiemannSumDirection")

        self.start = start
        self.end = end
        self.steps = steps
        self.delta_x = (end - start) / steps
        self.func = func
        self.direction = direction

        self.total = self.integrate()

    def integrate(self) -> float:
        acc: float = 0

        for step in range(self.steps):
            width = self.delta_x
            height = self._get_height(self._get_height_position(step))

            area = width * height
            acc += area

        return acc

    def _get_steps_coordinates(self, step: int) -> tuple[float, float]:
        start = self.start + step * self.delta_x
        finish = start + self.delta_x

        return start, finish

    def _get_height(self, x: float) -> float:
        return self.func(x)

    def _get_height_position(self, step: int) -> float:
        start, finish = self._get_steps_coordinates(step)

        if self.direction == RiemannSumDirection.LEFT:
            return start
        elif self.direction == RiemannSumDirection.RIGHT:
            return finish

        return (start + finish) / 2
