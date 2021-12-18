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
        self.pressedLeft= False
        self.pressedRight = False
        self.pressedUp = False
        self.pressedDown = False
        while(self.running):
            try:
                self.game = network.send("getGame")
                self.winner = self.game.du.getWinner()
                if self.game.getState ==1:
                    break
            except:
                pass
            if self.game ==None:
                continue
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
                 #draw own character
                pygame.draw.polygon(self.screen,self.p2color, [(self.game.du.getP2Loc()[0]-40,self.game.du.getP2Loc()[1]), (self.game.du.getP2Loc()[0], self.game.du.getP2Loc()[1]-50), (self.game.du.getP2Loc()[0]+40, self.game.du.getP2Loc()[1]), (self.game.du.getP2Loc()[0], self.game.du.getP2Loc()[1]+50)])
                pygame.draw.polygon(self.screen,self.p2color, [(self.game.du.getP2Loc()[0],self.game.du.getP2Loc()[1]-40), (self.game.du.getP2Loc()[0]-50, self.game.du.getP2Loc()[1]), (self.game.du.getP2Loc()[0], self.game.du.getP2Loc()[1]+40), (self.game.du.getP2Loc()[0]+50, self.game.du.getP2Loc()[1])])
                pygame.draw.polygon(self.screen,(255,255,255), [(self.game.du.getP2Loc()[0]-40,self.game.du.getP2Loc()[1]), (self.game.du.getP2Loc()[0], self.game.du.getP2Loc()[1]-50), (self.game.du.getP2Loc()[0]+40, self.game.du.getP2Loc()[1]), (self.game.du.getP2Loc()[0], self.game.du.getP2Loc()[1]+50)], width =3)
                pygame.draw.polygon(self.screen,(255,255,255), [(self.game.du.getP2Loc()[0],self.game.du.getP2Loc()[1]-40), (self.game.du.getP2Loc()[0]-50, self.game.du.getP2Loc()[1]), (self.game.du.getP2Loc()[0], self.game.du.getP2Loc()[1]+40), (self.game.du.getP2Loc()[0]+50, self.game.du.getP2Loc()[1])], width = 3)

                #draw opponent indicator
                pygame.draw.polygon(self.screen, self.p1color, [(self.game.du.getP1Loc()[0], 30),(self.game.du.getP1Loc()[0]+10, 35),(self.game.du.getP1Loc()[0], 10),(self.game.du.getP1Loc()[0]-10, 35)])
            #check ammo and display
            if player.number ==1:
                if self.game.du.P1Ammo<6 and self.game.du.currentTime1 ==0:
                    network.send("Time1")
                elif self.game.du.P1Ammo<6:
                    if self.game.du.getTime()-self.game.du.currentTime1>4000:
                        network.send("ResetTime1")
                        network.send("DuelAmmo1Inc")
                if self.game.du.P1Ammo>0:
                    pygame.draw.circle(self.screen, (255,255,255), (self.game.du.getP1Loc()[0]-47, self.game.du.getP1Loc()[1]+17), 5)
                if self.game.du.P1Ammo>1:
                    pygame.draw.circle(self.screen, (255,255,255), (self.game.du.getP1Loc()[0]-30, self.game.du.getP1Loc()[1]+30), 5)
                if self.game.du.P1Ammo>2:
                    pygame.draw.circle(self.screen, (255,255,255), (self.game.du.getP1Loc()[0]-17, self.game.du.getP1Loc()[1]+47), 5)
                if self.game.du.P1Ammo>3:
                    pygame.draw.circle(self.screen, (255,255,255), (self.game.du.getP1Loc()[0]+17, self.game.du.getP1Loc()[1]+47), 5)
                if self.game.du.P1Ammo>4:
                    pygame.draw.circle(self.screen, (255,255,255), (self.game.du.getP1Loc()[0]+30, self.game.du.getP1Loc()[1]+30), 5)
                if self.game.du.P1Ammo>5:
                    pygame.draw.circle(self.screen, (255,255,255), (self.game.du.getP1Loc()[0]+47, self.game.du.getP1Loc()[1]+17), 5)



            elif player.number==2:
                if self.game.du.P2Ammo<6 and self.game.du.currentTime2 ==0:
                    network.send("Time2")
                elif self.game.du.P2Ammo<6:
                    if self.game.du.getTime()-self.game.du.currentTime2>4000:
                        network.send("ResetTime2")
                        network.send("DuelAmmo2Inc")
                if self.game.du.P2Ammo>0:
                    pygame.draw.circle(self.screen, (255,255,255), (self.game.du.getP2Loc()[0]-47, self.game.du.getP2Loc()[1]+17), 5)
                if self.game.du.P2Ammo>1:
                    pygame.draw.circle(self.screen, (255,255,255), (self.game.du.getP2Loc()[0]-30, self.game.du.getP2Loc()[1]+30), 5)
                if self.game.du.P2Ammo>2:
                    pygame.draw.circle(self.screen, (255,255,255), (self.game.du.getP2Loc()[0]-17, self.game.du.getP2Loc()[1]+47), 5)
                if self.game.du.P2Ammo>3:
                    pygame.draw.circle(self.screen, (255,255,255), (self.game.du.getP2Loc()[0]+17, self.game.du.getP2Loc()[1]+47), 5)
                if self.game.du.P2Ammo>4:
                    pygame.draw.circle(self.screen, (255,255,255), (self.game.du.getP2Loc()[0]+30, self.game.du.getP2Loc()[1]+30), 5)
                if self.game.du.P2Ammo>5:
                    pygame.draw.circle(self.screen, (255,255,255), (self.game.du.getP2Loc()[0]+47, self.game.du.getP2Loc()[1]+17), 5)

            #keybinds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_a:
                        self.pressedLeft = True
                    if event.key==pygame.K_w:
                        self.pressedUp = True
                    if event.key == pygame.K_s:
                        self.pressedDown = True          
                    if event.key==pygame.K_d:
                        self.pressedRight = True
                if event.type ==pygame.KEYUP:
                    if event.key ==pygame.K_a:
                        self.pressedLeft = False
                    if event.key==pygame.K_w:
                        self.pressedUp = False
                    if event.key == pygame.K_s:
                        self.pressedDown = False         
                    if event.key==pygame.K_d:
                        self.pressedRight = False
            if self.pressedLeft:
                self.network.send("DuelP"+str(self.player.number)+" Left")
            if self.pressedRight:
                self.network.send("DuelP"+str(self.player.number)+" Right")
            if self.pressedUp:
                self.network.send("DuelP"+str(self.player.number)+" Up")
            if self.pressedDown:
                self.network.send("DuelP"+str(self.player.number)+" Down")

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




class Projectile:
    '''
    1-nomral
    2-1dot
    3-3dot
    4-4dot
    5-5dot
    6-6dot
    7-lazer
    8-homing
    '''
    def __init__(self, tip, ShooterNumber, game, network):
        self.type = tip
        self.shooter = ShooterNumber
        self.game = game
        self.network = network
        #assigning attributes depending on which type of projectile
        if self.type ==1:
            self.damage =10
            self.speed = 10
        elif self.type ==2:
            self.damage = 15
            self.speed = 9
        elif self.type ==3:
            self.damage = 20
            self.speed = 8
        elif self.type ==4:
            self.damage = 25
            self.speed = 7
        elif self.type ==5:
            self.damage = 30
            self.speed = 6
        elif self.type ==6:
            self.damage = 35
            self.speed = 5
        elif self.type ==7:
            self.damage = 100
            self.speed = -1
        #assiging location based on player
        if ShooterNumber==1:
            self.xLoc = self.game.du.getP1Loc()[0]
            self.yLoc = self.game.du.getP1Loc()[1]-60
        elif Shooternumber ==2:
            self.xLoc = self.game.du.getP2Loc()[0]
            self.yLoc = self.game.du.getP2Loc()[1]-60
    #changes pos of projectile
    #checks for collision and reduces health if does so. 
    def running(self):
        pass
