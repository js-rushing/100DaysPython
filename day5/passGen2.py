import random

# VARIABLES
letterList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
              'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbolList = ['!', '@', '#', '$', '%', '^',
              '&', '*', '(', ')', '~', '?', '<', '>']
passArr = []
password = ""

numLetters = random.randint(6, 10)
numNumbers = random.randint(6, 10)
numSymbols = random.randint(6, 10)

# Populate numbers array
for n in range(0, numNumbers):
    randNum = random.randint(0, 9)
    passArr.append(str(randNum))

# Populate letters array
for n in range(0, numLetters):
    randLet = random.choice(letterList)
    lowerOrNot = random.randint(0, 1)
    if (lowerOrNot == 0):
        passArr.append(randLet)
    else:
        passArr.append(randLet.lower())

# Populate symbols array
for n in range(0, numSymbols):
    passArr.append(random.choice(symbolList))

# Generate password
while (len(passArr) > 0):
    randNum = random.randint(0, len(passArr) - 1)
    password += passArr[randNum]
    passArr.pop(randNum)

print("Welcome to the PyPassword Generator!\n")
print(f"Your randomly generated password is: {password}.")
