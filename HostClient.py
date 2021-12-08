from TicTacToeDisplay import TicTacGame
import pygame
import HostMainMenu
import PlayerInfo
import HostGameChoiceMenu
import os
from network import Network
pygame.init()
width = 800
height = 800
win = pygame.display.set_mode((width, height))

os.system("start cmd /k python server.py") 
#os.system("start cmd /k python network.py") 
n = Network()


clientNumber = 0
GameScreen = 0
m = HostMainMenu.Menu(win, False,n)
Player1 =PlayerInfo.player("", 1)
game = None
def redrawWindow(win):
    # player.draw(win) 
    global GameScreen
    global Player1
    global m
    print("Client"+str(GameScreen))
    if GameScreen == 0:
        m = HostMainMenu.Menu(win, True, n)
        Player1 = PlayerInfo.player(m.username,1)
        pygame.display.update()
    if GameScreen==1:
        win.fill((0,0,0))
        m = HostGameChoiceMenu.GameMenu(win, True, Player1, n)
        pygame.display.update()
    if GameScreen ==2:
        win.fill((0,0,0))
        m=TicTacGame(win, True, n, Player1)
        game.setState("GamesMenu")
        pygame.display.update()
    pygame.display.update()

    


def main():
    global GameScreen
    global Player1
    global game
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        try:
            game = n.send("getGame")
            Player1 = game.getPlayer1()
            GameScreen = game.getState()
        except:
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
                
        # p.move()
        redrawWindow(win)


main()
