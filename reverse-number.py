from math import copysign


def reverse_number(n) -> float:
    return copysign(float(str(n)[::-1].replace("-", "")), n)



if __name__ == "__main__":
    print(reverse_number(981))  # 189
    print(reverse_number(-500)) # -5
    print(reverse_number(73.6))  # 6.37
    print(reverse_number(-5.23))  # -32.5