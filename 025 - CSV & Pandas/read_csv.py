# 28/02/2024
# Day - 025



##################################################
print("\n\n*** Weather Data ***")


import csv


DIRECTORY_CSV = ".\\025 - CSV and Pandas\\weather_data.csv"
data = []


with open(DIRECTORY_CSV) as file:
    data = csv.reader(file)
    print(data)
    
    temperatures = []
    
    # data is an iterator: once you do 1 for loop, it is exhausted
    for row in data:
        print(row)
        
        if row[1] != "temp":
            temperatures.append(int(row[1]))

        
    print(temperatures)