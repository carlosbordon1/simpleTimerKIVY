from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class HomeScreen(Screen):
    def saludo(self):
        print("Hola desde HomeScreen")


#Builder.load_file("")
modelos = Builder.load_string("""
<HomeScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Saludar de Nuevo'
            on_press: root.saludo()
        Label:
            text: 'this on top'
        Label:
            text: 'this right aligned'
            size_hint_x: None
            size: self.texture_size
            pos_hint: {'right': 1}
        Label:
            text: 'this on bottom'

HomeScreen:
""")

class MyApp(App):
    def build(self):

        return modelos

if __name__ == "__main__":
    MyApp().run()
