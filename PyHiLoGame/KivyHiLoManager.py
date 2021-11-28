from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

Builder.load_file('HiLo.kv')
import random

class HiLoGame(Widget):
    caption = StringProperty()

    def __init__(self, **kwargs):
        super(HiLoGame, self).__init__(**kwargs)
        self.caption = "Hello"


class HiLoApp(App):

    def build(self):
        self.score = 0
        self.old_card = self.get_new_card()
        self.game = HiLoGame()
        return self.game
        
    A = 1
    J = 11
    Q = 12
    K = 13

    cards = [ A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K ]

    

    def get_new_card(self):
        card = random.choice(self.cards)
        return card


    def new_card_is_higher(self, old_card, new_card):
        if old_card > new_card:
            return False
        else:
            return True

    def choose_higher(self):
        new_card = self.get_new_card()
        is_higher = self.new_card_is_higher(self.old_card, new_card)
        if(is_higher == True):
            self.score += 1
            self.game.caption = "Correct"

    def choose_lower(self):
        new_card = self.get_new_card()
        is_lower = self.new_card_is_higher(self.old_card, new_card)
        if (is_lower == True):
            self.score += 1

    def game_run(self):
        print("doing stuff...")


if __name__ == '__main__':
    HiLoApp().run()
