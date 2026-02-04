import random
import Hangman ######From Hangman import word
import Hand
#Making word list
print("Welcom to HANGMAN!!!!!!!!!!!")
life = 6


#picking single word as lowercase from list
a = random.choice(Hangman.word).lower()#######word
#ask for letter to guess in lower case
b=len(a)
#create space equal number of letter in word
c=""
for i in range(0,b):
    c += "_"
display=""
correct=[]
#guessed =[]
print(f"Word to guess: {c}")
while display != a: 
    guess = input("Guess a letter: ".lower())
    res=""
    if guess in correct:
        print(f"You have already guessed {guess}")
    for i in a:
        if i == guess:
            res += i
            correct.append(guess)
            
        elif i in correct:
            res += i
        else:
            res += "_"
    if guess not in a:
        life -= 1
        print(f"You have guessed {guess}, that's not in the word.")
        print(Hand.list[life])
        print(f"You have {life} lives left")
    else:
        print(res)
        print(Hand.list[life])
        print(f"You have {life} lives left")
    if life ==0:
        print("************************************You lose***************************************")
        break
    print(f"Word to guess: {res}")
    
    display = res
if display == a:
    print("*******************************************You win**********************************************")
    
    





