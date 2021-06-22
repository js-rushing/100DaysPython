import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before function
        function()
        # Run twice
        function()
        # Do something after function
    return wrapper_function


def say_hello():
    time.sleep(2)
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


def say_greeting():
    print("How are you?")


say_hello()
say_bye()
say_greeting()
