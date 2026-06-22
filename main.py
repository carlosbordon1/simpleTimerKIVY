from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


# Clase que representa el layout
class BoxFondo(BoxLayout):
    pass

# Clase principal de la aplicación
class Aplicacion(App):
    def build(self):
        # Carga la definición KV
        return Builder.load_file("componentes/definicionesKV.kv")
    
    # Metodo para cerrar la app correctamente
    def cerrar_aplicacion(self, instance):
        # Detiene la aplicación de forma segura
        self.stop()

# Punto de entrada
if __name__ == "__main__":
    Aplicacion().run()