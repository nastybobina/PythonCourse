first_input = int(input("Введите первое число: "))
second_input = int(input("Введите второе число: "))
result = (first_input % 100) + (second_input % 100)
print("Сумма последних двух разрядов:", result)
