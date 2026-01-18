
# Concept of the perceptron cycle:
# 1. Take an example (x, y)
# 2. Make a prediction
# 3. If you made a mistake:
# 4. Tweak the weights and bias
# 5. Repeat


# Perceptron is not a formula,
# but a process of multiple corrections.

# =========================
# ДАННЫЕ (AND)
# =========================
data = [
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 1),
] # x1, x2, y_true (correct answer)

# =========================
# ПАРАМЕТРЫ МОДЕЛИ
# =========================
w1, w2 = 0.0, 0.0
b = 0.0
lr = 0.1

# =========================
# ОБУЧЕНИЕ
# =========================
epochs = 10 # number of iterations of the cycle

for epoch in range(epochs):
    errors_in_epoch = 0

    print(f"\n=== EPOCH {epoch} ===")

    for x1, x2, y_true in data:
        # --- predict ---
        s = x1 * w1 + x2 * w2 + b
        y_pred = 1 if s >= 0 else 0

        # --- error ---
        error = y_true - y_pred

        print(
            f"x=({x1},{x2}) "
            f"pred={y_pred} "
            f"true={y_true} "
            f"error={error}"
        )

        # --- update ---
        if error != 0:
            errors_in_epoch += 1

            w1 += lr * error * x1
            w2 += lr * error * x2
            b  += lr * error

            print(
                f"  update → "
                f"w1={w1:.2f}, w2={w2:.2f}, b={b:.2f}"
            )

    print(f"Errors in epoch {epoch}: {errors_in_epoch}")


# ❗ Perceptron is not looking for numbers, but for a rule.
# Numbers are just its specific implementation.
 