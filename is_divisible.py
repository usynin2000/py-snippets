

def is_divisibile(dividend: int, divisor: int) -> bool:
    return dividend % divisor == 0


if __name__ == "__main__":
    print(is_divisibile(6, 3))
    print(is_divisibile(2, 10))
    print(is_divisibile(200, 10))
    print(is_divisibile(3241, 4))