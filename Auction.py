import AuctArt
from os import system
print (AuctArt.logo)
people={}
anymore ="yes"
while anymore != "no":
    name = input("What is your name? ")
    price = int(input("What's your auction price? $"))
    people[name]=price
    
    anymore = input("Is there anyone for auction? 'yes' or 'no' " )
    if anymore == "yes":
        system("cls")

max = 0
for i in people:
    if people[i]>max:
        a = i
        max = people[i]
print(f"Hooray!! {a} win the bids with cost price of {max}$")


#######################################

#OR
#To print key with max value in dictionaries
# a ={
#     "a":2,"b":4,"c":3,"d":1}

# max(a, key=a.get)