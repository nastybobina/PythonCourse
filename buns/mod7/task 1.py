def validate_args(func):
    def wrapper(*arguments):
        if len(arguments) < 1:
            return "Not enough arguments"
        elif len(arguments) > 1:
            return "Too many arguments"
        elif not isinstance(arguments[0], int):
            return 'Wrong types'
        elif arguments[0] < 0:
            return 'Negative argument'

        return func(*arguments)
    return wrapper

@validate_args
def multiply_args(n):
    return 245 * n


print(multiply_args(2))  # правильный аргумент
print(multiply_args())  # отсутствие аргументов
print(multiply_args(-1))  # отрицательный аргумент
print(multiply_args(2, 3))  # больше 1 аргумента
print(multiply_args('lol'))  # не тот тип аргумента
