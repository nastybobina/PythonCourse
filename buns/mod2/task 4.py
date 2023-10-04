try:
    user_input = int(input("Введите любое число: "))
except ValueError:
    print("Неверный ввод")
    exit()

if user_input <= 0:
    print("Неверный ввод")
    exit()

def translation(to_convert, base):
    if base < 2 or base > 36:
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
