import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")

#get series lists of squirrel colors in the DataFrame (or get specific column data)
fur_color = data["Primary Fur Color"]

# print(fur_color)

#determine every colors

# Get unique colors
unique_colors = fur_color.unique()

# Print the unique colors
print("Unique fur colors:", unique_colors)

#get the each row of the unique colors, sum.
nan = data[data["Primary Fur Color"] == "nan"]
gray_fur = data[data["Primary Fur Color"] == "Gray"]
cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
black = data[data["Primary Fur Color"] == "Black"]

nan_count = len(nan)
gray_fur_count = len(gray_fur)
cinnamon_count = len(cinnamon)
black_count = len(black)

#Create a dataframe for Squirrel Fur numbers from scratch
squirrel_fur = {
    "fur_color":["nan", "Gray","Cinnamon","Black"],
    "count":[nan_count,gray_fur_count,cinnamon_count,black_count]
}

#create csv
df = pandas.DataFrame(squirrel_fur)
df.to_csv("squirrel_count.csv")





