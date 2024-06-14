# 14/06/2024
# Day - 034



##################################################
print("\n\n*** Datatypes: Type Hints ***")


print("The following data expects a followind datatype")

age: int = 10
name: str = "Tom"
height: float = 1.69
is_human: bool = False


# function expects an age: int
# function returns a -> bool
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(19):
    print("You may pass")
else:
    print("Pay a fine")