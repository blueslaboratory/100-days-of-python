# 13/02/2024
# Day - 010



##################################################
print("\n\n*** Functions with Outputs ***")


# https://stackoverflow.com/questions/8347048/how-to-convert-string-to-title-case-in-python
def format_name(f_name, l_name):
    """DOCSTRING: Take a first and last name and format it 
    to return the title case version of the name.
    This will show up when you hover the cursor over the 
    function name: format_name"""
    
    # Escaping the return function early
    if f_name == "" or l_name == "":
        return "Early return: empty first name or empty last name."

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"
    print("This never gets printed. Return is the end of the function.")


# Storing output in a variable
formatted_name = format_name(input("\nYour first name: "), input("Your last name: "))
print(formatted_name)


# Printing output directly
print(format_name("AnGElA", "YU"))
print(format_name(input("\n1st Name: "), input("2nd Name: ")))


# A function inside a function: surprisingly it works
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)