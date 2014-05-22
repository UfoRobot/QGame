#
# Imports
#
from __future__ import print_function

from classes import QField, Settings

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.properties import ListProperty, StringProperty, NumericProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

class CustomPopup(ModalView):
    newGameFunction = ObjectProperty()
    winner = NumericProperty()

    def newGame(self):
        print("NEW GAME")
        self.dismiss()
        self.newGameFunction()

    def switchToSettings(self):
        self.ids.s_manager.transition = SlideTransition(direction = "left")
        self.ids.s_manager.current = "settings_screen"

    def close(self):
        self.dismiss()
        self.ids.s_manager.current = "result_screen"
        #self.newGame()

class MainLayout(GridLayout):
    """ The main grid, where everything takes place... """


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
        
       
    def newGame(self, *args):
        """ Starts a new game """

        print("New game")

        self.reset()

    def reset(self, *args):
        """ Reset buttons and field table """

        print("Reset")
        
        # Reset field table
        self.field.reset()

        self.updateButtons()


    def setSettings(self, *args):
        print("SETTINGS CALLED")

    def updateButtons(self):
        """ Updates buttons background based on field table """

        for child in self.children:
            i, j = child.coords
            
            if self.field.field[i][j] == 0:
                child.background_color = (1,1,1,1)
            if self.field.field[i][j] == -1:
                child.background_color = (1,0,1,1)


    def button_pressed(self, button):
        x, y = button.coords

        if self.field.isFree(x, y):
            self.field.move(self.player, x, y)
            button.background_color = self.settings.playersColors[self.player]

            if self.player == 1:
                print ("Player is 2")
                self.player = 2
            else:
                print ("Player is 1")
                self.player = 1

        #Cross rule here
        self.crossRule()

        mayWin = self.field.checkWin()
        if mayWin != None:
            self.winner = mayWin
            self.callPopup()

    def crossRule(self):
        self.field.cross_rule()
            
    def callPopup(self):
        """ Pops out when game ends.
        Shows result and allows to start a new game or modify settings """

        print("Result Popup")   # For debugging
        self.popup = CustomPopup(newGameFunction=self.newGame, winner = self.winner)
        self.popup.open()



 


class GridEntry(Button):
    """ A custom button widget """
    
    coords = ListProperty([0, 0])

class QApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    QApp().run()

