class duel:
    def __init__(self, P1, P2):
        self.P1 =P1
        self.P2 = P2
        self.winner = ""
        self.P1Health = 3
        self.P2Health =3
        self.P1Ammo = 6
        self.P2Ammo = 6
        self.P1Loc = [400,400]
        self.P2Loc = [400,400]
    def getP1Loc(self):
        return self.P1Loc
    def getP2Loc(self):
        return self.P2Loc

    #movement
    def moveLeft(self, num):
        if num==1:
            self.P1Loc[0] = self.P1Loc[0]-5
        elif num==2:
            self.P2Loc[0] = self.P2Loc[0]-5
    def moveUp(self, num):
        if num==1:
            self.P1Loc[1] = self.P1Loc[1]-5
        elif num==2:
            self.P2Loc[1] = self.P2Loc[1]-5
    def moveRight(self, num):
        if num==1:
            self.P1Loc[0] = self.P1Loc[0]+5
        elif num==2:
            self.P2Loc[0] = self.P2Loc[0]+5
    def moveDown(self, num):
        if num==1:
            self.P1Loc[1] = self.P1Loc[1]+5
        elif num==2:
            self.P2Loc[1] = self.P2Loc[1]+5