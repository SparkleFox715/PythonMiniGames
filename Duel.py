import pygame
class duel:
    def __init__(self, P1, P2):
        pygame.init()
        #self.clock = pygame.time.Clock()
        self.currentTime = 0
        self.P1 =P1
        self.P2 = P2
        self.winner = ""
        self.P1Health = 3
        self.P2Health =3
        self.P1Ammo = 0
        self.P2Ammo = 6
        self.P1Loc = [400,400]
        self.P2Loc = [400,400]
    def resetTime(self):
        self.currentTime=0
    def incAmmo(self, number):
        if number ==1:
            self.P1Ammo = (self.P1Ammo)%6+1
        elif number ==2:
            self.P2Ammo = (self.P2Ammo)%6+1
    def assignTime(self):
        self.currentTime = pygame.time.get_ticks()%1000000000
    def getP1Loc(self):
        return self.P1Loc
    def getP2Loc(self):
        return self.P2Loc
    #getCurrentTime
    def getTime(self): 
        return pygame.time.get_ticks()%1000000000
    #movement
    def moveLeft(self, num):
        if num==1:
            if self.P1Loc[0]>0:
                self.P1Loc[0] = self.P1Loc[0]-5
        elif num==2:
            if self.P2Loc[0]>0:
                self.P2Loc[0] = self.P2Loc[0]-5
    def moveUp(self, num):
        if num==1:
            if self.P1Loc[1]>0:
                self.P1Loc[1] = self.P1Loc[1]-5
        elif num==2:
            if self.P2Loc[1]>0:
                self.P2Loc[1] = self.P2Loc[1]-5
    def moveRight(self, num):
        if num==1:
            if self.P1Loc[0]<800:
                self.P1Loc[0] = self.P1Loc[0]+5
        elif num==2:
            if self.P2Loc[0]<800:
                self.P2Loc[0] = self.P2Loc[0]+5
    def moveDown(self, num):
        if num==1:
            if self.P1Loc[1]<800:
                self.P1Loc[1] = self.P1Loc[1]+5
        elif num==2:
            if self.P2Loc[1]<800:
                self.P2Loc[1] = self.P2Loc[1]+5