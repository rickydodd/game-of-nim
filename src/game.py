from piles import Piles

class Game:
    def __init__(self):
        self.piles = Piles()
        self.__possibleGameModes = ["standard", "misere"]
        self.__selectedGameMode = self.__possibleGameModes[0]
        self.__turnToggle = True

    def initialState(self):
        return (self.piles.getNumberOfPiles(), self.piles.getTotalItems())

    def isGoalState(self, state):
        if state == (self.piles.getNumberOfPiles(), 0):
            return True
        return False

    def getGameMode(self):
        return self.__selectedGameMode()

    def getTurnToggle(self):
        return self.__turnToggle
    
    def switchTurnToggle(self):
        self.__turnToggle = not self.__turnToggle

    def possibleMoves(self, state):
        # returns a list of tuples containing the pile index and the number that could be removed at a given state
        moves = []
        if state[1] >= 1:
            indexOfPile  = 0
            numberInPile = 0
            for pile in self.piles.getPiles():
                for item in pile:
                    numberInPile += 1
                    moves.append((indexOfPile, numberInPile))
                indexOfPile += 1
                numberInPile = 0
        return moves

    def optimalMove(self, state):
        bestValue = float('-inf')
        optimalMove = None

        for move in self.possibleMoves(state):
            self.piles.removeItems(move)
            value = self.minimax(state, False)
            self.piles.addItems(move)
            if value > bestValue:
                bestValue = value
                optimalMove = move
        
        if optimalMove:
            self.piles.removeItems(optimalMove)
        return optimalMove

    def minimax(self, state, isMaximizing):
        # recursive minimax

        possibleMoves = self.possibleMoves(state)
        # storing the possible moves at the given state

        if not possibleMoves:
            # base case
            # if there are no possible moves (therefore a terminal node)
            if isMaximizing:
                # heuristic value of 1, node terminates on max
                return 1
            else:
                # heuristic value of -1, node terminates on min
                return -1
        
        if isMaximizing:
            bestValue = float('-inf')
            for move in possibleMoves:
                self.piles.removeItems(move)
                value = max(bestValue, self.minimax(move, False))
                self.piles.addItems(move)
        else:
            # else if minimizing
            bestValue = float('+inf')
            for move in possibleMoves:
                self.piles.removeItems(move)
                value = min(bestValue, self.minimax(move, True))
                self.piles.addItems(move)
        return value
