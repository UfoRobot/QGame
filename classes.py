from __future__ import print_function
from RandomDeadBlocks import rand_dead_blocks as rndebl

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
        self.disabledBlocks = int(0.1 * (self.m*self.n)) + int(0.3*((self.m*self.n)/10))
        self.randomEnable = True
        self.lineLgt = 5
        self.nPlayers = 2
        self.playersSymbols = {1: "X", 2: "O"}
        self.playersColors = {1: (1, 0, 0, 1), 2: (0, 0, 1, 1), 0 : (1,1,1,1),
                              -1 : (1,0,1,1) }
        self.playersColorsImg = {
            0: {"normal": "./img/base.png", "down": "./img/base_down.png"},
            1: {"normal": "./img/blue.png", "down": "./img/blue_down.png"},
            2: {"normal": "./img/red.png", "down": "./img/red_down.png"},
           -1: {"normal":  "./img/dead.png", "down": "./img/dead_down.png"}
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

    def __init__(self, settings=Settings):
        """ Initialzize an empty field. Custom size can be passed as argument
        """
        self.settings = settings()
        self.field = [[0 for x in range(self.settings.m)] for y in range(self.settings.n)] 
        if self.settings.randomEnable is True:
            self.addRandomBlocks()

    def addRandomBlocks(self):
        rndebl(self, self.settings.disabledBlocks, -1, 2)

    def reset(self):
        for row in range(self.settings.n):
            for tile in range(self.settings.m):
                self.field[row][tile] = 0
        if self.settings.randomEnable is True:
            self.addRandomBlocks()

    def move(self, player, x, y):
        self.field[x][y] = player

    def isFree(self, x, y):
        if self.field[x][y] is 0:
            return True
        else:
            return False

    def isDraw(self):
        for i in range(self.settings.m):
            for j in range(self.settings.n):
                if self.field[i][j] is 0:
                    return False
        return True

    def cross_rule(self):
        """ Apply cross rule: a cross get's muted """
        Cross = lambda x, y: [self.field[x+i][y+j]
                              for i, j in zip([0, 0, 0, -1, 1],
                                              [0, 1, -1, 0, 0])]
        def Xoss(x,y,to_check):
            while to_check:
                to_check.pop()
            to_check.append([Cross(x,y)])
        # List to be checked by __checkSequence
        
        for i in range(1 ,self.settings.m-1):
            for j in range(1, self.settings.n-1):
                # i, j is the position of the center of the cross
                if self.field[i][j] > 0:
                    cross = Cross(i,j)
                    if self.__checkSequence(cross, 5) is not None:
                        self.field[i][j] = -1
                    Xoss(i,j,cross)

    def __checkSequence(self, sequence, lgt=None):
        """ Given a sequence returns the element that occurs 4 times
            in a row. If more the first, if none None """
        if lgt is None:
            lgt = self.settings.lineLgt
        mayWin = sequence[0]
        count = 0
        for x in sequence:
            if x == mayWin:
                count += 1
            else:
                mayWin = x
                count = 1
            if count == lgt and mayWin is not 0:
                return mayWin
        return None

    def __checkRows(self):
        """ Checks for a winner on field's rows """

        for row in self.field:
            mayWin = self.__checkSequence(row)
            if mayWin is not None:
                return mayWin

    def __checkColumns(self):
        """ You can get that...."""

        column = []
        for j in range(self.settings.n):
            for i in range(self.settings.m):
                column.append(self.field[i][j])
            mayWin = self.__checkSequence(column)
            if mayWin is not None:
                return mayWin
            else:
                column = []
        return None

    def __checkBlocks(self):
        """ Checks for a winning block """
        fBlock = lambda x, y: [self.field[x+i][y+j]
                              for i, j in zip([0, 0, 1, 1],
                                              [0, 1, 0, 1])]
        for i in range(self.settings.m-1):
            for j in range(self.settings.n-1):
                mayWin = self.__checkSequence(fBlock(i,j), 4)
                if mayWin is not None:
                    return mayWin
        return None

    def checkWin(self, field=None):
        """ Checks for a victor on the field. May be passed a differet field (for testing) """
        if field is None:
            field = self.field
        rowWinner = self.__checkRows()
        columnWinner = self.__checkColumns()
        blockWinner = self.__checkBlocks()
        for x in (blockWinner, rowWinner, columnWinner):
            if x is not None:
                return x
        return None

