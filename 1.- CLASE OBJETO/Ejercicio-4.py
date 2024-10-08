# Defino la clase Empleado
class Empleado:
    # Metodo Constructor
    def __init__(self, nombre, edad, cargo, salario, años_experiencia):
        # Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.salario = salario
        self.años_experiencia = años_experiencia

    # Metodo para mostrar detalles del objeto
    def mostrar_informacion(self):
        print(f"Informacion del Empleado:\n")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Cargo: {self.cargo}")
        print(f"Salario: ${self.salario}")
        print(f"Años de Experiencia: {self.años_experiencia}\n")

    # Metodo para trabajar
    def trabajar(self):
        print(f"{self.nombre} esta trabajando como {self.cargo}.")
        print("_______________________________________________________")

    # Metodo para calcular bono
    def calcular_bono(self):
        bono = self.salario * 0.1  # Bono del 10% del salario
        print(f"{self.nombre} recibira un bono de ${bono}.")
        print("_______________________________________________________")


# Creamos los objetos a partir de instanciar la clase Empleado
empleado_1 = Empleado("Luis", 45, "Maestro de Obra", 2500000, "20 Años")
empleado_2 = Empleado("Juan", 30, "Desarrollador", 3500000, "7 Años")
empleado_3 = Empleado("Ana", 39, "Gerente", 8000000, "12 Años")

# Mostrar los detalles empleado_1
empleado_1.mostrar_informacion()
# Trabajar
empleado_1.trabajar()
# Calcular bono
empleado_1.calcular_bono()

# Mostrar los detalles empleado_2
empleado_2.mostrar_informacion()
# Trabajar
empleado_2.trabajar()
# Calcular bono
empleado_2.calcular_bono()

# Mostrar los detalles empleado_3
empleado_3.mostrar_informacion()
# Trabajar
empleado_3.trabajar()
# Calcular bono
empleado_3.calcular_bono()
