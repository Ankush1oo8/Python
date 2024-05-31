import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome")
nLetter=int(input("Enter Number Of Letter You Want: \n"))
nSymbol=int(input("How Many Symbols you want: \n"))
nNumber=int(input("How many Number you want: \n"))

#easy level
password=""
for char in range(1,nLetter+1):
    rChar=random.choice(letters)
    password+=rChar
for sym in range(1,nSymbol+1):
    rSym=random.choice(symbols)
    password+=rSym
for char in range(1,nNumber+1):
    password+=random.choice(numbers)
print(password)

#Hard Level
passwordList=[]
for char in range(1,nLetter+1):
    rChar=random.choice(letters)
    passwordList.append(rChar)
for sym in range(1,nSymbol+1):
    rSym=random.choice(symbols)
    passwordList.append(rSym)
for char in range(1,nNumber+1):
    passwordList.append(random.choice(numbers))
random.shuffle(passwordList)
hard_Password=""
for char in passwordList:
    hard_Password+=char
print(hard_Password)