import ast

code = """
def hello(name: str) -> str:
    return f"Hello {name}!"
"""


tree = ast.parse(code)


if __name__ == "__main__":
    print(ast.dump(tree, indent=4))