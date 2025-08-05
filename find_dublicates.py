

## return dublicates and unique values
def find_dublicates_On2(a: list) -> tuple[list, list]:
    ## return dublicates list and unique values list

    dublicates = list()
    unique_values = list()

    for i in a:
        if i in a[i:]:
            dublicates.append(i)
        else:
            unique_values.append(i)

    return list(set(dublicates)), list(set(unique_values))


from collections import Counter

def find_dublicates_On(a: list) -> tuple[list, list]:
    counter = Counter(a)

    dublicates = [key for key, value in counter.items() if value > 1]
    unique = [key for key, value in counter.items() if value == 1]

    return list(set(dublicates)), unique



if __name__ == "__main__":
    print(find_dublicates_On2([1, 2, 3, 3, 4, 2, 123, 34, 2, 5, 6]))
    print(find_dublicates_On([1, 2, 5,  3, 3, 4, 2, 123, 34, 2, 5, 6]))