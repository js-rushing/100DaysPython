import os
from auction_dictionaries_functions import getNameAndBid
from auction_dictionaries_functions import clearConsole
from auction_dictionaries_functions import callWinner

bids = []
print("Welcome to the secret auction program.")
getNameAndBid(bids)
otherBidders = input(
    "Are there any other bidders? Type 'yes' or 'no'.").lower()

while (otherBidders == 'yes'):
    clearConsole(os)
    getNameAndBid(bids)
    otherBidders = input(
        "Are there any other bidders? Type 'yes' or 'no'.").lower()

winningObj = callWinner(bids)
for key in winningObj:
    name = key

print(f"The winner is {name} with a bid of ${winningObj[name]}.")
