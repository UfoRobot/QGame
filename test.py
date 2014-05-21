#
# Imports
#
from __future__ import print_function

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder

Builder.load_string('''
<GameGrid>:
    orientation: 'vertical'

    Label:
        text: 'GAME GRID'

    Button:
        size_hint_y: 0.1
        text: 'Open Popup'
        on_release: root.startPopup()

<CustomPopup>:
    size_hint_x: 0.7
    size_hint_y: 0.7
    auto_dismiss: False


    ScreenManager:
        id: s_manager

        Screen:
            id: r_screen
            name: 'result_screen'

            BoxLayout:
                orientation: 'vertical'
                padding: 10

                Label:
                    halign: 'center'
                    size_hint_y: None
                    height: 100
                    text: "END OF GAME"
            
                Label:
                    text: 'Result Text inside r_s'

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: 50

                    Button:
                        text: 'New Game'
                        on_release: root.newGame()

                    Button:
                        text: 'Settings'
                        on_release: root.switchToSettings()        
        Screen:
            id: s_screen
            name: 'settings_screen'

            BoxLayout:
                orientation: 'vertical'
                padding: 10

            Label:
                text: 'SETTINGS HERE'

            Button:
                size_hint_y: None
                height: 50
                text: 'Back'
                on_release: root.close()


''')


class CustomPopup(ModalView):
    aFunction = ObjectProperty()

    def newGame(self):
        print("NEW GAME")
        self.dismiss()
        self.aFunction()

    def switchToSettings(self):
        self.ids.s_manager.transition = SlideTransition(direction = "left")
        self.ids.s_manager.current = "settings_screen"

    def close(self):
        self.dismiss()
        self.ids.s_manager.current = "result_screen"
        self.newGame()



class Settings():

    def __init(self):
        self.value = 0
    def show(self):
        print(self.value)

class GameGrid(BoxLayout):

    def startPopup(self):
        p = CustomPopup(aFunction=self.aFunc)
        p.open()

    def aFunc(self):
        print("Shalalalal")
        

class MyApp(App):
    def build(self):
        return GameGrid()

if __name__ == "__main__":
    MyApp().run()

