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
    function_name = func.__name__
    function_documentary = func.__doc__
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
    def wrapper(n, *args, **kwargs):
        if not hasattr(wrapper, 'start_timer'):
            wrapper.start_time = time.time()
        result = func(n, *args, **kwargs)
        if not hasattr(wrapper, 'execution_time'):
            wrapper.execution_time = time.time() - wrapper.start_time
            return f"Результат: {result}, Время выполнения: {wrapper.execution_time} секунд"
        else:
            return result
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@timer
def testing_fibonacci_with_memoize(n):
    return fibonacci_with_memoize(n)

@timer
def testing_fibonacci_without_memoize(n):
    return fibonacci_without_memoize(n)

@validate_args
@memoize
def fibonacci_with_memoize(n):
    if n < 2:
        return n
    return fibonacci_with_memoize(n - 1) + fibonacci_with_memoize(n - 2)

@validate_args
def fibonacci_without_memoize(n):
    if n < 2:
        return n
    return fibonacci_without_memoize(n - 1) + fibonacci_without_memoize(n - 2)


print(f"Тест функции с декоратором memoize:\n{testing_fibonacci_with_memoize(31)}\n\nТест функции без декоратора "
      f"memoize:\n{testing_fibonacci_without_memoize(31)}")
