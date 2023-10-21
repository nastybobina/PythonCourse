user_input = int(input("Введите свое число: "))
n = int(input("Введите степень числа: "))
def fast_exponentiation(user_data, base):
    if base == 0:
        return 1
    if base % 2 == 0:
        return fast_exponentiation(user_data ** 2, base // 2)
    if base % 2 != 0:
        return user_data * fast_exponentiation(user_data, base - 1)


print("Результат возведения в степень:", fast_exponentiation(user_input, n))
