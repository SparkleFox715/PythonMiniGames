import time
import pygame
import PlayerInfo
import ConnectMainMenu
import ConnectGameChoiceMenu
from TicTacToeDisplay import TicTacGame
from network import Network
time.sleep(0.5)
n = Network()
pygame.init()
width = 800
height = 800
win = pygame.display.set_mode((width, height))
clientNumber = 0
GameScreen = 0
Player2 = PlayerInfo.player("",2)
m = ConnectMainMenu.Menu(win, False,n, "")
def redrawWindow(win, game):
    # player.draw(win)
    global GameScreen
    global Player2
    global m
    if GameScreen == 0:
        m = ConnectMainMenu.Menu(win, True, n, game)
        Player2 = PlayerInfo.player(m.username, 2)
    if GameScreen ==1:
        win.fill((0,0,0))
        m = ConnectGameChoiceMenu.GameMenu(win, True, Player2, n)
    if GameScreen ==2:
        win.fill((0,0,0))
        m = TicTacGame(win, True, n, Player2)
    pygame.display.update()


def main():
    global GameScreen
    global Player2
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        try:
            game = n.send("getGame")
            Player2 = game.getPlayer2()
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