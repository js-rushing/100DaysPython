print("Welcome to the Love Calculator!")
name1 = (input("What is your name? \n")).lower()
name2 = (input("What is their name? \n")).lower()

love = 0

t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")

l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")

love = int(str(t + r + u + e) + str(l + o + v + e))

if(love < 10) or (love > 90):
    message = f"Your score is {love}, you go together like coke and mentos."
elif(love >= 40) and (love <= 50):
    message = f"Your score is {love}, you are alright together."
else:
    message = f"Your score is {love}."

print(message)
