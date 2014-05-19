#
# Imports
#
from __future__ import print_function

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label



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
        self.m = 6
        self.n = 6
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

 
    def move(self, player, x, y):
        """ Re-written version for gui integration """

        self.field[x][y] = player

    def isFree(self, x, y):
        if self.field[x][y] == 0:
            return True
        else:
            return False





class QGrid(GridLayout):
    """ A custom GridLayout to place widgets on """

    field = QField()
    settings = Settings()
    player = 1

    def __init__(self, *args, **kwargs):
        """ Sets up the grid and overloads init """

        super(QGrid, self).__init__(*args, **kwargs)
        self.cols = self.settings.n
        for row in range(self.settings.m):
            for column in range(self.settings.n):
                entry = GridEntry()
                entry.coords = [row, column]
                entry.bind(on_release = self.button_pressed)
                self.add_widget(entry)

    def newGame(self, *args):
        """ Starts a new game """

        print("New game")

        self.reset()

    def reset(self, *args):
        """ Reset buttons and field table """

        print("Reset")

        self.clear_widgets()
        for row in range(self.settings.m):
            for column in range(self.settings.n):
                entry = GridEntry()
                entry.coords = [row, column]
                entry.bind(on_release = self.button_pressed)
                self.add_widget(entry)
        print("Is this causing crash?")
        self.field.reset()




    def setSettings(self):
        print("SETTINGS CALLED")
        

    def button_pressed(self, button):
        print("Button {} clicked!".format(button.coords))
        x, y = button.coords

        if self.field.isFree(x, y):
            self.field.move(self.player, x, y)
            button.background_color = self.settings.playersColors[self.player]
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1
        winner = self.field.checkWin()
        if winner != None:
            self.resultPopup(winner)

    def resultPopup(self, winner):
        """ Pops out when game ends.
        Shows result and allows to start a new game or modify settings """

        print("Result Popup")                                                   # For debugging

        popupLabel = Label(text="Player {} won!".format(winner))                # Label object
        newGameButton = Button(text='New game', size_hint_y=None, height=50)    # Button object
        settingsButton = Button(text='Settings', size_hint_y=None, height=50)   # Button object
        settingsButton.bind(on_release = self.setSettings)
        newGameButton.bind(on_release = self.reset())
        content = BoxLayout(orientation='vertical')                             # Layout for popup
        content.add_widget(popupLabel)

        buttons = BoxLayout(orientation='horizontal')                           # Layout for buttons on the bottom
        buttons.add_widget(newGameButton)
        buttons.add_widget(settingsButton)
        content.add_widget(buttons)                                             # Adding buttons' layout under label object

        popup = Popup(                                                          # Setting popup propreties
                title = "END OF GAME",
                content = content,
                size_hint=(None, None),
                size=(400, 400),
                auto_dismiss = False)
        newGameButton.bind(on_release = self.newGame)                           # New game on release
        newGameButton.bind(on_release = popup.dismiss)                          # Also dismiss popup
        popup.open()



 


class GridEntry(Button):
    """ A custom button widget """
    
    coords = ListProperty([0, 0])

class QApp(App):
    def build(self):
        return QGrid()

if __name__ == "__main__":
    QApp().run()

