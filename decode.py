logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



 
def encryption( original_text,shift_amount,WTD):
    
    
        if WTD == "decode":
            shift_amount *= -1
        after_letter =""
        for i in original_text:
            if i not in alphabet:
                after_letter += i
            else:
                position=alphabet.index(i)
                    
                after_position = position + shift_amount

                if after_position > 25:                      #after_position %=len(alphabet)[0,25]
                    after_position = after_position - 26      #after_letter += alphabet[after_position]
                    after_letter +=alphabet[after_position]
                else:
                    after_letter +=alphabet[after_position]
        print(f"Your {WTD} message is {after_letter}")
print(logo)
again="yes"
decision=""
while again == "yes":
    

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encryption(original_text=text,shift_amount=shift,WTD=direction)
    decision=input("Do You want to do it again 'yes' or 'no' ? \n")
    if decision == "no":
        print("GoodBye!!!")
        break
