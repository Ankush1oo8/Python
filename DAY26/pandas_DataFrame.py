students={
    "student":["Ankush","Alex","Arvind"],
    "score":[90,88,78]
}
import pandas as p
data=p.DataFrame(students)
print(data)
for(index,row)in data.iterrows():
    print(row.student)