from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *

class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (25, 255, 40))
        self.state = {
            'moveTo': '',
            'winner': '',
        }
        

    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke),
            Trainer(trainer2Poke)
        ]
        
    def elementsToDisplay(self):
        if self.state['winner'] != 0:
            return
        self.elements = [
            Image((50, 50), 100, 100, './imgs/battlescreen.png'),
        ]
    


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
        screen.trainers[1].pokemon[1].takeDamage(self.move)
        screen.checkHealth()
        screen.trainers[1].removeFaintedPokemon()
        screen.trainers.reverse()
        if len(screen.trainers[1]) == 0:
            screen.state['winner'] = screen.trainers[0]
            return

        
        


    # def checkWinner(self):
    #     for trainer in self.trainers:
