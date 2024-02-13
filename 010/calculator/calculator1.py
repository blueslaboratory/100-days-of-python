# 13/02/2024
# Day - 010



##################################################
# DAY 10 PROJECT: CALCULATOR 1

print("\n*** Welcome to the Calculator 1 ***")

# one function to rule them all
def eval_operation(x, y, symbol):
    expression = f"{x} {symbol} {y}"
    result = eval(expression)
    
    print(f"{expression} = {result}")
    
    return result

    
# add
def add(n1, n2):
    return n1 + n2

# substract
def substract(n1, n2):
    return n1 - n2

# multiply
def multiply(n1, n2):
    return n1 * n2

# divide
def divide(n1, n2):
    return n1 / n2


dict_operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


num1 = int(input("\nWhat's the 1st number?: "))
num2 = int(input("What's the 2nd number?: "))

for key_symbol in dict_operations:
    print(key_symbol)

op_symbol = input("Pick an operation: ")


# 1st answer
calculation_function = dict_operations[op_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {op_symbol} {num2} = {first_answer}")

# one function to rule them all
eval_operation(num1, num2, op_symbol)


# 2nd answer
op_symbol = input("\nPick another operation: ")
num3 = int(input("What's the next number?: "))
calculation_function = dict_operations[op_symbol]

# second_answer = calculation_function(calculation_function(num1, num2), num3)
# second_answer = multiply(multiply(num1, num2), num3)
# second_answer = 2 * 3 * 3 = 18
# To fix this bug we need to change the code:

second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {op_symbol} {num3} = {second_answer}")