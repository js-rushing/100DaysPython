import random

quit = ""

while (quit.lower() != 'q'):
    callIt = input("Call it; Heads or Tails: (H or T)\n")
    callIt = callIt.lower()
    if (callIt == 'h'):
        intCall = 1
    elif (callIt == 't'):
        intCall = 0

    hORt = random.randint(0, 1)
    if (hORt == 0):
        print("Tails it is\n")
    else:
        print("Heads it is\n")

    if (hORt == intCall):
        win = True
    else:
        win = False

    if (win):
        print("You Win!\n")
    else:
        print("You Lose!\n")

    quit = input("Press Enter to flip coin; 'Q' to quit: \n")
