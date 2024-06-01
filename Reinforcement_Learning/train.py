from agent import *
from tictactoe import *

def train(numEpisodes, epsilon, alpha, discountFactor):
    agent = QLearningAgent(epsilon, alpha, discountFactor)
        
    for i in range(numEpisodes):
        game = TicTacToe([agent, agent], np.zeros((3,3)))
        state = game.board
        
        while not game.isOver():
            
            # choose an action
            availableMoves = game.availableMoves()
            action = agent.chooseAction(state, availableMoves)
            
            # get the state and reward
            (nextState, reward) = game.move(action)            
            # game.printBoard()
            
            # agent learn the environment
            nextAvailableMoves = TicTacToe(players=[], board=nextState).availableMoves()            
            agent.updateQValue(state, action, reward, nextState, nextAvailableMoves)
            state = nextState

        print("game is over")        
        
    return agent
    