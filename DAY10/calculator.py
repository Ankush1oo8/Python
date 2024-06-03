#add
def add(n1,n2):
    return n1+n2

#subtract
def sub(n1,n2):
    return n1-n2

#multiply
def mul(n1,n2):
    return n1*n2

#divide
def div(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

num1=int(input("Whats the first Number: "))


for symbol in operations:
    print(symbol)

operation_symbol=input("Pick an operation from the line Above: ")

num2=int(input("Whats the second Number: "))

function=operations[operation_symbol]
ans=function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {ans}")
