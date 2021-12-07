import time
import pygame
import PlayerInfo
import ConnectMainMenu
from network import Network
time.sleep(1)
n = Network()
pygame.init()
width = 800
height = 800
win = pygame.display.set_mode((width, height))
clientNumber = 0
GameScreen = 0
m = ConnectMainMenu.Menu(win, False,n, "")
def redrawWindow(win, game):
    # player.draw(win)
    global GameScreen
    global Player1
    global m
    if GameScreen == 0:
        m = ConnectMainMenu.Menu(win, True, n, game)
        GameScreen+=1
        Player1 = PlayerInfo.player(m.username)
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
        redrawWindow(win, game)


main()