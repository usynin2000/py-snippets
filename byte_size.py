

def byte_size(s: str) -> int:
    return len(s.encode("utf-8"))



if __name__ == "__main__":
    print(byte_size(""))
    print(byte_size(" "))
    print(byte_size("huy"))
    print(byte_size("Hello World!"))
    print(byte_size("😀"))