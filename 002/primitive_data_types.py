# 02/02/2024
# Day - 002



##################################################
print("\n\n*** Python primitive data types ***")

# Strings
print("\nStrings:")
print("Hello"[0] + "Hello"[4] + "Hello"[1])

# Integers
print("\nIntegers:")
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
