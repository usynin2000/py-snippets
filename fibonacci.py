def fibonacci(n: int) -> list:
    if n <= 0:
        return [0]
    sequence = [0, 1]

    while len(sequence) < n:
        next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        sequence.append(next_value)

    return sequence


if __name__ == "__main__":
    print(fibonacci(7))
    print(fibonacci(15))
