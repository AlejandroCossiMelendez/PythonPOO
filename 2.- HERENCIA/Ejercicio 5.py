class Reloj:
    def __init__(self, marca, tipo, material):
        self.marca = marca
        self.tipo = tipo
        self.material = material
        self.precio = str(input(f"Digite el precio del reloj: "))

    def registrar(self):
        print("-----------------")
        print("RELOJ REGISTRADO")
        print("-----------------")
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Material: {self.material}")
        print(f"Precio: $ {self.precio}")

class RelojInteligente(Reloj):
    def __init__(self, marca, tipo, material, pantalla):
        super().__init__(marca, tipo, material)
        self.pantalla = pantalla
        self.sistema_operativo = str(input("Digite el sistema operativo del reloj: "))

    def encender(self):
        print(f"Encendiendo el reloj inteligente {self.marca} con pantalla {self.pantalla} y sistema {self.sistema_operativo}")

# Instanciar un objeto de la clase RelojInteligente
mi_reloj = RelojInteligente('Samsung', 'Deportivo', 'Metal', 'OLED')
mi_reloj.registrar()
mi_reloj.encender()
