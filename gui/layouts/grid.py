from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout


class TelaApp(GridLayout):
    pass


class Grid(App):
    def build(self):
        return TelaApp()


Grid().run()
