# Create the logging_decorator() function


def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {function(*args)}")
    return wrapper


# Use the decorator


@logging_decorator
def use_it(first, second, last):
    return first * second - last


use_it(5, 10, 15)
