

def compact(lst: list) -> list:
    return list(filter(None, lst))



if __name__ == '__main__':

    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, False, '', "", "s", " ", None, 0]
    print(compact(lst))