# Defino la clase Carro
class Carro:
    # Metodo Constructor
    def __init__(self, marca, modelo, año, tipo_combustible, color):
        # Defino los atributos de instancia de la clase
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.tipo_combustible = tipo_combustible
        self.color = color
        self.velocidad = 0  # Velocidad inicial en 0

    # Metodo para mostrar detalles del objeto
    def mostrar_informacion(self):
        print(f"Informacion del Carro:\n")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Tipo de Combustible: {self.tipo_combustible}")
        print(f"Color: {self.color}\n")

    # Metodo para acelerar
    def acelerar(self):
        incremento = int(input(f"¿Cuantos km/h deseas acelerar el {self.marca} {self.modelo}?: "))
        self.velocidad += incremento
        print(f"El carro ha acelerado. Velocidad actual: {self.velocidad} km/h")
        print("_______________________________________________________")

    # Metodo para frenar
    def frenar(self):
        decremento = int(input(f"¿Cuantos km/h deseas reducir la velocidad del {self.marca} {self.modelo}?: "))
        if self.velocidad - decremento >= 0:
            self.velocidad -= decremento
        else:
            self.velocidad = 0
        print(f"El carro ha frenado. Velocidad actual: {self.velocidad} km/h")
        print("_______________________________________________________")


# Creamos los objetos a partir de instanciar la clase Carro
carro_1 = Carro("Toyota", "Supra MK4", 2024, "Gasolina", "Rojo")
carro_2 = Carro("Ford", "Pickup", 1980, "Gasolina", "Beich")
carro_3 = Carro("Tesla", "Model S", 2022, "Electrico", "Negro")

# Mostrar los detalles carro_1
carro_1.mostrar_informacion()
# Acelerar
carro_1.acelerar()
# Frenar
carro_1.frenar()

# Mostrar los detalles carro_2
carro_2.mostrar_informacion()
# Acelerar
carro_2.acelerar()
# Frenar
carro_2.frenar()

# Mostrar los detalles carro_3
carro_3.mostrar_informacion()
# Acelerar
carro_3.acelerar()
# Frenar
carro_3.frenar()
