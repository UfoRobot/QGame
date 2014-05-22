#
# Imports
#
from __future__ import print_function


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
        self.m = 10
        self.n = 10
        self.linelgt = 5
        self.nPlayers = 2
        self.playersSymbols = {1:"X", 2:"O"}
        self.playersColors = {1: (1, 0, 0, 1), 2: (0, 1, 0, 1)}

class QField():
    """ A field for the Q-Game and all methods needed to play """

    #
    # Class members
    #
    
    # Deafult member values, may be overwritten during init
    settings = Settings()

    #
    # Class methods
    #
    
    def __init__(self, settings = None):
        """ Initialzize an empty field. Custom size can be passed as argument """
        if settings != None:
            self.settings = settings
        self.reset()

    def reset(self):
        self.field = [] 
        for row in range(self.settings.n):
            self.field.append([0 for x in range(self.settings.m)])

    def move(self, player, x, y):
        self.field[x][y] = player

    def isFree(self, x, y):
        if self.field[x][y] == 0:
            return True
        else:
            return False

    def __checkSequence(self, sequence, lgt=None):
        """ Given a sequence returns the element that occurs 4 times
            in a row. If more the first, if none None """
        if lgt == None:
            lgt = self.settings.linelgt
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
