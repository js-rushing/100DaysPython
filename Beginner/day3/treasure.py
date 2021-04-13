print("Welcome to Treasure Island.  Find the treasure or die!")
print('''
           /"*._         _
      .-*'`    `*-.._.-'/
    < * ))     ,       ( 
      `*-._`._(__.--*"`.\\
''')
direction = input(
    "\nYou come to a fork in the road.\nDo you go left or right? L or R\n")
if direction.lower() == "l":
    print("\nSweet! Not dead yet.\n")
    travel_method = input(
        "Oh no.  We got too cocky, bros.\nThe treasure's on that island over there.\nDo you swim for it or wait for a boat? S or B\n")
    if travel_method.lower() == "b":
        print("\nGood choice.  Sharks EVERYWHERE!\n")
        door = input(
            "The treasure must be behind one of these three doors.\nWelp, which one, duderino?\nYellow, Red, or Blue? Y, R, or B\n")
        if door.lower() == "y":
            print("\nYES, MATE.  FRIGGIN YES, MATE!\nYou did it!\nYou're rich!")
        else:
            print("\nCancer.  You got cancer.  No treasure.  Just cancer.")
    else:
        print("\nDang, homie.  Did you have a cut on your thumb or something?  Instant shark food.")

else:
    print("\nOh, man.  I've never seen anyone die so hard.  Sucks, bro.\nDon't worry though.  I'll tell everyone you died a hero's death.")
