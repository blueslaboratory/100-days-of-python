# 29/02/2024
# Day - 026



##################################################
print("\n\n*** List Comprehension ***")



numbers = [1, 2, 3]
new_list = []

# This:
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)

# Is the same as this:
# new_list = [new_item for item in list]
new_list = [n+1 for n in numbers]
print(new_list)



name = "Blueslaboratory"
new_list = [letter for letter in name]
print(new_list)



# Challenge
new_list = [i*2 for i in range(1,5)]
print(new_list)



names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# new_list = [new_item for item in list if test]
short_names = [name for name in names if len(name)<=4]
upper_names = [name.upper() for name in names if len(name)>4]

print(short_names)
print(upper_names)
