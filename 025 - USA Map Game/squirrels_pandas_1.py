# 28/02/2024
# Day - 025


# pip install pandas
# https://pandas.pydata.org/docs/
# https://pandas.pydata.org/docs/reference/index.html


##################################################
print("\n\n*** Squirrels Pandas ***")

import pandas as pd



DIRECTORY_CSV = ".\\025 - USA Map Game\\squirrels_central_park_2018.csv"
data = pd.read_csv(DIRECTORY_CSV)



print("\nSquirrel Colors:")
print(data["Primary Fur Color"].unique())



all_furs = data["Primary Fur Color"]
# print(all_furs)

gray = 0
cinnamon = 0
black = 0
nan = 0

for squirrel in all_furs:
    if squirrel == "Gray":
        gray += 1
    elif squirrel == "Cinnamon":
        cinnamon += 1
    elif squirrel == "Black":
        black += 1
    else:
        nan += 1

print(f"Gray {gray}, Cinnamon {cinnamon}, Black {black}, NaN {nan}")
print(all_furs.value_counts()) # exclude NaN



print("\nCreate a Dataframe from scratch: ")
data_fur = {
    "Fur Color": ["gray", "cinnamon", "black", "NaN"],
    "Count": [gray, cinnamon, black, nan]
}
dataframe = pd.DataFrame(data_fur)
dataframe.to_csv(".\\025 - USA Map Game\\squirrels_fur.csv")
print(dataframe)