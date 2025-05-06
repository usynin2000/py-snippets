from typing import Any


def ez_example(lst_1: list, lst_2: list) -> Any:
    zipped = zip(lst_1, lst_2)
    return list(zipped)


def iterator_example(lst_1: list, lst_2: list) -> Any:
    zipped = zip(lst_1, lst_2)
    return zipped


if __name__ == "__main__":
    names = ["Serega", "Narek", "Zheka", "Max"]
    ages = [100, 28, 300, 22]
    print(ez_example(names, ages))

    # example of zip shortened
    ages = [20, 30, 40]
    print(ez_example(names, ages))

    zipped = iterator_example(names, ages)
    print(next(zipped))
    print(next(zipped))
    print(next(zipped))
    names = ["Serega", "Any"]
    ages = [24, 18]
    zipped = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
    names, ages = zip(*zipped)

    print(names)
    print(ages)
