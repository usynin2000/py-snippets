def to_dict(keys: list, values: list) -> dict:
    return dict(zip(keys, values))


if __name__ == "__main__":
    print(to_dict(["ke1", "key2"], ["value1", "value2"]))
