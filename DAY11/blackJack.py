import random
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)


def calc_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user,computer):
    if(user==computer):
        return "Draw"
    elif computer==0:
        return "Lose, Opponent Has BlackJack"
    elif user==0:
        return "Win with a BlackJack"
    elif user>21:
        return "You Went over. YOU LOSE"
    elif computer>21:
        return "Opponent went over, YOU WIN"
    elif user > computer:
        return "YOU WIN"
    else:
        return "YOU LOSS"

def play_game():
    user_card=[]
    computer_card=[]




    is_gameover=False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_gameover:
        user_score=calc_score(user_card)
        com_score=calc_score(computer_card)
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"computer's first card: {computer_card[0]}")


        if(user_score==0) or (com_score==0) or user_score>21:
            is_gameover=True
        else:
            drawCard=input("Type 'y' to get another card, type 'n' to pass: ")
            if(drawCard=="y"):
                user_card.append(deal_card())
            else:
                is_gameover=True


    while com_score!=0 and com_score<17:
        computer_card.append(deal_card())
        com_score=calc_score(computer_card)


    print(f"     Your Final hand: {user_card}, final score: {user_score} ")
    print(f"     Computer's final hand: {computer_card}, final score: {com_score}")
    print(compare(user_score,com_score))

while input("Do you wanr to play a game of blackjack ? type 'y' or 'n' : "):
    play_game()
