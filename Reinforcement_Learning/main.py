from train import *
from agentPlayer import *
from agent import QLearningAgent
from humanPlayer import *

numEpisodes = 1000
epsilon = 0.1
alpha = 0.5
discountFactor = 1.0

agent = train(numEpisodes, epsilon, alpha, discountFactor)
agentPlayer = AgentPlayer(agent)
human = Human()

player1 = human
# player2 = human
player2 = agentPlayer 

for _ in range(100):
    game = TicTacToe(players=[player1, player2], board=np.zeros((3,3)))
    game.printBoard()
    game.play()

