user_input = input("Введите любое слово: ")
vowel = 0
consonant = 0
for symbol in user_input: # делаем обратную проверку на то, является ли буква гласной
    if (symbol != ' ') and (symbol != 'ь') and (symbol != 'ъ'):
        if (symbol == 'а') or (symbol == 'у') or (symbol == 'о') or (symbol == 'и') or (symbol == 'э') or (symbol == 'ы') or (symbol == 'я') or (symbol == 'ю') or (symbol == 'е') or (symbol == 'ё'):
            vowel += 1 # добавляем к счетчику
        else:
            consonant += 1 # иначе добавляем к счетчику согласных
print("Количество гласных:", vowel, ", количество согласных:",  consonant)
