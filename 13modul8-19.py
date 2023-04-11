def mistake_enter(a):  # Функция проверки корректности ввода
    while True:
        try:
            number = int(input(a))
            while number < 0:  # если введено отрицательное число
                print("Вы ввели отрицательное число, попробуйте еще раз.")
                number = int(input(a))
            break
        except ValueError as e:  # если вмето числа введены символы
            print("Ввод не корректен, попробуйте еще раз.")
    return number


st = "Какое колличество билетов вы хотите приобрести: "
tickets = mistake_enter(st)  # вызываем функцию и сохраняем результат (колличество билетов)
cost_full, discount = 0, 0  # полная стоимость, скидка
for i in range(1, tickets + 1):
    st = f"Билет {i}, укажите возраст посетителя: "
    age = mistake_enter(st)  # вызываем функцию и сохраняем результат для каждой итерации
    if 18 <= age < 25:
        print("Стоимость билета 990 рублей.")
        cost_full += 990
    elif age >= 25:
        print("Стоимость билета 1390 рублей.")
        cost_full += 1390
    else:
        print("Бесплатно.")
if tickets > 3:
    discount = cost_full / 10
    cost_full -= discount
print()
print("-"*40)
print(f"Всего {tickets} билета. Сумма к оплате: {cost_full} рублей, с учетом скидки {discount} рублей.")