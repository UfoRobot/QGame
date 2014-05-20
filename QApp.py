#
# Imports
#
from __future__ import print_function

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from kivy.uix.screenmanager import ScreenManager, Screen



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


class MainLayout(GridLayout):
    """ The main grid, where everything takes place... """

    winner = NumericProperty

    def __init__(self, *args, **kwargs):
        """ Overloading init """

        super(MainLayout, self).__init__(*args, **kwargs)

        """ Init initializing gaming grid """
        self.field = QField()
        self.settings = Settings()
        self.player = 1                                                         # Starting player
        self.cols = self.settings.n
        for row in range(self.settings.m):
            for column in range(self.settings.n):
                entry = GridEntry()
                entry.coords = [row, column]
                entry.bind(on_release = self.button_pressed)
                self.add_widget(entry)
        self.winner = 0
        

        """ Initializing the result screen """
        popupLabel = Label(text="Player {} won!".format(self.winner))           # Label object for showing the end-game status
        newGameButton = Button(text='New game', size_hint_y=None, height=50)    # Button object for new game
        settingsButton = Button(text='Settings', size_hint_y=None, height=50)   # Button object accessing settings

        buttons = BoxLayout(orientation='horizontal')                           # Layout for buttons on the bottom
        buttons.add_widget(newGameButton)
        buttons.add_widget(settingsButton)

        resultContent = BoxLayout(orientation='vertical')                       
        resultContent.add_widget(popupLabel)
        resultContent.add_widget(buttons)                                       # Adding buttons' layout under label object

        resultScreen = Screen(name="rScreen")                                   # Screen object
        resultScreen.add_widget(resultContent)                                  

        """ Initializing the settings screen """

        settingsLabel = Label(text="SETTINGS HERE")
        closeButton = Button(text="Close", size_hint_y=None, height=50)
        settingsContent = BoxLayout(orientation="vertical")
        settingsContent.add_widget(settingsLabel)
        settingsContent.add_widget(closeButton)
        settingsScreen = Screen(name="sScreen")                                 # Screen object
        settingsScreen.add_widget(settingsContent)

        """ Initializing the sm (screen manager) widget and the popup  """
        self.sm = ScreenManager()                                               # ScreenManager object

        self.sm.add_widget(resultScreen)
        self.sm.add_widget(settingsScreen)

        self.popup = Popup(                                                     # Setting popup propreties
                title = "END OF GAME",
                content = self.sm,
                size_hint=(None, None),
                size=(400, 400),
                auto_dismiss = False)

        newGameButton.bind(on_release = self.popup.dismiss)                     # Dismiss popup first! The other order doesn't work.... boh!
        newGameButton.bind(on_release = self.newGame)                           # New game on release
        closeButton.bind(on_release = self.popup.dismiss)
        closeButton.bind(on_release = self.newGame)
        settingsButton.bind(on_release = self.setSettings)

    def newGame(self, *args):
        """ Starts a new game """

        print("New game")

        self.reset()

    def reset(self, *args):
        """ Reset buttons and field table """

        print("Reset")
        
        # Reset all grid-childs (buttons) to default color
        for child in self.children:
            child.background_color = (1,1,1,1)
        
        # Reset field table
        self.field.reset()


    def setSettings(self, *args):
        print("SETTINGS CALLED")

        self.sm.current = "sScreen"

        self.clear_widgets()
        for row in range(self.settings.m):
            for column in range(self.settings.n):
                entry = GridEntry()
                entry.coords = [row, column]
                entry.bind(on_release = self.button_pressed)
                self.add_widget(entry)
        # print("Is this causing crash?") # It isn't, remove it.
        self.field.reset()




    def setSettings(self, *spam):
        print("SETTINGS CALLED SPAM: %s", spam)
        

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
        mayWin = self.field.checkWin()
        if mayWin != None:
            self.winner = mayWin
            print("WE HAVE A WINNER!")
            print(mayWin)
            self.resultPopup()

    def resultPopup(self):
        """ Pops out when game ends.
        Shows result and allows to start a new game or modify settings """

        print("Result Popup")   # For debugging
        self.popup.open()
        print("Result Popup")                                                   # For debugging

        popupLabel = Label(text="Player {} won!".format(winner))                # Label object
        newGameButton = Button(text='New game', size_hint_y=None, height=50)    # Button object
        settingsButton = Button(text='Settings', size_hint_y=None, height=50)   # Button object
        settingsButton.bind(on_release = self.setSettings)
        
        newGameButton.bind(on_release = self.newGame)  
        newGameButton.bind(on_press = self.reset)
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
        
        newGameButton.bind(on_release = popup.dismiss)                          # Also dismiss popup
        popup.open()



 


class GridEntry(Button):
    """ A custom button widget """
    
    coords = ListProperty([0, 0])

class QApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    QApp().run()

