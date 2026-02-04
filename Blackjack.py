import random
from logo import logo
from os import system
def deal_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card =random.choice(cards)
    return card


def calculate_score(a):
    '''take a cards of user or computer as a and calculate its score'''
    if len(a)==2 and sum(a)==21:
        return 0
    elif len(a)==2 and sum(a)>22:
        a.remove(11)
        a.append(1)
    return sum(a)

def compare(u,c):
    if u == c:
        return "Draw"
    elif c == 0:
        return "Loose!! Opponent has BlackJack!!"
    elif u ==0:
        return "WIn !! Opponent has BlackJack!!"
    elif u > 21:
        return "Loose!! you went over!!"
    elif c >21:
        return "Win! Computer went Over!!"
    elif c>u:
        return "Loose! Computer has high score"
    elif u> c:
        return "Win !! User has High score"
def play_game():
    print(logo)
    user_card=[]
    computer_card=[]
    game_over = False

    for _ in range(2):
        computer_card.append(deal_cards())
        user_card.append(deal_cards())

    
    while game_over == False:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print(f"Your card {user_card},your score {user_score}")
        print(f"Computer first card {computer_card[0]}")

        if user_score==0 or computer_score == 0 or user_score>21:
            game_over = True
        else:
            ask = input("Do you want to draw another card? ")
            if ask =="y":
                user_card.append(deal_cards())
                print(user_card)
            else:
                game_over=True
        while computer_score<17 and computer_score !=0:
            computer_card.append(deal_cards())
            computer_score=calculate_score(computer_card)
    result = compare(u=user_score,c=computer_score)

    print(f"Your Final hand: {user_card}, final score {user_score}")
    print(f"computer's final hand: {computer_card}, final_score: {computer_score}")
    print(result)

while input("Do you want to play game of BlackJack? Type 'y' or 'n': ")=="y":
    system("cls")
    play_game()



