# 29/02/2024
# Day - 026



##################################################
# DAY 26 PROJECT: NATO SPELLING

print("\n*** Welcome to the NATO SPELLING! ***")



import pandas as pd

DIRECTORY_NATO_CSV = "026 - NATO Alphabet\\PJ_NATO\\nato_phonetic_alphabet.csv"



df_nato = pd.read_csv(DIRECTORY_NATO_CSV)
# print(df_nato)
# print(df_nato.to_dict())



# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

dict_nato = {row["letter"]: row["code"] for (index, row) in df_nato.iterrows()}
dict_nato = {row.letter: row.code for (index, row) in df_nato.iterrows()}

print(dict_nato)



# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")
list_letter = list(word.upper())
list_nato_word = []


# long for loop
for letter in list_letter:
    if letter in dict_nato:
        list_nato_word.append(dict_nato[letter])

print(list_nato_word)


# short for loop
list_nato_word = [dict_nato[letter] for letter in list_letter if letter in dict_nato]

print(list_nato_word)


# shorter for loop: exception with numbers
list_nato_word = [dict_nato[letter] for letter in list_letter]

print(list_nato_word)