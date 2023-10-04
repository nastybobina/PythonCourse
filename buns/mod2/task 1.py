user_input = input("Введите два числа: ")
number1 = ''
number2 = ''
cur_val = ''
check_first_num = False
for symbol_of_data in user_input: # переношу из ввода в переменные
    if not check_first_num:
        if symbol_of_data == ',': # проверяю на запятые
            check_first_num = True # строка началась, флаг подняли
            number1 = cur_val
            cur_val = ''
        else:
            cur_val += symbol_of_data
    else:
        if symbol_of_data != ' ': # если нет пробелов то вписываем в переменную последний символ
            number2 += symbol_of_data
print(int(number1) % int(number2))
