# Clase base InstrumentoMusicales
class InstrumentoMusicales:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def tocar(self):
        return "Este instrumento se esta tocando."

# Clase Guitarra que hereda de InstrumentoMusicales
class Guitarra(InstrumentoMusicales):
    def __init__(self, nombre, cuerdas):
        super().__init__(nombre)
        self.cuerdas = cuerdas
    
    def tocar(self):
        return f"\nLa {self.nombre} tiene {self.cuerdas} cuerdas y se toca pulsando las cuerdas.\n"

# Clase Piano que hereda de InstrumentoMusicales
class Piano(InstrumentoMusicales):
    def __init__(self, nombre, teclas):
        super().__init__(nombre)
        self.teclas = teclas
    
    def tocar(self):
        return f"El {self.nombre} tiene {self.teclas} teclas y se toca presionando las teclas.\n"

# Clase Trompeta que hereda de InstrumentoMusicales
class Trompeta(InstrumentoMusicales):
    def __init__(self, nombre, boquilla):
        super().__init__(nombre)
        self.boquilla = boquilla
    
    def tocar(self):
        return f"La {self.nombre} tiene una boquilla {self.boquilla} y se toca soplando a traves de ella.\n"

# Funcion que recibe cualquier tipo de instrumento y muestra como se toca
def mostrar_instrumento(instrumento):
    print(instrumento.tocar())

# Creacion de objetos
guitarra = Guitarra("Guitarra Electrica", 6)
piano = Piano("Piano de Cola", 88)
trompeta = Trompeta("Trompeta", "de metal")

# Llamado a la funcion para cada objeto
mostrar_instrumento(guitarra)
mostrar_instrumento(piano)
mostrar_instrumento(trompeta)
