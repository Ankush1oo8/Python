# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this
print("WELCOME")
height=int(input("ENTER YOUR HEIGHT in CM: "))
if height>=120:
    print("YOU CAN RIDE!!")
    age=int(input("WHAT IS YOUR AGE: "))
    if(age<12):
        print("YOUR FEES IS $5")
    elif age<=18:
        print("YOUR FEES IS $8")
    else:
        print("YOUR FEES IS $10")
else:
    print("YOU CAN NOT RIDE!!!")