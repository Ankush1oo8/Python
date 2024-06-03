# return is end of function
def formatNames(f_name,l_name):
    if f_name=="" or l_name=="":
        return "You Didn't Provide Valid Inputs"
    formated_fName=f_name.title()
    formated_lName=l_name.title()
    return (f"{formated_fName} {formated_lName}")

print(formatNames(input("Whats your first Name: "),input("Whats your Last Name: ")))
