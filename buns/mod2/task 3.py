string = input("Введите числа через пробел: ")
a, b, c = None, None, None
cur_var = ''
var_ind = 1
for i in string:
    if i != ' ':
        cur_var += i
    else:
        if cur_var:
            if var_ind == 1:
                a = int(cur_var)
            elif var_ind == 2:
                b = int(cur_var)
            elif var_ind == 3:
                c = int(cur_var)
            var_ind += 1
            cur_var = ''
if var_ind == 3:
    c = int(cur_var)
if (a >= 1000 or b >= 1000 or c >= 1000) and (a <= -1000 or b <= -1000 or c <= -1000):
    print("Неверный ввод")
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(b)
