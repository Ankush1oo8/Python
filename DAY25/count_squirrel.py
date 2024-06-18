import pandas as p
data=p.read_csv("DAY25/data_squirrel.csv")

gray_count=len(data[data["Primary Fur Color"]=="Gray"])
red_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_count=len(data[data["Primary Fur Color"]=="Black"])

data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[gray_count,red_count,black_count]
}

new_data=p.DataFrame(data_dict)
new_data.to_csv("DAY25/color_squirrel_count.csv")