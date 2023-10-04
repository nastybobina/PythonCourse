try:
    user_input = int(input("Введите любое число: ")) # проверяю правильно ли ввели число
except ValueError:
    print("Неверный ввод") # если нет, выдаем ошибку и выходим из проверки
    exit()

if user_input <= 0: # проверяем натуральное ли число
    print("Неверный ввод")
    exit()

def translation(to_convert, base): # функция перевода из 10й СС в любую СС
    if base < 2 or base > 36: # СС с основанием меньше 2 не существует, а больше 36 необходимы другие мат. вычисления
        return ''
    output = ''
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while to_convert > 0:
        output = alphabet[to_convert % base] + output
        to_convert = to_convert // base
    return output


print(translation(user_input, 2))
print(translation(user_input, 8))
print(translation(user_input, 16))
