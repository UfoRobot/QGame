#
# Imports under here
#

from __future__ import print_function
import itertools
import os

#
# System based functions
#
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

#
# Class definition
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
        self.m = 6
        self.n = 6
        self.nPlayers = 2
        self.players = {0:".", 1:"X", 2:"O"}

    def showSettings(self):
        clearScreen()
        print("Field size:\t\t\t{}x{}".format(self.m, self.n))
        print("Number of players:\t\t\t{}".format(self.nPlayers))
        for player in range(1, self.nPlayers+1):
            print("Player {} ---> {}".format(player, self.players[player]))



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
    
    # Deafult member values, may be overwritten during init
    settings = Settings()

    #
    # Class methods
    #
    
    def __init__(self, settings = None):
        """ Initialzize an empty field. Custom size can be passed as argument """
        if settings != None:
            self.settings = settings
        self.field = [] 
        for row in range(self.settings.n):
            self.field.append([0 for x in range(self.settings.m)])

    def show(self):
        clearScreen()
        for i in range(self.settings.m):
            for j in range(self.settings.n):
                toPrint = self.settings.players[self.field[i][j]]
                print(toPrint, end = "\t")
            print("\n")

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
                mayWin = self.__checkSequence(block)
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

    def move(self, player):
        """ Asks a player for it's move until he enters a valid one """

        playerMove = raw_input("Player {} enter move: ".format(player))
        i, j = playerMove.split()
        i = int(i)
        j = int(j)

        
        if i > self.settings.m or j > self.settings.n:
            print(" ERROR # QField.move --> Move out of field")
            self.move(player)
        elif self.field[i][j] != 0:
            print("ERROR # QField.move --> Not an empty cell!")
            self.move(player)
        else:
            self.field[i][j] = player

    def move2(self, player, x, y):
        """ Re-written version for gui integration """

        self.field[x][y] = player



class QMatch():
    """ A match of the QGame. Here's where the fight takes place """

    #
    # Class members
    #

    # Default member values, might be overwritten during init
    settings = Settings()
    field = QField(settings)

    #
    # Class methods
    #

    def __init__(self, settings = None, field = None):
        """ Initialize the match with custom or default field and settings.
            A match can therefore starts with a argument-passed non-empty field (mainly for testing) """
        if field != None:
            self.field = field               # Use argumet-passed field
        if settings != None:
           self.field = QField(settings)

    def playTurns(self):
        """ Loops players letting them make their moove, returns winner at the end of game """

        for player in itertools.cycle(range(1, self.settings.nPlayers+1)):
            self.field.show()
            self.field.move(player)
            mayWin = self.field.checkWin()
            if mayWin != None:
                return mayWin

    def startMatch(self):
        """ Let's have this started """

        print("STARTING THE MATCH")
        winner = self.playTurns()
        print("PLAYER {} WON THIS GAME".format(winner))

class Menu():
    """ A menu class to navigate through settings or start new game """

    #
    # Class members
    #

    settings = Settings()   # default settings may be changed via setSettings

    #
    # Class methods
    #

    def __init__(self):
        self.mainPage()
    
    def mainPage(self):
        loop = True
        while loop:
            clearScreen()
            print("*----------------*")
            print("|    MAIN MENU   |")
            print("*----------------*")
            print(" [1] New Game")
            print(" [2] Settings")
            print(" [0] Quit")
            answer  = raw_input("->")

            if answer == "1":
                print("New Game")
                game = QMatch(self.settings)
                game.startMatch()
            elif answer == "2":
                print("Settings")
                self.settings.showSettings()
                raw_input("Press enter to continue")
            elif answer == "0":
                print("Bye bye")
                loop = False
            else:
                print("ERROR # Menu.mainPage --> Not a valid option")
                raw_input("Press enter to continue")
                


if __name__ == "__main__":
    test = Menu()


