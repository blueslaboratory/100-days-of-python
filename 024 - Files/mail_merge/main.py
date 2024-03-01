# 28/02/2024
# Day - 024


# TODO: Create a letter using starting_letter.txt 
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


##################################################
print("\n\n*** Mail Merge ***")


DIRECTORY_NAMES = ".\\024 - Files\\mail_merge\\input\\names\\invited_names.txt"
DIRECTORY_STARTING_LETTER = ".\\024 - Files\\mail_merge\\input\\letters\\starting_letter.txt"
DIRECTORY_LETTERS = ".\\024 - Files\\mail_merge\\output\\ready\\"

names = []


with open(DIRECTORY_STARTING_LETTER) as file:
    letter = file.read()

with open(DIRECTORY_NAMES) as file:
    names = file.readlines()


for name in names:
    name_strip = name.strip()
    new_letter = letter.replace("[name]", name_strip)    

    with open(f"{DIRECTORY_LETTERS}letter_for_{name_strip}.txt", mode="w") as file:
        file.write(new_letter)