
def merge_dictionaries(*dicts) -> dict:
    res = dict()
    for d in dicts:
        res.update(d)
    return res




if __name__ == "__main__":
    ages_one = {
        'Peter': 10,
        'Isabel': 11,
    }
    ages_two = {
        'Anna': 9
    }
    ages_three = {
        "Sergo": 24
    }
    print(merge_dictionaries(ages_one, ages_two, ages_three))