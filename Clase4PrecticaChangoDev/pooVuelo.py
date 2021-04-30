"""
Creamos una clase que representa el
vuelo de una aerolínea

"""
class Vuelo():
    # Metodo para crear un nuevo vuelo con una capacidad dada
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = []

    #Metodo para agregar un pasajero al vuelo:
    def agregar_pasajero(self, nombre):
        if not self.asientos_disponibles():
            return False
        self.pasajeros.append(nombre)
        return True

    #Metodo para retornar el numero de asientos disponibles
    def asientos_disponibles(self):
        return self.capacidad - len(self.pasajeros)

    def __str__(self):
        return (f"Pasajero registrado {self.pasajeros}")

