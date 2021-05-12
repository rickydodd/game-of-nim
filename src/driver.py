from game import Game

if __name__ == "__main__":
    g = Game()
    state = g.initialState()
    selection = None

    while selection not in [0, 1]:
        # getting game mode selection from player
        print("GAME MODE SELECTION\nENTER NUMBER OF SELECTION\n0: Standard\n1: Misere")
        selection = int(input("Number of game mode: "))
    
    if(selection == 0):
        g.switchTurnToggle()

    while not g.isGoalState(state):
        pileIndex = 0
        itemsToRemove = 0
        move = (0, 0)

        g.piles.print()

        while move not in g.possibleMoves(state):
            # ensure move is valid (a possible move)
            pileIndex = int(input("Pile number (to remove items from): "))
            itemsToRemove = int(input("Number of items to remove: "))
            move = (pileIndex, itemsToRemove)
        
        g.piles.removeItems(move)
        state = (g.piles.getNumberOfPiles(), state[1]-move[1])
        g.switchTurnToggle()

        # opponent's move
        aiMove = g.optimalMove(state)
        if aiMove:
            state = (g.piles.getNumberOfPiles(), state[1]-aiMove[1])
            g.switchTurnToggle()
    
    if g.getTurnToggle():
        print("You won!")
    else:
        print("You lost.")