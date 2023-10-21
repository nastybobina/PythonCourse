user_input = str(input("Введите любую строку чисел: ")).split()
numbers_list = []
for word_data in user_input:
    if word_data.isnumeric():
        numbers_list.append(int(word_data))
print(numbers_list)
is_equal_num = False
for num_data in numbers_list:
    if numbers_list.count(num_data) > 1:
        if numbers_list.count(num_data) == len(numbers_list):
            print('Все числа равны')
            is_equal_num = True
            break
        else:
            print('Есть равные и неравные числа')
            is_equal_num = True
            break
if not is_equal_num:
    print('Все числа разные')