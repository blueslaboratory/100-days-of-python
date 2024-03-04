# 04/03/2024
# Day - 030



##################################################
# DAY 30 PROJECT: NATO SPELLING + EXCEPTIONS SOLUTION

print("\n*** Welcome to the NATO SPELLING + Exceptions solution! ***")



import pandas as pd

DIRECTORY_NATO_CSV = "030 - Exceptions & JSON\\PJ_NATO\\nato_phonetic_alphabet.csv"



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
def generate_phonetic():
    word = input("Enter a word: ").upper()

    # shorter for loop + KeyError exception
    try:
        list_nato_word = [dict_nato[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(list_nato_word)



generate_phonetic()