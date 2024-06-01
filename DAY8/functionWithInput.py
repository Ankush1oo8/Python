# def name():
#     do this
def greet():
    print("Hello")
    print("How do you do?")
    print("ohhh yeah")

greet()

#function with inputs
# def name(smething):
#     do this with something

def greet_input(name):
    print("hello "+name)
    print("how are you "+name)

greet_input("ankush")

#function with more than one input
def greet_mul_input(name,location):
    print("hello "+name)
    print(f"what's the wheather in {location}")

greet_mul_input("Ankush","Shivoor")

#keyword arguments
greet_mul_input(name="Ankush",location="Shivoor")
