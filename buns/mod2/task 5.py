user_data = input("Введите букву и разницу между ней: ")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
first_symbol = ''
delta = ''
current_value = ''
first_symbol_pos = 0
check_first_symbol = False

for symbol_of_data in user_data: # здесь я завожу данные в строку
    if not check_first_symbol:
        if symbol_of_data == ',':
            check_first_symbol = True
            first_symbol = current_value
            current_value = ''
        else:
            current_value = symbol_of_data
    else:
        if symbol_of_data != ' ':
            current_value += symbol_of_data
delta = int(current_value)

for symbol_of_alphabet in alphabet: # здесь я проверяю позицию символа
    if symbol_of_alphabet == first_symbol:
        break
    else:
        first_symbol_pos += 1
last_symbol_pos = first_symbol_pos + delta

while last_symbol_pos < 0: # здесь я закругляю алфавит
    last_symbol_pos += 26
while last_symbol_pos > 25:
    last_symbol_pos -= 26

print("Итоговая буква:", alphabet[last_symbol_pos])
