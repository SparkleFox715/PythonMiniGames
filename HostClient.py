import pygame
import MainMenu
import PlayerInfo
import socket
import os
pygame.init()
width = 800
height = 800
win = pygame.display.set_mode((width, height))
os.system("start cmd /k python server.py") 
os.system("start cmd /k python network.py") 

clientNumber = 0
GameScreen = 0
m = MainMenu.Menu(win, False)
Player =PlayerInfo.player("")
class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        self.rect = (self.x, self.y, self.width, self.height)


def redrawWindow(win, player):
    # player.draw(win)
    global GameScreen
    global Player
    global m
    if GameScreen == 0:
        m = MainMenu.Menu(win, True)
        GameScreen+=1
        Player = PlayerInfo.player(m.username)
    else:
        win.fill((246, 114, 128))
    pygame.display.update()


def main():
    run = True
    p = Player(50, 50, 100, 100, (0, 255, 0))
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
                
        # p.move()
        redrawWindow(win, p)


main()