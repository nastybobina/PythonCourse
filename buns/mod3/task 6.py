user_input = input("Введите любые слова через пробел: ").split()
result = ''.join([i[-1]for i in user_input])
print(result)
