year=int(input("Enter any YEAR: "))
if year%4==0:
    if(year%100==0):
        if(year%400==0):
            print("It Is A Leap Year!!!")
        else:
            print("Not a Leap Year!")
    else:
        print("It is leap Year")
else:
    print("Not a Leap year!!")