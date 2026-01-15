from functools import partial

def power(base, exponent, modulo=None):
    result  = base ** exponent
    return result % modulo if modulo else result 

# Add partluy useble func

square = partial(power, exponent=2)
cube = partial(power, exponent=3)
power_of_10 = partial(power, base=10)  


print("Squares")
print(f"square(5) = {square(5)}")
print(f"square(3) = {square(3)}")


print("\nCubes")
print(f"cube(2) = {cube(2)}")
print(f"cube(4) = {cube(4)}")


print("\n Power of 10:")
print(f"power_of_10(2) = {power_of_10(exponent=2)}")
print(f"power_of_10(3) = {power_of_10(exponent=3)}")
