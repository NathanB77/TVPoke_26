from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *

class WinScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (25, 255, 40))
        self.winner = ''

    def elementsToDisplay(self):
        self.elements = [
            Image((50 , 50), 100, 100, './imgs/Winner.jpg'),
            Label((50, 70), 70, 70, str(self.winner.name) + '\n' + 'You won!'),
            Label((50, 50), 100, 100,'Congratulations!'),
        ]