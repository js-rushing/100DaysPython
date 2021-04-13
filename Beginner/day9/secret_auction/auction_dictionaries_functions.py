def clearConsole(os):
    command = 'clear'
    os.system(command)


def getNameAndBid(bids):
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidObj = {name: bid}
    bids.append(bidObj)
    return bids


def callWinner(bids):
    winningObj = {}
    highestBid = 0
    for obj in bids:
        for key in obj:
            if obj[key] > highestBid:
                highestBid = obj[key]
        for key in obj:
            if obj[key] == highestBid:
                winningObj = obj
    return winningObj
