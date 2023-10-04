user_input = input("Введите ссылку на сайт: ")
reversed_site = ''
domain_piece = ''

def reverce(value): # функция разворота значений
    reverse_value = ''
    for element in range(len(value)-1, -1, -1):
        reverse_value += value[element]
    return reverse_value

reversed_site = reverce(user_input) # разворачиваю то, что ввел пользователь

for symbol_of_reversed_domain in reversed_site: # учитываю ввод точек
    if symbol_of_reversed_domain == '.':
        domain_piece = reverce(domain_piece)
        print(domain_piece)
        domain_piece = ''
    else:
        domain_piece += symbol_of_reversed_domain

domain_piece = reverce(domain_piece) # разворачиваю порядок частей сайта
print(domain_piece)
domain_piece = ''
