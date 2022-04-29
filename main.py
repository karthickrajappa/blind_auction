from replit import clear
# HINT: You can call clear() to clear the output in the console.

import art

print(art.logo)
bids = {}
bidding_finished = False
def find_winner(bidding_recoed):
    highest_bid = 0
    winner = ""
    for bidder in bidding_recoed:
        bid_amount = bidding_recoed[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            print(f"The winner is {winner} with a bid of ${highest_bid}")
while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid: $"))
    bids[name]= price
    should_continue = input("Are there anyother bidders?: Type 'yes/no'.\n")
    should_continue = should_continue.upper()
    if should_continue == "NO":
      bidding_finished = True
      find_winner(bids)
    elif should_continue == "YES"
        clear()









