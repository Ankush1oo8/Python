import random
names=input("Enter names sepereted by comma\n")
name=names.split(", ")
randNum=random.randint(0,len(name)-1)

print(name[randNum]+" is going to buy the meal")