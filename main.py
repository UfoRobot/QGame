#!/usr/bin/env kivy

from classes import QField, Settings
import sys
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.properties import ListProperty, StringProperty, NumericProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.event import EventDispatcher
from ia import AI

class MenuPopup(ModalView):
    
    newGameFunction = ObjectProperty()
    settings = ObjectProperty()

    def newGame(self):
        self.dismiss()
        self.newGameFunction()

    def backToMenu(self):
        self.ids.s_manager.transition = SlideTransition(direction = "right")
        self.ids.s_manager.current = "menu_screen"

    def switchToSettings(self):
        self.ids.s_manager.transition = SlideTransition(direction = "left")
        self.ids.s_manager.current = "settings_screen"

    def switchToHowtoplay(self):
        self.ids.s_manager.transition = SlideTransition(direction = "left")
        self.ids.s_manager.current = "howto_screen"

    def close(self):
        self.dismiss()
        
    def quitGame(self):
        sys.exit()

class EndPopup(ModalView):
    
    newGameFunction = ObjectProperty()
    winner = NumericProperty()

    def newGame(self):
        self.dismiss()
        self.newGameFunction()

    def close(self):
        self.dismiss()
        self.ids.s_manager.current = "result_screen"
        #self.newGame()

class TopBar(BoxLayout):

    settings = ObjectProperty()
    currentPlayer = NumericProperty()
    newGameFunction = ObjectProperty()
    def __init__(self, *args, **kwargs):
        """ Overloading init """

        super(TopBar, self).__init__(*args, **kwargs)
        self.menuPopup = MenuPopup(settings = self.settings)
        #self.menuPopup.newGameFunction=self.newGameFunction
    
    def startMenu(self):
        #self.newGameFunction() # enable for easy testing of newly generated games (disable following lines:)
        self.menuPopup.newGameFunction = self.newGameFunction
        self.menuPopup.open()

class GameGrid(GridLayout):
    """ The main grid, where everything takes place... """

    player = NumericProperty()
    
    def __init__(self, *args, **kwargs):
        """ Overloading init """

        super(GameGrid, self).__init__(*args, **kwargs)

        """ Init initializing gaming grid """
        self.field = QField()
        self.settings = Settings()
        self.player = 1
        self.AI = AI(self)
        # Starting player
        self.cols = self.settings.n
        for row in range(self.settings.m):
            for column in range(self.settings.n):
                entry = GridEntry()
                entry.coords = [row, column]
                entry.bind(on_release = self.button_pressed)
                self.add_widget(entry)
        self.winner = 0
        self.updateButtons()
       
    def newGame(self, *args):
        """ Starts a new game """
        self.field.reset()
        self.updateButtons()


    def setSettings(self, *args):
        pass

    def updateButtons(self):
        """ Updates buttons background based on field table """

        for child in self.children:
            try:
                i, j = child.coords
            except AttributeError:
                continue    
            child.background_color = self.settings.playersColors[self.field.field[i][j]]
            
            
    
    def button_pressed(self, button):
        x, y = button.coords

        if self.field.move(self.player, x, y):
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1

        self.field.cross_rule()
        self.updateButtons()
        mayWin = self.field.checkWin()
        if mayWin is not None:
            self.winner = mayWin
            self.callPopup()
        if self.field.isDraw():
            self.winner = 0
            self.callPopup()
        if self.player is self.settings.AIplayer:
            if self.AI.Move():
                self.player = 1
                self.updateButtons()
                
            
    def callPopup(self):
        """ Pops out when game ends.
        Shows result and allows to start a new game"""

        self.popup = EndPopup(newGameFunction=self.newGame, winner = self.winner)
        self.popup.open()

class MainLayout(BoxLayout):
    
    settings = ObjectProperty(Settings())
        
class GridEntry(Button):
    """ A custom button widget """
    
    coords = ListProperty([0, 0])

class QApp(App):
    
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    QApp().run()

