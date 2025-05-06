from math import sqrt


def is_prime(n: int) -> bool:
    if n <= 0 or (n % 2 == 0 and n > 3):
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(is_prime(3))
    print(is_prime(10))
    print(is_prime(121))
    print(is_prime(7))
