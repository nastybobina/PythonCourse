user_input = input("Введите любую последовательность цифр: ").split()
print(len(user_input) != len(set(user_input)))
