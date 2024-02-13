# 13/02/2024
# Day - 010



##################################################
# DAY 10 PROJECT: CALCULATOR 2

print("\n*** Welcome to the Calculator 2 ***")
    
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



num1 = float(input("\nWhat's the 1st number?: "))

for key_symbol in dict_operations:
    print(key_symbol)

should_continue = True

while should_continue:
    op_symbol = input("Pick another operation: ")
    num2 = float(input("What's the next number?: "))
    
    calculation_function = dict_operations[op_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {op_symbol} {num2} = {answer}")
    
    if input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to exit: ") == "y":
        num1 = answer
    else:
        should_continue = False