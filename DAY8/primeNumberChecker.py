def checkPrime(num):
    for i in range(2,num):
        if(num%i==0):
            print("Not a Prime Number")
            break
        else:
            print("It's a Prime Number")
            break

n=int(input("Enter a number: "))
checkPrime(n)