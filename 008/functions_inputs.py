# 09/02/2024
# Day - 008



##################################################
print("\n\n*** Functions with Inputs ***")

# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
print("\n\n*** Simple function ***")
def greet():
    print("\nHello, good morning")
    print("What you up to?")
    print("Hmmmmmm...")

greet()



# Function that allows for input
print("\n\n*** Function that allows for input ***")

def greetings_darling(name):
    print(f"\nHello {name}, good morning")
    print(f"What you up to {name}?")
    print("Hmmmmmm...")

greetings_darling(input("\nName: "))

# var --> parameter | 123 --> argument
var = 123



# Functions with more than 1 input
print("\n\n*** Functions with more than 1 input ***")
def greet_with(name, location):
    print(f"\nHello {name}, good morning")
    print(f"Your location is: {location}")

# positional arguments
greet_with("John", "Hogueras de San Juan")
# keyword arguments
greet_with(location="Hell", name="Alejandro")