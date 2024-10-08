class Instrumento:
    def __init__(self, tipo, marca, material):
        self.tipo = tipo
        self.marca = marca
        self.material = material
        self.precio = int(input(f"Digite el precio de la {self.tipo}: "))

    def registrar(self):
        print("-----------------")
        print("INSTRUMENTO REGISTRADO")
        print("-----------------")
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Material: {self.material}")
        print(f"Precio: $ {self.precio}")

class Guitarra(Instrumento):
    def __init__(self, tipo, marca, material, num_cuerdas):
        super().__init__(tipo, marca, material)
        self.num_cuerdas = num_cuerdas
        self.acordes_basicos = str(input(f"Digite los acordes basicos que conoce: "))

    def tocar(self):
        print(f"Los acordes basicos que conoces son : {self.acordes_basicos}")
        print(f"Tocando la guitarra con {self.num_cuerdas} cuerdas usando los acordes: {self.acordes_basicos}")

# Instanciar un objeto de la clase Guitarra
mi_guitarra = Guitarra('Guitarra', 'Fender', 'Madera', 6)
mi_guitarra.registrar()
mi_guitarra.tocar()
