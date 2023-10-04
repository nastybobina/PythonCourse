numbers = input("Введите любое число: ")
flag = False
first_number_pos, next_number_pos = 0, 0
for first_num_check in numbers: # прохожу по введенным числам
    if flag: # если в прошлой итерации флаг был поднят, то код останавливается, то есть текущая цифра уже записана
        break
    first_number_pos += 1 # счетчик позиции
    for second_num_check in numbers: # дальше проверяю введенные числа на пробелы
        if flag:
            break
        next_number_pos += 1 # счетчик следующего числа
        if first_number_pos != next_number_pos:
            if (first_num_check == next_number_pos) and (first_num_check != ' '):
                flag = True
                break
        continue # переходим на следующую итерацию
    next_number_pos = 0
print(flag)