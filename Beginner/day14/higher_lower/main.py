from art import banner
from art import trophy
from game_data import data
from functions import clearConsole
from functions import getMatchup
from functions import displayMatchup
from functions import getAnswer
from functions import evaluateAnswer

print(banner)

alreadySeenCelebs = []
matchup = getMatchup({}, alreadySeenCelebs)
score = 0
gameOver = False

while not gameOver:
    if len(alreadySeenCelebs) == 0:
        alreadySeenCelebs.append(matchup[0]['name'])
        alreadySeenCelebs.append(matchup[1]['name'])
    else:
        alreadySeenCelebs.append(matchup[1]['name'])
    displayMatchup(matchup)
    guess = getAnswer()
    if evaluateAnswer(guess, matchup):
        score += 1
        clearConsole()
        print(banner)
        print(f"That's right! Score: {score}")
        if (matchup[0]['follower_count'] > matchup[1]['follower_count']):
            matchup = getMatchup(matchup[0], alreadySeenCelebs)
        else:
            matchup = getMatchup(matchup[1], alreadySeenCelebs)
        if len(alreadySeenCelebs) == len(data):
            gameOver = True
    else:
        gameOver = True
        print("That's wrong! Game Over")

if score == 49:
    print("You've beaten the game!\nThere are no more celebrities to guess.")
    print(trophy)
