#
# Imports under here
#

#
# Class definition
#

class Settings():
    """ A settings class. It stores number of players and their custom symbols.
        Default is 2 players: X and O """
    
    #
    # Class members
    #

    self.nPlayers = 0   # Number of players
    self.players = {}   # Associates player's id and player's symbol

    #
    # Class methods
    #

    def __init__(self):
        # Sets default settings values
        self.nPlayers = 2
        self.players = {1:"X", 2:"O"}

    def setPlayers():
        # Sets custom setting values. More player and custom symbols
        self.nPlayers = raw_imput("Enter number of players:")
        for player in range(1, nPlayers+1):
            symbol = raw_imput("Choose a symbol for player n {}:".format(player))
            self.players[player] = symbol

class QField():
    """ A field for the Q-Game and all methods needed to play """

    #
    # Class members
    #

    n = 0        # Number of rows
    m = 0        # Number of columns
    field = []   # Field is a list of lists

    #
    # Class methods
    #
    
    def __init__(self, rows, columns):
    # init builds up a clear field n x m
        self.n = rows
        self.m = columns
        self.field = [] 
        for row in range(n):
            self.field.append([0 for x in range(m)])

    def show(self):
        for i in range

    def __checkSequence(self, sequence):
        """ Given a sequence returns the element that occurs 4 times
            in a row. If more the first, if none None """

        mayWin = sequence[0]
        count = 0
        for x in sequence:
            if x == mayWin:
                count += 1
            else:
                mayWin = x
                count = 1
            if count == 4 and mayWin != 0:
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
        for j in range(self.n):
            for i in range(self.m)
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
        for i in range(self.m-1):
            for j in range(self.n-1):
                block.append(field[i][j])
                block.append(field[i][j+1])
                block.append(field[i+1][j])
                block.append(field[i+1][j+1])
                mayWin = self.__checkSequence(block)
                if mayWin != None:
                    return mayWin
                block = []
        return None

    def checkWin(self, field = None):
        """ Checks for a victor on the field. May be passed a differet field for testing """
        if field == None:
            field = self.field
        rowWinner = self.__checkRows(field)
        if rowWinner != None:
            return rowWinner
        columnWinner = self.__checkColumns(field)
        if columnWinner != None:
            return columnWinner
        blockWinner = self.__checkBlocks(field)
        if blockWinner != None:
            return blockWinner
        return None

    def move(self, player, i, j):
        if self.field[i][j] != 0:
            print "ERROR # QField.move --> Not an empty cell!"
        else:
            self.field[i][j] = player





if __name__ == "__main__":
    test = QField(4,6)
#    print test.field
    
#    sequenceLine = [0,0,3,3,3,2,2,0,0,0,0,0,0,0,1,1,1,1]
#    print sequenceLine
#    print test.checkSequence(sequenceLine)

    testField = [
            [1,2,2,0,0,1],
            [1,1,0,0,2,1],
            [2,0,2,2,1,1],
            [2,2,1,2,1,1]
            ]
#    print testField
#    print test.checkRows(testField)
    print test.checkBlock(testField)

