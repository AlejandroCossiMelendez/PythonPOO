# Clase base Animales
class Animales:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def sonido(self):
        return "Este animal hace un sonido."

# Clase Perro que hereda de Animal
class Perro(Animales):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
    
    def sonido(self):
        return f"\n{self.nombre}, un perro de raza {self.raza}, hace: ¡Guau guau! \n"

# Clase Gato que hereda de Animal
class Gato(Animales):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color
    
    def sonido(self):
        return f"{self.nombre}, un gato de color {self.color}, hace: ¡Miau miau! \n"

# Clase Pajaro que hereda de Animal
class Pajaro(Animales):
    def __init__(self, nombre, especie):
        super().__init__(nombre)
        self.especie = especie
    
    def sonido(self):
        return f"{self.nombre}, un pajaro de la especie {self.especie}, hace: ¡Pio pio!\n"

# Funcion que recibe cualquier tipo de animal y muestra su sonido
def mostrar_sonido(animal):
    print(animal.sonido())

# Creacion de objetos
perro = Perro("Max", "Labrador")
gato = Gato("Whiskers", "Negro")
pajaro = Pajaro("Tweety", "Canario")

# Llamado a la funcion para cada objeto
mostrar_sonido(perro)
mostrar_sonido(gato)
mostrar_sonido(pajaro)
