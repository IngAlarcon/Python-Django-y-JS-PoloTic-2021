'''3.
Escribe un programa en Python que acepte una cadena de caracteres y cuente el tamaño de la
cadena y cuantas veces aparece la letra A ( mayuscula y minúscula)
'''

cadena = input("Ingrese una cadena de caracteres: ")

tamanioCadena = len(cadena)
#aMinuscula= cadena.count('a') #manera corta de hacerlo
#aMayuscula= cadena.count('A') #con funciones del leguaje

indice = 0
aMinuscula = 0
aMayuscula = 0

while indice < len(cadena):
    letra = cadena[indice]

    if ( letra == "a"):
        aMinuscula = aMinuscula +1
        indice = indice +1
    elif (letra == "A"):
        aMayuscula = aMayuscula +1
        indice = indice + 1

    indice = indice +1


print(f"El tamaño de mi cadena '{cadena}' es de {tamanioCadena} caracteres.")

print(f"Se encontraron {aMinuscula} caracteres  'a'.")

print(f"Se encontraron {aMayuscula} caracteres  'A'.")