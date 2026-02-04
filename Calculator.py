import calculatorart
from os import system


def addition(a,b):
    return a+b
add = addition

def multiply(a,b):
    return a*b
multiple = multiply

def substract ( a,b):
    return a-b
sub = substract

def division(a,b):
    return a/b
div = division
operation = { 
    "+":add,
    "-":sub,
    "*":multiple,
    "/":div,
    }
def calculator():
    print(calculatorart.logo)
    first= float (input("What is your first number?: "))
    a = 1
    while a != 0:
        for i in operation:
            print(i)
        operator = input("Pick an operator.")
        second = float(input("What is your second number?: "))


            
       

        calculation = operation[operator](first,second)
        print(f"{first} {operator} {second} = {calculation}")

        again = input(f"Type 'y' to continue calculating with {calculation}, or type 'n' to do new calculation!! or 'q' to exit!!")

        if again =="y":
            first = calculation
        elif again == 'n':
            
            a = 0
            system("cls")
            calculator()
        elif again =='q':
            exit()

            

calculator()







