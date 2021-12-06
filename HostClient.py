import pygame
import HostMainMenu
import PlayerInfo
import os
from network import Network
pygame.init()
width = 800
height = 800
win = pygame.display.set_mode((width, height))

os.system("start cmd /k python server.py") 
#os.system("start cmd /k python network.py") 
n = Network()
n.send("P1 Connected")


clientNumber = 0
GameScreen = 0
m = HostMainMenu.Menu(win, False,n)
Player =PlayerInfo.player("")
USERNAME = ""
USERNAME2 = ""
def redrawWindow(win):
    # player.draw(win)
    global GameScreen
    global Player
    global m
    global USERNAME
    if GameScreen == 0:
        m = HostMainMenu.Menu(win, True, n)
        GameScreen+=1
        Player = PlayerInfo.player(m.username)
        USERNAME = Player.username
        USERNAME2 = m.username2
        print(USERNAME+" "+USERNAME2)
    else:
        win.fill((246, 114, 128))
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
                
        # p.move()
        redrawWindow(win)


main()
