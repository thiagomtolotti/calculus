class RiemannSum:
    def __init__(self, start: float, end: float, steps: int):
        """
        Calculates the area of a simple parable (x²) using Riemann Sum.

        :param start: The start of the interval
        :param end: The end of the interval
        :param steps: The number of steps to calculate the area
        """

        self.start = start
        self.end = end
        self.steps = steps
        self.delta_x = (end - start) / steps

        self.area = self.get_area()

    def get_area(self) -> float:
        acc: float = 0

        for step in range(self.steps):
            start, _ = self._get_steps_coordinates(step)

            width = self.delta_x
            height = self._get_height(start)

            area = width * height
            acc += area

        return acc

    def _get_steps_coordinates(self, step: int) -> tuple[float, float]:
        start = self.start + step * self.delta_x
        finish = start + self.delta_x

        return start, finish

    def _get_height(self, x: float) -> float:
        return x**2
