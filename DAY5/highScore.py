score=input("Enter the score of Students: ").split()
for n in range(0,len(score)):
    score[n]=int(score[n])
print(score)

# print(max(score))
highest=0;
for s in score:
    if(s>highest):
        highest=s

print(f"Highest Score is {highest}")