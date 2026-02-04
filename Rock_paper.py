import random
a ="rock"
b ="paper"
c ="scissor"
d=[a,b,c]
computer = random.choice(d)

your = str(input("Rock, paper,scissor?").lower())
if computer == your:
    print("Draw")
elif computer == "rock" and your == "scissor":
    print("You lose")
elif computer == "rock" and your == "paper":
    print("You win")
elif computer == "paper" and your == "rock":
    print("You lose")
elif computer == "paper" and your == "scissor":
    print("You win")
elif computer == "scissor" and your == "paper":
    print("You lose")
elif computer == "scissor" and your == "rock":
    print("You win")




    
