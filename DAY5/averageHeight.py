heights=input("Input students heights: ").split()
for n in range(0,len(heights)):
    heights[n]=int(heights[n])
print(heights)
# can use sum()
total=0
num=0
for h in heights:
    total+=h
    num+=1

avg=round(total/num)
print(avg)