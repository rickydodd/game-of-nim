from random import randint

class Piles:
    def __init__(self):
        self.__data = []
        self.__numberOfPiles = 0
        self.__totalItems = 0
        self.__constructPiles()
        self.__generateItems()
    
    def __constructPiles(self):
        # appends 2-5 (inclusive) piles to self.__data, each pile is
        # therefore represented as a sublist of self.__data
        for n in range(0, randint(2, 5)):
            self.__data.append([])
            self.__numberOfPiles += 1
    
    def __generateItems(self):
        # generates the items and distributed them as evenly as possible
        # could easily be altered to distribute randomly, but may result
        # in some piles being under-utilized or not utilized at all
        tracker = 0
        for n in range(0, 2*self.__numberOfPiles+1):
            if tracker >= self.__numberOfPiles:
                tracker = 0
            self.__data[tracker].append("*")
            self.__totalItems += 1
            tracker += 1

    def __isEnoughItems(self, move):
        # takes a tuple move, in the form (pileIndex, numberToRemove)
        # returns true if it doesn't result in the pile having a negative
        # number of items. Returns false otherwise.
        pileIndex, numberToRemove = move
        if self.numberOfItems(pileIndex) - numberToRemove >= 0:
            return True
        return False

    def getNumberOfPiles(self):
        return self.__numberOfPiles

    def getTotalItems(self):
        return self.__totalItems

    def numberOfItems(self, pileIndex):
        return len(self.__data[pileIndex])

    def removeItems(self, move):
        pileIndex, numberToRemove = move
        if self.__isEnoughItems(move):
            for n in range(0, numberToRemove):
                self.__data[pileIndex].pop()
                self.__totalItems -= 1

    def addItems(self, move):
        pileIndex, numberToAdd = move
        for n in range(0, numberToAdd):
            self.__data[pileIndex].append("*")
            self.__totalItems += 1

    def print(self):
        for pile in range(0, self.__numberOfPiles):
            print(pile, end=": ")
            for item in range(0, self.numberOfItems(pile)):
                print(self.__data[pile][item], end="")
            print()

    def getPiles(self):
        return self.__data