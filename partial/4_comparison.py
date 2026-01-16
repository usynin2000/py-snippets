from functools import partial
from string import punctuation
import time

# Compare partial with lambda and ordinary funcs

def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"


# 1. Using partial
greet_casual = partial(greet, greeting="Hi", punctuation="!")
greet_formal = partial(greet, greeting="Good morning", punctuation=".")

# Usning lambda
greet_casual_lambda = lambda name: greet(name, greeting="Hi", punctuation="!")
greet_formal_lambda = lambda name: greet(name, greeting="Good morning", punctuation=".")


# 3. Использование обычных функций
def greet_casual_function(name):
    return greet(name, greeting="Hi", punctuation="!")

def greet_formal_function(name):
    return greet(name, greeting="Good morning", punctuation=".")


# Testing
names = ["Alice", "Bob", "Charlie", "Diana"]
print("Testing partial:")
start = time.time()
for name in names:
    result = greet_casual(name)
    print(f"   {result}")
partial_time = time.time() - start

print("\Testing lambda:")
start = time.time()
for name in names:
    result = greet_casual_lambda(name)
    print(f"  {result}")
lambda_time = time.time() - start

print("\Testing ordinary func:")
start = time.time()
for name in names:
    result = greet_casual_function(name)
    print(f"  {result}")
function_time = time.time() - start



print(f"\Time :")
print(f"  Partial: {partial_time:.6f} сек") # 
print(f"  Lambda: {lambda_time:.6f} сек")
print(f"  Function: {function_time:.6f} сек")


# Benefits of partial
# 1. Readble code
# 2. We can inspect params
def process_data(data, operation, threshold=0):
    return [operation(x) for x in data if x > threshold]

get_squares = partial(process_data, operation=lambda x: x**2)

print(f"  Function: {get_squares.func}")
print(f"  Arguments: {get_squares.keywords}")