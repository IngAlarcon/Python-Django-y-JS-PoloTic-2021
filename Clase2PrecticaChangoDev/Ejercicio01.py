"""
1. Escribe un programa Python que acepte el radio de un círculo del usuario y calcule el área.

"""

#importando modulo

import math

# Entrada de dato

radio = float(input("Digite el radio del circulo en cm: "))


if radio > 0 :
    # Procesando el area
    area = math.pi * radio ** 2

    print(f"El Area del circulo es: {area:.2f}cm2")

else:

    print("El valor del radio no es correcto")



