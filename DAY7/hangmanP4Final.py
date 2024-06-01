import random

words=["ardvark","baboon","camel"]

choosen_word=random.choice(words)
print(choosen_word)
lives=6
display=[]
for char in choosen_word:
    display+="_"
print(display)
end=False
while not end:
    guess=input("Guess a letter: ")

    for i in range(len(choosen_word)):
        letter=choosen_word[i]
        if(letter==guess):
            display[i]=letter
    
    if guess not in choosen_word:
        lives-=1
        if lives==0:
            end=True
            print("YOU LOSE")


    print(display)
    if "_" not in display:
        end=True
        print("YOU WIN")
    
    print(stages[lives])