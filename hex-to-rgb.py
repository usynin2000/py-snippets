
def hex_to_rgb(hex_string: str) -> tuple:
    return tuple(int(hex_string[i:i+2], 16) for i in (0, 2, 4))


if __name__ == "__main__":

    print(hex_to_rgb("FFA501"))