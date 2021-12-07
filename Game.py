class game:
    def __init__(self, player1, player2):
        self.state = 0
        self.player1 = player1
        self.player2 = player2
    def getState(self):
        return self.state
    def setState(self, ST):
        if ST=="GamesMenu":
            self.state = 1
        else:
            self.state = 0
    def getPlayer1(self):
        return self.player1
    def getPlayer2(self):
        return self.player2