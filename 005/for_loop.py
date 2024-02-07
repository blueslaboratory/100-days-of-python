# 07/02/2024
# Day - 005



##################################################
# https://haveibeenpwned.com/
# https://en.wikipedia.org/wiki/List_of_the_most_common_passwords
print("\n\n*** For Loop with Lists ***")

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

print(fruits)



print("\n\n*** For Loop and the range() function ***")

print("\n[0, 10) --> step = 1")
for number in range(0, 10):
    print(number)

print("\n[10, 0) --> step = -2")
for number in range(10, 0, -2):
    print(number)

print("\nAdding numbers from [0, 100]")
sum = 0
for n in range(0, 101):
    sum += n

print(sum)