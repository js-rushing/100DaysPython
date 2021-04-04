cont = ''
answer = 0


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


while (cont != 'q'):
    if (cont == 'y'):
        num = answer
    else:
        num = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    valid = False
    while (not valid):
        operation = input("Pick an operation: ")
        for key in operations:
            if operation == key:
                valid = True
        if (not valid):
            print("Invalid operation")
            for key in operations:
                print(key)
    nextNum = float(input("What's the next number?: "))
    answer = operations[operation](num, nextNum)
    print(f"{num} {operation} {nextNum} = {answer}")
    cont = input(
        f"Type 'y' to continue with {answer},  or 'n' to clear calculator; 'q' to quit: ").lower()
