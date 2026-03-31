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

        # y = 30
        # x = 10
        # for poke in self.trainers[0].pokemon:
        #     self.elements.append(Image((x, y), 15, 15, poke.img))
        #     self.elements.append(Label((x, 20), 20, 10, poke.name, 17, (0, 0, 0)))
        #     x += 13
        #     # y = 50
        #     # x = 10
        #     # x += 10

        # y = 30
        # x = 60
        # for poke in self.trainers[1].pokemon:
        #     self.elements.append(Image((x, y), 15, 15, poke.img))
        #     self.elements.append(Label((x, 20), 20, 10, poke.name, 17, (0, 0, 0)))
        #     x += 13
        #     # y = 50
        #     # x = 60
        #     # x += 10

    


        poke = self.trainers[0].pokemon[0]
        x = 25
        y = 35
        self.elements.append
        self.elements.append(Image((x,y), 25, 25, poke.img))
        self.elements.append(Label((15, 45), 20, 10, poke.name + '\n' + str(poke.hp), 20, (0, 0, 0)))
        self.elements.append(Label((15, 45), 20, 10, poke.name + '\n' + str(poke.hp), 19, (255, 255, 255)))
        
        

        poke = self.trainers[1].pokemon[1]
        x = 75
        y = 35
        self.elements.append(Image((x,y), 25, 25, poke.img))
        self.elements.append(Label((85, 45), 20, 10, poke.name + '\n' + str(poke.hp), 20, (0, 0, 0)))
        self.elements.append(Label((85, 45), 20, 10, poke.name + '\n' + str(poke.hp), 19, (255, 255, 255)))  

        xs = [40, 60]
        ys = [80, 70]

        moveIndex = 0
        for x in xs:
            for y in ys:
                self.elements.append(Attack(x, y, self.trainers[0].pokemon[0].moves[moveIndex]))
                moveIndex += 1
                 

class Attack(Button):
    def __init__(self, x, y, move):
        self.move = move
        super().__init__((x, y), 20, 10, move.name)
    def onClick(self, screen):
        screen.trainers[0].pokemon[1].takeDamage(self.move)
        screen.trainers.reverse()
        # screen.trainers[0].removeFaintedPokemon()
        # if len(screen.trainers[1]) == 0:
        #     #the other wins


        #you'll want that trainer to check and handle fainted pokemon
        #check if someone won
        # screen.trainers.reverse()
        


# def checkWinner(self):
#     for trainer in self.trainers:
