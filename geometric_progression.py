from math import floor, log


def geometric_progression(
    end: int,
    start: int = 1,
    step: int = 2,
):
    return [
        start * step ** i for i in range(floor(log(end / start) / log(step)) + 1)
    ]





if __name__ == "__main__":
    print(geometric_progression(256))  # [1, 2, 4, 8, 16, 32, 64, 128, 256]
    print(geometric_progression(256, 3))  # [3, 6, 12, 24, 48, 96, 192]
    print(geometric_progression(256, 1, 4))  # [1, 4, 16, 64, 256]