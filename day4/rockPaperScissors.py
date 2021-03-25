import random

scissors = ('''
    _______
---'   ____)___
          ______)
       __________)
      (____)
---.__(___)
''')

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = ('''
    _______
---'   ____)____
          ______)
          _______)
          ______)
---.___________)
''')

artArr = [rock, paper, scissors]

choices = ["rock", "paper", "scissors"]

user_choice = -1

while (user_choice < 0 or user_choice > 2):
    user_choice = int(
        input("Alright, on three, 0 for Rock, 1 for Paper or 2 for Scissors: "))
    if(user_choice < 0 or user_choice > 2):
        print("Invalid choice.  Try again.\n")

computer_choice = random.randint(0, 2)

if user_choice == 0 and computer_choice == 2:
    win = "win"
elif computer_choice > user_choice:
    win = "lose"
elif computer_choice == user_choice:
    win = "tie"
else:
    win = "win"


print(f"You chose {choices[user_choice]}: ")
print(artArr[user_choice])

print(f"Computer chose {choices[computer_choice]}: ")
print(artArr[computer_choice])

print(f"\nYou {win}.")
