user_input = input("Введите номер штрих-кода: ")
count = 0
even_numbers_summ = 0
odd_numbers_summ = 0
for symbol_data in user_input: # добавляю данные из ввода в нужную переменную и перевожу их в инт
    count += 1
    if (count % 2) != 0:
        odd_numbers_summ += int(symbol_data)
    else:
        even_numbers_summ += int(symbol_data)
if (odd_numbers_summ + 3 * even_numbers_summ) % 10 == 0: # проверяю правильный ли номер по условию
    print('yes')
else:
    print('no')
