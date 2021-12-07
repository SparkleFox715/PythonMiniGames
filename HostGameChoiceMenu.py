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

            tile1 = pygame.Rect(20, 60,355, 180)
            tile1a = pygame.Rect(10,50,375,200)
            pygame.draw.rect(self.screen, self.buttoncolor, tile1)
            pygame.draw.rect(self.screen, self.buttoncolor, tile1a, 10, 10)
            tile2 = pygame.Rect(20, 310,355,180)
            tile2a = pygame.Rect(10,300,375,200)
            pygame.draw.rect(self.screen, self.buttoncolor, tile2)
            pygame.draw.rect(self.screen, self.buttoncolor, tile2a, 10, 10)
            tile3 = pygame.Rect(20, 560,355, 180)
            tile3a = pygame.Rect(10,550,375,200)
            pygame.draw.rect(self.screen, self.buttoncolor, tile3)
            pygame.draw.rect(self.screen, self.buttoncolor, tile3a, 10, 10)
            tile4 = pygame.Rect(100, 100,40, 40)
            tile4a = pygame.Rect(415,50,375,200)
            pygame.draw.rect(self.screen, self.buttoncolor, tile4)
            pygame.draw.rect(self.screen, self.buttoncolor, tile4a, 10, 10)
            tile5 = pygame.Rect(100, 100,40, 40)
            tile5a = pygame.Rect(415,300,375,200)
            pygame.draw.rect(self.screen, self.buttoncolor, tile5)
            pygame.draw.rect(self.screen, self.buttoncolor, tile5a, 10, 10)
            tile6 = pygame.Rect(100, 100,40, 40)
            tile6a = pygame.Rect(415,550,375,200)
            pygame.draw.rect(self.screen, self.buttoncolor, tile6)
            pygame.draw.rect(self.screen, self.buttoncolor, tile6a, 10, 10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                        pass
                
            pygame.display.update()