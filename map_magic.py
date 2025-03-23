

def square_numbers(numbers: list) -> list:
    return list(map(lambda num: num ** 2, numbers))

def string_casting(numbers: list) -> list:
    return list(map(str, numbers))

def list_addings(a: list, b: list) -> list:
    return list(
        map(
            lambda x, y: x + y,
            a,
            b,
        )
    )

def upper_words(words: list) -> list:
    return list(map(str.upper, words))


def len_words(words: list) -> list:
    return list(map(len, words))

def rm_not_digits(lst: list) -> list:
    return list(
        map(
            lambda x: int(x) if x.isdigit() else None,
            lst
        )
    )




if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print(square_numbers(lst))
    print(string_casting(lst))
    lst_2 = [10, 20, 30, 40, 50]
    print(list_addings(lst, lst_2))

    lst_3 = ["hello", "world", "we", "are", "here"]
    print(upper_words(lst_3))

    print(len_words(lst_3))

    lst_4 = ["1", "3", "hey", "foo", "bar"]
    print(rm_not_digits(lst_4))
