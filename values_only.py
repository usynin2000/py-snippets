
def values_only(flat_dict: dict) -> dict:
    return list(flat_dict.values())



if __name__ == "__main__":
    ages = {
        'Peter': 10,
        'Isabel': 11,
        'Anna': 9,
    }
    print(values_only(ages))