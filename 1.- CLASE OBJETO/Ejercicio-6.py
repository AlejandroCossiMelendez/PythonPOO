# Defino la clase Moto
class Moto:
    # Metodo Constructor
    def __init__(self, marca, modelo, cilindraje, tipo_combustible, color):
        self.marca = marca
        self.modelo = modelo
        self.cilindraje = cilindraje
        self.tipo_combustible = tipo_combustible
        self.color = color
        self.motor_encendido = False
        self.nivel_combustible = 100  # Nivel de combustible inicial en porcentaje

    # Metodo para mostrar detalles del objeto
    def mostrar_informacion(self):
        print(f"Informacion de la Moto:\n")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cilindraje: {self.cilindraje}")
        print(f"Tipo de Combustible: {self.tipo_combustible}")
        print(f"Color: {self.color}")
        print(f"Nivel de Combustible: {self.nivel_combustible}%")
        print("_______________________________________________________")

    # Metodo para encender el motor
    def encender_motor(self):
        if not self.motor_encendido:
            self.motor_encendido = False
            print(f"El motor de la {self.marca} {self.modelo} esta encendido.")
        else:
            print(f"El motor de la {self.marca} {self.modelo} ya esta encendido.")
        print("_______________________________________________________")

    # Metodo para revisar el combustible
    def revisar_combustible(self):
        print(f"Nivel de combustible en la {self.marca} {self.modelo}: {self.nivel_combustible}%")
        if self.nivel_combustible < 20:
            print("Advertencia: Bajo nivel de combustible.")
        print("_______________________________________________________")


# Creamos los objetos a partir de instanciar la clase Moto
moto_1 = Moto("Yamaha", "80", "80CC", "Gasolina", "Roja")
moto_2 = Moto("Honda", "XR", "190CC", "Gasolina", "Blanca")
moto_3 = Moto("Harley", "Davidson", "200CC", "Gasolina", "Marron")

# Mostrar detalles y realizar acciones para cada moto
moto_1.mostrar_informacion()
moto_1.encender_motor()
moto_1.revisar_combustible()

moto_2.mostrar_informacion()
moto_2.encender_motor()
moto_2.revisar_combustible()

moto_3.mostrar_informacion()
moto_3.encender_motor()
moto_3.revisar_combustible()
