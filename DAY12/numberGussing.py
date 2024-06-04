import random
EASY_LEVEL=10
HARD_LEVEL=5
def check(guess,ans,turns):
    if guess>ans:
        print("TOO HIGH")
        return turns-1
    elif guess<ans:
        print("TOO LOW")
        return turns-1
    else:
        print(f"You have got it ! the answer is {ans}")


def set_difficulty():
    level=input("Choose a difficulty type 'easy' or 'hard' :")
    if(level=="easy"):
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print("Welcome to the Number Gussing game!")
    print("I'm thinking of a number between 1 to 100")
    answer=random.randint(1,100)

    turns=set_difficulty()
    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the Number")
        guess=int(input("Make a Guess: "))
        turns=check(guess,answer,turns)
        if turns==0:
            print("you have run out of guesses")
            return

game()