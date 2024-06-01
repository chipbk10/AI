import random
from tictactoe import *

class QLearningAgent:
    
    def __init__(self, epsilon, alpha, discountFactor):
        self.Q = {} # (state, action) -> reward
        self.alpha = alpha
        self.discountFactor = discountFactor
        self.epsilon = epsilon
    
    def chooseAction(self, state, availableMoves):
        
        # exploration: choose random action
        if random.uniform(0, 1) < self.epsilon:
            # print("exploration....")                    
            return random.choice(availableMoves)
        
        # exploitation: choose the best action
        else:
            # print("exploitation ....")
            QValues = [self.getQValue(state, action) for action in availableMoves]
            print(f"QValues = {QValues}")
            
            maxQ = max(QValues)
            if maxQ != 0: print(f"maxQ = {maxQ}")
            
            if QValues.count(maxQ) > 1:
                best_moves = [i for i in range(len(QValues)) if QValues[i] == maxQ]
                i = random.choice(best_moves)
            else:
                i = QValues.index(maxQ)
            return availableMoves[i]
    
    def getQValue(self, state, action):
        key = self.key(state, action)
        if key not in self.Q:
            self.Q[key] = 0.0
        return self.Q[key]
    
    def updateQValue(self, state, action, reward, nextState, nextAvailableMoves):
        nextQValues = []
        for nextAction in nextAvailableMoves:
            nextQValues.append(self.getQValue(nextState, nextAction))
        # print(f"nextQValues = {nextQValues}")
        
        maxNextQValue = max(nextQValues) if nextQValues else 0.0
        self.getQValue(state, action)
        
        #if reward != 0:
        #    print(f"reward = {reward}, alpha = {self.alpha}, discountFactor = {self.discountFactor}, maxNextQValue = {maxNextQValue}")
        
        key = self.key(state, action)
        self.Q[key] += self.alpha * (reward + self.discountFactor * maxNextQValue - self.Q[key])
        # if reward != 0:
        #    print(f"{state}")
        #    print(f"self.Q[(str(state), action)] = {self.Q[(str(state), action)]}")
        
    def key(self, state, action):
        s = ""
        for i in range(3):
            for j in range(3):
                s += str(state[i][j])                
        (i, j, p) = action
        s += "-" + str(i) + "-" + str(j) + "-" + str(p)