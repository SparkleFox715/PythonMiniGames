import pygame
import time
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
        self.winner = None
        self.game = None
        while(self.running):
            try:
                self.game = network.send("getGame")
                self.winner = self.game.tic.getWinner()
                self.board = self.game.tic.getBoard()
                if self.game.getState ==1:
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
                        pygame.draw.circle(self.screen, self.Olettercolor, ((a*200)+200, (b*200)+200), 75, width=25)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                if self.player.number-1 == self.game.tic.getTurn():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                        if tile00.collidepoint(event.pos):
                            possible =network.send("place "+str(player.number)+" 0 0")
                        if tile01.collidepoint(event.pos):
                            possible =network.send("place "+str(player.number)+" 0 1")
                        if tile02.collidepoint(event.pos):
                            possible =network.send("place "+str(player.number)+" 0 2")
                        if tile10.collidepoint(event.pos):
                            possible =network.send("place "+str(player.number)+" 1 0")
                        if tile11.collidepoint(event.pos):
                            possible =network.send("place "+str(player.number)+" 1 1")
                        if tile12.collidepoint(event.pos):
                            possible =network.send("place "+str(player.number)+" 1 2")
                        if tile20.collidepoint(event.pos):
                            possible =network.send("place "+str(player.number)+" 2 0")
                        if tile21.collidepoint(event.pos):
                            possible =network.send("place "+str(player.number)+" 2 1")
                        if tile22.collidepoint(event.pos):
                            possible =network.send("place "+str(player.number)+" 2 2")
                        
            if not self.winner==None:
                self.running = False
                try:
                    self.game = network.send("getGame")
                except:
                    pass
                temp = ""
                if self.winner == "P1" and self.player.number ==1:
                    temp  = "You Won!"
                elif self.winner == "P2" and self.player.number ==2:
                    temp = "You Won!"
                else:
                    temp = "You Lost..."
                font = pygame.font.Font('gillsans.ttf', 50)
                text = font.render(temp, True, self.textcolor)
                textRect = text.get_rect()
                textRect.center = (400,400)
                screen.blit(text, textRect)
                pygame.display.update()
                time.sleep(2)
                self.network.send("Begin")
            pygame.display.update()
        # for x in range(10000000):

       
        # self.game.setState("GamesMenu")
        
            