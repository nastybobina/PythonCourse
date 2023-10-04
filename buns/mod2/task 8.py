user_input = input("Введите строку и символ: ")
current_data = ''
symbol_at_the_beginning = ''
cur_val = ''
symbol_count = 0
check_start_sentence = False

for symbol_of_data in user_input: # записываю в переменную введенные данные
    if not check_start_sentence:
        if symbol_of_data == ',': # не учитываю запятые
            check_start_sentence = True
            current_data = cur_val
            cur_val = ''
        else:
            cur_val += symbol_of_data
    else:
        if symbol_of_data != ' ':
            symbol_at_the_beginning = symbol_of_data

for symbol_of_data_str in current_data: # считаю сколько символов вышло
    if symbol_of_data_str == symbol_at_the_beginning:
        symbol_count += 1
    else:
        break
print(symbol_count)
