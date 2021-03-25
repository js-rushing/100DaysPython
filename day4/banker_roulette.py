import random

names_string = input("Enter names separated by a comma: \n")

names = names_string.split(', ')

howManyPeople = len(names)

random_person = random.randint(0, howManyPeople - 1)

print(howManyPeople)
print(random_person)

print(f"Looks like {names[random_person]} will be paying the bill tonight!")
