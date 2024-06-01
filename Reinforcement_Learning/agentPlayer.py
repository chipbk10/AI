
from player import *
from tictactoe import *
from agent import QLearningAgent

class AgentPlayer(Player):
    
    def __init__(self, agent):        
        self.agent = agent
    
    def nextMove(self, game):
        state = game.board
        availableMoves = game.availableMoves()
        return self.agent.chooseAction(state, availableMoves) 