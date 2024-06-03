# def my_function():
#     return 3*2
# print(my_function())

def formatNames(f_name,l_name):
    formated_fName=f_name.title()
    formated_lName=l_name.title()
    return (f"{formated_fName} {formated_lName}")

name=formatNames("AnKush","chudiwal")
print(name)
