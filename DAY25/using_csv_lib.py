# with open("DAY25/weather_data.csv") as file:
#     content=file.readlines()
import csv

with open("DAY25/weather_data.csv") as file:
    data=csv.reader(file)
    #making list of temperature
    temp=[]
    for row in data:
        if row[1]!="temp":
            temp.append(int(row[1]))
    print(temp)

