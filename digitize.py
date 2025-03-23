

def digitize(number: int) -> list:
    return list(map(int, str(number)))


if __name__ == "__main__":
    print(digitize(123))