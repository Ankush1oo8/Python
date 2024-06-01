import random

words=["ardvark","baboon","camel"]

choosen_word=random.choice(words)
print(choosen_word)

display=[]
for char in choosen_word:
    display+="_"
print(display)

guess=input("Guess a letter: ")

for i in range(len(choosen_word)):
    letter=choosen_word[i]
    if(letter==guess):
        display[i]=letter

print(display)