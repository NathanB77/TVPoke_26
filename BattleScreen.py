from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *

class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (25, 255, 40))
        self.state = {
            'moveTo': '',
        }
        

    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke),
            Trainer(trainer2Poke)
        ]
        
    def elementsToDisplay(self):
        self.elements = [
            Image((50, 50), 100, 100, './imgs/battlescreen.png'),
        ]

        # y = 0
        # #two rows of three
        # for trainer in self.trainers:
        #     x = 0
        #     y += 100/3
        #     for poke in trainer.pokemon:
        #         x += 100/4
        #         self.elements.append(Image((x, y), 20, 20, poke.img))
        #         self.elements.append(Label((x, y + 10), 20, 10, poke.name))

        y = 30
        x = 10
        for poke in self.trainers[0].pokemon:
            self.elements.append(Image((x, y), 15, 15, poke.img))
            self.elements.append(Label((x, 20), 20, 10, poke.name, 20, (0, 221, 221)))
            x += 13
            # y = 50
            # x = 10
            # x += 10

        y = 30
        x = 60
        for poke in self.trainers[1].pokemon:
            self.elements.append(Image((x, y), 15, 15, poke.img))
            self.elements.append(Label((x, 20), 20, 10, poke.name, 20, (0, 221, 221)))
            x += 13
            # y = 50
            # x = 60
            # x += 10
                
class ContinueButton(Button):
    def onclick(self):
        self.elementsToDisplay = []
        



