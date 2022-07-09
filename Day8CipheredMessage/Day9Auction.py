import os
auction ={}
"""
A terminal based auction program
"""
def max_bidder(dictionary : dict) -> str:
    maximum =0
    person =""
    for key in dictionary:
        if dictionary[key]>maximum:
            maximum = dictionary[key]
            person = key 
    return person



is_more_bidders = True

while is_more_bidders:
    user_name = input("Enter the bidder's name: ")
    bid = int(input("Enter the bidding value"))
    auction[user_name]= bid
    inp =input("Do you want to add more bidders? type y/n: ")

    if inp =="y":
        os.system('cls')
        continue
    elif inp == "n":
        is_more_bidders = False

print(f"The Product Is Sold to {max_bidder(auction)}")