user_data = input("Введите свои символы: ")
listed_user_data = list(user_data)
list_copy = listed_user_data[:]
equal_symbols = []
equal_sym_ID = 0
is_palindrome = False
palindrome = []
palindrome_str = ''

for symbol_data in range(len(listed_user_data)):
    palindrome.append('*')

for symbol in listed_user_data:
    while list_copy.count(symbol) >= 2:
        equal_symbols.append(symbol)
        list_copy.remove(symbol)
        list_copy.remove(symbol)

if len(listed_user_data) % 2 == 0:
    if len(list_copy) == 0:
        is_palindrome = True
else:
    if len(list_copy) == 1:
        is_palindrome = True
        palindrome[(len(palindrome) // 2)] = list_copy[0]

if is_palindrome:
    for equal_symbol in equal_symbols:
        palindrome[equal_sym_ID] = equal_symbol
        palindrome[-equal_sym_ID - 1] = equal_symbol
        equal_sym_ID += 1

for symbol_data in palindrome:
    palindrome_str += symbol_data

print("Палиндром из символов", palindrome_str)
