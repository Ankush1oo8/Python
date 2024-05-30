import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_img=[rock,paper,scissors]
print("0 for Rock, 1 for Paper, 2 for Scissors")
user=int(input("Enter your choice :"))
print(game_img[user])
computer=random.randint(0,2)
print("Computer choose: \n")
print(game_img[computer])
if user==0 and computer==2:
    print(f"you win")
elif computer==0 and user==2:
    print("you lose")
elif user>=3 or user<0:
    print("Invalid,you lose!!")
elif computer>user:
    print("you lose")
elif user>computer:
    print("you win")
elif computer==user:
    print("it is Draw !!")
