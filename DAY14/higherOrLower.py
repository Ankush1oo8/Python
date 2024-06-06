import art
import gameData
import random

print(art.logo)
score=0

def formate_data(account):
    account_name=account["name"]
    account_des=account["description"]
    account_country=account["country"]
    return (f"{account_name}, a {account_des}, from {account_country}")


def check(guess,follower_a,follower_b):
    if follower_a>follower_b:
        return guess=="A"
    else:
        return guess=="B"

account_b=random.choice(gameData.data)
game_continue=True
while game_continue:
    account_a=account_b
    account_b=random.choice(gameData.data)
    if account_a==account_b:
        account_b=random.choice(gameData.data)


    print(f"Compare A: {formate_data(account_a)}")
    print(art.vs)
    print(f"Against B: {formate_data(account_b)}")

    guess=input("who has more followers? Type 'A' or 'B': ")

    a_follower=account_a["follower_count"]
    b_follower=account_b["follower_count"]

    correct=check(guess,a_follower,b_follower)

    if correct:
        score+=1
        print(f"YOU ARE RIGHT!! Current Score :{score}")
    else:
        game_continue=False
        print(f"SORRY< THAT'S WRONG! Final Score:{score}")



