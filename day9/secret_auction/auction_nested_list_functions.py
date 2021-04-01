def clearConsole(os):
    command = 'clear'
    os.system(command)


def getNameAndBid(bids):
    name = input("What is your name?: ")
    bids[0].append(name)
    bid = int(input("What's your bid?: $"))
    while bid <= max(bids[1]):
        bid = int(input("You have not beat the highest bid.\nYou must bid higher."))
    bids[1].append(bid)
    return bids


def callWinner(bids):
    highest = max(bids[1])
    winner = bids[0][bids[1].index(highest)]
    winningArr = [winner, highest]
    return winningArr
