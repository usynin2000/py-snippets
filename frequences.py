from collections import defaultdict


def frequencies(lst) -> dict:
    freq = defaultdict(int)
    for a in lst:
        freq[a] += 1
    return dict(freq)


def frequenceies_without_defaultdict(lst: list) -> dict:
    freq = {}
    for el in lst:
        if el in freq:
            freq[el] += 1
        else:
            freq[el] = 1
    return freq


if __name__ == "__main__":
    info = ["a", "b", "a", "c", "a", "c"]
    print(frequencies(info))
    print(frequenceies_without_defaultdict(info))
