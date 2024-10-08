# Clase Aprendiz
class Aprendiz:
    def __init__(self, nombres, apellidos, cedula, sexo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.sexo = sexo
        self.formacion = input("Programa de formacion: ")
        self.regional = input("Regional: ")

    def mostrar_info(self):
        print("\nHola, soy un aprendiz SENA")
        print(f"{self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Sexo: {self.sexo}")
        print(f"Estudiante del programa: {self.formacion} de la Regional {self.regional}\n\n")

# Clase Instructor
class Instructor:
    def __init__(self, nombres, apellidos, cedula, area):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.area = area

    def mostrar_info(self):
        print("Hola, soy un instructor del SENA")
        print(f"{self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"area de instruccion: {self.area}\n\n")

# Clase Coordinador
class Coordinador:
    def __init__(self, nombres, apellidos, cedula, departamento):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.departamento = departamento

    def mostrar_info(self):
        print("Hola, soy un coordinador del SENA")
        print(f"{self.nombres} {self.apellidos}")
        print(f"CC: {self.cedula}")
        print(f"Departamento: {self.departamento}\n\n")

# Funcion que muestra la informacion de cualquier tipo de objeto (polimorfismo)
def mostrar_informacion(persona):
    persona.mostrar_info()

# Creacion de instancias de cada clase
objeto_aprendiz = Aprendiz("Samuel Elias", "Vega Barrios", 1231338164, "Masculino")
objeto_instructor = Instructor("Laura", "Rodriguez", 987654321, "Programacion")
objeto_coordinador = Coordinador("Carlos", "Martinez", 123456789, "Recursos Humanos")

# Llamado al metodo mostrar_info para cada objeto
mostrar_informacion(objeto_aprendiz)
mostrar_informacion(objeto_instructor)
mostrar_informacion(objeto_coordinador)
