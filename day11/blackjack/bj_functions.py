from random import randint
from random import shuffle
import os


freshDeck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7,   7, 7, 8, 8, 8, 8, 9, 9, 9,
             9, 10, 10, 10, 10, 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K', 'A', 'A', 'A', 'A']


def clearConsole():
    os.system('clear')


def playOrNot():
    play = input(
        "\nDo you want to play BlackJack?: ('y' for yes; 'n' for no)").lower()
    if play == 'y':
        return True
    else:
        return False


def dealHands():
    hands = {
        "player": [],
        "dealer": [],
        "deck": []
    }
    hands["deck"] = freshDeck
    shuffle(hands["deck"])
    hands = dealCard(hands, 'p')
    hands = dealCard(hands, 'd')
    hands = dealCard(hands, 'p')
    hands = dealCard(hands, 'd')
    # print(hands["player"])
    print(f"Your cards: {hands['player']}")
    print(f"Dealer's cards: [#, {hands['dealer'][1]}]")
    hit = ''
    while hit != 's':
        hit = input("Type 'h' to hit, type 's' to stand: ").lower()
        if hit == 'h':
            dealCard(hands, 'p')
            print(f"Your cards: {hands['player']}")
    print(f"Your cards: {hands['player']}")
    print(f"Dealer's cards: {hands['dealer']}")
    playerTotal = calculateHand(hands['player'])
    dealerTotal = calculateHand(hands['dealer'])
    if playerTotal > 21:
        print(f"Your total is {playerTotal}.  You Bust! Dealer Wins.")
        return
    elif playerTotal == 21:
        print(f"Your total is {playerTotal}.  You Win!")
        return
    else:
        print(f"Your total: {playerTotal}")
        print(f"Dealer total: {dealerTotal}")
        while dealerTotal < 17:
            print("Dealer hits.")
            dealCard(hands, 'd')
            dealerTotal = calculateHand(hands['dealer'])
            print(f"Dealer's cards: {hands['dealer']}")
        dealerTotal = calculateHand(hands['dealer'])
        if dealerTotal > 21:
            print(f"Dealer total is {dealerTotal}.  Dealer busts! You win!")
        elif dealerTotal > playerTotal:
            print(
                f"Your total is {playerTotal}.\nDealer total is {dealerTotal}.\nDealer Wins.")
        elif dealerTotal == playerTotal:
            print(
                f"Your total is {playerTotal}.\nDealer total is {dealerTotal}.\nIt's a push.")
        else:
            print(
                f"Your total is {playerTotal}.\nDealer total is {dealerTotal}.\nYou Win!")


def dealCard(hands, hand):
    playerHand = hands["player"]
    dealerHand = hands["dealer"]
    deck = hands["deck"]
    if hand == 'p':
        playerHand.append(deck[len(deck)-1])
    else:
        dealerHand.append(deck[len(deck)-1])
    deck.pop(len(deck)-1)
    hands = {
        "player": playerHand,
        "dealer": dealerHand,
        "deck": deck
    }
    return hands


def calculateHand(hand):
    # Make copy of array
    copyArr = hand
    # Count Aces
    aceCount = 0
    for card in hand:
        if card == 'A':
            aceCount += 1

    # Replace all face cards in copy that aren't Aces with int 10
    for card in hand:
        if type(card) is not int:
            if card != 'A':
                copyArr[copyArr.index(card)] = 10

    # Get total of cards that aren't Aces
    total = 0
    for card in hand:
        if card != 'A':
            total += card
    # print(f"Total minus aces is {total}.")

    if aceCount == 1:
        if total <= 10:
            copyArr[hand.index('A')] = 11
        else:
            copyArr[hand.index('A')] = 1
    elif aceCount > 0:
        for n in range(aceCount-1):
            copyArr[hand.index('A')] = 1
            total += 1
        if total > 10:
            copyArr[hand.index('A')] = 1
        else:
            copyArr[hand.index('A')] = 11

    total = sum(copyArr)
    return total
