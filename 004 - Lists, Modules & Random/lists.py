# 06/02/2024
# Day - 004



##################################################
# https://docs.python.org/3/tutorial/datastructures.html
print("\n\n*** Lists ***")


# Lists have an order, determined by the order in the list
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0])
print(states_of_america[-1])
print(states_of_america[49])
print(states_of_america[len(states_of_america)-1])
print(len(states_of_america))

print("\nComplete list of the american states:")
for i in range(0, len(states_of_america)):
    print(f"{i}. {states_of_america[i]}")



print("\n*** List methods ***")

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple')) # 2
print(fruits.count('tangerine')) # 0
print(fruits.index('banana')) # 3
print(fruits.index('banana', 4))  # Find next banana starting at position 4: 6

fruits.reverse()
print(fruits) # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

fruits.append('grape')
print(fruits) # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

fruits.sort()
print(fruits) # ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

print(fruits.pop()) # 'pear'
print(fruits) # ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']

print(fruits.pop(0)) # 'apple'
print(fruits) # ['apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']

fruits.extend(["watermelon", "strawberry"])
print(fruits) # ['apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'watermelon', 'strawberry']



print("\n*** Nested Lists ***")

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes"]
vegetables = ["Spinach", "Kale", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)