height=float(input("ENter the height: "))
weight=int(input("ENter the weight: "))
if height>3:
    raise ValueError("Human height should not be greater than 3 meter")
bmi=weight/height**2
print(bmi)