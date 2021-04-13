import os
from random import randint
from art import vs
from game_data import data


def clearConsole():
    os.system('clear')


def getMatchup(celebAObj, alreadySeenArr):
    if celebAObj == {}:
        celeb1Num = randint(0, len(data)-1)
        celeb2Num = celeb1Num
        while celeb1Num == celeb2Num:
            celeb2Num = randint(0, len(data)-1)
        celeb1Obj = data[celeb1Num]
        while celeb1Obj['name'] in alreadySeenArr:
            celeb1Obj = data[celeb1Num]
        celeb2Obj = data[celeb2Num]
        while celeb2Obj['name'] in alreadySeenArr:
            celeb1Obj = data[celeb1Num]
        matchupArr = [celeb1Obj, celeb2Obj]
    else:
        celeb2Obj = celebAObj
        while celeb2Obj == celebAObj or celeb2Obj['name'] in alreadySeenArr and len(alreadySeenArr) < len(data):
            celeb2Obj = data[randint(0, len(data))-1]
        matchupArr = [celebAObj, celeb2Obj]
    return matchupArr


def displayMatchup(matchupObj):
    print(
        f"Compare A: {matchupObj[0]['name']}, {matchupObj[0]['description']}, from {matchupObj[0]['country']}.")
    print(vs)
    print(
        f"Against B: {matchupObj[1]['name']}, {matchupObj[1]['description']}, from {matchupObj[1]['country']}.")


def getAnswer():
    answer = ''
    while answer != 'a' and answer != 'b':
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if answer != 'a' and answer != 'b':
            print("Invalid guess")
    return answer


def evaluateAnswer(answer, matchupObj):
    if answer == 'a':
        # RIGHT
        if matchupObj[0]['follower_count'] > matchupObj[1]['follower_count']:
            return True
        # WRONG
        else:
            return False
    else:
        # RIGHT
        if matchupObj[1]['follower_count'] > matchupObj[0]['follower_count']:
            return True
        # WRONG
        else:
            return False
