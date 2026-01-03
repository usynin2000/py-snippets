x1 = 1 # Fact that weather is good
x2 = 0 # Fact that I don't have time

w1 = 0.7
w2 = 1.0

b = -0.8 # Threshold / bias  that I am lazy

s1 = x1 * w1 + x2 * w2 + b

y = 1 if s1 >= 0 else 0

print(y)

# Читается как:

# «Тепло важно, время ещё важнее, но я ленив»