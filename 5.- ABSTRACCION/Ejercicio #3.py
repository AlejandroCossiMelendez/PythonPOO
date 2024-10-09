from abc import ABC, abstractmethod

class TareaEmpleado(ABC):
    @abstractmethod
    def realizar_tarea(self):
        pass

class Ingeniero(TareaEmpleado):
    def realizar_tarea(self):
        return "El ingeniero está diseñando un puente."

class Doctor(TareaEmpleado):
    def realizar_tarea(self):
        return "El doctor está diagnosticando a un paciente."

# Uso de las clases
ingeniero = Ingeniero()
print(ingeniero.realizar_tarea())

doctor = Doctor()
print(doctor.realizar_tarea())
