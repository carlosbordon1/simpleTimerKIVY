from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import get_color_from_hex

class WindowManager(ScreenManager):
    pass

class PantallaInicial(Screen):
    pass

class PantallaAyuda(Screen):
    pass
# Clase que representa el layout
class BoxFondo(BoxLayout):
    pass

# Clase principal de la aplicación
class Aplicacion(App):
    def build(self):
        # Convertir HEX a [R,G,B,A]
        self.mi_color_hex = get_color_from_hex("#B518A0") 
        self.a = True



        # Carga la definición KV
        return Builder.load_file("componentes/definicionesKV.kv")
        
    def cambiar_pantalla(self, pantalla_destino):
        # Cambia a la pantalla especificada
        if self.a == True: 
            self.root.transition.direction = "left" 
            self.a = False
        else:
            self.root.transition.direction = "right" 
            self.a = True

        self.root.current = pantalla_destino

    # Metodo para cerrar la app correctamente
    def cerrar_aplicacion(self, instance):
        # Detiene la aplicación de forma segura
        self.stop()

# Punto de entrada
if __name__ == "__main__":
    Aplicacion().run()