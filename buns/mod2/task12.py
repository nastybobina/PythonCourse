user_input = input("Введите номер телефона: ")
edited_number = ''
for number_data in user_input: # убираю из номера лишние символы и записываю в переменную
    if (number_data != '-') and (number_data != '(') and (number_data != ')') and (number_data != ' '):
        edited_number += number_data
print(edited_number)