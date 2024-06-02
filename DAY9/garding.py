students={
    "harry":81,
    "ron":78,
    "hermione":99,
    "draco":74,
    "neville":62,
}

grading={}

for student in students:
    score=students[student]
    if score>90:
        grading[student]="OutStanding"
    elif score>80:
        grading[student]="Exceeds Expectation"
    elif score>70:
        grading[student]="Acceptable"
    else:
        grading[student]="Fail"

print(grading)

