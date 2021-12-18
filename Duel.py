import pygame
class duel:
    def __init__(self, P1, P2):
        pygame.init()
        #self.clock = pygame.time.Clock()
        self.currentTime1 = 0
        self.currentTime2 = 0
        self.P1 =P1
        self.P2 = P2
        self.winner = ""
        self.P1Health = 100
        self.P2Health =100
        self.P1Ammo = 0
        self.P2Ammo = 0
        self.P1Loc = [400,400]
        self.P2Loc = [400,400]
    
    #deciding winner
    def getWinner(self):
        if self.P1Health<=0:
            return "P2"
        elif self.P2Health <=0:
            return "P1"
        return None

    #increase ammo
    def incAmmo(self, number):
        if number ==1:
            self.P1Ammo = (self.P1Ammo)%6+1
        elif number ==2:
            self.P2Ammo = (self.P2Ammo)%6+1

    #locations
    def getP1Loc(self):
        return self.P1Loc
    def getP2Loc(self):
        return self.P2Loc

    #getCurrentTime
    def getTime(self): 
        return pygame.time.get_ticks()%1000000000
    def resetTime(self, num):
        if num==1:
            self.currentTime1 = 0
        elif num==2:
            self.currentTime2=0
    def assignTime(self, num):
        if num ==1:
            self.currentTime1 = pygame.time.get_ticks()%1000000000
        elif num==2:
            self.currentTime2 = pygame.time.get_ticks()%1000000000

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


   