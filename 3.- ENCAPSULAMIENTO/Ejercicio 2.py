class Dispositivo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.capacidad_bateria = int(input("Digite la capacidad de la bateria en mAh: "))

    def registrar(self):
        print("-----------------")
        print("DISPOSITIVO REGISTRADO")
        print("-----------------")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Capacidad de batería: {self.capacidad_bateria} mAh")

class Smartphone(Dispositivo):
    def __init__(self, marca, modelo, año, sistema_operativo):
        super().__init__(marca, modelo, año)
        self.sistema_operativo = sistema_operativo
        self.conectividad = str(input("Digite que tipo de conectividad tiene este dispositivo: "))
    
    def encender(self):
        print(f"La conectividad del dispositivo {self.modelo} es: {self.conectividad}")
        print(f"El smartphone {self.marca} con {self.sistema_operativo} y conectividad {self.conectividad} está encendido")

# Instanciar un objeto de la clase Smartphone
mi_smartphone = Smartphone('Apple', 'iPhone 14', 2023, 'iOS')
mi_smartphone.registrar()
mi_smartphone.encender()
