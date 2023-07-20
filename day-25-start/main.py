import pandas

file= open("day-25-start/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data= pandas.read_csv(file)
gray_squirrel= (len(data[data["Primary Fur Color"] == "Gray"]))
Cinnamon_squirrel= (len(data[data["Primary Fur Color"] == "Cinnamon"]))
Black_squirrel= (len(data[data["Primary Fur Color"] == "Black"]))

print(f"Gray: {gray_squirrel}, Cinnamon: {Cinnamon_squirrel}, Black: {Black_squirrel}")




my_dict= {"Fur": ["Gray", "Cinnamon", "Black"],
          "Count": [gray_squirrel, Cinnamon_squirrel, Black_squirrel]
          }

dataa= pandas.DataFrame(my_dict)
dataa.to_csv("/Users/air/Desktop/100daysofpython/day-25-start/squirrel.csv")