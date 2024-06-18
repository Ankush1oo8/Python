import pandas as p

data=p.read_csv("DAY25/weather_data.csv")
#print temperature 
# print(data["temp"])

data_dict=data.to_dict()
# print(data_dict)


#calculate average of temperature
temp_list=data["temp"].to_list()
total=len(temp_list)
sum=0
for _ in temp_list:
    sum +=int(_)
print(sum/total)

#by panda methods
print(data["temp"].mean())

#max value
print(f"Max value:{data["temp"].max()}")

#not using square brackets/using column like object
print(data.condition)

#Get Data In Row
print(data[data.day=="Monday"])

#row where temp is max
print(data[data.temp==data.temp.max()])

monday=data[data.day=="Monday"]
print(monday.temp)
print(monday.condition)

#create a dataframe from scratch
data_dict={
    "students":["Amy","James","BKP"],
    "scores":[76,75,74]
}
data=p.DataFrame(data_dict)
data.to_csv("DAY25/new_data.csv")