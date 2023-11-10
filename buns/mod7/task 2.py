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

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
