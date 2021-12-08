import pygame
class TicTacGame:
    def __init__(self, screen, running, network, player):
        self.screen = screen
        self.running =  running
        self.network  = network
        self.player = player
        self.backgroundcolor = (246,171,182)
        self.Xlettercolor = (5, 30, 62)
        self.Olettercolor = (133, 30, 62)
        self.textcolor = (30, 31, 38)
        self.linecolor = (0,0,0)
        self.board = None
        while(self.running):
            game = None
            try:
                game = network.send("getGame")
                self.board = game.tic.getBoard()
                if game.getState ==1:
                    break
            except:
                pass
            self.screen.fill(self.backgroundcolor)
            font = pygame.font.Font('gillsans.ttf', 32)
            text = font.render(player.username, True, self.textcolor)
            textRect = text.get_rect()
            textRect.center = (400,15)
            screen.blit(text, textRect)

            pygame.draw.line(self.screen, self.linecolor, (300,100), (300,700), 10)
            pygame.draw.line(self.screen, self.linecolor, (500,100), (500,700), 10)
            pygame.draw.line(self.screen, self.linecolor, (100,300), (700,300), 10)
            pygame.draw.line(self.screen, self.linecolor, (100,500), (700,500), 10)

            tile00 =pygame.Rect(100, 100, 200, 200)
            tile10 =pygame.Rect(300, 100, 200, 200)
            tile20 =pygame.Rect(500, 100, 200, 200)
            tile01 =pygame.Rect(100, 300, 200, 200)
            tile11 =pygame.Rect(300, 300, 200, 200)
            tile21 =pygame.Rect(500, 300, 200, 200)
            tile02 =pygame.Rect(100, 500, 200, 200)
            tile12 =pygame.Rect(300, 500, 200, 200)
            tile22 =pygame.Rect(500, 500, 200, 200)
            # pygame.draw.rect(self.screen, self.Xlettercolor, tile21)
            
            for a in range(3):
                for b in range(3):
                    if self.board[a][b] == "X":
                        pygame.draw.line(self.screen, self.Xlettercolor, ((a*200)+130, (b*200)+130), (((a+1)*200+80),((b+1)*200+80)), 25)
                        pygame.draw.line(self.screen, self.Xlettercolor, (((a+1)*200+80), (b*200)+130), ((a*200)+130,((b+1)*200+80)), 25)
                    elif self.board[a][b]=="O":
                        pass
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                    if tile00.collidepoint(event.pos):
                        possible =network.send("place "+str(player.number)+" 0 0")

            pygame.display.update()