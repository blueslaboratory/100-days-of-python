# 02/02/2024
# Day - 002



##################################################
# DAY 2 PROJECT: TIP CALCULATOR
# https://docs.python.org/3/tutorial/floatingpoint.html
# the actual stored value is the nearest representable binary fraction.

print("\n\n*** Welcome to the tip calculator ***")

bill = float(input("What was the total bill? 丰"))
tip = int(input("What percentage would you like to give? (10, 12 or 15): "))
persons = int(input("How many people to split the bill? "))

pay_per_person = (bill*(1 + tip/100))/persons

print("Each person should pay: 丰" +str(pay_per_person))
print(f"Each person should pay: 丰{pay_per_person:.2f}")