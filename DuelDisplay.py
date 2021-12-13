import pygame
import time
class DuelGame:
    def __init__(self,screen, running, network, player):
        self.screen = screen
        self.running = running
        self.network = network
        self.player = player
        self.backgroundcolor = (0,0,0)
        self.p1color = (237, 27,118)
        self.p2color = (3,122,118)
        self.p1textcolor = (244,71,134)
        self.p2textcolor = (36, 159,156)
        self.game = None
        self.winner = None
        self.text = None
        while(self.running):
            try:
                self.game = network.send("getGame")
                self.winner = self.game.tic.getWinner()
                if self.game.getState ==1:
                    break
            except:
                pass
            #display username
            self.screen.fill(self.backgroundcolor)
            font = pygame.font.Font('gillsans.ttf', 32)
            if self.player.number==1:
                self.text = font.render(self.player.username, True, self.p1textcolor)
            elif self.player.number==2:
                self.text= font.render(self.player.username, True, self.p2textcolor)
            textRect = self.text.get_rect()
            textRect.center = (400,785)
            screen.blit(self.text, textRect)
            #display player objects
            if self.player.number==1:
                #draw own character
                pygame.draw.polygon(self.screen,self.p1color, [(self.game.du.getP1Loc()[0]-40,self.game.du.getP1Loc()[1]), (self.game.du.getP1Loc()[0], self.game.du.getP1Loc()[1]-50), (self.game.du.getP1Loc()[0]+40, self.game.du.getP1Loc()[1]), (self.game.du.getP1Loc()[0], self.game.du.getP1Loc()[1]+50)])
                pygame.draw.polygon(self.screen,self.p1color, [(self.game.du.getP1Loc()[0],self.game.du.getP1Loc()[1]-40), (self.game.du.getP1Loc()[0]-50, self.game.du.getP1Loc()[1]), (self.game.du.getP1Loc()[0], self.game.du.getP1Loc()[1]+40), (self.game.du.getP1Loc()[0]+50, self.game.du.getP1Loc()[1])])
                pygame.draw.polygon(self.screen,(255,255,255), [(self.game.du.getP1Loc()[0]-40,self.game.du.getP1Loc()[1]), (self.game.du.getP1Loc()[0], self.game.du.getP1Loc()[1]-50), (self.game.du.getP1Loc()[0]+40, self.game.du.getP1Loc()[1]), (self.game.du.getP1Loc()[0], self.game.du.getP1Loc()[1]+50)], width =3)
                pygame.draw.polygon(self.screen,(255,255,255), [(self.game.du.getP1Loc()[0],self.game.du.getP1Loc()[1]-40), (self.game.du.getP1Loc()[0]-50, self.game.du.getP1Loc()[1]), (self.game.du.getP1Loc()[0], self.game.du.getP1Loc()[1]+40), (self.game.du.getP1Loc()[0]+50, self.game.du.getP1Loc()[1])], width = 3)

                #draw opponent indicator
                pygame.draw.polygon(self.screen, self.p2color, [(self.game.du.getP2Loc()[0], 30),(self.game.du.getP2Loc()[0]+10, 35),(self.game.du.getP2Loc()[0], 10),(self.game.du.getP2Loc()[0]-10, 35)])
            elif self.player.number==2:
                pass

            #keybinds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_a:
                        self.network.send("DuelP"+str(self.player.number)+" Left")
                    if event.key==pygame.K_w:
                        self.network.send("DuelP"+str(self.player.number)+" Up")
                    if event.key == pygame.K_s:
                        self.network.send("DuelP"+str(self.player.number)+" Down")
                    if event.key==pygame.K_d:
                        self.network.send("DuelP"+str(self.player.number)+" Right")

            #endgame
            if not self.winner==None:
                    self.running = False
                    try:
                        self.game = network.send("getGame")
                    except:
                        pass
                    temp = ""
                    if self.winner == "P1" and self.player.number ==1:
                        temp  = "You Won!"
                        network.send("Inc"+str(player.number))
                    elif self.winner == "P2" and self.player.number ==2:
                        temp = "You Won!"
                        network.send("Inc"+str(player.number))
                    elif self.winner =="Tie":
                        temp = "Tie"
                    else:
                        temp = "You Lost..."
                    font = pygame.font.Font('gillsans.ttf', 50)
                    text = font.render(temp, True, (255,255,255))
                    textRect = text.get_rect()
                    textRect.center = (400,400)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    time.sleep(2)
                    self.network.send("Begin")
            pygame.display.update()
