import time

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

def memoize(func):
    cache = {}

    def wrapper(*arguments):
        arguments = arguments[0]
        if arguments in cache.keys():
            return cache[arguments]
        else:
            cache[arguments] = func(arguments)
            return cache[arguments]
    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start_timer = time.time()
        result = func(*args, **kwargs)
        end_timer = time.time()
        resulting_time = (end_timer - start_timer) * 10**3
        print(f'Время выполнения функции {func.__name__}:{resulting_time} ms')
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

