import time

current = time.time()
print(current)


def speed_calc_decorator(function):
    def wrapper():
        start = time.time()
        function()
        end = time.time()
        print(f"{function.__name__}: {end - start}")
    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
