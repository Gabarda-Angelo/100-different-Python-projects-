# data_list = []
# def get_weather_data():
#     with open("weather_data.csv") as weather_data_file:
#         new_format = weather_data_file.readlines()
#         for info in new_format:
#             each = info.strip()
#             data_list.append(each)

# import csv

# #
# # temperature = []
# # with open ("weather_data.csv") as data_file:
# #     data = list(csv.reader(data_file))
# #
# #     for row in data[1:]:
# #         temperature.append(int(row[1]))
# # print(temperature)


import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# s = pandas.Series(temp_list)
#
# maximum = s.max()
#
# print(data["temp"].max())

# # Get Data in columns

# print(data["condition"])
# print(data.condition)

#Get Data in Row

# print(data[data.day == "Monday"])
#
# print(data["temp"].max())
#print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# celsius = monday.temp
# fahrenheit = celsius * 9/5 + 32
# print(fahrenheit)

#Create a dataframe from scratch
data_dict = {
    "students":["Amy", "James","Angela"],
    "scores":[76,56,65]
}


data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)








