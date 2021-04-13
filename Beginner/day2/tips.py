print("Welcome to the tip calculator.")
total = float(input("What was the total bill? "))
people = int(input("How many people to split the bill? "))
percentage = int(
    input("What percentage tip would you like to give? (10, 12, or 15)? "))
tip = total * (percentage / 100)
perPerson = (total + tip) / people
print("Each person should pay: $" + str(format(perPerson, '.2f')))
