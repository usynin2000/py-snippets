

def all_equal(lst: list):
    return len(set(lst)) == 1

def all_unique(lst: list) -> bool:
    return len(set(lst)) == len(lst)






if __name__ == "__main__":
    lst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lst_2 = [2, 2, 2, 2, 2]

    print(all_equal(lst_1))
    print(all_equal(lst_2))
    print(all_unique(lst_1))
    print(all_unique(lst_2))