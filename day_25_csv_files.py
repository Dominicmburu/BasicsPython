# import csv

# with open("day_25_file.csv") as data_file:

#     data = csv.reader(data_file)

#     temperatures = []

#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data = pd.read_csv("day_25_file.csv")

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(len(temp_list))

print(data["temp"].mean())

print(data["temp"].max())

# get data in rows
## print row with name monday
print(data[data["day"] == "Monday"])

## print row with the highest temperature
print(data[data["temp"] == data["temp"].max()])


monday = data[data["day"] == "Monday"]
print(monday["condition"])

monday_temp = int(monday["temp"])
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)








