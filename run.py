from PyUI.Window import Window
##import the custom screens you made---
from SelectScreen import SelectScreen
from BattleScreen import BattleScreen
from WinScreen import WinScreen

##-------------------------------------


window = Window("TVPoke26", (0,255,0), './imgs/pokeIcon.png') ##Create the window to work with

##Create Screen Objects for use------
selectScreen = SelectScreen(window)
battleScreen = BattleScreen(window)
winScreen = WinScreen(window)
##-----------------------------------

screen = selectScreen ##set screen to be the starting screen

while True: ##Game loop
    ##Enter code here to handle changes between screens---
    if selectScreen.state["goTo"] == "BATTLE":
        selectScreen.state["goTo"] = ''
        pokemonList1 = selectScreen.state["selectedPoke"][0]
        pokemonList2 = selectScreen.state["selectedPoke"][1]
        battleScreen.addTrainers(pokemonList1, pokemonList2)
        screen = battleScreen

    if battleScreen.winner != '':
       winScreen.winner = battleScreen.winner
       screen = winScreen
       battleScreen.winner = ''




    ##----------------------------------------------------

    window.checkForInput(screen) 
    window.update(screen) 
