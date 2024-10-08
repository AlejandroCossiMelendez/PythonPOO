# Defino la clase Animal
class Animal:
    # Metodo Constructor
    def __init__(self, nombre, especie, edad, tamaño, color):
        # Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.tamaño = tamaño
        self.color = color
        self.comida = None
        self.forma_movimiento = None

    # Metodo para mostrar detalles del objeto
    def mostrar_informacion(self):
        print(f"Informacion del Animal:\n")
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Color: {self.color}\n")

    # Metodo para hacer sonido
    def hacer_sonido(self):
        sonido = input(f"¿Que sonido hace {self.nombre} ({self.especie})?: ")
        print(f"{self.nombre} hace el sonido: {sonido}")
        print("_______________________________________________________")

    # Metodo para moverse
    def moverse(self):
        self.forma_movimiento = input(f"¿Como se mueve {self.nombre} ({self.especie})?: ")
        print(f"{self.nombre} se mueve de esta forma: {self.forma_movimiento}")
        print("_______________________________________________________")


# Creamos los objetos a partir de instanciar la clase Animal
animal_1 = Animal("Rex", "Perro", 5, "Grande", "Marron")
animal_2 = Animal("Luna", "Gato", 3, "Mediano", "Blanco")
animal_3 = Animal("Kiwi", "Ave", 2, "Pequeño", "Verde")

# Mostrar los detalles animal_1
animal_1.mostrar_informacion()
# Hacer sonido
animal_1.hacer_sonido()
# Moverse
animal_1.moverse()

# Mostrar los detalles animal_2
animal_2.mostrar_informacion()
# Hacer sonido
animal_2.hacer_sonido()
# Moverse
animal_2.moverse()

# Mostrar los detalles animal_3
animal_3.mostrar_informacion()
# Hacer sonido
animal_3.hacer_sonido()
# Moverse
animal_3.moverse()
