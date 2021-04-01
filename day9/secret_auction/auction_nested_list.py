import os
from auction_nested_list_functions import getNameAndBid
from auction_nested_list_functions import clearConsole
from auction_nested_list_functions import callWinner

bids = [["minimum"], [1]]
print("Welcome to the secret auction program.")
getNameAndBid(bids)
otherBidders = input(
    "Are there any other bidders? Type 'yes' or 'no'.").lower()

while (otherBidders == 'yes'):
    clearConsole(os)
    getNameAndBid(bids)
    otherBidders = input(
        "Are there any other bidders? Type 'yes' or 'no'.").lower()

winningArr = callWinner(bids)

print(f"The winner is {winningArr[0]} with a bid of ${winningArr[1]}.")
