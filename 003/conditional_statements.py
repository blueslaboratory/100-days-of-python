# 05/02/2024
# Day - 003



##################################################
print("\n\n*** Conditional statements (if, elif, else) ***")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    
    # nesting: if/elif/else (secuential)
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print(f"Child tickets price: 丰{bill}")
    elif age <=18:
        bill = 7
        print(f"Youth tickets price: 丰{bill}")
    elif age >= 45 and age <= 55:
        print("MIDLIFE CRISIS FREE RIDE!")
    else:
        bill = 12
        print(f"Adult tickets price: 丰{bill}")

    wants_photo = input("Do you want a photo taken? Y or N: ").upper()
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is 丰{bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

# Comparison operators:
# >     greater than
# <     less than
# >=    greater than or equal to
# <=    less than or equal to
# ==    equal to
# !=    not equal to