user_input = int(input("Введите любое число: "))
print("Неверный ввод" if user_input < 0 else " ".join([bin(user_input)[2:], oct(user_input)[2:], hex(user_input)[2:]]))
