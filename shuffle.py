from copy import deepcopy
from random import randint

#Randomizes the order of the values of an list, returning a new list.

#Uses the Fisher-Yates algorithm to reorder the elements of the list.
#random.shuffle provides similar functionality to this snippet.

def shuffle_fisher_yates_(lst: list) -> list:
    temp_lst = deepcopy(lst)
    m = len(temp_lst)
    while m:
        m -= 1
        i = randint(0, m)
        temp_lst[i], temp_lst[m] = temp_lst[m], temp_lst[i]

    return temp_lst


if __name__ == "__main__":
    print(shuffle_fisher_yates_([1, 2, 3, 4, 5]))