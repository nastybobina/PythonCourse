user_input = int(input("Введите любое четырехзначное число: "))
print("Первый разряд числа:", user_input // 1000)
print("Второй разряд числа:", (user_input // 100 % 10))
print("Третий разряд числа:", (user_input // 10 % 10))
print("Четвертый разряд числа:", (user_input % 10))