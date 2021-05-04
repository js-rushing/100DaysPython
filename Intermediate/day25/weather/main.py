# with open("weather_data.csv") as file:
#     data = file.readlines()
#     cleaned_data = []
#     for line in data:
#         cleaned_data.append(line[:-1])
#     print(data)
#     print(cleaned_data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))

# temp_total = 0
# for temp in temp_list:
#     temp_total += temp
# average_temp = temp_total / len(temp_list)
# average_temp = sum(temp_list) / len(temp_list)
average_temp = data["temp"].mean()
max_temp = data["temp"].max()
# print(int(average_temp))
# print(f"Max Temp: {max_temp}")

# Get Data in Columns
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(int(monday.temp) * 9/5+32)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}


data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
