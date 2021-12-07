class game:
    def __init__(self):
        self.state = 0
    def getState(self):
        return self.state
    def setState(self, ST):
        if ST=="GamesMenu":
            self.state = 1
        else:
            self.state = 0