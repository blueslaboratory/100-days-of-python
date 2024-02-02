# 02/02/2024
# Day - 002



##################################################
print("\n\n*** Python primitive data types ***")

# Strings
print("\nStrings:")
print("Hello"[0] + "Hello"[4] + "Hello"[1])

# Integers
print("\nIntegers:")
print(3.14159)
print("123" + "345")
print(123 + 345)
# underscores make numbers readable
print(123_456_789)

# Floats
print("\nFloats:")
print(3.141592)
print(3.141_592)

# Booleans
print("\nBooleans:")
print(True or False)
print(True and False)



##################################################
print("\n\n*** Types ***")

num_char = len(input("Name: "))
print(type(num_char))
print("Characters: " +str(num_char))

n = 70 + float(123.4)
print(type(n))



##################################################
print("\n\n*** Mathematical operations in python ***")

print()
print("6/3 =", 6/3, "---> class:", type(6/3))
print("Powers 2^3: ", 2**3)

print()
print("Order of operations ---> P.E.M.D.A.S.:")
print("P.arentheses:\t\t ()")
print("E.xponents:\t\t **")
print("M.ultiplication:\t *")
print("D.ivision:\t\t /")
print("A.ddition:\t\t +")
print("S.ubstraction:\t\t -")

print()
print("3 * 3 + 3 / 3 - 3 = ", (3 * 3 + 3 / 3 - 3)) #7
print("3 * (3 + 3) / 3 - 3 = ", (3 * (3 + 3) / 3 - 3)) #3



##################################################
print("\n\n*** Number Manipulation and F-Strings in Python ***")

print(round(8/3, 2))
print(round(2.6666666666, 2))

print(type(8/3))
print(type(8//3))


print("\nshortcutting")
n = 4/2

n /= 2
print(n)
n -= 2
print(n)
n += 2
print(n)
n *= 2
print(n)


print("\nf-String")
score = 0
height = 1.8
isWinning = True
print(f"Score: {score} \tHeight: {height} \tWinning: {isWinning}")



##################################################
# Auditorium --> https://app.auditorium.ai/courses
print("\n\n*** Auditorium ***")


# Day 2 - Lesson 5 - Data Types
two_digit_number = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
d1 = int(two_digit_number[0])
d2 = int(two_digit_number[1])

print(d1 + d2)


# Day 2 - Lesson 6 - Data Types
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI = float(weight)/float(height)**2
print(int(BMI))


# Day 2 - Lesson 7 - Life in weeks
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 

weeks_left = (90-int(age))*52

print(f"You have {weeks_left} weeks left.")



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