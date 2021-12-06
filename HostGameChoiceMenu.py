import pygame

class GameMenu:
    def __init__(self, screen, running, player):
        self.screen = screen
        self.running = running
        self.player = player
        self.score = self.player.score
        self.backgroudcolor= (168,230,206)
        while(self.running):
            self.screen.fill(self.backgroudcolor)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
            pygame.display.update()