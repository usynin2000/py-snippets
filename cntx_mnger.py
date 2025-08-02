from contextlib import contextmanager

## first option with Class


class ContextManager:
    def __enter__(self):
        print("Entering the context manager")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context manager")
        if exc_type:
            print("Error", exc_val)
        return True


@contextmanager
def temporary_append(lst, item):
    lst.append(item)
    try:
        yield lst
    except Exception as e:
        print("Error", e)
    finally:
        lst.remove(item)
        print("Done. Exiting the context manager", lst)


if __name__ == "__main__":
    with ContextManager():
        print("Working inside the class")


    with temporary_append([1, 2, 3], 99) as temp:
        print("Inside", temp)