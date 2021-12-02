import random
from tkinter import *
import gui

A = 1
J = 11
Q = 12
K = 13

cards = [ A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K ]


def get_new_card():
    card = random.choice(cards)
    return card


def new_card_is_higher(old_card, new_card):
    if old_card > new_card:
        return False
    else:
        return True
    

def game_run_cl():
    print("Welcome to the ZM Higher or Lower Game! \n The game will deal you a card,\n" 
        "each time you must guess whether the next card dealt is higher or lower than the previously dealt card.\n"
        "Everytime you get the answer right, you earn a point.\n If you guess wrong however, the game ends.\n"
        "--------------------------------------------")
    # Game loop runs continuously until the answer given is wrong
    is_wrong = False
    score = 0

    old_card = get_new_card()
    while not is_wrong:
        print("Your card is: (",old_card , ") .\n Is the next card higher or lower?")
        user_in = input("h or l? ")
        new_card = get_new_card()
        is_higher = new_card_is_higher(old_card, new_card)
        if user_in == "h" and is_higher:
            print(new_card)
            print("Correct")
            score += 1
            print(score)
        elif user_in == "h" and not is_higher:
            print(new_card)
            is_wrong = True
        elif user_in == "l" and not is_higher:
            print(new_card)
            print("Correct")
            score += 1
        else:
            print(new_card)
            is_wrong = True
        # Replace the old card with the new card
        old_card = new_card
    print("Game Over")


if __name__ == '__main__':
    game_run_cl()
