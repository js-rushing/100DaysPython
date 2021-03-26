import random
from hangman_art import hangmanArt
from hangman_art import gallowsArr
from hangman_words import wordList

# Gameplay Variables
gameOver = False
wrongGuesses = 0

# Set game word
word = random.choice(wordList).upper()
wordArr = [ch for ch in word]

# Make array and corresponding string for guess tracking and comparison
guessingArr = []
for n in wordArr:
    guessingArr.append("_")

guessingStr = ""
for n in word:
    guessingStr += "_"

alreadyGuessedArr = []


# Function to display strings with a space between characters
def printWithSpaces(theString):
    count = 0
    formattedStr = ""
    for n in theString:
        formattedStr += theString[count]
        formattedStr += " "
        count += 1
    print(formattedStr)


# Begin Game
print(hangmanArt)

while (not gameOver and (guessingStr != word)):
    print(gallowsArr[wrongGuesses])
    printWithSpaces(guessingStr)
    guess = input("Guess a letter: ").upper()
    while (guess in alreadyGuessedArr):
        print(f"You've already guessed {guess.upper()}")
        guess = input("Guess a different letter: ").upper()
    alreadyGuessedArr.append(guess)

    if (guess in wordArr):
        step = -1
        for n in wordArr:
            step += 1
            if wordArr[step] == guess:
                guessingArr[step] = guess
        guessingStr = ''.join(guessingArr)
        if (guessingStr == word):
            print(word)
            print("You win!")
            gameOver = True
    else:
        wrongGuesses += 1
        if wrongGuesses == len(gallowsArr)-1:
            print(gallowsArr[wrongGuesses])
            print("Game Over.")
            print("You lose.")
            print(f"The word is {word}")
            gameOver = True
