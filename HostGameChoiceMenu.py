import pygame

class GameMenu:
    def __init__(self, screen, running, player, network):
        self.screen = screen
        self.running = running
        self.player = player
        self.score = self.player.score
        self.network = network
        self.backgroudcolor= (47,31,43)
        self.buttoncolor =(255,211,181)
        self.buttontextcolor = (255,140,148)
        self.textcolor = (205,236,194)
        while(self.running):
            game = None
            game = network.send("getGame")
            try:
                if not game.getState()==1:
                    break
            except:
                pass
            self.screen.fill(self.backgroudcolor)
            font = pygame.font.Font('gillsans.ttf', 32)
            text = font.render(player.username+" "+str(player.score), True, self.textcolor)
            textRect = text.get_rect()
            textRect.center = (400,15)
            screen.blit(text, textRect)

            font = pygame.font.Font('gillsans.ttf', 30)

            tile1 = pygame.Rect(20, 60,355, 180)
            tile1a = pygame.Rect(10,50,375,200)
            pygame.draw.rect(self.screen, self.buttoncolor, tile1)
            pygame.draw.rect(self.screen, self.buttoncolor, tile1a, 10, 10)
            text = font.render("Tic-Tac-Toe", True, self.buttontextcolor)
            textRect = text.get_rect()
            textRect.center = (197, 150)
            screen.blit(text, textRect)

            tile2 = pygame.Rect(20, 310,355,180)
            tile2a = pygame.Rect(10,300,375,200)
            pygame.draw.rect(self.screen, self.buttoncolor, tile2)
            pygame.draw.rect(self.screen, self.buttoncolor, tile2a, 10, 10)
            text = font.render("Game2", True, self.buttontextcolor)
            textRect = text.get_rect()
            textRect.center = (197, 400)
            screen.blit(text, textRect)

            tile3 = pygame.Rect(20, 560,355, 180)
            tile3a = pygame.Rect(10,550,375,200)
            pygame.draw.rect(self.screen, self.buttoncolor, tile3)
            pygame.draw.rect(self.screen, self.buttoncolor, tile3a, 10, 10)
            text = font.render("Game3", True, self.buttontextcolor)
            textRect = text.get_rect()
            textRect.center = (197, 650)
            screen.blit(text, textRect)

            tile4 = pygame.Rect(425, 60,355, 180)
            tile4a = pygame.Rect(415,50,375,200)
            pygame.draw.rect(self.screen, self.buttoncolor, tile4)
            pygame.draw.rect(self.screen, self.buttoncolor, tile4a, 10, 10)
            text = font.render("Game4", True, self.buttontextcolor)
            textRect = text.get_rect()
            textRect.center = (602, 150)
            screen.blit(text, textRect)

            tile5 = pygame.Rect(425, 310,355, 180)
            tile5a = pygame.Rect(415,300,375,200)
            pygame.draw.rect(self.screen, self.buttoncolor, tile5)
            pygame.draw.rect(self.screen, self.buttoncolor, tile5a, 10, 10)
            text = font.render("Game5", True, self.buttontextcolor)
            textRect = text.get_rect()
            textRect.center = (602, 400)
            screen.blit(text, textRect)

            tile6 = pygame.Rect(425, 560,355, 180)
            tile6a = pygame.Rect(415,550,375,200)
            pygame.draw.rect(self.screen, self.buttoncolor, tile6)
            pygame.draw.rect(self.screen, self.buttoncolor, tile6a, 10, 10)
            text = font.render("Game6", True, self.buttontextcolor)
            textRect = text.get_rect()
            textRect.center = (602, 650)
            screen.blit(text, textRect)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                        if tile1.collidepoint(event.pos):
                            self.network.send("TicTacToe")
                        elif tile2.collidepoint(event.pos):
                            pass
                        elif tile3.collidepoint(event.pos):
                            pass
                        elif tile4.collidepoint(event.pos):
                            pass
                        elif tile5.collidepoint(event.pos):
                            pass
                        elif tile6.collidepoint(event.pos):
                            pass
            pygame.display.update()