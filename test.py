#
# Imports
#
from __future__ import print_function

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty, ObjectProperty, NumericProperty
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder

Builder.load_string('''
<CustomLabel>
    text: 'Value is {}'.format(root.value)

<WorkingClass>:
    orientation: 'vertical'

    Button:
        text: 'Update'
        on_release: root.update()

<MainLayout>
    orientation: 'vertical'

''')

class CustomLabel(Label):
    value = NumericProperty()

class WorkingClass(BoxLayout):

    def __init__(self, *args, **kwargs):

        super(WorkingClass, self).__init__(*args, **kwargs)

        self.a = 5

    def update(self):
        self.a += 1
        print(self.a)

class MainLayout(BoxLayout):

    def __init__(self, *args, **kwargs):

        super(MainLayout, self).__init__(*args, **kwargs)
        
        self.workingClass = WorkingClass()
        self.customLabel = CustomLabel(value=self.workingClass.a)

        self.add_widget(self.customLabel)
        self.add_widget(self.workingClass)



        

class MyApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    MyApp().run()

