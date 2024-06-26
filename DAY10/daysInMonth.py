def isLeap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

def daysInMonth(year,month):
    if month>12 or month<1:
        return "Invalid Input!!!"
    month_days=[31,28,30,31,30,31,31,30,31,30,30,31]
    if isLeap(year) and month==2:
        return 29
    return month_days[month-1]


year=int(input("Enter a Year: "))
month=int(input("Enter a Month: "))
days=daysInMonth(year,month)

print(days)