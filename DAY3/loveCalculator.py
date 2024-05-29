print("Welcome")
name1=input("Enter name one: ")
name2=input("Enter name two: ")
added=name1+name2
lowerStr=added.lower();

t=lowerStr.count("t")
r=lowerStr.count("r")
u=lowerStr.count("u")
e=lowerStr.count("e")

true=t+r+u+e

l=lowerStr.count("l")
o=lowerStr.count("o")
v=lowerStr.count("v")
e=lowerStr.count("e")

love=l+o+v+e

total=int(str(true)+str(love))

if total<10 or total>90:
    print(f"your total is {total}, you go together like coke and mentos")
elif total>=40 and total<=50:
    print(f"your total is {total}, you are alright together")
else:
    print(f"your total is {total}")
