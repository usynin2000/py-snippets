# Солнце, Дождь, Правильный ответ (Гуляем?)
data = [
    (1, 0, 1),  # есть солнце, нет дождя → идем
    (1, 1, 0),  # солнце + дождь → не идем
    (0, 1, 0),  # нет солнца, дождь → не идем
    (0, 0, 0),  # ни солнца, ни дождя → не идем
]

# Перцептрон ничего не знает, он пока нейтрален ко всему.
w_sun = 0.0     # вес солнца
w_rain = 0.0    # вес дождя
lazy = -0.5      # моя лень (bias)


def perceptron(sun, rain):
    result = sun * w_sun + rain * w_rain + lazy
    return 1 if result > 0 else 0


# Насколько сильно мы корректируем веса
learning_rate = 0.1



# Обучение, корректировка весов
# Прогоним несколько раз
for epoch in range(10):
    for sun, rain, correct_answer in data:
        prediction = perceptron(sun, rain)

        error = correct_answer - prediction
        w_sun = w_sun + learning_rate * error * sun
        w_rain = w_rain + learning_rate * error * rain
        # Как алтернатива, можно использовать следующий код:
        # if error == 1 and sun == 1:
        #     w_sun = w_sun + learning_rate
        # elif error == -1 and sun == 1:
        #     w_sun = w_sun - learning_rate

        # if error == 1 and rain == 1:
        #     w_rain = w_rain + learning_rate
        # elif error == -1 and rain == 1:
        #     w_rain = w_rain - learning_rate 


        lazy = lazy + learning_rate * error


# Посмотрим итоговые результаты в конце:
print("Вес солнца:", w_sun)
print("Вес дождя:", w_rain)
print("Лень:", lazy)

# сравним резуьтат, с тем, что нам давалось изначально:
for sun, rain, _ in data:
    print(sun, rain, "→", perceptron(sun, rain))