#
# Imports
#
from __future__ import print_function
from random import randint as rndint

#
# Class definitions
#
class Settings():
    """ A settings class. It stores number of players and their custom symbols.
        Default is 2 players: X and O """

    #
    # Class members
    #


    #
    # Class methods
    #

    def __init__(self):
    # Sets default settings values
        self.m = 3
        self.n = 3
        self.disabledBlocks = int(0.1 * (self.m*self.n) )
        self.randomEnable = True
        self.lineLgt = 5
        self.nPlayers = 2
        self.playersSymbols = {1:"X", 2:"O"}
        self.playersColors = {1: (1,0,0,1), 2: (0,0,1,1,)}
        self.playersColorsImg = {
                0: {"normal": "./img/base.png", "down": "./img/base_down.png"},
                1: {"normal": "./img/blue.png", "down": "./img/blue_down.png"},
                2: {"normal": "./img/red.png", "down": "./img/red_down.png"}
            }
        # 1: red; 2: green; -1 (blocked): purple

class QField():
    """ A field for the Q-Game and all methods needed to play """

    #
    # Class members
    #
    

    #
    # Class methods
    #
    
    def __init__(self, settings = Settings):
        """ Initialzize an empty field. Custom size can be passed as argument """
        self.settings = settings()
        self.field = [[0 for x in range(self.settings.m)] for y in range(self.settings.n)] 
        if self.settings.randomEnable == True:
            self.addRandomBlocks()
    def addRandomBlocks(self):
        for n in range(self.settings.disabledBlocks):
            self.field[rndint(0, self.settings.m-1)][rndint(0, self.settings.n-1)] = -1
    def reset(self):
        for row in range(self.settings.n):
            for tile in range (self.settings.m):
                self.field[row][tile] = 0
        if self.settings.randomEnable == True:
            self.addRandomBlocks()

    def move(self, player, x, y):
        self.field[x][y] = player

    def isFree(self, x, y):
        if self.field[x][y] == 0:
            return True
        else:
            return False
    def isDraw(self):
        for i in range(1, self.settings.m):
            for j in range(1, self.settings.n):
                if self.field[i][j] == 0 :
                    return False
        return True
    
    def cross_rule(self):
        """ Apply cross rule: a cross get's muted """

        for i in range(1, self.settings.m-1):
            for j in range(1, self.settings.n-1):
                # i, j is the position of the center of the cross
                if self.field[i][j] >0:
                    cross = []                              # List to be checked by __checkSequence
                    cross.append(self.field[i][j])
                    cross.append(self.field[i-1][j])
                    cross.append(self.field[i+1][j])
                    cross.append(self.field[i][j+1])
                    cross.append(self.field[i][j-1])

                    if self.__checkSequence(cross) != None:
                        self.field[i][j] = -1
                        #self.field[i+1][j] = -1
                        #self.field[i-1][j] = -1
                        #self.field[i][j+1] = -1
                        #self.field[i][j-1] = -1
    

    def __checkSequence(self, sequence, lgt = None):
        """ Given a sequence returns the element that occurs 4 times
            in a row. If more the first, if none None """
        if lgt == None:
            lgt = self.settings.lineLgt
        mayWin = sequence[0]
        count = 0
        for x in sequence:
            if x == mayWin:
                count += 1
            else:
                mayWin = x
                count = 1
            if count == lgt and mayWin != 0:
                return mayWin
        return None

    def __checkRows(self):
        """ Checks for a winner on field's rows """

        for row in self.field:
            mayWin = self.__checkSequence(row)
            if mayWin != None:
                return mayWin

    def __checkColumns(self):
        """ You can get that...."""

        column = []
        for j in range(self.settings.n):
            for i in range(self.settings.m):
                column.append(self.field[i][j])
            mayWin = self.__checkSequence(column)
            if mayWin != None:
                return mayWin
            else:
                column = []
        return None

    def __checkBlocks(self):
        """ Checks for a winning block """

        block = []
        for i in range(self.settings.m-1):
            for j in range(self.settings.n-1):
                block.append(self.field[i][j])
                block.append(self.field[i][j+1])
                block.append(self.field[i+1][j])
                block.append(self.field[i+1][j+1])
                mayWin = self.__checkSequence(block, 4)
                if mayWin != None:
                    return mayWin
                block = []
        return None

    def checkWin(self, field = None):
        """ Checks for a victor on the field. May be passed a differet field (for testing) """
        if field == None:
            field = self.field
        rowWinner = self.__checkRows()
        if rowWinner != None:
            return rowWinner
        columnWinner = self.__checkColumns()
        if columnWinner != None:
            return columnWinner
        blockWinner = self.__checkBlocks()
        if blockWinner != None:
            return blockWinner
        return None

