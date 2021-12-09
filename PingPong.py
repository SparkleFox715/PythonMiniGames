from random import randint
class Pong:
    def __init__(self, P1, P2):
        self.P1 = P1
        self.P2 = P2
        self.winner = ""
        self.turn = randint(0,1)
        self.round = 0
        self.play1score = 0
        self.play2score =0
        self.ballspeed = 0
        self.canhit = False
    def getWinner(self):
        if self.play1score==3:
            self.winner = "P1"
        elif self.play2score ==3:
            self.winner ="P2"
        else:
            self.winner = ""
        return self.winner
    