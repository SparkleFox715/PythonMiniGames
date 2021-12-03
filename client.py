import pygame
import MainMenu

pygame.init()
width = 800
height = 800
win = pygame.display.set_mode((width, height))

clientNumber = 0
GameScreen = 0
m = MainMenu.Menu(win, False)

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
    if GameScreen == 0:
        win.fill((246, 114, 128))
        m = MainMenu.Menu(win, True)
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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if m.outsideX < pygame.mouse.get_pos()[0] < m.outsideX+m.outsideWidth and m.b1OutsideY<pygame.mouse.get_pos()[1] < m.b1OutsideY+m.outsideHeight:
                    print("begin")
                elif m.outsideX < pygame.mouse.get_pos()[0] < m.outsideX+m.outsideWidth and m.b2OutsideY<pygame.mouse.get_pos()[1] < m.b2OutsideY+m.outsideHeight:
                    run = False
                    pygame.quit()
        # p.move()
        redrawWindow(win, p)


main()
