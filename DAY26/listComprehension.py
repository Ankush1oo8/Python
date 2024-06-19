numbers=[1,2,3,4,5,6,7,8,9]
new_list=[n+1 for n in numbers]
print(new_list)

#using with strings
name="Ankush"
list=[letter for letter in name]
print(list)

#conditional list comprehension
names=["Alex","Beth","Dave","Ankush","yash","Chudiwal"]
new_names=[name.upper() for name in names if len(name)>5]
print(new_names)