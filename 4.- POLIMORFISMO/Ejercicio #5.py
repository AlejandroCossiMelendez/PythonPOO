# Clase base Profesiones
class Profesiones:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
    
    def trabajar(self):
        return "Este Profesiones esta trabajando."

# Clase Medico que hereda de Profesiones
class Medico(Profesiones):
    def __init__(self, nombre, especialidad, hospital):
        super().__init__(nombre, especialidad)
        self.hospital = hospital
    
    def trabajar(self):
        return f"\nDr(a). {self.nombre}, especialista en {self.especialidad}, trabaja en el hospital {self.hospital}, atendiendo a sus pacientes.\n"

# Clase Ingeniero que hereda de Profesiones
class Ingeniero(Profesiones):
    def __init__(self, nombre, especialidad, proyecto):
        super().__init__(nombre, especialidad)
        self.proyecto = proyecto
    
    def trabajar(self):
        return f"{self.nombre}, ingeniero especializado en {self.especialidad}, esta trabajando en el proyecto {self.proyecto}.\n"

# Clase Docente que hereda de Profesiones
class Docente(Profesiones):
    def __init__(self, nombre, especialidad, instituto):
        super().__init__(nombre, especialidad)
        self.instituto = instituto
    
    def trabajar(self):
        return f"{self.nombre}, docente de {self.especialidad}, imparte clases en el instituto {self.instituto}.\n"

# Funcion que recibe cualquier tipo de Profesiones y muestra su trabajo
def mostrar_trabajo(Profesiones):
    print(Profesiones.trabajar())

# Creacion de objetos
medico = Medico("Ana Gomez", "Cardiologia", "Hospital Central")
ingeniero = Ingeniero("Luis Perez", "Ingenieria Civil", "Construccion del puente")
docente = Docente("Marta Ruiz", "Matematicas", "Universidad Nacional")

# Llamado a la funcion para cada objeto
mostrar_trabajo(medico)
mostrar_trabajo(ingeniero)
mostrar_trabajo(docente)
