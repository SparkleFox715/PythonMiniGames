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
Player1 =PlayerInfo.player("")
Player2 =PlayerInfo.player("")
USERNAME = ""
USERNAME2 = ""
def redrawWindow(win):
    # player.draw(win) 
    global GameScreen
    global Player1
    global Player2
    global m
    global USERNAME
    global USERNAME2
    if GameScreen == 0:
        m = HostMainMenu.Menu(win, True, n)
        GameScreen+=1
        Player1 = PlayerInfo.player(m.username)
        USERNAME = Player1.username
        USERNAME2 = m.username2
        Player2 = PlayerInfo.player(USERNAME2)
        print(GameScreen)
    elif GameScreen==1:
        win.fill((0,0,0))
        m = HostGameChoiceMenu.GameMenu(win, True, Player1)
    else:
        win.fill((246, 114, 128))
    pygame.display.update()


def main():
    global GameScreen
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        try:
            game = n.send("getGame")
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
