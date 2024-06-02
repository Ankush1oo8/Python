flag=False
database={}
def highest_bid(bids):
    highest=0
    winner=""
    for bidder in bids:
        amount=bids[bidder]
        if amount>highest:
            highest=amount
            winner=bidder
    print(f"The winner is {winner} with highest bid of ${highest}")





while not flag:
    name=input("What is your name: ")
    price=int(input("What is your bid: "))
    database[name]=price
    ask=input("If there are other who want to bid? ")
    if ask=="no":
        flag=True

highest_bid(database)
