# 28/02/2024
# Day - 025


# pip install pandas
# https://pandas.pydata.org/docs/
# https://pandas.pydata.org/docs/reference/index.html


##################################################
print("\n\n*** Squirrels Pandas Solution***")

import pandas as pd



DIRECTORY_CSV = ".\\025 - CSV and Pandas\\squirrels_central_park_2018.csv"
data = pd.read_csv(DIRECTORY_CSV)



print("\nSquirrel Colors:")
print(data["Primary Fur Color"].unique())



gray = len(data["Primary Fur Color"] == "Gray")
cinnamon = len(data["Primary Fur Color"] == "Cinnamon")
black = len(data["Primary Fur Color"] == "Black")
nan = data["Primary Fur Color"].isna().sum()



print("\nCreate a Dataframe from scratch: ")
data_fur = {
    "Fur Color": ["gray", "cinnamon", "black", "NaN"],
    "Count": [gray, cinnamon, black, nan]
}
dataframe = pd.DataFrame(data_fur)
dataframe.to_csv(".\\025 - CSV and Pandas\\squirrels_fur.csv")
print(dataframe)