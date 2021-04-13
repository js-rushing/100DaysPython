from random import randint

# GLOBAL VARIABLES
number = randint(1, 100)
guess = 0

# FUNCTIONS


def evaluateGuess():
    global number
    global guess
    if guess < number:
        hint = 'Too low.'
    elif guess > number:
        hint = 'Too high'
    else:
        hint = 'You guessed it!'
    return hint


def askDifficutly():
    difficulty = ''
    while difficulty != 'easy' and difficulty != 'hard':
        difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
        if difficulty == 'easy':
            turns = 10
        elif difficulty == 'hard':
            turns = 5
        else:
            print('There are only two valid options here, bubba.')
    return turns


# MAIN PROGRAM
print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100.')
attempts = askDifficutly()


while guess != number and attempts > 0:
    print(f'You have {attempts} attempts remaining to guess the number.')
    guess = int(input('Make a guess: '))
    attempts -= 1
    print(evaluateGuess())
    if guess == number:
        print(f'You got it! The answer was {number}')
        break
    else:
        print('Guess again')

if guess != number:
    print('You\'ve run out of guesses, you lose.')
    print(f'The answer was {number}')
