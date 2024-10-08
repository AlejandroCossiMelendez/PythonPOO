# Clase base Vehiculos
class Vehiculos:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año
    
    def descripcion(self):
        return f"Marca: {self.marca}, Año: {self.año}"

# Clase Carro que hereda de Vehiculos
class Carro(Vehiculos):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, año)
        self.modelo = modelo
    
    def descripcion(self):
        return f"Carro en venta:\nMarca: {self.marca}\nModelo: {self.modelo}\nAño: {self.año}\n"

# Clase Moto que hereda de Vehiculos
class Moto(Vehiculos):
    def __init__(self, marca, cilindrada, año):
        super().__init__(marca, año)
        self.cilindrada = cilindrada
    
    def descripcion(self):
        return f"Moto en venta:\nMarca: {self.marca}\nCilindrada: {self.cilindrada} cc\nAño: {self.año}\n"

# Clase Bicicleta que hereda de Vehiculo
class Bicicleta(Vehiculos):
    def __init__(self, marca, tipo, velocidad_maxima, año):
        super().__init__(marca, año)
        self.tipo = tipo
        self.velocidad_maxima = velocidad_maxima
    
    def descripcion(self):
        return f"Bicicleta en venta:\nMarca: {self.marca}\nTipo: {self.tipo}\nVelocidad Maxima: {self.velocidad_maxima} km/h\nAño: {self.año}\n"

# Funcion que recibe cualquier tipo de vehiculo y muestra su descripcion
def mostrar_descripcion(vehiculo):
    print(vehiculo.descripcion())

# Creacion de objetos
carro = Carro("Toyota", "Corolla", 2024)
moto = Moto("Honda", 250, 2025)
bicicleta = Bicicleta("Shimano", "Montaña", 25, 2023)

# Llamado a la funcion para cada objeto
mostrar_descripcion(carro)
mostrar_descripcion(moto)
mostrar_descripcion(bicicleta)
