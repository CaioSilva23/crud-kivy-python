from kivy.app import App
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class Principal(BoxLayout):
    text_principal = StringProperty('Eu sou uma label')
    size_text_principal = NumericProperty(30)

    def teste(self):
        self.text_principal = 'Fui clicado'
        self.size_text_principal += 20


class Teste(App):
    def build(self):
        return Principal()


Teste().run()
