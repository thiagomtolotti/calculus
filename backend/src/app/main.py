import argparse
import math
from typing import Callable

from model.riemann_sum import RiemannSum, RiemannSumDirection


def main():
    """
    Calculates the total area of a simple parable (x²)
    """

    start = -1
    end = 1
    steps = 1000

    def func(x: float) -> float:
        return math.sqrt(1 - x**2)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--start", type=int, default=start, help="The start of the interval"
    )
    parser.add_argument(
        "-e", "--end", type=int, default=end, help="The end of the interval"
    )
    parser.add_argument(
        "-t", "--steps", type=int, default=steps, help="The number of steps"
    )

    args = parser.parse_args()

    area = get_total_area(args.start, args.end, args.steps, func)
    volume = get_total_volume(args.start, args.end, args.steps, func)

    print("Total Area: ", area)
    print("Total Volume: ", volume)


def get_total_area(
    start: int, end: int, steps: int, func: Callable[[float], float]
) -> float:
    return RiemannSum(start, end, func, steps, RiemannSumDirection.MIDDLE).total


def get_total_volume(start: int, end: int, steps: int, func: Callable[[float], float]):
    def volume_func(x: float) -> float:
        return math.pi * (func(x) ** 2)

    return RiemannSum(start, end, volume_func, steps).total


main()
