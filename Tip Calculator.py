

print("Welcome to the tip calculator.")
Total_bill = float(input("What was the total bill? "))
Tip= float(input("What percentage tip would you like to give? 10,12, or 15? "))
person = float(input("How many people to split the bill? "))
After_tip = (Tip*Total_bill)/100 +Total_bill
Split = round(After_tip/person,2)
print(f"Each person should pay: ${Split}")

