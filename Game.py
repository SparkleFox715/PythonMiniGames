from TicTacToe import tictac
from Duel import duel
class game:
    def __init__(self, player1, player2):
        self.state = 0
        self.player1 = player1
        self.player2 = player2
        self.tic = None
        self.du = None
    def getState(self):
        return self.state
    def setState(self, ST):
        if ST=="GamesMenu":
            self.state = 1
        elif ST == "TicTacToe":
            self.state = 2
        elif ST =="Duel":
            self.state =3
        else:
            self.state = 0
    def getPlayer1(self):
        return self.player1
    def getPlayer2(self):
        return self.player2
    
    def startTicTacToe(self):
        self.tic = tictac(self.player1, self.player2)
    def getTicTacToe(self):
        return self.tic
    
    def startDuelGame(self):
        self.du = duel(self.player1, self.player2)
    def getDuel(self):
        return self.du