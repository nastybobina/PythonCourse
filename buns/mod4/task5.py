the_path_to_the_file = str(input("Введите путь к файлу: "))

opened_file = open(the_path_to_the_file, 'r')
files_list = opened_file.read()
dictionary_counter = {}
letters_counter = 0
for letter in files_list:
    if letter.isalpha():
        x = dictionary_counter.get(letter, 0)
        dictionary_counter[letter] = x + 1
        letters_counter += 1
count_letter_dict = [(k, "{:8.6f}".format(dictionary_counter[k] / letters_counter)) for k in dictionary_counter.keys()]
opened_file.close()
count_letter_dict.sort(key=lambda y: y[1], reverse=True)

the_path_to_the_end_file = str(input("Введите путь к файлу для статистики: "))
my_file = open(the_path_to_the_end_file, "w+")
for i in count_letter_dict:
    my_file.write(i[0] + " " + i[1] + ' * 100%')
    my_file.write('\n')
    print(i[0] + " " + i[1] + ' * 100%')
my_file.close()
