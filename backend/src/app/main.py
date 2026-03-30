import argparse
import math
from typing import Callable

from model import (
    Integrator,
    IntegrationMethod,
    get_volume_disk_method,
    get_volume_shell_method,
    get_arc_length,
)


def main():
    """
    Calculates the total area of a simple parable (x²)
    """

    start = 0
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
    trapezoid_area = get_total_area(
        args.start, args.end, args.steps, func, IntegrationMethod.TRAPEZOIDAL
    )
    volume = get_volume_disk_method(args.start, args.end, args.steps, func)
    shell = get_volume_shell_method(args.start, args.end, args.steps, func)
    arc = get_arc_length(args.start, args.end, func, args.steps)

    print("Total Area: \t\t", area)
    print("Trapezoid Area: \t", trapezoid_area)
    print("Disk Volume: \t\t", volume)
    print("Shell Volume: \t\t", shell)
    print("Arc length: \t\t", arc)


def get_total_area(
    start: int,
    end: int,
    steps: int,
    func: Callable[[float], float],
    direction: IntegrationMethod = IntegrationMethod.MIDPOINT,
) -> float:
    return Integrator(start, end, func, steps, IntegrationMethod.MIDPOINT).calculate()


main()
