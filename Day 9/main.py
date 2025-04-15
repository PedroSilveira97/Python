dict = {}
highest_bid = 0.00
highest_bidder = ""
while True:
    new_bidder = str(input("Are there any new bidders? ")).lower()
    if new_bidder == "yes":
        bidder_name = str(input("What is the bidder's name? "))
        bid_amount = float(input("What is the bid amount? "))
        dict[bidder_name] = bid_amount
    elif new_bidder == "no":
        for name, bid in dict.items():
            if bid > highest_bid:
                highest_bid = bid
                highest_bidder = name
                formatted_bid = "{:.2f}".format(highest_bid)
        print(f"The winner is {highest_bidder}, with a bid of ${formatted_bid}.")
        break
    else:
        print("Are there any new bidders? ")
