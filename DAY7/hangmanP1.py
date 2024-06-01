import random

words=["ardvark","baboon","camel"]

choosen_word=random.choice(words)

guess=input("Guess a letter: ")

for char in choosen_word:
    if(char==guess):
        print("RIGHT")
    else:
        print("WRONG")