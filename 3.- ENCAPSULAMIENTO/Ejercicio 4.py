class Electronico:
    def __init__(self, marca, modelo, procesador):
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.ram = str(input(f"Digite la cantidad de memoria Ram en GB: "))

    def registrar(self):
        print("-----------------")
        print("ELECTRÓNICO REGISTRADO")
        print("-----------------")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Procesador: {self.procesador}")
        print(f"RAM: {self.ram} GB")

class Laptop(Electronico):
    def __init__(self, marca, modelo, procesador, disco_duro):
        super().__init__(marca, modelo, procesador)
        self.disco_duro = disco_duro
        self.duracion_bateria = int(input("Digite la cantidad de horas que dura la bateria: "))

    def encender(self):
        print(f"Encendiendo la laptop {self.marca} con disco duro {self.disco_duro} y {self.duracion_bateria} horas de batería")

# Instanciar un objeto de la clase Laptop
mi_laptop = Laptop('HP', 'Envy', 'Intel i7', 'SSD 512GB')
mi_laptop.registrar()
mi_laptop.encender()
