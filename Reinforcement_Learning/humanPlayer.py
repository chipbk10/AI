
from player import *
from tictactoe import *

class Human(Player):
                                
    def nextMove(self, game):        
        move = input(f"Player {game.currentPlayer}'s turn. Enter row and column (e.g. 0 0): ")
        move = tuple(map(int, move.split()))
        return move