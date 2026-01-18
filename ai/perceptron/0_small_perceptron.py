x = 1        # input: fact or not
w = 0.2      # importance of the fact (weight) We can change it to make the perceptron more or less sensitive to the input
b = -0.5     # threshold / bias (порого или смещение )

s = x * w + b 

y = 1 if s >= 0 else 0

print(y)
