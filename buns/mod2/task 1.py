user_input = input("Введите два числа: ")
number1 = ''
number2 = ''
cur_val = ''
check_first_num = False
for symbol_of_data in user_input:
    if not check_first_num:
        if symbol_of_data == ',':
            check_first_num = True
            number1 = cur_val
            cur_val = ''
        else:
            cur_val += symbol_of_data
    else:
        if symbol_of_data != ' ':
            number2 += symbol_of_data
print(int(number1) % int(number2))
