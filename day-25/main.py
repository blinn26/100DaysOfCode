# Specify the path to weather_data.csv at the beginning to avoid repetition
import pandas
import csv
weather_data_path = "/Users/benlinn/Python Course/100DaysOfCode/day-25/weather_data.csv"

# Using just file methods
with open(weather_data_path) as data_file:
    data = data_file.readlines()
    print(data)

# Using csv library

with open(weather_data_path) as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# Using the pandas library

data = pandas.read_csv(weather_data_path)
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

print(data["temp"].mean())
print(data["temp"].max())

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# Get Row data value
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp.iloc[0])
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
students_data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
students_data = pandas.DataFrame(students_data_dict)
students_data.to_csv(
    "/Users/benlinn/Python Course/100DaysOfCode/day-25/new_data.csv")

# Central Park Squirrel Data Analysis
squirrel_data_path = "/Users/benlinn/Python Course/100DaysOfCode/day-25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
squirrel_data = pandas.read_csv(squirrel_data_path)
grey_squirrels_count = len(
    squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(
    squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(
    squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

squirrel_counts_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

squirrel_counts_df = pandas.DataFrame(squirrel_counts_dict)
squirrel_counts_df.to_csv(
    "/Users/benlinn/Python Course/100DaysOfCode/day-25/squirrel_count.csv")
