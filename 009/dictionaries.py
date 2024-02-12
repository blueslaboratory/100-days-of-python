# 12/02/2024
# Day - 009



##################################################
print("\n\n*** Dictionaries ***")

print('Dictionary: {"key1": "value1"}, {"key2": "value2"}')

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

# Retrieving items from a dictionary:
print(programming_dictionary["Bug"])

# Adding new items to the dictionary:
programming_dictionary["Method"] = "A method, like a function, is a set of instructions that perform a task."

# Printing a dictionary:
print("\nPrinting a dictionary:")
print(programming_dictionary)

# Editing an item
print("\nEditing an item:")
programming_dictionary["Bug"] = "🐛"

# Looping through a dictionary
print("\nLooping through the keys + values:")
for key in programming_dictionary:
    print(key, programming_dictionary[key])

# Create an empty dictionary:
empty_dictionary = {}

# Wipe an existing dictionary:
print("\nWiping a dictionary:")
programming_dictionary = {}
print(programming_dictionary)

# mini_dict error example
mini_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# you are calling a key that doesn't exist, KeyError
# Unlike with a Python List, using the [1] square bracket
# notation on a dictionary will *not* retrieve the second item.
print(mini_dict[1])