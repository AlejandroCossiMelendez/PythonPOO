class Electrodomestico:
    def __init__(self, marca, color, capacidad):
        self.marca = marca
        self.color = color
        self.capacidad = capacidad
        self.consumo = int(input("Digite el consumo en kWh: "))

    def registrar(self):
        print("---------------------------")
        print("ELECTRODOMÉSTICO REGISTRADO")
        print("---------------------------")
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Capacidad: {self.capacidad} litros")
        print(f"Consumo eléctrico: {self.consumo} kWh")

class Refrigerador(Electrodomestico):
    def __init__(self, marca, color, capacidad, tipo):
        super().__init__(marca, color, capacidad)
        self.tipo = tipo
        self.temperatura = int(input("Digite la temperatura inicial de el refrigerador: "))

    def ajustar_temperatura(self):
        print(f"Temperatura inicial: {self.temperatura}")
        self.temperaturaAjustada = int(input("\nDigite la nueva temperatura del refrigerador: "))
        print(f"\nLa nueva temperatura del refrigerador es: {self.temperaturaAjustada}°C")
        print("----------------------------------------------\n")

# Instanciar un objeto de la clase Refrigerador
mi_refrigerador = Refrigerador('Samsung', 'Blanco', 400, 'No Frost')
mi_refrigerador.registrar()
mi_refrigerador.ajustar_temperatura()
