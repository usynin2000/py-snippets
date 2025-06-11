from collections import defaultdict


def collect_dictionary(obj) -> dict:
    inv_obj = defaultdict(list)
    for key, value in obj.items():
        inv_obj[value].append(key)

    return dict(inv_obj)



if __name__ == "__main__":
    ages = {
        'Peter': 10,
        'Isabel': 10,
        'Anna': 9,
    }

    print(collect_dictionary(ages))