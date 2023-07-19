
import csv
import pandas

filee= open("day-25-start/weather_data.csv")
filedata= pandas.read_csv(filee)
temperatures=[]
for row in filedata:
    if row[1]!="temp":
        temperatures.append(row[1])

print(temperatures)



file= open("day-25-start/weather_data.csv")
filedataa= pandas.read_csv(file)
temperatures=[]


print(filedataa["temp"])

