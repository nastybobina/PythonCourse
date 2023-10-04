user_input = input("Введите три слова: ")
final_word = ''
latter_symbol = ''
for symbol in user_input: # переношу данные из ввода
    if symbol == ' ': # если видим пробел
        final_word += latter_symbol # то добавляем последний символ в итоговое слово
        latter_symbol = '' # и очищаем предыдущее число
    else:
        latter_symbol = symbol
if latter_symbol != ' ': # если пробела нет
    final_word += latter_symbol # добавляем в слово предыдущий символ
    latter_symbol = '' # очищаем
print(final_word)
