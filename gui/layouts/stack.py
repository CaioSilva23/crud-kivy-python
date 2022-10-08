from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout


class TelaApp(StackLayout):
    pass


class Stack(App):
    def build(self):
        return TelaApp()


Stack().run()
