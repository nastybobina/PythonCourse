user_input = str(input("Введите любое число из 0 и 1: "))
zero_count = 0
ones_count = 0
for i in user_input: # проверяю что ввели
    if i == '0': # если 0 то добавляем к счетчику
        zero_count += 1
    if i == '1':
        ones_count += 1
if zero_count == ones_count: # проверяем одинаковое ли количество 0 и 1
    print("yes")
else:
    print("no")