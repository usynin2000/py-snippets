def average(*args):
    return sum(args, 0.0) / len(args)


## 0.0 to make it float


if __name__ == "__main__":
    print(average(*[1, 2, 3]))
    print(average(1, 2, 3))
    print(average(1, 2, 5))
