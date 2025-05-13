

def invert_dict(obj: dict) -> dict:
    return {
        value: key for key, value in obj.items()
    }



if __name__ == "__main__":
    ages = {
        'Peter': 10,
        'Isabel': 11,
        'Anna': 9,
    }

    print(invert_dict(ages))