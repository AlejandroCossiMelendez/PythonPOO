# Defino la clase FigurasGeometricas
class FigurasGeometricas:
    # Metodo Constructor
    def __init__(self, tipo, color, lados, longitud_lado):
        self.tipo = tipo
        self.color = color
        self.lados = lados
        self.longitud_lado = longitud_lado
        self.area = None # lo defino sin valor
        self.perimetro = None # lo defino sin valor

    # Metodo para calcular el area (solo para figuras regulares)
    def calcular_area(self):
        if self.tipo == "Cuadrado":
            self.area = self.longitud_lado ** 2
        elif self.tipo == "Triangulo":
            self.area = (self.longitud_lado ** 2 * (3 ** 0.5)) / 4
        elif self.tipo == "Circulo":
            radio = self.longitud_lado / 2 
            self.area = 3.14 * (radio ** 2)
        else:
            self.area = "area no calculable para esta figura"
        print(f"area del {self.tipo}: {self.area}")
        print("_______________________________________________________")

    # Metodo para calcular el perimetro
    def calcular_perimetro(self):
        if self.tipo == "Cuadrado":
            self.perimetro = 4 * self.longitud_lado
        elif self.tipo == "Triangulo":
            self.perimetro = 3 * self.longitud_lado
        elif self.tipo == "Circulo":
            self.perimetro = 3.14 * self.longitud_lado  # Longitud del lado es el diametro
        else:
            self.perimetro = "Perimetro no calculable para esta figura"
        print(f"Perimetro del {self.tipo}: {self.perimetro}")
        print("_______________________________________________________")


# Creamos los objetos a partir de instanciar la clase FigurasGeometricas
figura_1 = FigurasGeometricas("Cuadrado", "Rojo", 4, 5)
figura_2 = FigurasGeometricas("Triangulo", "Azul", 3, 6)
figura_3 = FigurasGeometricas("Circulo", "Verde", 0, 10)

# Mostrar el area y el perimetro para cada figura
figura_1.calcular_area()
figura_1.calcular_perimetro()

figura_2.calcular_area()
figura_2.calcular_perimetro()

figura_3.calcular_area()
figura_3.calcular_perimetro()
