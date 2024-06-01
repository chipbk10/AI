# import necessary libraries
import numpy as np
from player import Player

# mimic TicTacToe game
class TicTacToe:
    
    def __init__(self, players, board):
        self.players = [0] + players
        self.board = board
        self.currentPlayer = 1 # 1 or 2
        self.winner = None        
        self.__update()
    
    def reset(self):
        self.board = np.zeros((3, 3))
        self.currentPlayer = 1
        self.winner = None
        self.__update()

    # human vs human
    def play(self):
        action = self.players[self.currentPlayer].nextMove(self)
        self.move(action)
        self.printBoard()
        if self.isOver(): print(f"The player {self.winner} has won!")
        else: self.play()
        
    def availableMoves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0: moves.append((i, j))        
        return moves
    
    def move(self, action):
        (i, j) = action
        return self.__move(i, j)
    
    def __move(self, i, j):
        self.board[i][j] = self.currentPlayer
        x = self.currentPlayer * self.currentPlayer
        self.rows[i] += x
        self.cols[j] += x
        self.d1 += x if i==j else 0
        self.d2 += x if i==2-j else 0
        self.__checkWinner(i, j)
        result = (self.board, self.__score())        
        self.__switch()
        return result # (state, reward)
                
    def isOver(self):                        
        return self.winner or not self.availableMoves()
            
    def printBoard(self):        
        for i in range(3):
            str = ""
            for j in range(3):                
                str += self.__mark(self.board[i][j])
                str += " "                
            print(str, "\n")
        print("-------------------")
        # print(f"cols: {self.cols}")
        # print(f"rows: {self.rows}")
        
    # helper functions        
                
    def __value(self, i, j):
        return self.board[i][j] * self.board[i][j]
    
    def __score(self):
        if self.winner == 0: return 0
        if self.winner == self.currentPlayer: return 1
        else: return -1
                
    def __checkWinner(self, i, j):
        x = self.__value(i, j)
        isWin = (self.rows[i] == 3*x or self.cols[j] == 3*x or self.d1 == 3*x or self.d2 == 3*x)
        if isWin: self.winner = self.currentPlayer         
        
    def __switch(self):
        if self.currentPlayer == 1: self.currentPlayer = 2
        else: self.currentPlayer = 1
    
    def __mark(self, n):
        match n:
            case 0: return "-"
            case 1: return "X"
            case 2: return "O"
    
    def __updateRows(self):
        self.rows = []
        for i in range(3):
            sum = 0
            for j in range(3):
                sum += self.__value(i, j)
            self.rows.append(sum)
            
    def __updateCols(self):
        self.cols = []
        for j in range(3):
            sum = 0
            for i in range(3):
                sum += self.__value(i, j)
            self.cols.append(sum)
            
    def __updateDiagnols(self):
        self.d1 = 0
        self.d2 = 0
        for i in range(3):
            self.d1 += self.__value(i, i)
            self.d2 += self.__value(i, 2-i)
            
    def __update(self):
        self.__updateRows()
        self.__updateCols()
        self.__updateDiagnols()        