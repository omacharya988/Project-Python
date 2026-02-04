import random
letters =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers =['0','1','2','3','4','5','6','7','8','9']
symbols =['!','#','$','%','&','(',')','*','+']

print("Welcom to password generator")
letter = int(input("How many letter you like in password\n"))
symbol = int(input("How many symbol you want in password\n"))
number = int(input("How many number you want in password\n"))
#Easy
password = []
for i in range (0,letter):
    password += random.choice(letters)
for i in range (0,symbol):
    password += random.choice(symbols)
for i in range (0,number):
    password += random.choice(numbers)


random.shuffle(password)


'''It will join the letter contain in the list'''
print("".join(password))


#Hard = 2nd way to do it with append
passwords = []
for i in range (0,letter):
    passwords.append(random.choice(letters))
for i in range (0,symbol):
    passwords.append(random.choice(symbols))
for i in range (0,number):
    passwords.append(random.choice(numbers))
#print(passwords)
random.shuffle(passwords)

passwordgen =""
for i in passwords:
    passwordgen += i

print(f"Your password is: {passwordgen}")
