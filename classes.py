from RandomDeadBlocks import rand_dead_blocks as rndebl

#
# Class definitions
#


class Settings():
    """ A settings class. It stores number of players and their custom symbols.
        Default is 2 players: X and O """

    def __init__(self):
        # Game settings 
        self.m = 10 # Lines
        self.n = 10 # Columns
        self.lineLgt = 5 # Line length (to score)
        self.nPlayers = 2
        self.playersSymbols = {1: "X", 2: "O"}
        self.playersColorName = {1 : 'Red', 2: 'Blue'} # Will (shall) be used in
                                                       # kv file for proper output
        self.playersColors = {
            1: (1, 0, 0, 1), # RGBA: Red
            2: (0, 0, 1, 1), # RGBA: Blue
            0: (1, 1, 1, 1), # RGBA: ()
            -1: (1, 0, 1, 1)}# RGBA: Purple (Dead Block)
        self.playersColorsImg = {
            0: {"normal": "./img/base.png", "down": "./img/base_down.png"},
            1: {"normal": "./img/blue.png", "down": "./img/blue_down.png"},
            2: {"normal": "./img/red.png", "down": "./img/red_down.png"},
            -1: {"normal":  "./img/dead.png", "down": "./img/dead_down.png"}
        }
        # Settings about random dead blocks: 
        self.disabledBlocks = int(0.1 * (self.m*self.n)) + int(0.3*((self.m*self.n)/10))
        self.coeff_disabledBlocks = -1 # Chance of 2 neighbor blocks
        self.fade_disabledBlocks = True 
        self.range_disabledBlocks = 2
        self.randomEnable = True

class QField():
    """ A field for the Q-Game and all methods needed to play """

    def __init__(self, settings=Settings):
        """ Initialzize an empty field. Size is based on settings(.m and .n)
        """
        self.settings = settings()
        self.field = [[0 for x in range(self.settings.m)] for y in range(self.settings.n)] 
        if self.settings.randomEnable is False:
            self.firstMove = False
        else:
            self.firstMove = True

    def addRandomBlocks(self):
        # This function adds random "dead" blocks to prevent some easy tricks,
        #   thus improving gameplay
        rndebl(self, self.settings.disabledBlocks, self.settings.coeff_disabledBlocks,
               self.settings.range_disabledBlocks,self.settings.fade_disabledBlocks)

    def reset(self):
        for row in range(self.settings.n):
            for tile in range(self.settings.m):
                self.field[row][tile] = 0
        if self.settings.randomEnable is True:
            self.firstMove = True

    def move(self, player, x, y):
        if self.isFree(x,y):
            self.field[x][y] = player
            if self.firstMove:
                self.addRandomBlocks()
                self.firstMove = False
            
            return True
        else:
            return False

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
        """ Apply cross rule: the center of a "cross" (plus-sign shape) is turned
            into a dead block hence preventing the player to easily win     """
        Cross = lambda x, y: [self.field[x+i][y+j]
                              for i, j in zip([0, 0, 0, -1, 1],
                                              [0, 1, -1, 0, 0])]
        def free(to_check):
            while to_check:
                to_check.pop()
        # List to be checked by __checkSequence
        
        for i in range(1, self.settings.m-1):
            for j in range(1, self.settings.n-1):
                # i, j is the position of the center of the cross
                if self.field[i][j] > 0:
                    cross = Cross(i, j)
                    if self.__checkSequence(cross, 5) is not None:
                        self.field[i][j] = -1
                    free(cross)

    def __checkSequence(self, sequence, lgt=None):
        """ Given a sequence returns the element that occurs 'lgt' times
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

        for row in self.field:
            mayWin = self.__checkSequence(row)
            if mayWin is not None:
                return mayWin

    def __checkColumns(self):

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
        """ Checks for a winning block (a square with 2-tile side) """
        def free(to_check):
            while to_check:
                to_check.pop()
        fBlock = lambda x, y: [self.field[x+i][y+j]
                               for i, j in zip([0, 0, 1, 1],
                                               [0, 1, 0, 1])]
        for i in range(self.settings.m-1):
            for j in range(self.settings.n-1):
                block = fBlock(i, j)
                mayWin = self.__checkSequence(block, 4)
                free(block)
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
                # Return the winner if it is a player, if it is -1 (dead block),
                #   return None
                return x if x is not -1 else None
        return None
