import pygame

class GameMenu:
    def __init__(self, screen, running, player, network):
        self.screen = screen
        self.running = running
        self.player = player
        self.score = self.player.score
        self.network = network
        self.backgroudcolor= (168,230,206)
        self.buttoncolor =(255,211,181)
        self.buttontextcolor = (255,170,166)
        self.textcolor = (205,236,194)
        while(self.running):
            game = ""
            try:
                game = network.send("getGame")
            except:
                pass
            self.screen.fill(self.backgroudcolor)
            font = pygame.font.Font('gillsans.ttf', 32)
            text = font.render(player.username, True, self.textcolor)
            textRect = text.get_rect()
            textRect.center = (400,15)
            screen.blit(text, textRect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
            pygame.display.update()