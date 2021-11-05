from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
Builder.load_file('HiLo.kv')

class HiLoGame(Widget):
    pass

class HiLoApp(App):
    def build(self):
        return HiLoGame()

if __name__ == '__main__':
    HiLoApp().run()