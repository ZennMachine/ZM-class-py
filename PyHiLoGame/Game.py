from tkinter import *
from tkinter.ttk import *
import random

def __init__(self, root):
    self.root = root

old_card = 0
score = 0
cards = []
A = 1
J = 11
Q = 12
K = 13

def initialise_game(self):
    print("Game Started")
    A = 1
    J = 11
    Q = 12
    K = 13

    self.cards = [ A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K ]

    self.score = 0
    self.old_card = get_new_card()

def choose_lower(self):
    print("chose lower")
    cardLabel.set("Current Card is: " + str(old_card))
    new_card = self.get_new_card
    is_higher = new_card_is_higher(self.old_card, new_card)
    if is_higher == False:
        self.score + 1
        self.old_card = new_card
    else:
        print("GameOver")
        self.game_over(self)

def choose_higher(self):
    print("chose higher")
    cardLabel.set("Current Card is: " + str(old_card))
    new_card = self.get_new_card
    is_higher = new_card_is_higher(self.old_card, new_card)
    if is_higher == True:
        self.score + 1
        self.old_card = new_card
    else:
        print("GameOver")
        self.game_over(self)

    
def get_new_card():
    card = random.choice(cards)
    return card

def new_card_is_higher(old_card, new_card):
    if old_card > new_card:
        return False
    else:
        return True

def game_over(self):
    self.labelToChange.set("Game Over")


root = Tk()
root.minsize(width=720, height=360)
root.resizable(width=False, height=False)
root.title("Higher Lower")

welcome = Label(root, text="Welcome to Higher or Lower!").pack()

initialise_game
cardLabel = StringVar()
cardLabel.set("Current Card is: " + str(old_card))
scoreLabel = StringVar()
scoreLabel.set("Score: " + str(score))

scoreLabel = Label(root, text="Score: ").place(x=720/2 - 20, y=30)
currentCardLabel = Label(root, text=cardLabel).place(x=720/2 - 40, y=60)
lowerButton = Button(root, text="Lower", command=choose_lower).place(x=720/2 - 80, y=100)
higherButton = Button(root, text="Higher", command=choose_higher).place(x=720/2 , y=100)

root.mainloop()