"""
    1. Escribe una clase de Python llamada Rectangulo que se define por una
longitud y un ancho y un método que calculará el área de un rectángulo.

"""

class Rectangulo():

    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def area(self):
        return self.longitud * self.ancho

    def __str__(self):
         return (f'Longitud {self.longitud} y Ancho {self.ancho} Area: {self.area()}')



area1 = Rectangulo(4,2)

print(area1)