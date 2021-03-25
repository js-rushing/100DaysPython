import random

# VARIABLES
letterList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
              'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbolList = ['!', '@', '#', '$', '%', '^',
              '&', '*', '(', ')', '~', '?', '<', '>']
passArr = []
password = ""

# Get user input
print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))

# Populate numbers array
for n in range(0, numbers):
    randNum = random.randint(0, 9)
    passArr.append(str(randNum))

# Populate letters array
for n in range(0, letters):
    randLet = random.choice(letterList)
    lowerOrNot = random.randint(0, 1)
    if (lowerOrNot == 0):
        passArr.append(randLet)
    else:
        passArr.append(randLet.lower())

# Populate symbols array
for n in range(0, symbols):
    passArr.append(random.choice(symbolList))

# Generate password
while (len(passArr) > 0):
    randNum = random.randint(0, len(passArr) - 1)
    password += passArr[randNum]
    passArr.pop(randNum)

print(password)
