file_path = str(input("Введите путь к файлу: "))
final_file_path = str(input("Введите путь к файлу для статистики: "))
statistics = []
statistics_symbol_ID = 0
file_open = open(file_path, 'r', encoding='utf-8')
file_data = file_open.read()
file_data = list(file_data)
another_file_data = file_data[:]
for symbol_data in file_data:
    if symbol_data.isalpha() and another_file_data.count(symbol_data) != 0:
        statistics.append([symbol_data, another_file_data.count(symbol_data)])
        for statistics_data in range(another_file_data.count(symbol_data)):
            another_file_data.remove(symbol_data)
file_open.close()
statistics.sort(key=lambda x: x[1])
final_file = open(final_file_path, "w+")
for stats_of_one_symbol in statistics:
    for statistics_data in stats_of_one_symbol:
        final_file.write(str(statistics_data))
        final_file.write(' ')
    final_file.write('\n')
final_file.close()
