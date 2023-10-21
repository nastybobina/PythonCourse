first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
def euclids_algorithm(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    else:
        if a > b:
            return euclids_algorithm(a % b, b)
        else:
            return euclids_algorithm(a, b % a)


greatest_common_divisor = euclids_algorithm(first_number, second_number)
print('Наибольший общий делитель числа', first_number, 'и', second_number, 'равен', greatest_common_divisor)
