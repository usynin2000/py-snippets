# =========================
# 1. ДАННЫЕ (одИН ПРИМЕР)
# =========================

# Входы: что произошло в реальности
x1 = 1          # фактор 1 (например: тепло)
x2 = 0          # фактор 2 (например: есть время)

# Правильный ответ
y_true = 0      # для AND: (1, 0) -> 0

print("=== INPUT ===")
print(f"x1 = {x1}, x2 = {x2}")
print(f"y_true (correct answer) = {y_true}")


# =========================
# 2. ПАРАМЕТРЫ МОДЕЛИ
# =========================

# Веса — насколько важен каждый фактор
w1 = 0.6
w2 = 0.6

# Смещение — общее "настроение" модели
b = -0.5

# Скорость обучения — насколько сильно реагируем на ошибку
lr = 0.1

print("\n=== INITIAL MODEL ===")
print(f"w1 = {w1}, w2 = {w2}")
print(f"b  = {b}")
print(f"learning rate = {lr}")


# =========================
# 3. ПРЯМОЙ ПРОХОД (PREDICT)
# =========================

# Считаем уверенность модели
# Это просто взвешенная сумма + порог
s = x1 * w1 + x2 * w2 + b

# Применяем правило перцептрона:
# если уверенность >= 0 → говорим 1, иначе 0
y_pred = 1 if s >= 0 else 0

print("\n=== PREDICT ===")
print(f"s = x1*w1 + x2*w2 + b")
print(f"s = {x1}*{w1} + {x2}*{w2} + {b} = {s}")
print(f"y_pred (model answer) = {y_pred}")


# =========================
# 4. ОШИБКА
# =========================

# Ошибка — это сигнал:
# - нужно ли менять веса
# - и в какую сторону
error = y_true - y_pred

print("\n=== ERROR ===")
print(f"error = y_true - y_pred = {y_true} - {y_pred} = {error}")

if error == 0:
    print("→ Model was correct. No changes needed.")
elif error > 0:
    print("→ Model was too pessimistic (said 0, but should be 1).")
else:
    print("→ Model was too optimistic (said 1, but should be 0).")


# =========================
# 5. ОБУЧЕНИЕ (UPDATE)
# =========================

print("\n=== TRAINING (UPDATE) ===")
print("Rule: change only what participated in the decision")

# Обновляем вес первого входа
print("\nUpdating w1:")
print(f"w1 = w1 + lr * error * x1")
print(f"w1 = {w1} + {lr} * {error} * {x1}")

w1_new = w1 + lr * error * x1
print(f"w1_new = {w1_new}")

# Обновляем вес второго входа
print("\nUpdating w2:")
print(f"w2 = w2 + lr * error * x2")
print(f"w2 = {w2} + {lr} * {error} * {x2}")

w2_new = w2 + lr * error * x2
print(f"w2_new = {w2_new}")

# Обновляем смещение
print("\nUpdating b (global strictness):")
print(f"b = b + lr * error")
print(f"b = {b} + {lr} * {error}")

b_new = b + lr * error
print(f"b_new = {b_new}")


# =========================
# 6. ПРИМЕНЯЕМ ИЗМЕНЕНИЯ
# =========================

w1, w2, b = w1_new, w2_new, b_new

print("\n=== UPDATED MODEL ===")
print(f"w1 = {w1}, w2 = {w2}")
print(f"b  = {b}")


# =========================
# 7. ПРОВЕРКА ПОСЛЕ ОБУЧЕНИЯ
# =========================

s = x1 * w1 + x2 * w2 + b
y_pred = 1 if s >= 0 else 0

print("\n=== AFTER TRAINING PREDICT ===")
print(f"s = {s}")
print(f"y_pred = {y_pred}")


# Если коротко, что ты тут должен почувствовать

# error — это решение, а не формула

# веса меняются только если вход участвовал

# b меняется всегда, потому что он про «общее»

# код — это обычная логика, не ML-магия