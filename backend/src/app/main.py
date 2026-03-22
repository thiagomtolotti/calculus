from model.rienmann_sum import RiemannSum


def main():
    """
    Calculates the total area of a simple parable (x²)
    """

    start = 0
    end = 1
    steps = 1000

    area = get_total_area(start, end, steps)
    print("Total Area: ", area)


def get_total_area(start: int, end: int, steps: int) -> float:
    return RiemannSum(start, end, steps).area


main()
