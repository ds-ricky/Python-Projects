import art

print(art.logo)

def high_bid(bid_record):
    winner = ""
    highest_bid = 0
    for key in bid_record:
        bid_amount = bid_record[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
    print(f"Winner of the Auction is {winner}, with Bidding amount ${highest_bid}")
    


bid_inf = {}

more_bidders = True
while more_bidders:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid amount: $"))
    bid_inf[name] = bid

    repeat = input("Are there any other bidders? Type 'yes or no'.\n").lower()
    if repeat == "yes":
        print("\n"*20)
        print(art.logo)
    elif repeat == "no":
        more_bidders = False
        print("\n"*2)
        high_bid(bid_inf)
        print("\n"*2)
    # else:
    #     print("You typed invalid value.")