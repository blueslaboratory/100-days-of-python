# 28/02/2024
# Day - 025


# pip install pandas
# https://pandas.pydata.org/docs/
# https://pandas.pydata.org/docs/reference/index.html


##################################################
print("\n\n*** Weather Data ***")



import pandas as pd

DIRECTORY_CSV = ".\\025 - CSV and Pandas\\weather_data.csv"
data = pd.read_csv(DIRECTORY_CSV)



print("\nData: ")
print(data)



print("\nTemperatures: ")
print(data["temp"])
print(type(data["temp"]))



print("\nTemperatures List: ")
temp_list = data["temp"].to_list()
print(temp_list)
print(type(temp_list))



print("\nTemperatures Average: ")
total = 0
for t in temp_list:
    total += t

average = sum(temp_list)
    
print(total/len(temp_list))
print(average/len(temp_list))
print(data["temp"].mean())



print("\nTemperature Max: ")
print(data["temp"].max())



print("\nGet Data in Columns: ")
print(data["condition"])
print(data.condition)



print("\nGet Rows: ")
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])



print("\nGet Data in Row: ")
monday = data[data.day == "Monday"]
print(monday.condition)
temp_fahrenheit = monday.temp[0]*9/5 +32
print(temp_fahrenheit)



print("\nCreate a Dataframe from scratch: ")
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
dataframe = pd.DataFrame(data_dict)
dataframe.to_csv(".\\025 - CSV and Pandas\\new_data.csv")
print(dataframe)