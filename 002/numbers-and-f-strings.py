# 02/02/2024
# Day - 002



##################################################
print("\n\n*** Number Manipulation and F Strings in Python ***")

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