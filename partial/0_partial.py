from functools import partial

# Ordindary func
def multiply(x, y, z=1):
    return x * y * z

# Create partly executed fun

double = partial(multiply, y=2)  # state that y = 2
triple = partial(multiply, y=3)  # start that y = 3

print(double(5))
print(triple(5))

print(double(5, z=3))