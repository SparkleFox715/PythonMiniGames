class tictac:
    def __init__(self, P1, P2):
        self.board = [["","",""],["","",""],["","",""]]
        self.P1 = P1
        self.P2 = P2
        self.winner = ""
    def getWinner(self):
        if self.winner == "":
            return None
        else:
            return self.winner
    def getBoard(self):
        return self.board
    def place(self, row, col, player):
        if self.board[row][col]=="":
            if player ==1:
                self.board[row][col] = "X"
            elif player ==2:
                self.board[row][col] ="O"
            return "True"
        else:
            return "False"
    def checkWin(self):
        if self.board[0][0]=="X" and self.board[1][0]=="X" and self.board[2][0]=="X":
            self.winner = "P1"
        elif self.board[0][1]=="X" and self.board[1][1]=="X" and self.board[2][1]=="X":
            self.winner = "P1"
        elif self.board[0][2]=="X" and self.board[1][2]=="X" and self.board[2][2]=="X":
            self.winner = "P1"
        elif self.board[0][0]=="X" and self.board[0][1]=="X" and self.board[0][2]=="X":
            self.winner = "P1"
        elif self.board[1][0]=="X" and self.board[1][1]=="X" and self.board[1][2]=="X":
            self.winner = "P1"
        elif self.board[2][0]=="X" and self.board[2][1]=="X" and self.board[2][2]=="X":
            self.winner = "P1"
        elif self.board[0][0]=="X" and self.board[1][1]=="X" and self.board[2][2]=="X":
            self.winner = "P1"
        elif self.board[0][2]=="X" and self.board[1][1]=="X" and self.board[2][0]=="X":
            self.winner = "P1"
        

        if self.board[0][0]=="O" and self.board[1][0]=="O" and self.board[2][0]=="O":
            self.winner = "P2"
        elif self.board[0][1]=="O" and self.board[1][1]=="O" and self.board[2][1]=="O":
            self.winner = "P2"
        elif self.board[0][2]=="O" and self.board[1][2]=="O" and self.board[2][2]=="O":
            self.winner = "P2"
        elif self.board[0][0]=="O" and self.board[0][1]=="O" and self.board[0][2]=="O":
            self.winner = "P2"
        elif self.board[1][0]=="O" and self.board[1][1]=="O" and self.board[1][2]=="O":
            self.winner = "P2"
        elif self.board[2][0]=="O" and self.board[2][1]=="O" and self.board[2][2]=="O":
            self.winner = "P2"
        elif self.board[0][0]=="O" and self.board[1][1]=="O" and self.board[2][2]=="O":
            self.winner = "P2"
        elif self.board[0][2]=="O" and self.board[1][1]=="O" and self.board[2][0]=="O":
            self.winner = "P2"
        