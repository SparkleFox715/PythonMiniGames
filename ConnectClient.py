import time
import pygame
import PlayerInfo
import ConnectMainMenu
from network import Network
time.sleep(1)
n = Network()
n.send("P2 Connected")
pygame.init()
width = 800
height = 800
win = pygame.display.set_mode((width, height))
clientNumber = 0
GameScreen = 0
m = ConnectMainMenu.Menu(win, False,n)
Player =PlayerInfo.player("")
USERNAME = ""
def redrawWindow(win):
    # player.draw(win)
    global GameScreen
    global Player
    global m
    global USERNAME
    if GameScreen == 0:
        m = ConnectMainMenu.Menu(win, True, n)
        GameScreen+=1
        Player = PlayerInfo.player(m.username)
        USERNAME = Player.username
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