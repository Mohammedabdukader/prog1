from kivy.app import App
from kivy.uix.boxlayout import Boxlayout 
from kivy.uix.button import Button 
from kivy.uix.textinput import Textinput
class Mainapp(App):
    def build (self):
        self.operators = {"/","*","+","-"}

if __name__=="__ Main__":
    app = MainApp()
    app.run()