enemies=1 #global scope

def increase_enemies():
    global enemies#usesd to modify global scope
    enemies=2 #function scope
    print(enemies)

increase_enemies()
print(enemies)


#global constants

PI=3.14159

def cal():
    return PI

print(cal())
