# =========================
# 1. DATA (One Example)
# =========================

# Inputs: what happened in reality
x1 = 1          # factor 1 (for example: warm)
x2 = 0          # factor 2 (for example: time)

# Correct answer
y_true = 0      # for AND: (1, 0) -> 0

print("=== INPUT ===")
print(f"x1 = {x1}, x2 = {x2}")
print(f"y_true (correct answer) = {y_true}")


# =========================
# 2. PARAMETERS OF THE MODEL
# =========================

# Weights - how important each factor is
w1 = 0.6
w2 = 0.6

# Bias - overall "mood" of the model
b = -0.5

# Learning rate - how strongly we react to the error
lr = 0.1

print("\n=== INITIAL MODEL ===")
print(f"w1 = {w1}, w2 = {w2}")
print(f"b  = {b}")
print(f"learning rate = {lr}")


# =========================
# 3. DIRECT PASS (PREDICT)
# =========================

# Calculate the confidence of the model
# This is just a weighted sum + threshold
s = x1 * w1 + x2 * w2 + b

# Apply the perceptron rule:
# if confidence >= 0 → say 1, otherwise 0
y_pred = 1 if s >= 0 else 0

print("\n=== PREDICT ===")
print(f"s = x1*w1 + x2*w2 + b")
print(f"s = {x1}*{w1} + {x2}*{w2} + {b} = {s}")
print(f"y_pred (model answer) = {y_pred}")


# =========================
# 4. ERROR
# =========================

# Error is a signal:
# - do we need to change the weights
# - in which direction
error = y_true - y_pred

print("\n=== ERROR ===")
print(f"error = y_true - y_pred = {y_true} - {y_pred} = {error}")

if error == 0:
    print("→ Model was correct. No changes needed.")
elif error > 0:
    print("→ Model was too pessimistic, it says 0 too easily (said 0, but should be 1).")
elif error < 0:
    print("→ Model was too optimistic, it gives 1 to easily (said 1, but should be 0).")


# =========================
# 5. LEARNING (UPDATE)
# =========================

print("\n=== TRAINING (UPDATE) ===")
print("Rule: change only what participated in the decision")

# Update the weight of the first input
print("\nUpdating w1:")
print(f"w1 = w1 + lr * error * x1")
print(f"w1 = {w1} + {lr} * {error} * {x1}")

w1_new = w1 + lr * error * x1
print(f"w1_new = {w1_new}")

# Update the weight of the second input
print("\nUpdating w2:")
print(f"w2 = w2 + lr * error * x2")
print(f"w2 = {w2} + {lr} * {error} * {x2}")

w2_new = w2 + lr * error * x2
print(f"w2_new = {w2_new}")
print("x2 was 0, so it was not involved in the decision, so w2 is not updated")

# Update the bias
print("\nUpdating b (global strictness):")
print(f"b = b + lr * error")
print(f"b = {b} + {lr} * {error}")

b_new = b + lr * error
print(f"b_new = {b_new}")


# =========================
# 6. APPLYING THE CHANGES
# =========================

w1, w2, b = w1_new, w2_new, b_new

print("\n=== UPDATED MODEL ===")
print(f"w1 = {w1}, w2 = {w2}")
print(f"b  = {b}")


# =========================
# 7. CHECKING AFTER TRAINING
# =========================

s = x1 * w1 + x2 * w2 + b
y_pred = 1 if s >= 0 else 0

print("\n=== AFTER TRAINING PREDICT ===")
print(f"s = {s}")
print(f"y_pred = {y_pred}")



# If briefly, what you should feel here

# weights change only if the input participated

# b changes always, because it's about the «general»

# code is just a regular logic, not ML-magic