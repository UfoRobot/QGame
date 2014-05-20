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
from kivy.uix.screenmanager import ScreenManager, Screen


class ResultScreen(Screen):
    pass

class CustomScreenManager(ScreenManager):

    def newGame(self, *args):
        print("New game")

    def settings(self, *args):
        print("Settings")


class QApp(App):
    def build(self):
        return b

if __name__ == "__main__":
    QApp().run()

