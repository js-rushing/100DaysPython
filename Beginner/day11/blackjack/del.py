example1 = ['Q', 2, 'A']
example2 = [8, 'A', 'A', 10]
example3 = [2, 'A', 8]
example4 = [4, 'A', 'A', 5]
example5 = ['A', 3, 'A', 4, 'A']
example6 = ['A', 'A', 'A', 'A', 7]
example7 = ['A', 'A', 'A', 'A', 8]


def handleAces(hand):
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
    print(f"Total minus aces is {total}.")

    if aceCount == 1:
        if total <= 10:
            copyArr[hand.index('A')] = 11
        else:
            copyArr[hand.index('A')] = 1
    else:
        for n in range(aceCount-1):
            copyArr[hand.index('A')] = 1
            total += 1
        if total > 10:
            copyArr[hand.index('A')] = 1
        else:
            copyArr[hand.index('A')] = 11

    total = sum(copyArr)
    return total


print(handleAces(example1))
print(handleAces(example2))
print(handleAces(example3))
print(handleAces(example4))
print(handleAces(example5))
print(handleAces(example6))
print(handleAces(example7))
