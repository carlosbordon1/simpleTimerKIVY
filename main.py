from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

# Definición de la interfaz usando KV Language
KV = '''
BoxLayout:
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: 0.2, 0.6, 0.8, 0.4  # Azul claro
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        text: "¡Simple Timer!"
        font_size: 24
        color: 1, 1, 1, 1

    Button:
        text: "Salir"
        size_hint_y: None
        height: 50
        on_press: app.cerrar_aplicacion(self)
'''

# Clase que representa el layout
class BoxFondo(BoxLayout):
    pass

# Clase principal de la aplicación
class Aplicacion(App):
    def build(self):
        # Carga la definición KV
        return Builder.load_string(KV)
    
    # Metodo para cerrar la app correctamente
    def cerrar_aplicacion(self, instance):
        # Detiene la aplicación de forma segura
        self.stop()

# Punto de entrada
if __name__ == "__main__":
    Aplicacion().run()