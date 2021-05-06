# UNLIMITED POSITIONAL ARGS
def add(*args):
    total = 0
    for n in args:
        total += n
    return total


# print(add(3, 5, 6, 2, 1, 2, 6, 2, 4, 6, 8, 4, 2, 7, 2, 5, 3, 4))

# KEYWORD ARGUMENTS OR **KWARGS
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)

my_other_car = Car(make="Ford")
print(my_other_car.make)
print(my_other_car.model)
