print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") # What is your name?
name2 = input("What is your partner name? ") # What is their name?
combine = name1.lower() + name2.lower() #combine both name in lower case
t = combine.count("t") #Count letter t in combine string
r = combine.count("r")
u = combine.count("u")
e = combine.count("e")
first = t+r+u+e
print(first)
l = combine.count("l")
o = combine.count("o")
v = combine.count("v")
e = combine.count("e")
second = l+o+v+e
print(second)
total = str(first)+str(second)
total = int(total)
if total <10 or total > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif total >=40 and total <=50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")



