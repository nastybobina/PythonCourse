user_input = str(input("Введите любой сайт: ").split(".")[::-1])
print('\n'.join(map(str, user_input)))
