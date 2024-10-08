# Defino la clase
class Celular:
    # Metodo Constructor
    def __init__(self, marca, modelo, sistemaOperativo, capacidadBateria, memoriaRam, almacenamientoInterno):
        # Defino los atributos de instancia de la clase
        self.marca = marca
        self.modelo = modelo
        self.sistemaOperativo = sistemaOperativo
        self.capacidadBateria = capacidadBateria
        self.memoriaRam = memoriaRam
        self.almacenamientoInterno = almacenamientoInterno
        self.destino = None
        self.mensaje = None

    # Metodo para mostrar detalles del objeto
    def mostrar_informacion(self):
        print("Informacion del Celular:\n")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Sistema Operativo: {self.sistemaOperativo}")
        print(f"Capacidad de la Bateria: {self.capacidadBateria}")
        print(f"Tamaño de la Memoria Ram: {self.memoriaRam}")
        print(f"Almacenamiento Interno: {self.almacenamientoInterno}\n")

    # Metodo para hacer llamadas
    def hacer_llamadas(self):
        self.destino = input("Digite el numero al que desea llamar: ")
        
        if self.destino.isdigit() and int(self.destino) > 0:
            print(f"Llamando al: {self.destino} desde tu dispositivo {self.marca} {self.modelo}")
        else:
            print("Numero no válido")
        print("_______________________________________________________")

    # Metodo para enviar mensaje
    def enviar_mensaje(self):
        self.destino = input("Digite el numero al que desea enviar el mensaje: ")
        self.mensaje = input("Digite el mensaje que desea enviar: ")
        
        if self.destino.isdigit() and int(self.destino) > 0 and self.mensaje:
            print(f"\nEnviando mensaje a: {self.destino}")
            print(f"Mensaje: {self.mensaje}")
            print(f"Mensaje enviado al destinatario")
        else:
            print("Numero o mensaje no válidos")
        print("_______________________________________________________")


# Creamos los objetos a partir de instanciar la clase Celular
objeto_1 = Celular("Samsung", "Galaxy S21", "Android", "4000mAh", "8 GB", "128 GB")
objeto_2 = Celular("Apple", "Iphone XS", "iOS", "3200mAh", "6 GB", "256 GB")
objeto_3 = Celular("Xiaomi", "Redmi note 10", "Android", "5000mAh", "4 GB", "64 GB")

# Mostrar los detalle objeto_1
objeto_1.mostrar_informacion()
# Hacer llamada
objeto_1.hacer_llamadas()
# Enviar mensaje
objeto_1.enviar_mensaje()

# Mostrar los detalle objeto_2
objeto_2.mostrar_informacion()
# Hacer llamada
objeto_2.hacer_llamadas()
# Enviar mensaje
objeto_2.enviar_mensaje()

# Mostrar los detalle objeto_3
objeto_3.mostrar_informacion()
# Hacer llamada
objeto_3.hacer_llamadas()
# Enviar mensaje
objeto_3.enviar_mensaje()
