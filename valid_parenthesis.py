# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
#
# The input string s is valid if and only if:
#
# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.


def valid_parenthesis_brure_force(s: str) -> bool:
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")
    return s == ""


def valid_parenthesis_stack(s: str) -> bool:
    stack = list()
    pairs = {
        "]": "[",
        ")": "(",
        "}": "{"
    }

    for c in s:
        if c in pairs:
            if stack and stack[-1] == pairs[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False




if __name__ == "__main__":
    s = "([{}])"
    print(valid_parenthesis_brure_force(s))
    print(valid_parenthesis_stack(s))