# 23/02/2024
# Day - 019



##################################################
print("\n\n*** Higher Order Functions ***")


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Higher Order Function: can work with other functions:
def calculator(n1, n2, func):
    return func(n1, n2)


result = calculator(2, 3, divide)
print(result)